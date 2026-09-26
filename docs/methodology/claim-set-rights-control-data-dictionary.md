# Claim-set Rights Control 0.1 — Data Dictionary

> Experimental only. Not part of the formal v1 Patent Value Ledger schema.

| Field | Meaning | Rule |
|---|---|---|
| `rights_control_id` | Rights Control快照唯一ID | 全数据集唯一 |
| `schema_version` | 实验Schema版本 | 当前固定为 `experimental-0.1` |
| `source_ledger_ids` | 对应现有Patent Value Ledger | 至少1个，必须存在 |
| `patent_id` | 专利/授权标识 | 不推断整件专利全部claim状态 |
| `claim_set_id` | 本记录研究的claim或claim set | 必须明确到claim层 |
| `claims_at_issue` | 具体claims | 至少1个 |
| `jurisdiction` | 权利状态所属司法辖区 | 不跨辖区继承 |
| `as_of_date` | 状态快照T0 | 所有事件/证据不得晚于T0 |
| `scope_type` | 单一claim、多claim、asserted set等 | 不代表价值高低 |
| `value_carrier_mapping.status` | claim set与价值载体映射是否建立 | Unknown ≠ no mapping |
| `value_carrier_mapping.carrier_ids` | 对应现有Ledger的value carrier | 不自动继承产品价值 |
| `adjudication_events` | 权利相关裁判/行政程序事件 | 可以有多个、方向可以变化 |
| `proceeding_type` | court / reexam / IPR / ITC等 | 只描述程序类型 |
| `outcome_category` | rights_upheld / rights_adverse / mixed等 | 不是总分 |
| `procedural_status` | final / remanded / further review等 | 与outcome分开 |
| `finality_state.status` | 整体正式性状态 | 与实体方向分开 |
| `finality_state.formal_effect` | 是否已有正式确认/取消等法律效果 | Caterpillar示例允许 `not_issued` |
| `operative_control.enforceability_state` | 当前排他控制是否实际可运作 | 允许与PTAB方向不一致 |
| `operative_control.remedy_types` | 与排他控制相关的禁令/排除令 | 不记录money damages |
| `operative_control.remedy_status` | remedy是否operative/stayed/vacated等 | 不等于cash realization |
| `evidence_ids` | 本对象使用的证据集合 | 必须存在且不晚于T0 |
| `notes` | 必要边界说明 | 不用于补造缺失事实 |

## Explicit non-fields

0.1明确**没有**：

- rights_control_score
- patent_value_score
- damages_amount
- realized_cash
- enforcement_financing_score
- design_around_score
- blocking_power_score

这些要么属于别的对象，要么尚未验证。
