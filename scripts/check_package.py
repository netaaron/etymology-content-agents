#!/usr/bin/env python3
"""Publisher Prep 自動檢查：檔案完整性、metadata.json、各平台字元／hashtag 限制。

用法：python3 scripts/check_package.py output/<slug>-<YYYY-MM-DD>
只用 Python 標準函式庫，不需安裝任何套件。
"""
import json
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "main-content.md",
    "kdp-description.md",
    "youtube-script.md",
    "social-posts.md",
    "image-prompts.md",
    "metadata.json",
    "checklist.md",
]
WORK_FILES = ["_work/01-research.md", "_work/02-plan.md"]

LIMITS = {
    "kdp_description": 4000,
    "kdp_title_subtitle": 200,
    "kdp_keywords": 7,
    "kdp_keyword_len": 50,
    "yt_title": 100,
    "yt_description": 5000,
    "yt_tags_total": 500,
    "ig_caption": 2200,
    "ig_hashtags": 5,
    "threads": 500,
    "threads_tags": 1,
}

CJK = re.compile(r"[㐀-鿿豈-﫿]")
HASHTAG = re.compile(r"(?<![\w&])#[\w㐀-鿿]+")

results = []  # (level, message)


def ok(msg):
    results.append(("✅", msg))


def warn(msg):
    results.append(("⚠️", msg))


def fail(msg):
    results.append(("❌", msg))


def fenced_blocks(text, lang):
    return re.findall(r"```" + lang + r"\n(.*?)```", text, flags=re.S)


def check_files(folder):
    for name in REQUIRED_FILES:
        p = folder / name
        if name == "checklist.md" and not p.exists():
            warn(f"{name} 尚未建立（Publisher Prep 會在檢查後建立）")
        elif p.exists() and p.stat().st_size > 0:
            ok(f"檔案存在：{name}")
        else:
            fail(f"缺少或空白：{name}")
    for name in WORK_FILES:
        if (folder / name).exists():
            ok(f"中間產物存在：{name}")
        else:
            warn(f"缺少中間產物：{name}")


def check_metadata(folder):
    p = folder / "metadata.json"
    if not p.exists():
        return None
    try:
        meta = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"metadata.json 不是合法 JSON：{e}")
        return None
    ok("metadata.json 是合法 JSON")

    required = ["slug", "date", "topic", "language", "titles", "kdp", "youtube", "social", "keywords", "sources"]
    missing = [k for k in required if k not in meta]
    if missing:
        fail(f"metadata.json 缺少欄位：{', '.join(missing)}")
    else:
        ok("metadata.json 必要欄位齊全")

    expected = folder.name
    if meta.get("slug") and meta.get("date") and f"{meta['slug']}-{meta['date']}" != expected:
        warn(f"slug＋date（{meta.get('slug')}-{meta.get('date')}）與資料夾名稱（{expected}）不一致")

    kdp = meta.get("kdp", {})
    ts = len(kdp.get("title", "")) + len(kdp.get("subtitle", ""))
    (ok if ts <= LIMITS["kdp_title_subtitle"] else fail)(f"KDP 書名＋副標 {ts}/{LIMITS['kdp_title_subtitle']} 字元")
    kws = kdp.get("keywords", [])
    (ok if len(kws) <= LIMITS["kdp_keywords"] else fail)(f"KDP 關鍵字 {len(kws)}/{LIMITS['kdp_keywords']} 組")
    for kw in kws:
        if len(kw) > LIMITS["kdp_keyword_len"]:
            fail(f"KDP 關鍵字過長（{len(kw)} 字元）：{kw}")

    yt = meta.get("youtube", {})
    tl = len(yt.get("title", ""))
    (ok if tl <= LIMITS["yt_title"] else fail)(f"YouTube 標題 {tl}/{LIMITS['yt_title']} 字元")
    # YouTube 計算方式：標籤以逗號分隔，含空白的標籤會自動加上引號（+2）
    tags = yt.get("tags", [])
    tag_total = sum(len(t) + (2 if " " in t else 0) for t in tags) + max(len(tags) - 1, 0)
    (ok if tag_total <= LIMITS["yt_tags_total"] else fail)(f"YouTube 標籤合計 {tag_total}/{LIMITS['yt_tags_total']} 字元")

    ig = meta.get("social", {}).get("instagram_hashtags", [])
    (ok if len(ig) <= LIMITS["ig_hashtags"] else fail)(f"metadata Instagram hashtag {len(ig)}/{LIMITS['ig_hashtags']}")
    return meta


def check_kdp(folder):
    p = folder / "kdp-description.md"
    if not p.exists():
        return
    blocks = fenced_blocks(p.read_text(encoding="utf-8"), "html")
    if not blocks:
        fail("kdp-description.md 找不到 ```html 區塊")
        return
    n = len(blocks[0].strip())
    (ok if n <= LIMITS["kdp_description"] else fail)(f"KDP 描述 {n}/{LIMITS['kdp_description']} 字元（含 HTML 標籤）")


def check_youtube(folder):
    p = folder / "youtube-script.md"
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    m = re.search(r"## 影片說明欄.*?```text\n(.*?)```", text, flags=re.S)
    if not m:
        warn("youtube-script.md 找不到「## 影片說明欄」的 ```text 區塊")
    else:
        n = len(m.group(1).strip())
        (ok if n <= LIMITS["yt_description"] else fail)(f"YouTube 說明欄 {n}/{LIMITS['yt_description']} 字元")
    if "CTA" not in text:
        warn("youtube-script.md 沒有標出 CTA")


def check_social(folder):
    p = folder / "social-posts.md"
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    sections = re.split(r"\n(?=### )", text)
    count = 0
    for sec in sections:
        if not sec.startswith("### "):
            continue
        title = sec.splitlines()[0][4:].strip()
        m = re.search(r"平台[:：]\s*(\S+)", sec)
        platform = (m.group(1) if m else "").lower()
        blocks = fenced_blocks(sec, "text")
        if not blocks:
            continue
        count += 1
        body = blocks[-1].strip()  # 最後一個 text 區塊 = 可直接貼上的貼文
        n = len(body)
        tags = HASHTAG.findall(body)
        if "instagram" in platform:
            (ok if n <= LIMITS["ig_caption"] else fail)(f"[{title}] IG 說明 {n}/{LIMITS['ig_caption']} 字元")
            (ok if len(tags) <= LIMITS["ig_hashtags"] else fail)(f"[{title}] IG hashtag {len(tags)}/{LIMITS['ig_hashtags']}")
        elif "threads" in platform:
            (ok if n <= LIMITS["threads"] else fail)(f"[{title}] Threads {n}/{LIMITS['threads']} 字元")
            (ok if len(tags) <= LIMITS["threads_tags"] else fail)(f"[{title}] Threads 標籤 {len(tags)}/{LIMITS['threads_tags']}")
        else:
            ok(f"[{title}] {platform or '未標平台'} {n} 字元")
    if count == 0:
        fail("social-posts.md 沒有任何含 ```text 區塊的貼文")


def check_main(folder):
    p = folder / "main-content.md"
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    # 只算正文：速查表、小測驗、來源不計
    body = re.split(r"\n## (?:Word Family|Quick Check|Sources)", body)[0]
    en_words, en_paras, zh_paras = 0, 0, 0
    for para in re.split(r"\n\s*\n", body):
        s = para.strip()
        if not s or s.startswith(("#", "|", "```", "`", ">")):
            continue
        cjk = len(CJK.findall(s))
        latin = len(re.findall(r"[A-Za-z]", s))
        # 以字元比例判斷語言：英文段裡夾幾個中文例字（唇槍舌劍）仍算英文段
        if cjk > latin * 0.25:
            zh_paras += 1
        else:
            en_paras += 1
            en_words += len(re.findall(r"[A-Za-z][A-Za-z'\-]*", s))
    msg = f"主文英文正文約 {en_words} 字（目標 1,200–1,800）"
    (ok if 1200 <= en_words <= 1800 else warn)(msg)
    if en_paras and abs(en_paras - zh_paras) > max(2, en_paras * 0.2):
        warn(f"英文段 {en_paras}、中文段 {zh_paras}，數量差距偏大，請檢查是否漏譯")
    else:
        ok(f"雙語段落數：英 {en_paras}／中 {zh_paras}")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    folder = Path(sys.argv[1])
    if not folder.is_dir():
        print(f"找不到資料夾：{folder}")
        sys.exit(2)
    check_files(folder)
    check_metadata(folder)
    check_main(folder)
    check_kdp(folder)
    check_youtube(folder)
    check_social(folder)

    for level, msg in results:
        print(f"{level} {msg}")
    fails = sum(1 for l, _ in results if l == "❌")
    warns = sum(1 for l, _ in results if l == "⚠️")
    print(f"\n總結：❌ {fails}　⚠️ {warns}　✅ {len(results) - fails - warns}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
