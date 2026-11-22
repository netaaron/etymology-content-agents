# 共用規範：英語詞源內容產線（Etymology Content Pipeline）

所有 agent 都必須遵守本檔。個別 agent 檔只寫「自己這一關的任務」，不重複本檔內容。

## 1. 讀者與語言

**讀者**：想把英文學深的台灣學習者（高中以上、成人自學、英文老師），以及對詞源有興趣的雙語讀者。

**語言：中英雙語對照**，規則如下：

1. **段落對照**：每段先英文、後繁中，兩段意思一致。不在同一句裡中英夾雜。
2. **關鍵詞首次出現**：`English term（中文譯名）`，之後可單用英文。
3. **詞源標記統一格式**：`meta-`（跨越）＋ `pherein`（攜帶）→ `metaphora`（搬運、轉移）
4. **希臘字**：原文＋羅馬拼音，例 μεταφορά (metaphorá)。拉丁字只用斜體，例 *transferre*。
5. **繁體中文、台灣用語**：影片（非視頻）、資訊（非信息）、程式（非程序）、品質（非質量）。
6. 中文不是英文的逐字翻譯，可以改寫成自然中文，但**事實、例子、數字必須一致**。

## 2. 語氣與寫作風格

- 清晰、有層次、教學感：**先給結論，再給推導**。
- 每一節只講一個重點；能用一個好例子講清楚，就不用三個普通例子。
- 不寫空洞讚嘆（「太神奇了！」「你一定想不到！」），用事實本身製造驚訝。
- 讀者很聰明，不要過度解釋常識。

## 3. 事實準則（最重要）

- 詞源事實必須有來源。優先順序：Etymonline → Wiktionary → OED／Merriam-Webster → Perseus（古典原典）→ 學術著作。
- 研究摘要中每條事實標記可信度：
  - ✅ 已核實：一個權威來源或兩個獨立來源
  - ⚠️ 需人工確認：只有一個非權威來源，或來源間有出入
- **⚠️ 的事實不得進入 main-content.md**，除非改寫成保守說法並在 checklist 標出。
- 常見陷阱：民俗詞源（folk etymology）、長得像但不同源（false cognates）、把現代用法倒推回古代。
- 引文：只直接引用 **1929 年前出版的公有領域譯本**（例：Butcher 1895 譯 Aristotle、Butler 1920 譯 Quintilian），單則引文少於 40 字。現代著作一律**改寫轉述**，並標作者與年份。

## 4. 單一真相來源（SSOT）

- `main-content.md` 是唯一的真相來源。
- Adapter 只能從 `main-content.md` 取材，**不得新增主文沒有的事實**。要加新事實，回到 Writer。

## 5. 檔案與資料夾

```
output/<slug>-<YYYY-MM-DD>/
├── _work/
│   ├── 01-research.md      ← Topic Analyzer
│   └── 02-plan.md          ← Content Planner
├── main-content.md         ← Writer
├── kdp-description.md      ← Adapter
├── youtube-script.md       ← Adapter
├── social-posts.md         ← Adapter
├── image-prompts.md        ← Adapter
├── metadata.json           ← Adapter（格式見 templates/metadata.schema.json）
└── checklist.md            ← Publisher Prep
```

- `slug`：主題英文小寫、以連字號連接，例 `metaphor`、`greek-root-graph`。
- 日期用執行當天（台灣時間）。
- 每個 agent 完成後，在對話中回報：寫了哪些檔、有哪些 ⚠️ 項目、下一關該注意什麼。

## 6. 平台限制（Adapter 與 Publisher Prep 必查）

| 平台 | 欄位 | 限制 |
|---|---|---|
| KDP | 書名＋副標 | 合計 ≤ 200 字元 |
| KDP | 書籍描述 | ≤ 4,000 字元，**HTML 標籤也計入**；可用 `<b> <i> <br> <p> <ul> <li> <h4>` |
| KDP | 關鍵字 | 最多 7 組，每組 ≤ 50 字元；不可放書名已有的字、不可放其他作者／書名 |
| YouTube | 標題 | ≤ 100 字元（建議 ≤ 60，避免被截斷） |
| YouTube | 說明 | ≤ 5,000 字元 |
| YouTube | 標籤 | 合計 ≤ 500 字元 |
| Instagram | 貼文說明 | ≤ 2,200 字元；hashtag **最多 5 個**（2025/12 起） |
| Threads | 貼文 | ≤ 500 字元；主題標籤 1 個 |
| Facebook | 貼文 | 無硬性限制，建議前 125 字元內講完重點 |

平台規則會變動。Publisher Prep 若發現與官方說明不符，在 checklist 標 ⚠️。
