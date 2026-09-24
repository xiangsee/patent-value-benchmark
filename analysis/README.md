# Analysis

这里记录模型开发与样本外验证。

## Development Set

第 26 届 Gold / Silver：
- 用于形成和反证 V0.6
- 需控制 T0 与 Outcome Leakage
- 不作为最终外部验证集

## Out-of-Sample Validation

第 25 届：
- V0.6 冻结后进入
- T0 = 2024-02-05
- 不因为单个反例临时添加变量
- 记录模型能够解释和不能解释的样本

核心原则：

> 不能解释的 Gold / Silver 差异应记录为 Unknown，而不是用事后故事补齐。
