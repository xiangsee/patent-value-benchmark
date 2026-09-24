# Patent Value Benchmark V0.7

状态：**Adopted research architecture**

采用日期：2026-09-24

V0.7不是中国专利金奖预测模型。

它是一套把“专利真实价值”“价值归因证据”“证据可观察性”和“价值实现阶段”分开的研究架构。

## 1. Value State

回答：

> 现实世界里，这项技术 / 专利所对应的价值载体究竟走到了哪里？

观察：
- Relative Technological Differentiation
- Value Carrier Centrality
- Real-world Validation
- Scale & Diffusion
- Industry / Social Impact

## 2. Attribution / Evidence State

回答：

> 我们有什么资格把产品、工程、临床或经济价值归因到这件exact patent？

证据等级继续使用：
- E1 Enterprise
- E2 Product / Project
- E3 Exact Patent → Value Carrier
- E4 Patent-level Attributable Value
- E5 Independent Verification

特别注意：

E5是“独立核验属性”，并不天然高于E4的“归因深度”；二者可同时出现。

## 3. Observability State

回答：

> 证据究竟在哪里，外部研究者能不能看到？

状态：
- Public
- Disclosed / Regulated
- Internal
- Restricted
- Unknown

Unknown不得自动解释为低价值。

## 4. Value Realization Stage

- R0 — Right Exists
- R1 — Market / Transfer Intent
- R2 — Rights Transaction
- R3 — Implemented in Value Carrier
- R4 — Scaled Real-world Validation
- R5 — Patent-level Attributable Value

### Non-inheritance rule

严格禁止自动继承：

`Enterprise R4 → Product R4 → Patent R4`

只有存在足够的E3连接时，产品层状态才能谨慎关联到exact patent。

同理：

`Product Revenue → Patent Value`

必须经过E4归因，不能直接等同。

## 5. Time rule

每项历史研究都设置T0。

post-T0信息只能用于：
- outcome label
- later ground truth

不得用于提升历史T0的Value / Evidence / Observability / Realization状态。

## 6. Public vs Internal engine

### Public Screening
目标：
- 发现候选核心专利
- 识别evidence gaps
- 识别observability gaps

不输出Gold probability。

### Internal Patent Value / Readiness
企业授权内部数据后补充：
- exact patent → product/process mapping
- 性能与成本贡献
- 销售/利润增量
- 合同、客户、审计
- R3–R5 / E3–E5证据

## 7. Adoption evidence

架构由第25届10组Gold–Silver matched pairs提出。

随后使用第24届4组未用于架构形成的跨届样本进行压力测试：
- 创新药
- 软件基础设施
- 电力电子
- 生物制品

四组均显示，把Value、Attribution、Observability、Realization混成一个分数会产生明显误判。

因此V0.7正式采用为研究架构。

**不宣称奖项预测能力。**
