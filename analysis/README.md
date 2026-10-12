# Analysis

本目录记录 Xiangsee Patent Value Benchmark 的模型开发、反证测试、样本外验证与专项研究。

从2026-09-24起，分析层明确拆分为两条线。

## Track A — General Patent Value Research

通用专利价值研究不以任何奖项为目标变量。

主要内容：
- `theory/`：value construct、rights control、option value、portfolio context等理论研究
- `non-award-validation/`：非奖项机制样本与综合（含 Round 1 / Round 2）
- V0.8及以后模型的预注册测试（**research-only；不改变 V0.7 adopted**）

Round 2 adoption-readiness（#11 关闭后）：
- `non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`


Counterfactual Control（analysis-only；**无** schema）：
- 导读：`../docs/methodology/counterfactual-control-research-overview.md`
- 笔记：`non-award-validation/counterfactual-*.md`
- Issue [#37](https://github.com/xiangsee/patent-value-benchmark/issues/37) 复制门已关闭；**不** adopt V0.8


核心要求：
- 先声明 value construct
- Screening Signal 与 Value Proof 分开
- Unknown ≠ 0
- 不允许企业/产品价值自动继承到 exact patent
- 历史研究使用 T0 防止 outcome leakage

## Track B — China Patent Award Research

中国专利奖作为独立专项模块长期保留。

入口：
- `china-patent-award/README.md`

历史验证记录：
- `24th-validation/`
- `25th-validation/`

这些样本曾参与 V0.6/V0.7 的形成，因此不会删除或重写历史结论。

但从现在开始：

> **Gold / Silver / Excellent 不再是通用 Patent Value Benchmark 的默认样本框架。**

奖项样本可以：
- 用于研究中国专利奖本身；
- 作为某些价值维度的外部验证；
- 提供可迁移到通用模型的候选变量。

奖项样本不能：
- 定义“真正的专利价值”；
- 自动成为通用模型的正负标签；
- 让模型重新退化为Gold预测器。
