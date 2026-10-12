# P1 — Rights Control 最小字段升格清单（对照 experimental-0.1）

> 状态：**V0.8 probe — research-only；NOT frozen / NOT adopted**。正式面仍为 **V0.7 + schema 1.0**。本文件不改任何 schema / validator / ledger。来源：[`../model-v0.8-design-draft.md`](../model-v0.8-design-draft.md) §7。

对象：`schema/experimental/claim-set-rights-control.schema.json`（14 required + notes）。依据：Package A 四对照 + Round 2 §2.1「claim-set identity、scope、adjudication、finality、operative control」。

| 字段 | 建议 | 理由 |
|---|---|---|
| `rights_control_id` | keep | 主键 |
| `schema_version` | keep（值待定；**不**决定） | 版本叙事属 Gate 1 / Q-M1 |
| `source_ledger_ids` | keep | 与 Ledger 1.0 并行链接的唯一桥 |
| `patent_id` | keep | |
| `claim_set_id` | keep | claim-set 粒度是核心发现 |
| `claims_at_issue` | keep | |
| `jurisdiction` | keep | Jurisdiction A ≠ B |
| `as_of_date` | rename → `t0_date`（候选） | 与 Ledger T0 术语统一；仅建议 |
| `scope_type` | keep；enum 可能需 `all_granted_claims` | 普通未诉专利无「asserted」集合 |
| `adjudication_events` | keep，但 **minItems 1 → 0（候选）** | **硬阻塞**：普通专利无裁决即无法建对象（见 P2） |
| `finality_state` | keep；无事件时需 `not_applicable` | 当前 enum 无此值 |
| `operative_control` | keep | LEO+不利 FWD 并存证据 |
| `value_carrier_mapping` | **drop from RC core**（候选） | 与 V0.7 E3 重复，存在双写漂移风险；改为经 `source_ledger_ids` 引用 |
| `evidence_ids` | keep | |
| `notes` | keep optional | |

最小核（8）：id、version、source_ledger_ids、patent_id、claim_set_id、jurisdiction、t0、operative_control。  
**未修改** experimental schema——改 minItems 会改变实验校验行为，留待 Gate 2 决策后再做。
