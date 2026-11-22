# 發布檢查清單：金融英文的詞源

**狀態：🟡 需小修**（YouTube 與社群可進入製作；KDP 依系列合輯計畫處理，見下方第 1 項）

Agent：publisher-prep｜檢查日期：2026-11-22

## 自動檢查結果

```text
✅ 檔案存在：main-content.md
✅ 檔案存在：kdp-description.md
✅ 檔案存在：youtube-script.md
✅ 檔案存在：social-posts.md
✅ 檔案存在：image-prompts.md
✅ 檔案存在：metadata.json
✅ 檔案存在：checklist.md
✅ 中間產物存在：_work/01-research.md
✅ 中間產物存在：_work/02-plan.md
✅ metadata.json 是合法 JSON
✅ metadata.json 必要欄位齊全
✅ KDP 書名＋副標 106/200 字元
✅ KDP 關鍵字 7/7 組
✅ YouTube 標題 42/100 字元
✅ YouTube 標籤合計 214/500 字元
✅ metadata Instagram hashtag 5/5
✅ 主文英文正文約 1211 字（目標 1,200–1,800）
✅ 雙語段落數：英 21／中 21
✅ KDP 描述 1515/4000 字元（含 HTML 標籤）
✅ YouTube 說明欄 1004/5000 字元
✅ [S1｜Instagram 輪播：從牛到信用] IG 說明 433/2200 字元
✅ [S1｜Instagram 輪播：從牛到信用] IG hashtag 5/5
✅ [S2｜Threads：羅馬士兵沒有領鹽當薪水] Threads 252/500 字元
✅ [S2｜Threads：羅馬士兵沒有領鹽當薪水] Threads 標籤 1/1
✅ [S3｜Threads：debt 的 b 是學者硬塞的] Threads 250/500 字元
✅ [S3｜Threads：debt 的 b 是學者硬塞的] Threads 標籤 1/1
✅ [S4｜Facebook：英文的錢來自牛，中文的錢來自貝殼] facebook 521 字元
✅ [S5｜Shorts／Reels：mortgage 是「死亡抵押」] shorts 115 字元

總結：❌ 0　⚠️ 0　✅ 28
```

## 第一輪檢查發現並已退回修正

| 問題 | 退回關卡 | 處理 |
|---|---|---|
| IG 說明寫「9 個金融字」，輪播實際列了 10 個 | Adapter | 改為 10 ✅ |
| 主文第 5 節中文段引了《說文》「信，誠也」，英文段沒有，雙語不一致 | Writer | 英文段補上 Shuowen 的釋義 ✅ |
| KDP 書名候選的字元數是估計值（105、98），與實際（106、101）不符 | Adapter | 改為實際計算值 ✅ |
| YouTube 規劃 5–6 分鐘，實際旁白約 3:50 | Adapter | 依實際字數重算時間碼；不灌水，在腳本開頭註明可放慢的段落 ✅ |

## 事實核對（抽樣回溯到 main-content.md）

| 產出檔 | 句子 | main-content 出處 | 結果 |
|---|---|---|---|
| kdp-description | coins struck beside a Roman temple | 第 3 節（near her temple） | ✅ |
| kdp-description | the *b* in *debt* was never pronounced | 第 5 節 | ✅ |
| kdp-description | Roman soldiers paid in salt has no ancient evidence | 第 8 節 | ✅ |
| youtube-script | German *Vieh* still means livestock today | 第 1 節 | ✅ |
| youtube-script | Was Moneta "the goddess who warns"? … the origin is uncertain | 第 3 節 | ✅ |
| youtube-script | failed dealers had their benches smashed … Etymologists doubt it | 第 4 節 | ✅ |
| social S2 | salary 來自 salarium，源自 salarius「與鹽有關的」 | 第 8 節 | ✅ |
| social S4 | 《說文解字》：「古者貨貝而寶龜…至秦廢貝行錢。」 | 第 3 節 | ✅ |
| social S5 | 17 世紀英國法學家 Coke 的解釋 | 第 6 節 | ✅ |

## 雙語一致性（抽 4 組）

| 段落 | 英 | 中 | 結果 |
|---|---|---|---|
| 第 3 節《說文》 | compiled around AD 100 | 約成書於西元 100 年 | ✅ |
| 第 4 節 bankrupt | entered English in the 1560s | 1560 年代進入英語 | ✅ |
| 第 5 節 信 | 人＋言；Shuowen: "sincerity" | 人＋言；「信，誠也」 | ✅（第二輪） |
| 第 7 節 finance | appeared only in 1770 | 直到 1770 年才出現 | ✅ |

## ⚠️ 項目處理確認

| 研究摘要 | 內容 | 產出中的寫法 | 結果 |
|---|---|---|---|
| F9 | Moneta 與 *monere*「警告」 | 主文與影片都寫成「傳統說法，來源不確定」；輪播與貼文不提 | ✅ |
| F13 | 砸長凳的習俗 | 一律以「存疑／大概只是比喻」出現 | ✅ |
| F18 | debt 加 b 的確切年代 | 所有產出都只寫「後來的學者」，不寫年代 | ✅ |
| F24 | 士兵領鹽 | 一律以「無古代證據」出現 | ✅ |

## 平台格式

- KDP 描述標籤：`<p> <b> <i> <h4> <ul> <li>`，皆在允許範圍 ✅
- YouTube 章節：第一個為 0:00、共 8 段、每段 ≥ 10 秒 ✅
- 圖片提示詞全部帶 `--no text, letters, words`；風格關鍵字與 metaphor 一集相同（系列一致）✅

## CTA

| 產出 | CTA | 結果 |
|---|---|---|
| YouTube | 3:38 留言：下一個想查的金融字＋訂閱 | ✅ |
| IG 輪播 | P8＋說明：留言 | ✅ |
| Threads S2／S3 | 留言提問 | ✅ |
| Facebook S4 | 留言分享帶「貝」的字 | ✅ |
| Shorts S5 | 追蹤 | ✅ |
| KDP | 翻開第一頁 | ✅ |

## ⚠️ 需人工確認

1. **KDP 成書方式**：本集英文約 1,210 字，和 metaphor 一樣適合當系列中的一章。目前系列累積 2 集，建議累積到 8–12 集再合輯上架。
2. **《說文解字》引文**：本集引用「古者貨貝而寶龜，周而有泉，至秦廢貝行錢」「木下曰本」「信，誠也」，依據漢典收錄。發布前可對照紙本或其他版本，確認用字。
3. **英文對《說文》的轉述**：英文段只轉述「以貝為幣、秦廢貝行錢」，省略了「寶龜」「周而有泉」，屬於精簡而非錯誤；若要完整，可在英文補半句。
4. **投資觀點句**：第 9 節「信任一消失，信用就跟著消失」是詮釋，不是詞源事實；符合你的投資寫作定位，但請確認語氣是否合適。
5. **影片長度**：約 3:50，比規劃短。若頻道偏好 5 分鐘以上，錄製時放慢「貝」「信」兩段並加漢字書寫動畫。

## 發布步驟（人工）

- [ ] 讀一遍 main-content.md，確認語氣與事實（必備人工審核）
- [ ] 用 image-prompts.md 產生 6 組圖片，後製文字
- [ ] YouTube：錄英文旁白 → 剪輯 → 上傳中文字幕 → 貼上標題、說明欄、標籤
- [ ] Instagram：8 頁輪播＋說明
- [ ] Threads：S2、S3 分兩天發
- [ ] Facebook：S4 搭配 IMG-06
- [ ] Shorts／Reels：S5
- [ ] KDP：併入系列合輯計畫
