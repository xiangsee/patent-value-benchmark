# Experimental Claim-set Rights Control 0.1

状态：**experimental / non-adopted**  
依据：Rights Control 4/4 preregistered replication threshold  
正式架构：V0.7 remains adopted

## 1. 为什么现在可以做Schema

Package A已经完成四组跨场景复制：

1. i4i × Amgen
2. Apple ’381 claim 19 × ’915 claim 8
3. SynQor ’702 claim 56 × ’021 claim 30
4. Wirtgen ’309 claim 29 × Caterpillar ’693 claim 19

四组都出现了同一结构：

> **Value Realization不能推导Claim-set Rights Control。**

而且第四组证明，Rights Control甚至不能压成简单的valid / invalid。

因此本轮允许把已经重复出现的字段变成**实验性数据对象**。

## 2. 设计目标

这个对象只回答：

> 在某一T0、某一司法辖区，对某一claim/claim set，法律控制状态是什么？

它不回答：
- 这项专利总价值多少；
- 技术有多先进；
- 产品赚了多少钱；
- 诉讼最终能收多少钱；
- 权利人资金有多强。

## 3. 最小对象

```text
claim_set_rights_control
├─ identity
│  ├─ patent_id
│  ├─ claim_set_id
│  ├─ claims_at_issue[]
│  ├─ jurisdiction
│  └─ as_of_date
├─ value_carrier_mapping
├─ adjudication_events[]
├─ finality_state
├─ operative_control
└─ evidence_ids[]
```

### adjudication_events

记录：
- proceeding_type
- forum
- decision_date
- claims_at_issue
- outcome_category
- outcome_detail
- procedural_status
- evidence_ids

它允许多个事件按时间进入同一claim-set记录。

### finality_state

专门回答：

> 裁判已经产生到什么正式法律效果？

这是Wirtgen/Caterpillar Pair #4证明必须独立存在的维度。

### operative_control

专门回答：

> 即便存在某个不利/有利裁判，当前是否仍存在实际排除或执行能力？

例如 Caterpillar claim 19 在2020-01-21可以同时出现：
- PTAB FWD：unpatentable
- cancellation certificate：not issued
- ITC LEO：operative

这是**合法状态，不是数据冲突**。

## 4. 为什么不提供Rights Control Score

实验对象明确拒绝：

`rights_control_score = 82`

因为同一T0可以存在方向相反的状态：
- adverse adjudication
- incomplete finality
- operative exclusion remedy

如果压成一个分数，最重要的信息会被消失。

## 5. 与Realization Path的边界

Taction之后，以下字段不进入本对象：

- accused-party infringement path
- damages / royalty / apportionment
- jury verdict amount
- settlement / collection
- litigation financing
- counsel/expert capacity

这些属于独立的 **Realization Path / Enforcement Capacity** 研究对象。

Rights Control只保留与当前排他控制直接相关的operative control。

## 6. 暂缓字段

以下仍是Counterfactual Control研究候选，不进入0.1：

- design_around_cost
- design_around_time
- blocking_power
- FTO_dependency
- performance_loss_if_removed

原因不是它们不重要，而是4/4复制没有系统验证它们。

## 7. 验证规则

实验validator执行：

1. JSON Schema严格校验；
2. rights_control_id唯一；
3. source Ledger必须存在；
4. Evidence ID必须存在；
5. adjudication event不能晚于T0；
6. Evidence observed_date不能晚于T0；
7. 非Unknown mapping/finality/operative state必须有证据；
8. **不禁止“adverse adjudication + operative remedy”并存。**

第8条是本Schema最关键的反布尔逻辑。

## 8. Backfill

`data/experimental/rights-control/four-pair-backfill.jsonl`

当前包含四组研究对应的全部可用claim-set对象，包括：
- i4i asserted claims 14/18/20
- Amgen ’165 claims 19/29
- Amgen ’741 claim 7
- Apple ’381 claim 19
- Apple ’915 claim 8
- SynQor ’702 claim 56
- SynQor ’021 claim 30
- Wirtgen ’309 claim 29
- Caterpillar ’693 claim 19

## 9. Adoption boundary

Experimental 0.1通过CI，只表示：

> **Rights Control已经从研究文字变成可测试数据对象。**

它不表示：
- V0.8 adopted；
- 正式Ledger Schema改变；
- Rights Control已经可以做总分；
- Counterfactual Control已经验证。

