# P4 — Network JSON 键名对齐草图（三例）

> 状态：**V0.8 probe — research-only；NOT frozen / NOT adopted**。正式面仍为 **V0.7 + schema 1.0**。本文件不改任何 schema / validator / ledger。来源：[`../model-v0.8-design-draft.md`](../model-v0.8-design-draft.md) §7。

| 文件 | 顶层独有键 | edge 键 | relation 词表 |
|---|---|---|---|
| `crispr-portfolio-network.json` | `non_inheritance_rules` | from/to/relation/status/evidence_ids | **自由文本**（11 种句子） |
| `avc-sep-pool-network.json` | `anchor_patent`、`v0_7_standalone_limit`、`comparison_to_crispr` | from/to/relation/detail（无 evidence_ids） | snake_case 9 种 |
| `byd-blade-ctp-portfolio-network.json` | `anchor_patent`、`h3_pressure_test` | from/to/relation/detail/status/evidence_ids | snake_case 7 种 |

共通核：`network_id, status, t0_date, purpose, nodes[id,label,type], edges[from,to,relation]`。

## 命名约定草案（不改现有 JSON）

1. edge 统一 `from,to,relation,status,evidence_ids,detail`；`evidence_ids` 应必有（AVC 缺）。
2. relation 用 snake_case 受控词表；共享项候选：`owns, licenses_to, member_of, contains_claim_set, essential_to, blocks, complements, exact_implemented_in, not_apportioned_to`。
3. `not_apportioned_to` 在 AVC 与 Blade 都独立出现 → 支持「非继承」作为一等边，而非注释。
4. 节点 type 已大体一致（patent / claim_set / portfolio / product），保留。

历史 `relation` 字符串仍不回写。**词汇约定已固化为** [`p8-network-relation-vocabulary-v0.md`](p8-network-relation-vocabulary-v0.md)；三例仅增加非破坏顶层 `convention` 指针。完整 schema/S3 仍需非教科书样本与用户批准。
