# V0.8 Research Agenda — Value Construct, Rights Control & Portfolio Network

状态：**Research Agenda — not adopted**（Round 2 复制门槛已完成；adoption 仍需用户显式决定）

V0.7继续是当前正式架构。Formal Ledger / Diagnostic schema 保持冻结的 `1.0`。

Round 2 adoption-readiness 综合：

`analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`

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
- **H2c Clean early-stage option value:** four clean retrospectives completed (US8278036B2 @ T0=2012-10-02 → R0; US4539507A @ T0=1987-09-21 → R0; US4668595A @ T0=1987-05-26 → R0; US4949039A @ T0=1990-08-14 → R0); **4 / 4 Package B** (threshold met; stop expanding unless H2c is falsified).
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

**预注册（replication before schema）：** [#37](https://github.com/xiangsee/patent-value-benchmark/issues/37)

Matched cases + synthesis（analysis-first；**不**新增 formal Ledger；**不**建 experimental schema）：

1. i4i / US5787449 @ T0=2010-03-10（R5）— hard feature-level NIA → `analysis/non-award-validation/counterfactual-i4i-us5787449.md`
2. Apple / US7469381 claim 19 @ Counterfactual T0=2014-03-06（R4 锚点）— documented NIA + low product-level blocking → `analysis/non-award-validation/counterfactual-apple-us7469381-bounceback.md`
3. **Replication-gate synthesis**（勾选 Issue #37 pass 条）→ `analysis/non-award-validation/counterfactual-i4i-apple381-pair-synthesis.md`
4. Exploratory（different R；不计入 matched 最低门槛）：Via LA AVC SEP US6825782 — standard-lock + FRAND/pool FTO → `analysis/non-award-validation/counterfactual-via-la-us6825782-sep-fto.md`

硬边界：禁令/终局 ∈ Rights Control；金额事件 ∈ Realization Path；**禁止**把 design-around 写成伪精确美元或 score。仍 **不** adopt V0.8。

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

对外导读与库存：`docs/methodology/rights-control-research-overview.md`。

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

**已完成：**

- CRISPR portfolio case（US8697359，R2）
- SEP / patent-pool 外部复制：**US6825782B2**（NTT Docomo）∈ Via LA AVC/H.264 Patent Portfolio License；T0=2026-10-12；standalone **R2**；池费率与被许可人生态不得继承为单件专利价值
- 非生命科学复杂产品组合：**CN110165116B**（比亚迪刀片电池 CTP 族）；T0=2026-10-12；standalone **R0**；同权利人产品系统多专利栈；「300+」仅为 program scope

检验结果（摘要）：
- Portfolio & Jurisdiction Network 在生命科学许可网络、标准专利池、同 assignee 复杂产品栈三类机制上均可增加决策信息；
- graph object 有用，但尚不足以自动升格为正式 schema。

分析：
- `analysis/non-award-validation/avc-us6825782-sep-pool-packagec.md`
- `analysis/non-award-validation/byd-blade-cn110165116-portfolio-packagec.md`

---

## Adoption rule

V0.8只有在至少完成以下门槛后才讨论adopted：

- **4组** Rights Control matched pairs — 当前 **4 / 4（门槛完成）**
- **4个** clean early-stage option retrospectives — 当前 **4 / 4**
- **至少1个** portfolio case — 当前 **1 / 1**（CRISPR；另有 Blade 非生科复制）
- **至少1个** Two Clocks case — 当前 **1 / 1**
- **至少1个** SEP / patent-pool / cross-license外部复制案例 — 当前 **1 / 1**（US6825782B2 / Via LA AVC pool）
- **至少1个** 非生命科学复杂产品组合复制 — 当前 **1 / 1**（CN110165116B）

并且必须完成一次新的cross-case synthesis，证明候选结构跨样本增加解释力而不是历史过拟合。

**Round 2 cross-case synthesis：** `analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`（2026-10-12）

门槛状态：**预注册复制门槛已满足。**

但这只解除「禁止讨论」的硬阻塞，**不触发自动 adoption**。

显式建议（见综合文 §4）：

> **保持 V0.7 adopted；V0.8 research-only；formal schema 保持冻结的 1.0，直到用户另行显式批准。**

V0.7继续作为正式架构。


---

## Exploratory dimension discovered after Package A — Realization Path

对外导读与库存：`docs/methodology/realization-path-research-overview.md`。

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



### Realization Path experimental 0.1 — implementation status

Issue #16的三路径复制完成后，Issue #20已将Realization Path实现为独立实验对象。

当前结构：

```text
Canonical Events
      ↓ deterministic projection
Current Snapshot
├─ entitlement_state
├─ realization_mechanisms
└─ economic_realization
   ├─ cash
   ├─ control
   └─ contractual_future_value
```

关键治理规则：

- source event log禁止手工填写`current_snapshot`；
- observed amount不自动求和成intrinsic patent value；
- verdict amount与cash receipt分离；
- exclusion/control可构成economic realization而不要求cash；
- infringement不是license/transaction路径的必经节点；
- Enforcement Capacity继续作为context，不进入score。

这仍是exploratory object，不计入既有V0.8 adoption门槛，也不修改formal v1 Ledger Schema。
