# H-E3 盲评 · 可见文档包（固定路径）

日期：2026-10-28 Asia/Shanghai  
用途：Coder A/B **允许**打开的通识文档清单。Facilitator 发案时把本页与对应 `t4-he3-coder-pack-{a|b}.md` 一起发。

> **不要**打开案表全文 `t4-inter-rater-blind-case-table-h-e3.md`（内含 Facilitator §F 密封键）。  
> 案件与顺序只看你的 **coder-pack**。

---

## 允许打开（固定路径）

| # | 路径 | 内容 |
|---|---|---|
| 1 | [`docs/getting-started.md`](../getting-started.md) | Getting Started |
| 2 | [`docs/methodology/model-v0.7.md`](model-v0.7.md) | Formal model V0.7 |
| 3 | [`schema/patent-value-ledger.schema.json`](../../schema/patent-value-ledger.schema.json) | Ledger schema 1.0 |
| 4 | [`schema/patent-value-diagnostic.schema.json`](../../schema/patent-value-diagnostic.schema.json) | Diagnostic schema 1.0 |
| 5 | [`schema/v0.7-state.schema.json`](../../schema/v0.7-state.schema.json) | V0.7 state 块 |
| 6 | [`docs/cold-start-trap-checklist.md`](../cold-start-trap-checklist.md) | 陷阱表 |
| 7 | [`docs/cold-start-quick-reference.md`](../cold-start-quick-reference.md) | 冷启动速查 |
| 8 | [`docs/methodology/t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md) | 盲评协议（无密封键表） |
| 9 | 你的 coder-pack：[`t4-he3-coder-pack-a.md`](t4-he3-coder-pack-a.md) 或 [`t4-he3-coder-pack-b.md`](t4-he3-coder-pack-b.md) | 案表摘录 + 顺序 + 禁链 |

另允许：公开专利文本 / 官网 / 监管页（自行检索）；`validate_data` / CI 用法说明（若在 Getting Started 内）。

---

## 禁止打开（试验期间）

- `docs/methodology/t4-inter-rater-blind-case-table-h-e3.md`（**全文**，含 §F）  
- 任意 `analysis/non-award-validation/holdout-*-synthesis.md`  
- 任意 `analysis/non-award-validation/holdout/` 下与本轮专利对应的笔记  
- 任意 `reports/generated/DIAG-LEDGER-HOLDOUT-*`（及同义诊断）  
- 已合并 `data/ledgers/holdout-*` 中与本轮专利号对应的 Ledger  
- 另一 Coder 的草稿 / PR / 频道

完整禁链以各自 coder-pack §2 为准。

---

## 变更记录

| 日期 | 变更 |
|---|---|
| 2026-10-28 | 初版：固定可见路径；明确禁读全文案表 |
