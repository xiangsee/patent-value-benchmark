# Realization Path 0.1 — Data Dictionary

> Experimental only. Event logs are canonical; snapshots are generated.

## Event Log

| Field | Meaning | Rule |
|---|---|---|
| `path_id` | 一条价值实现路径的唯一ID | 全实验集唯一 |
| `rights_subject.scope_type` | 路径针对的权利经济对象 | claim_set / patent / portfolio / field_rights / receivable |
| `rights_subject.identifiers` | 对象标识 | 不自动拆分/合并价值 |
| `path_type` | 路径主要类型 | 不等于价值大小 |
| `actor` | 价值实现主体 | 通常为权利人/许可方 |
| `counterparties` | 对手方/交易方 | 至少1个 |
| `jurisdiction` | 路径所在法律/交易语境 | 不跨辖区继承 |
| `as_of_date` | Snapshot截止日 | Event/Evidence不得晚于此日 |
| `events[]` | 唯一事实源 | Snapshot不得手工维护 |
| `event_type` | 状态迁移事件 | 见event vocabulary |
| `event_date` | 精确日期（如有） | exact时必须填写 |
| `date_precision` | 日期精度 | exact / quarter / year / unknown |
| `state_effect` | 事件改变了什么 | 描述事实，不打分 |
| `amount` | 某事件观察到的金额 | 保留scope/payment status |
| `amount_scope` | 金额法律/交易类型 | verdict、license_upfront、annual_fee等 |
| `payment_status` | 金额是否实际兑现 | verdict可以是unresolved |
| `economic_object` | 该金额针对什么经济对象 | portfolio / field_rights / receivable等 |
| `contractual_future_effects` | 新产生的未来合同权利 | 不视为已收现金 |
| `evidence_ids` | 事件证据 | 必须存在且不晚于T0 |
| `enforcement_capacity_context` | 实现能力背景 | 0.1不评分 |

## Generated Snapshot

| Field | Meaning | Rule |
|---|---|---|
| `snapshot_id` | 派生快照ID | `SNAP-<path_id>` |
| `entitlement_state` | 当前权利/合同路径状态 | 由事件投影 |
| `realization_mechanisms` | 已出现的实现机制 | 可多种并存 |
| `economic_realization.cash.status` | 现金实现状态 | verdict不等于received |
| `economic_realization.control.status` | 排除/控制实现状态 | 允许cash=not_required |
| `contractual_future_value.states` | 未来合同/应收权利 | 与cash分离 |
| `observed_amount_events` | 原scope金额事件 | **不求和为专利总价值** |
| `evidence_ids` | Snapshot依赖的证据集合 | 由Events自动汇总 |
| `warnings` | 固定治理提示 | 由projector生成 |

## Event Vocabulary 0.1

### Entitlement / merits
- rights_available
- assertion
- infringement_alleged
- adverse_merits_decision
- infringement_established

### Procedure
- appeal
- vacatur_remand
- reopened

### Valuation / damages
- apportionment_challenged
- expert_evidence_excluded
- expert_evidence_admitted
- jury_verdict
- judgment_entered
- judgment_modified
- verdict_vacated

### Transaction
- license_executed
- settlement_executed
- assignment
- sale
- cash_payment_received
- partial_cash_received
- recurring_fee_received
- contingent_payment_created
- receivable_created
- receivable_monetized

### Control
- injunction_issued
- exclusion_order_issued
- remedy_stayed
- remedy_modified
- remedy_vacated
- remedy_expired
- remedy_outstanding

### Loss
- written_off

## Explicit non-fields

0.1没有：

- realization_score
- intrinsic_patent_value
- total_observed_amount
- enforcement_capacity_score
- verdict_to_cash_multiplier

这是有意设计。
