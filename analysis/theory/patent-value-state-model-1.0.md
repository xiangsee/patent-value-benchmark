# Patent Value State Model 1.0

日期：2026-09-26  
状态：Conceptual research model — not a formal schema version  
正式架构：V0.7 remains adopted  
V0.8：research-only

## 一、核心区分

本模型从一个最容易混淆的问题开始：

> **一项专利创造了多少经济价值，和权利人在某个时间点能够实现多少价值，不是同一个问题。**

这里至少有两类对象：

### Economic Value Base

回答：

> 技术 / 产品 / 市场到底创造了什么价值？

它主要来自：
- technology
- product / process / platform
- market / operating results
- patent-to-value-carrier mapping

### State-dependent Realizable Value

回答：

> 在时间 t、司法辖区 j、给定当前权利状态、程序状态和权利人能力的条件下，这项权利还有哪些价值实现路径？

它不是一个固定金额。

它是一组**条件状态**。

---

## 二、不要把“动态价值”当成理论发明

本项目不声称发现“专利价值是动态的”。

既有研究已经明确讨论：
- 专利在不完全可执行、有效性不确定的条件下具有实物期权特征；
- 专利价值不仅由底层技术决定，也受property-right uncertainty影响；
- 法律请求权可以沿程序节点变化，并包含继续、和解、放弃等选择权。

理论锚点包括：

- Alan C. Marco, *The option value of patent litigation: Theory and evidence*, Review of Financial Economics 14 (2005), 323–351.
  - https://ideas.repec.org/a/eee/revfin/v14y2005i3-4p323-351.html
- Jose Portela, Eduardo S. Schwartz & Jaime Aparicio Garcia, *Litigation Risk and the Valuation of Legal Claims: A Real Option Approach*, NBER Working Paper 33790 (2025).
  - https://www.nber.org/papers/w33790

本项目更具体的贡献是：

> **把抽象的动态价值问题，拆成可追溯、可比较、可进入benchmark的数据状态。**

---

# 三、三层模型，而不是六个孤立分数

Taction案例启发出六类状态：

- Technology
- Product
- Rights
- Infringement
- Remedy
- Realization

但在benchmark中，更适合把它们组织成三层。

## Layer A — Value Base

### Technology State

回答：
- 技术解决什么问题？
- 技术机制是什么？
- 与替代方案相比如何？

对应现有资产：
- `technology`
- `relative_differentiation`
- Value State中的technical differentiation

### Product State

回答：
- 技术进入了什么产品 / 工艺 / 平台？
- 是否真实实施？
- 是否规模化？
- 有什么产品 / 项目 / 企业层经济暴露？

对应现有资产：
- `value_carriers`
- `value_links`
- real-world validation
- scale / diffusion
- product / enterprise metrics

**Value Base回答“价值被创造在哪里”。**

它不等于权利人能够捕获的价值。

---

## Layer B — Rights Control

### Rights State

回答：
- 哪些claim真正覆盖价值载体？
- scope如何？
- validity / patentability处于什么状态？
- proceeding / finality如何？
- 当前是否还能实际排除？

这就是已经完成4/4复制验证的：

> **Claim-set Rights Control**

核心原则：

> Patent-level analysis ≠ Claim-set rights analysis.

并且：

> Rights Control不是valid / invalid布尔值，而是带T0的状态向量。

---

## Layer C — Realization Path

这是Taction对现有模型真正新增的部分。

### Infringement State

回答：

> 针对特定主体 / 产品 / claim set，侵权问题目前走到了哪里？

候选状态不能只写 yes / no。

至少可能出现：
- not asserted
- claim-charted / alleged
- IPR / validity challenge pending
- summary judgment noninfringement
- summary judgment vacated / remanded
- trial infringement
- no infringement
- appeal pending
- infringement affirmed / vacated

它与Product State不同。

产品可能明确实施某技术，但某个被告是否**法律上侵犯特定claim**是另一件事。

### Remedy State

回答：

> 在当前法律状态下，权利人能够主张什么救济，以及金额论证走到了哪里？

至少区分：
- no remedy theory yet
- royalty theory
- lost profits
- damages expert model
- apportionment disputed
- expert evidence excluded / admitted
- jury verdict
- court judgment
- injunction / exclusion order
- enhanced damages
- remedy vacated / modified

核心原则：

> **Observed remedy amount ≠ intrinsic patent price.**

### Cash / Economic Realization State

回答：

> 已经形成的法律请求或判决，最终兑现到什么程度？

至少区分：
- verdict unpaid
- post-trial motions pending
- appeal pending
- settlement reached
- judgment final
- enforcement / execution pending
- collected / paid
- partially collected
- written off / unrecoverable
- unknown

这一步不能和jury verdict混为一谈。

---

# 四、避免与V0.7的“Realization Stage”发生概念冲突

V0.7已有：

`R0 → R5`

它描述：
- right exists
- market/transfer intent
- rights transaction
- implementation
- scaled validation
- patent-level attributable value

这个结构继续保留，不应为了Taction马上改名或破坏兼容性。

但需要明确：

> **V0.7 Realization Stage ≠ Cash / Legal Realization State。**

V0.7主要回答：

> 专利与现实价值载体、现实价值证据连接到了哪里？

新的Realization Path回答：

> 权利人沿某条许可 / 诉讼 / 执行路径，已经走到哪个法律和经济节点？

两者并列，而不是互相替代。

---

# 五、四个横切变量

六个状态不能脱离上下文。

## 1. Time / T0

所有状态都必须带时间。

2023的不侵权简易判决不能用2026年的陪审团结果回填。

## 2. Jurisdiction

同一claim family在不同国家可能：
- validity不同
- infringement标准不同
- remedy不同
- enforcement能力不同

Jurisdiction必须贯穿Rights / Infringement / Remedy。

## 3. Evidence / Observability

同一个真实状态可能：
- public
- regulated/disclosed
- internal
- restricted
- unknown

Unknown ≠ zero。

## 4. Enforcement Capacity

这是Taction带来的另一个重要修正。

它回答的不是：

> 这件专利质量有多高？

而是：

> 权利人有没有能力把潜在法律权利推进到更远的价值实现节点？

候选上下文包括：
- litigation / enforcement financing
- lawyer / expert resources
- claim-chart and testing readiness
- discovery access
- procedural endurance / appeal capacity
- execution / collection capability

核心原则：

> **Enforcement Capacity可以改变Realization Path，但不能反向证明Technology Quality或Rights Quality。**

诉讼融资、强律师团队或充足专家预算：
- 可以让权利走得更远；
- 不能证明专利一定有效；
- 不能证明一定侵权；
- 不能证明最终一定胜诉。

Enforcement Capacity暂时只作为research context，不进入正式Schema。

---

# 六、Taction案例：为什么需要Realization Path

研究对象：

- US10,659,885
- US10,820,117
- Taction Technology v. Apple

## Snapshot A — 2023

地区法院作出不侵权简易判决。

正确表达不是：

> 专利价值 = 0

而是：

```text
Value Base:
  technology / product exposure still exists

Rights Control:
  patent rights still exist

Infringement State:
  adverse — summary judgment noninfringement

Remedy State:
  effectively blocked against Apple at this stage

Cash Realization:
  none from this claim path
```

对Apple这一条路径的**State-dependent Realizable Value显著下降**。

## Snapshot B — 2025-08-13

Federal Circuit撤销并发回。

法院认为地区法院在claim construction以及专家证据处理方面存在错误。

没有马达因为上诉发生变化。

变化的是：

```text
Infringement State:
  summary judgment vacated
  claim path reopened

Rights / procedural uncertainty:
  changed

Future realization paths:
  expanded
```

## Snapshot C — 2026-08 / 09

庭前围绕apportionment出现激烈专家证据争议。

2026-08-11，地区法院排除部分技术apportionment意见，并连带排除依赖这些意见的reasonable-royalty意见。

2026-09-03，法院只允许有限补充既有证据，不允许用全新的测试体系重做apportionment。

这说明：

> 即使假设“有权利 + 有侵权”，也不能自动得到“值多少钱”。

Remedy State需要单独记录：
- damages theory
- apportionment evidence
- expert admissibility
- royalty / lost-profits methodology

## Snapshot D — 2026-09-25

陪审团认定Apple侵犯两件Taction专利，并给出约USD 5.7bn损害赔偿verdict。

这是：

> **Legal Valuation Event**

但不是最终现金实现。

因此截至verdict时，更准确的状态是：

```text
Infringement State:
  jury infringement finding

Remedy State:
  ~USD 5.7bn jury verdict

Cash / Economic Realization State:
  post-trial / appeal / settlement / execution unresolved
```

所以：

> **$5.7B Jury Verdict ≠ $5.7B Realized Value**

---

# 七、State-dependent Realizable Value不是新总分

本项目不应引入：

`realizable_value_score = 87`

更不应引入：

`patent_value = technology × rights × enforcement × damages`

原因是：
- 状态可能互相冲突；
- 程序可能逆转；
- 金额scope不同；
- 不同路径之间存在optionality；
- Enforcement Capacity属于owner/context，不属于专利内在属性。

更合理的输出是一个Snapshot：

```text
Patent Value Snapshot @ T0
├─ Value Base
│  ├─ Technology State
│  └─ Product State
├─ Rights Control
├─ Realization Path
│  ├─ Infringement State
│  ├─ Remedy State
│  └─ Cash Realization State
├─ Value Horizon
├─ Portfolio & Jurisdiction Context
├─ Enforcement Capacity Context
└─ Evidence / Observability
```

这是：

> **价值 × 状态 × 实现路径**

而不是一个总分。

---

# 八、与现有Benchmark的关系

这次不是推翻现有架构。

相反，它把各模块的位置变清楚了。

### 已经被验证的

- V0.7 Realization / Evidence architecture
- Claim-set Rights Control
- Two Clocks / Value Horizon
- Portfolio & Jurisdiction Network

### Taction新暴露的

- Infringement State
- Remedy State
- Cash / Economic Realization State
- Enforcement Capacity context

因此下一步应当：

1. Issue #15继续只设计Claim-set Rights Control；
2. 另开Realization Path实验对象；
3. 不把Infringement / Remedy / Cash realization塞进Rights Control；
4. 不改正式v1 Ledger Schema；
5. 先用Taction及至少两个不同实现路径案例验证。

---

# 九、研究治理

Taction带来的新维度是在Round 2过程中发现的。

因此不能偷偷修改原V0.8 adoption threshold。

正确做法：

> **先作为exploratory dimension记录；重新预注册验证条件；验证后再决定是否成为V0.8正式候选。**

这避免“看到一个漂亮案例就改模型”。

---

# 十、一句话定义

Patent Value State Model 1.0可以暂时定义为：

> **专利价值不是一个静止价格，而是一组在特定时间、司法辖区、权利状态与实现能力条件下不断迁移的价值状态；benchmark的任务不是替它算出一个永恒分数，而是记录价值在哪里被创造、权利控制到哪里、以及它距离真正实现还有多远。**

