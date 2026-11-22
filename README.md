# Etymology Content Agents｜英語詞源內容產線

丟一個主題進去，出來一個可直接上傳或排程的**中英雙語內容包**：主文、KDP 描述、YouTube 腳本、社群貼文、圖片提示詞、metadata、發布檢查清單。

## 流程

```
主題 ──▶ ① topic-analyzer ──▶ ② content-planner ──▶ ③ writer ──▶ ④ adapter ──▶ ⑤ publisher-prep ──▶ 人工審核 ──▶ 發布
          研究＋定角度            大綱＋平台規格          雙語主文(SSOT)     5 個平台檔         自動檢查＋清單
          [可選：確認角度]                               [抽查]                                 [必備]
```

| 關 | Agent | 讀 | 寫 |
|---|---|---|---|
| 1 | `topic-analyzer` | 主題 | `_work/01-research.md` |
| 2 | `content-planner` | 01-research | `_work/02-plan.md` |
| 3 | `writer` | 02-plan, 01-research | `main-content.md` |
| 4 | `adapter` | main-content, 02-plan | `kdp-description.md` `youtube-script.md` `social-posts.md` `image-prompts.md` `metadata.json` |
| 5 | `publisher-prep` | 全部 | `checklist.md` |

## 檔案結構

```
.github/
├── copilot-instructions.md      ← 所有 agent 共用：讀者、雙語格式、事實準則、平台限制
└── agents/
    ├── topic-analyzer.agent.md
    ├── content-planner.agent.md
    ├── writer.agent.md
    ├── adapter.agent.md
    └── publisher-prep.agent.md
scripts/check_package.py         ← 自動檢查（純 Python 標準函式庫）
templates/metadata.schema.json   ← metadata.json 欄位規格
output/
├── metaphor-2026-11-22/          ← 第 1 集：metaphor（單字型主題）
└── financial-english-2026-11-22/ ← 第 2 集：金融英文（主題型主題）
```

## 怎麼用（層級 A：GitHub Copilot）

**建議環境：VS Code 的 Copilot Chat（Agent 模式）**

1. 用 VS Code 開啟這個 repo，Copilot Chat 的 agent 下拉選單會自動出現 5 個 agent。
2. 選 `topic-analyzer`，輸入主題，例如：`希臘詞根 graph`。
3. 看完 `01-research.md`，按對話下方的 **「交給 Content Planner 規劃大綱」** 按鈕（handoff），依序往下走。
4. 最後在 `publisher-prep` 跑完檢查，讀 `checklist.md`，人工審核後發布。

**三個要知道的限制**

| 環境 | handoff 按鈕 | 網路搜尋 | 適合 |
|---|---|---|---|
| VS Code Copilot Chat | ✅ | ✅ | **全流程（建議）** |
| Copilot CLI | ❌（手動換 agent） | ✅ | 全流程 |
| GitHub.com Cloud Agent | ❌（會被忽略） | ❌ | 第 2–5 關；**第 1 關不要在這裡跑** |

- Topic Analyzer 必須查網路核實詞源，Cloud Agent 沒有 web 工具，在那裡跑會變成憑記憶寫詞源。
- CLI 用法：`copilot --agent topic-analyzer --prompt "metaphor 的詞源"`

**換成 Claude 或其他模型也能用**：每個 `.agent.md` 的 frontmatter 以下就是純提示詞，連同 `copilot-instructions.md` 貼進 Claude Project 的指示即可。

## 自動檢查

```bash
python3 scripts/check_package.py output/metaphor-2026-11-22
```

檢查 7 個必要檔案、metadata.json 合法性與欄位、KDP 描述 ≤ 4,000 字元（含 HTML）、書名＋副標 ≤ 200、YouTube 標題／說明／標籤、Instagram hashtag ≤ 5、Threads ≤ 500 字元、主文英文字數與中英段落數。有 ❌ 時回傳非零代碼，之後接 n8n 可直接當成「是否通知人類」的判斷。

## 層級 B：升級成 n8n 自動化（之後）

```
Google Sheet 新增一列主題
  → n8n：依序呼叫 LLM（system prompt = copilot-instructions.md + 該關 agent 檔內文）
  → 每關輸出寫入 output/<slug>-<date>/
  → 執行 check_package.py
  → ❌ 或 ⚠️ → 通知你；全 ✅ → 只在角度確認與最終審核時通知你
```

agent 檔就是 n8n 每個節點的提示詞，不需要重寫。

## 新增主題時

- slug 用英文小寫加連字號：`greek-root-graph`、`latin-root-port`
- 平台規則會變，`copilot-instructions.md` 第 6 節是唯一要更新的地方。
