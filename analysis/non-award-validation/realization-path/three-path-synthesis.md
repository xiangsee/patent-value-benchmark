# Realization Path — Three-Path Replication Synthesis

日期：2026-09-26  
状态：Issue #16 preregistered three-path replication complete  
正式架构：V0.7 remains adopted  
V0.8：research-only

## 一、三条路径

### Path A — Taction v. Apple

类型：

> litigation → merits → damages verdict

关键状态：

```text
summary judgment noninfringement
→ CAFC vacatur/remand
→ apportionment evidence dispute
→ jury infringement
→ ~$5.7bn verdict
→ cash realization unresolved
```

### Path B — Editas → Vertex → DRI

类型：

> voluntary license → cash → recurring fee → secondary monetization

关键状态：

```text
non-exclusive license
→ $50m upfront cash received
→ $10m annual fee received
→ future license receivables
→ $57m DRI monetization
```

没有merits infringement verdict。

### Path C — Wirtgen ITC

类型：

> infringement → exclusion order → continuing control

关键状态：

```text
claim 29 infringement
→ Limited Exclusion Order
→ order remains outstanding
```

主要实现的是排除/控制，而不是现金。

---

# 二、原来的线性模型没有通过压力测试

Taction之后，我们曾暂时设想：

```text
Infringement State
→ Remedy State
→ Cash Realization State
```

三路径复制以后，这个模型需要修改。

原因：

### Editas

没有Infringement State，仍然可以直接实现现金。

### Wirtgen

有侵权和救济，但价值实现主要表现为control，不是cash。

### Editas → DRI

许可路径还可以继续分叉，未来应收款本身被再次金融化。

所以：

> **Realization Path不是一条固定流水线，而是一张事件驱动的有向路径。**

---

# 三、建议的新核心抽象

## 1. Rights Subject

Realization Path的对象不能只允许exact patent / claim set。

需要至少支持：

- claim_set
- patent
- portfolio
- field_rights
- license_receivable

Editas证明portfolio/field rights本身就是可实现价值对象。

## 2. Entitlement State — optional

用于记录：
- infringement alleged
- infringement adjudicated
- contractual entitlement
- ownership / license entitlement
- not_required

不能把infringement设为所有路径的必填项。

## 3. Realization Mechanism

替代过于诉讼中心的`Remedy State`。

候选机制：

- license
- settlement
- damages_verdict
- judgment
- injunction
- exclusion_order
- assignment
- sale
- receivable_monetization

## 4. Economic Realization State

替代过窄的`Cash Realization State`。

至少区分：

### Cash

- cash_received
- partial_cash
- payment_due
- contingent_cash
- judgment_unpaid
- unknown

### Control

- exclusion_operative
- injunction_operative
- stayed
- vacated
- expired
- not_applicable

### Contractual / Future Value

- recurring_fee_right
- royalty_right
- contingent_payment_right
- receivable
- receivable_sold

---

# 四、最重要的新发现：Event Log + Snapshot

三条路径都说明，仅记录“当前状态”还不够。

更稳的结构应该是：

```text
Realization Path
├─ rights_subject
├─ path_type
├─ events[]
│   ├─ event_type
│   ├─ date
│   ├─ state_effect
│   └─ evidence
└─ current_snapshot
    ├─ entitlement_state
    ├─ mechanisms[]
    └─ economic_realization
```

也就是说：

> **事实先进入Event Log，Snapshot由事件确定性投影出来。**

这与我们现有Ledger → Diagnostic的治理逻辑一致。

不应该让研究者手工分别维护事件史和当前状态，否则一定会漂移。

---

# 五、建议的State-transition Vocabulary 0.1

## Entitlement / merits

- assertion
- infringement_alleged
- adverse_merits_decision
- infringement_established
- contractual_entitlement
- not_required

## Procedure

- appeal
- vacatur_remand
- stay
- finality
- reopened

## Valuation / damages

- apportionment_challenged
- expert_evidence_excluded
- expert_evidence_admitted
- jury_verdict
- judgment_entered
- judgment_modified
- verdict_vacated

## Transaction

- license_executed
- settlement_executed
- assignment
- sale
- recurring_fee_received
- receivable_created
- receivable_monetized

## Control remedy

- injunction_issued
- exclusion_order_issued
- remedy_stayed
- remedy_modified
- remedy_vacated
- remedy_expired
- remedy_outstanding

## Economic realization

- cash_received
- partial_cash_received
- contingent_payment
- control_realized
- future_cash_right_created
- written_off
- unknown

---

# 六、预注册门槛判定

Issue #16要求至少三种路径：

1. Taction-type merits + damages path — **完成**
2. License / settlement without merits verdict — **完成：Editas–Vertex**
3. Injunction / exclusion-order path — **完成：Wirtgen**

另要求至少一个案例包含重大事件后的后续实现/变化。

Editas满足：

```text
license
→ upfront received
→ annual fee received
→ future receivables monetized to DRI
```

因此：

# Three-path preregistration threshold met

---

# 七、Enforcement Capacity还没有达到Schema门槛

Taction中存在诉讼融资和强诉讼资源。

但Editas和Wirtgen说明Realization Path也可以：
- 通过交易形成；
- 通过政府排除救济形成。

因此目前最多可以保留：

> **Enforcement Capacity affects available path choices and path endurance.**

但还不能冻结：
- financing score
- counsel score
- expert score
- evidence-readiness score

Issue #16中Enforcement Capacity应继续作为context，不进入第一个Realization Path Schema必填字段。

---

# 八、下一步

现在已经满足“设计实验Schema之前先完成三路径复制”的治理条件。

因此下一轮可以进入：

# Experimental Realization Path Schema 0.1

但必须采用这一轮修正后的结构：

> **Event Log + deterministic Snapshot**

而不是原来固定的：

> Infringement → Remedy → Cash

