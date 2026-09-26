# Experimental Realization Path 0.1

状态：**experimental / non-adopted**  
依据：Issue #16 三路径复制完成  
正式架构：V0.7 remains adopted  
V0.8：research-only

## 1. 设计结论

三路径复制否定了线性的：

```text
Infringement → Remedy → Cash
```

实验0.1采用：

> **Canonical Event Log → Deterministic Snapshot**

研究者只维护事件。

当前状态由程序生成。

## 2. 两层数据结构

### Canonical input

`schema/experimental/realization-path-events.schema.json`

```text
Realization Path
├─ rights_subject
├─ path_type
├─ actor / counterparties
├─ jurisdiction
├─ as_of_date
└─ events[]
```

### Generated output

`schema/experimental/realization-path-snapshot.schema.json`

```text
Snapshot
├─ entitlement_state
├─ realization_mechanisms[]
├─ economic_realization
│  ├─ cash
│  ├─ control
│  └─ contractual_future_value
├─ observed_amount_events[]
├─ evidence_ids[]
└─ warnings[]
```

## 3. Rights Subject不是固定等于一件专利

0.1支持：

- claim_set
- patent
- portfolio
- field_rights
- receivable

这是Editas–Vertex路径带来的必要修正。

Portfolio/field license的金额不能机械继承给某一件成员专利。

## 4. Infringement不是必经节点

Editas路径没有merits infringement judgment。

因此Snapshot中的`entitlement_state`可以来自：

- rights_available
- asserted
- adverse
- unresolved
- established
- contractual
- unknown

其中`contractual`允许license / settlement / assignment等非侵权路径。

## 5. Realization Mechanism

0.1支持：

- license
- settlement
- damages_verdict
- judgment
- injunction
- exclusion_order
- assignment
- sale
- receivable_monetization

它取代过于诉讼中心的“Remedy State”。

## 6. Economic Realization

### Cash

回答：

> 现金到底有没有真正收到？

状态包括：
- none
- not_required
- unresolved
- received
- partial
- due
- contingent
- written_off
- mixed
- unknown

### Control

回答：

> 是否已经形成现实的排除/控制效果？

状态包括：
- operative
- stayed
- modified
- vacated
- expired
- not_applicable
- unknown

### Contractual / Future Value

保存：
- recurring_fee_right
- royalty_right
- contingent_payment_right
- receivable
- receivable_sold

## 7. 金额为什么单独保存

Snapshot有：

`observed_amount_events[]`

而没有：

`total_patent_value`

例如Taction：

- jury verdict：USD 5.7bn
- payment_status：unresolved
- cash.status：unresolved

因此代码层明确阻止：

> verdict amount = realized cash

Editas的三个金额也分别保留：
- license upfront
- annual fee
- receivable-sale proceeds

不自动相加成“专利价值”。

## 8. Event-sourcing规则

事件是唯一事实源。

`generated-snapshots.jsonl`由：

```bash
python tools/project_realization_paths.py
```

生成。

CI执行：

```bash
python tools/project_realization_paths.py --check
```

只要人工改了Snapshot而没有相应事件，CI失败。

## 9. 三个Canonical Fixtures

### Taction

必须得到：

```text
mechanism = damages_verdict
observed amount = ~USD 5.7bn
cash = unresolved
```

### Editas

必须得到：

```text
entitlement = contractual
mechanisms = license + receivable_monetization
cash = received
future value includes recurring / contingent / receivable_sold
```

### Wirtgen

必须得到：

```text
mechanism = exclusion_order
control = operative
cash = not_required
```

## 10. 与Rights Control的边界

Claim-set Rights Control回答：

> 权利本身当前控制到哪里？

Realization Path回答：

> 权利人实际上沿什么路径取得经济结果？

二者可以互相链接，但不能合并。

## 11. Enforcement Capacity

0.1只保留可选context：

- not_assessed
- observed_context
- unknown

不设置：
- financing score
- counsel score
- expert score
- enforcement score

原因是三路径复制尚未证明这些变量可以作为价值正向指标。

## 12. Adoption Boundary

Experimental 0.1通过CI意味着：

> Realization Path已经成为可测试的event-sourced数据对象。

不意味着：
- V0.8 adopted；
- formal v1 Ledger改变；
- 可以计算Realization Score；
- observed amounts可以汇总为intrinsic patent value。

