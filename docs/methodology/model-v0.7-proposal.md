# V0.7 Architecture Proposal

状态：**Proposal — not yet adopted**

提出依据：第25届 10组 Gold–Silver matched-pair 的 V0.6 Cross-pair Synthesis。

V0.7 的目标不是提高“奖项预测准确率”，而是解决 V0.6 暴露出的核心混淆：

> 价值低、证据弱、以及公开看不见，不是同一件事。

## Layer 1 — Value State

描述专利实际处于什么价值状态。

候选维度：
- Relative Technological Differentiation
- Value Carrier Centrality
- Real-world Validation Depth
- Scale & Diffusion
- Industry / Social Impact

注意：这是“现实状态”，不是证据可得性。

## Layer 2 — Attribution / Evidence State

描述我们有什么资格把价值归给具体专利。

核心问题：
- 是否存在 exact patent → value carrier 映射？
- 是否存在 patent → performance / cost / revenue 的归因？
- 是否有合同、审计、监管、标准或第三方材料验证？

继续使用 E1–E5，但应更加明确：
- E1 enterprise
- E2 product / project
- E3 exact patent → value carrier
- E4 patent-level attributable value
- E5 independent verification

E4 可以和 E5 组合出现；二者含义不同。

## Layer 3 — Observability State

新增独立字段，不再把“没有公开证据”等价为“证据弱”。

建议状态：

- **Public**：任何外部研究者可取得
- **Disclosed / Regulated**：招股书、年报、监管文件等正式披露
- **Internal**：企业内部可取得，但公开层不可见
- **Restricted**：合同、客户、审计或许可信息受限
- **Unknown**：不知道证据是否存在

同一价值事实可以同时具有 evidence level 与 observability state。

例如：
- 产品收入：E2 + Public/Disclosed
- 专项审计的专利贡献收入：E4/E5 + Internal/Restricted

## Layer 4 — Value Realization Stage

用于避免把所有“成果转化”混为一谈。

候选阶段：

- **R0 — Right Exists**：专利权存在
- **R1 — Market/Transfer Intent**：挂牌、报价、寻求许可
- **R2 — Rights Transaction**：许可、转让、质押等发生
- **R3 — Implemented in Value Carrier**：进入产品 / 工艺 / 平台 / 工程
- **R4 — Scaled Real-world Validation**：规模部署、市场、临床、工程验证
- **R5 — Patent-level Attributable Value**：能够把性能、成本、收入或社会价值归因到该专利

重要规则：

> R1/R2 不等于 R3；R3 不等于 R4；R4 也不等于 R5。

## Public vs Internal Engines after V0.7

### Public Screening
主要能观察：
- R0–R4 的部分状态
- E1–E3 为主
- 少数 E4
- Public / Disclosed evidence

输出应是：
- candidate
- evidence gaps
- observability gaps

而不是 Gold probability。

### Internal Patent Value / Gold Readiness
在企业授权后尝试补：
- R3–R5
- E3–E5
- Internal / Restricted evidence

输出：
- value-carrier mapping
- attribution gap
- evidence package
- readiness diagnosis

## Adoption test

V0.7 只有经过第24届新的外部验证后才正式 adopted。

第25届数据只能作为提出架构的依据，不能同时作为其独立验证集。

