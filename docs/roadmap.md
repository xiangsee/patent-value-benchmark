# Roadmap

## Research Preview — current

当前模型：**V0.6 frozen**

目标不是预测奖项，而是建立可复核的高价值专利基准与 Gold Readiness 诊断框架。

### 已完成
- 第 26 届：开发集 / 反事实测试
- 第 25 届：样本外验证 Round 1–2
- 数据 Schema
- Source Registry
- T0 / Outcome Leakage 规则
- 自动数据校验

## Milestone A — 25th Validation Set

目标：
- 扩展至约 10–12 组高质量 Gold–Silver matched pairs（当前 10 组，Milestone A 最低目标已完成）
- 覆盖至少：
  - 生命科学
  - 医疗器械
  - 通信
  - 半导体 / 装备
  - 先进材料
  - 新能源 / 电力
  - AI / 软件基础设施
  - 记录无法形成高质量 matched pair 的产业缺口，而非强行配对
- 明确记录“可区分 / 不可区分 / 不确定”
- 不因单个案例修改 V0.6

状态：**完成最低目标，停止扩样，进入 Cross-pair Synthesis。**

完成条件：
- 跨行业重复出现的规律与失败模式可被独立复核
- 数据全部通过 Schema 与 cross-reference validation

## Milestone B — V0.7 Decision

只有在 Milestone A 完成后才决定：
- 保持 V0.6
- 或提出 V0.7

任何新增变量必须说明：
1. 哪些旧样本促使修改；
2. 是否属于真实机制而非历史过拟合；
3. 如何在未见样本上检验。

## Milestone C — Historical Benchmark

逐步扩展：
- 第 20–24 届 Gold / Silver
- 后续再加入 Excellent
- 逐步回溯更早届次

历史数据必须区分当时的评奖制度与当前制度，避免跨制度直接横比。

## Milestone D — Patent Value Ledger

发布开放的 Patent Value Ledger Schema：

```text
Knowledge
  → Technology
  → Patent
  → Product / Process / Platform / Project
  → Regulatory / Standard / Market
  → Revenue / Social Impact
```

每条连接保留证据、日期、置信状态和来源。

## Milestone E — v0.1.0 Public Release

首次正式版本发布前完成：
- README 完整化
- 数据字典
- 示例记录
- CONTRIBUTING
- CITATION.cff
- 开放许可证策略（代码 / 数据 / 文档分别处理）
- 首批可复核 benchmark dataset
- CI 全部通过

> License 在正式发布前单独确定，不在研究阶段擅自替用户选择。


## Milestone A Result — V0.6 Cross-pair Synthesis

第25届 10 组 matched pairs 已完成横向综合。

结果：
- Yes: 2
- No: 4
- Uncertain: 4

正式结论：
- V0.6 保留为 readiness / evidence research baseline；
- 不将其表述为 Gold-vs-Silver prediction model；
- 进入 V0.7 architecture proposal；
- 下一外部验证集为第24届。


## Milestone B — 24th External Validation

状态：**进行中**

- T0 = 2022-10-31
- V0.7 仍为 Proposal，未 adopted
- 第25届结果冻结
- Round 1：2组配对
  - P24-PHARMA-001
  - P24-SOFT-001
- Round 2：新增 P24-POWER-001，当前累计3组
- 计划达到4–6组后再做架构判断
