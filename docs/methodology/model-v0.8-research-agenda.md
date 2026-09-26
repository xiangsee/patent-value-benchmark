# V0.8 Research Agenda — Value Construct, Rights Control & Portfolio Network

状态：**Research Agenda — not adopted**

V0.7继续是当前正式架构。

V0.8研究的核心问题不是“再多加几个指标”，而是解决：

> **不同value construct被混用，以及专利权控制力、价值时间结构、组合/许可/司法辖区网络尚未被显式建模。**

## Round 1 non-award pressure test — completed

第一轮机制型非奖项样本已完成：

1. **i4i v. Microsoft** — patent-level litigation value / enforcement
2. **Amgen v. Sanofi** — claim-set validity / enablement
3. **PageRank / Stanford → Google** — same-patent two-T0 / Two Clocks
4. **CRISPR-Cas9** — portfolio / license / jurisdiction dependency

综合见：

`analysis/non-award-validation/round1-cross-case-synthesis-v0.8.md`

### Round 1 hypothesis status

- **H1 Rights Control:** supported in the first contrasting pair; replication still required.
- **H2a Date/context dependence:** supported.
- **H2b Two Clocks:** supported.
- **H2c Clean early-stage option value:** not yet tested.
- **H3 Portfolio Dependency:** supported.
- **H4 Monetary evidence is contextual, not intrinsic price:** supported across litigation and portfolio-license mechanisms.

这些结果**不触发V0.8 adoption**。

---

## Candidate additions

### 1. Value Construct

每次研究先声明目标：

- policy_statistical
- technological_quality
- private_asset
- realized_operating
- social_strategic

可多选，但必须区分。

### 2. Claim / Claim-set Rights Control

Amgen压力测试表明，简单的patent-level valid / invalid状态可能过粗。

候选对象：

- claim_set_id
- scope_type
- legal_status
- validity_status
- adjudication_status
- enforceability
- ownership_clarity
- jurisdiction
- remaining_term
- encumbrance
- value_carrier_mapping

核心原则：

> **Patent-level analysis ≠ Claim-set rights analysis.**

### 3. Counterfactual Control

候选问题：

- next_best_alternative
- design_around_cost
- design_around_time
- performance_loss_if_removed
- blocking_power
- freedom_to_operate_dependency

### 4. Value Horizon

PageRank同一专利双T0测试支持把Patent Age拆成“两只钟”：

- realized_value_history
- survival / revealed-value clock
- remaining_exclusivity clock
- remaining_patent_term
- option / future value

核心原则：

> **Realization Stage ≠ Value Level.**

R0–R5回答“价值实现到了哪里”，不承担跨时间的价值大小或折旧评分。

### 5. Portfolio & Jurisdiction Network

CRISPR压力测试表明，“Portfolio Context”很可能不能只是Ledger中的一个枚举字段。

候选独立graph object：

```text
PORTFOLIO & JURISDICTION NETWORK
├─ patents / applications
├─ claim sets
├─ owners / co-owners
├─ licensees / sublicensees
├─ complementary rights
├─ blocking / competing rights
├─ interference / opposition / litigation edges
├─ product / process mappings
├─ jurisdiction-specific rights state
└─ time / procedural state
```

至少需要支持：

- standalone patent
- complementary portfolio
- blocking / competing portfolio
- cross-license
- stacked licenses
- SEP / standard
- patent pool
- jurisdiction-specific validity/enforceability

核心原则：

> **Portfolio value ≠ sum of single-patent values.**

> **Jurisdiction A status ≠ Jurisdiction B status.**

### 6. Screening Signals

单独放置，不进入价值事实：

- forward citations
- backward citations
- NPL citations
- family size
- claims
- generality/originality/radicalness
- grant lag
- renewal age
- litigation/opposition

所有signals需要考虑：

- technical-field normalization
- cohort/age normalization
- data lag
- jurisdiction differences

---

## Monetary evidence rule

Round 1横跨两种金额场景：

- i4i：litigation damages
- CRISPR：portfolio/field license consideration

暂定硬规则：

> **Observed money is evidence with scope, date, actor and legal context — not intrinsic patent price.**

因此必须区分：

- patent-level damages
- single-patent license
- portfolio license
- field license
- product revenue
- enterprise revenue
- transaction price

不同scope不得互相继承。

---

## Non-goals

V0.8不以：

- 生成总分
- 预测Gold
- 把bibliometric proxy变成直接价值
- 用年龄做单向正/负指标
- 把portfolio value机械平均到成员专利
- 把一个司法辖区的权利状态复制到其他国家
- 把产品收入自动归因给专利

为目标。

---

## Validation design — Round 2

Round 1已经明确架构方向，下一阶段不继续无边界增加字段，而进入**最小复制验证集**。

### Package A — Rights Control Replication

目标：累计完成至少4组 Same-realization / Different-rights-control 对照。

当前已完成：
1. i4i v. Microsoft × Amgen v. Sanofi
2. Apple v. Samsung：US7469381 claim 19 × US7844915 claim 8
3. SynQor：US7564702 claim 56 × US7272021 claim 30
4. Wirtgen US7828309 claim 29 × Caterpillar US7140693 claim 19

第四组进入工业道路铣刨机械，并继续保持R4对R4。Wirtgen claim 29在IPR中未被证明不可专利；Caterpillar claim 19则出现PTAB不可专利FWD，但同一T0尚未发出取消证书且ITC LEO仍然有效。由此进一步验证Rights Control需要claim-set、程序、finality和operative remedy四类状态。

**Package A 4/4预注册门槛已完成。**

Experimental Claim-set Rights Control Schema 0.1 已实现并进入CI验证：

- `schema/experimental/claim-set-rights-control.schema.json`
- `data/experimental/rights-control/four-pair-backfill.jsonl`
- `tools/validate_rights_control.py`
- `tests/test_rights_control.py`

它是可测试实验对象，不等于V0.8 adopted，也不改变正式v1 Ledger Schema。

样本要求：
- realization stage接近；
- rights-control状态显著不同；
- 尽量跨行业；
- 优先具有claim-level裁判或明确法律状态。

检验：
- Claim-set Rights Control是否在不同技术领域重复提供新增解释力。

### Package B — Early-stage Option Value

目标：完成4个真正的early-stage retrospectives。

严格要求：
- T0时为R0/R1；
- T0信息中不能使用后来成功结果；
- 后来形成重大产品 / 标准 / 平台；
- early T0确实存在可观察的option/future-value signals。

**PageRank不计入这一完成数。**

### Package C — Portfolio / Licensing Replication

CRISPR已完成第一个portfolio case。

下一步至少增加：
- 1个SEP / patent-pool / cross-license案例；
- 1个非生命科学复杂产品案例。

检验：
- Portfolio & Jurisdiction Network是否跨行业成立；
- graph object是否真的增加决策信息，而非仅增加叙事复杂度。

---

## Adoption rule

V0.8只有在至少完成以下门槛后才讨论adopted：

- **4组** Rights Control matched pairs — 当前 **4 / 4（门槛完成）**
- **4个** clean early-stage option retrospectives — 当前 **0 / 4**
- **至少1个** portfolio case — 当前 **1 / 1**
- **至少1个** Two Clocks case — 当前 **1 / 1**
- **至少1个** SEP / patent-pool / cross-license外部复制案例 — 当前 **0 / 1**

并且必须完成一次新的cross-case synthesis，证明候选结构跨样本增加解释力而不是历史过拟合。

V0.7继续作为正式架构。


---

## Exploratory dimension discovered after Package A — Realization Path

Taction v. Apple exposes a distinction not fully represented by the current V0.7 / Rights Control objects:

> **Economic Value Base ≠ State-dependent Realizable Value.**

The conceptual model is documented at:

`analysis/theory/patent-value-state-model-1.0.md`

First case note:

`analysis/non-award-validation/taction-state-migration-2026.md`

### Three-layer organization

```text
Value Base
├─ Technology State
└─ Product State

Rights Control
└─ Claim-set legal control

Realization Path
├─ Infringement State
├─ Remedy State
└─ Cash / Economic Realization State
```

Cross-cutting:
- Time / T0
- Jurisdiction
- Evidence / Observability
- Enforcement Capacity
- Portfolio & Jurisdiction Network

### Important boundary

This does **not** modify the existing V0.8 adoption rule.

The Realization Path dimension was discovered during research and therefore requires separate preregistration and replication before any schema adoption decision.

It must not be silently absorbed into Claim-set Rights Control.

### Conceptual guardrails

- jury verdict ≠ intrinsic patent price
- jury verdict ≠ realized cash
- litigation financing / enforcement resources ≠ patent quality
- infringement state ≠ product implementation state
- remedy state ≠ rights validity state
- V0.7 R0–R5 ≠ cash/legal realization state

