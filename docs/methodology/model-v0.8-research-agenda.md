# V0.8 Research Agenda — Value Construct & Rights Control

状态：**Research Agenda — not adopted**

V0.7继续是当前正式架构。

V0.8研究的核心问题不是“再多加几个指标”，而是解决：

> **不同value construct被混用，以及专利权控制力/未来期权/组合语境尚未被显式建模。**

## Candidate additions

### 1. Value Construct
每次研究先声明目标：

- policy_statistical
- technological_quality
- private_asset
- realized_operating
- social_strategic

可多选，但必须区分。

### 2. Rights Control State
候选字段：
- legal_status
- ownership_clarity
- claim_scope
- validity_resilience
- jurisdiction_coverage
- remaining_term
- encumbrance
- enforceability

### 3. Counterfactual Control
候选问题：
- next_best_alternative
- design_around_cost
- design_around_time
- performance_loss_if_removed
- blocking_power
- freedom_to_operate_dependency

### 4. Value Horizon
- realized
- near_term
- option_future
- obsolete/declining

并拆分：
- survival_clock
- remaining_exclusivity_clock

### 5. Portfolio Context
- standalone
- complementary_portfolio
- blocking_portfolio
- cross_license
- SEP/standard
- patent_pool

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

## Non-goals

V0.8不以：
- 生成总分
- 预测Gold
- 把bibliometric proxy变成直接价值
- 用年龄做单向正/负指标

为目标。

## Validation design

下一阶段建议建立两类研究样本。

### A. Same-realization, different-rights-control
选两件都已经R4的专利，比较：
- claim scope
- validity challenge
- design-around
- remaining term
- geography
- blocking role

检验Rights Control是否提供新增解释力。

### B. Early-stage option sample
选择R0/R1但后来成为重大产品/标准的历史专利，使用早期T0复原：
- 当时realized value很低；
- 但哪些signals / option factors已经可观察？

用来防止模型把“尚未实现”误判为“低价值”。

## Adoption rule

至少完成：
- 4组Rights Control matched pairs
- 4个early-stage option retrospectives
- 1个SEP/portfolio案例
- 1个高龄但剩余期限短的“two clocks”案例

之后才讨论V0.8是否adopted。
