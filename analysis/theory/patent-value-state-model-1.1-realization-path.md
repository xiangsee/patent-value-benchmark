# Patent Value State Model 1.1 — Realization Path Refinement

日期：2026-09-26  
状态：Research refinement after Issue #16 three-path replication  
正式架构：V0.7 remains adopted  
V0.8：research-only

## 一、为什么需要1.1

Patent Value State Model 1.0把Realization Path暂时写成：

```text
Infringement State
→ Remedy State
→ Cash / Economic Realization State
```

三路径复制以后，这个结构被证明过于线性、过于诉讼中心。

三个样本：

1. Taction — litigation / damages verdict
2. Editas–Vertex — voluntary license / cash / receivable monetization
3. Wirtgen — ITC exclusion / control realization

说明：

> **Realization Path不是固定流水线，而是事件驱动、可以分叉的路径。**

## 二、三个必须修正的地方

### 1. Infringement不是必经节点

Editas–Vertex没有merits infringement judgment。

但：
- license executed
- upfront cash received
- annual fee received
- future receivables monetized

所以：

`infringement_state`

只能是optional path state。

### 2. Remedy State太窄

License不是remedy。

Assignment不是remedy。

Receivable monetization也不是remedy。

因此应改为：

# Realization Mechanism

可能包括：
- license
- settlement
- damages verdict
- judgment
- injunction
- exclusion order
- sale / assignment
- receivable monetization

### 3. Cash Realization太窄

Wirtgen的LEO实现了真实经济控制，却不需要一笔现金赔偿。

因此应改为：

# Economic Realization State

并区分channel：

```text
Cash
Control
Contractual / Future Value
```

## 三、1.1核心对象

```text
Realization Path
├─ rights_subject
│  ├─ claim_set
│  ├─ patent
│  ├─ portfolio
│  ├─ field_rights
│  └─ receivable
│
├─ path_type
│
├─ events[]
│  ├─ event_type
│  ├─ event_date
│  ├─ actor / counterparty
│  ├─ state_effect
│  └─ evidence_ids
│
└─ current_snapshot
   ├─ entitlement_state
   ├─ realization_mechanisms[]
   └─ economic_realization
      ├─ cash
      ├─ control
      └─ contractual_future_value
```

## 四、Event Log优先于Snapshot

这一轮最重要的治理发现是：

> **事实先进入事件日志，当前状态由事件确定性投影出来。**

原因：

- Taction的状态会被上诉逆转；
- License会产生持续付款；
- Receivable可以被再次转让；
- Exclusion order会被stay / modify / vacate / expire。

如果研究者手工维护“当前状态”，很容易和事件史漂移。

因此未来实验Schema必须支持：

```text
Events → deterministic projection → Snapshot
```

而不是两个地方分别人工填写。

## 五、建议的三类Economic Realization

### A. Cash

- cash_received
- partial_cash_received
- payment_due
- contingent_payment
- judgment_unpaid
- unknown

### B. Control

- injunction_operative
- exclusion_operative
- stayed
- modified
- vacated
- expired
- not_applicable

### C. Contractual / Future Value

- recurring_fee_right
- royalty_right
- contingent_payment_right
- receivable
- receivable_sold

## 六、Realization Path与Rights Control仍然分开

Rights Control回答：

> 这个claim set现在有没有法律控制能力？

Realization Path回答：

> 权利人实际上沿哪条路径把这种控制转化成经济结果？

例如Wirtgen：

```text
Rights Control:
  claim 29 survives IPR challenge

Realization Path:
  ITC infringement → LEO → exclusion remains outstanding
```

例如Editas：

```text
Rights Subject:
  portfolio / field rights

Realization Path:
  license → cash → recurring fee → receivable monetization
```

两者不应合并。

## 七、Enforcement Capacity继续延后

三路径复制没有支持把：

- financing
- counsel quality
- expert budget
- procedural endurance

做成价值正向指标。

最多可以说：

> **Enforcement Capacity影响哪些路径可用、路径能坚持多久，但不证明权利或技术质量。**

所以1.1继续把它保留为context。

## 八、Schema设计资格

Issue #16预注册的三条路径已经完成：

- litigation/damages：Taction
- license/cash：Editas–Vertex
- exclusion/control：Wirtgen

并且Editas案例已经提供后续变化：

```text
license
→ upfront cash
→ annual cash fee
→ receivable monetization
```

因此现在满足：

> **Experimental Realization Path Schema 0.1 可以开始设计。**

但正式Ledger Schema仍不修改。

