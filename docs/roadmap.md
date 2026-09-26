# Roadmap

## Research Preview — current

当前正式研究架构：**V0.7 adopted**

主项目目标是建立可复核、可反驳、可持续更新的 **Patent Value Benchmark**，而不是预测任何奖项。

从2026-09-24起，研究分为两条线：

- **Track A — Patent Value Benchmark**：通用专利价值主干
- **Track B — China Patent Award Research**：中国专利奖专项模块

两条线共享证据纪律、T0规则和数据治理，但不共享目标变量。

详见 `docs/research-tracks.md`。

---

## Track A — Patent Value Benchmark

### 当前正式架构：V0.7

已采用：

- Value State
- Attribution / Evidence State
- Observability State
- Value Realization Stage (R0–R5)

V0.7不输出总分，也不预测Gold。

### V0.8 Research — Round 1 complete, not adopted

第一轮完全不依赖中国专利奖标签的机制型压力测试已完成：

| Archetype | Tested mechanism | Main result |
|---|---|---|
| i4i v. Microsoft | Litigation value / enforcement | R5仍不能替代Rights Control |
| Amgen v. Sanofi | Claim-set validity | Rights Control需要claim-set granularity |
| PageRank | Same patent / two T0s | Two Clocks成立；R-stage不是价值等级 |
| CRISPR-Cas9 | Portfolio dependency | 单件专利Ledger之外需要Portfolio & Jurisdiction Network |

Round 1综合：

`analysis/non-award-validation/round1-cross-case-synthesis-v0.8.md`

当前假说状态：

- H1 Rights Control：第一组对照支持，仍需复制
- H2a Date/context dependence：支持
- H2b Two Clocks：支持
- H2c Clean early-stage option sample：尚未验证
- H3 Portfolio Dependency：支持
- H4 Monetary evidence is contextual：跨诉讼/组合许可两类场景支持

### V0.8 adoption progress

- Rights Control matched pairs：**1 / 4**
- clean early-stage option retrospectives：**0 / 4**
- portfolio case：**1 / 1**
- Two Clocks case：**1 / 1**
- SEP / patent-pool / cross-license replication：**0 / 1**

因此：

> **V0.8 remains not adopted.**

下一阶段转入最小复制验证，而不是继续增加未经验证的新字段。

#### Package A — Rights Control Replication
再做3组跨行业对照。

#### Package B — Early-stage Option Value
寻找4个真正T0=R0/R1、后来形成重大现实价值的历史专利。PageRank不计入。

#### Package C — Portfolio / Licensing Replication
至少再做：
- 1个SEP / patent-pool / cross-license；
- 1个非生命科学复杂产品。

### Candidate architecture after Round 1

```text
Value Construct
    +
Value Realization R0–R5
    +
Attribution / Evidence
    +
Observability
    +
Claim-set Rights Control
    +
Value Horizon / Two Clocks
    +
Portfolio & Jurisdiction Network

Screening Signals remain outside value facts.
```

这仍是研究候选结构，不是冻结Schema。

---

## Patent Value Ledger + Diagnostic

状态：**核心输入/输出闭环已建立**

已完成：

- Patent Value Ledger 1.0 Draft
- Patent Value Diagnostic 1.0 Draft
- Ledger → Diagnostic 确定性生成器
- Diagnostic → Markdown report 渲染
- CI校验 non-inheritance、cross-reference、T0 和版本一致性
- R0 / R2 / R4 / R5公开样例
- 非奖项机制样本已进入同一数据链

下一步：

- 外部冷启动复现
- 根据复现结果修正文档 / schema
- 在V0.8研究与v0.1.0基础设施release之间保持版本边界
- Schema freeze
- v0.1.0 release

---

## Track B — China Patent Award Research

中国专利奖研究作为独立长期模块保留。

### 已完成的历史研究

#### 第25届
- 10组 Gold–Silver matched pairs
- Cross-pair Synthesis
- V0.6 的主要形成样本

#### 第24届
- 4组跨届压力测试
- 创新药、软件基础设施、电力电子、生物制品
- 用于V0.7外部验证

这些记录继续保存在：
- `analysis/25th-validation/`
- `analysis/24th-validation/`

专项入口：
- `analysis/china-patent-award/README.md`

### 后续独立议程

逐步扩展：
- 历届 Gold / Silver / Excellent
- 评奖标准与结果的制度史
- 同届同领域匹配研究
- 获奖后技术、市场、许可、诉讼、标准、产业化表现
- 金奖是否对某些 value constructs 提供稳定外部信号

历史数据必须区分当时的评奖制度与当前制度，避免跨制度直接横比。

---

## Historical provenance — V0.6 / V0.7

项目早期曾以中国专利奖样本为主要现实世界验证入口。

### V0.6 Cross-pair Synthesis

第25届10组 matched pairs：

- Yes: 2
- No: 4
- Uncertain: 4

得到的关键结论不是“能预测Gold”，而是：

- 单一readiness分数无法稳定区分奖项结果；
- 必须拆开价值、归因、可观察性和实现阶段；
- 不能用事后故事修补 Unknown。

### V0.7 External Validation

第24届4组跨届压力测试达到预设最低门槛。

正式采用：

- Value State
- Attribution / Evidence State
- Observability State
- Value Realization Stage (R0–R5)

这些结果现在被视为：

> **通用架构的历史形成证据 + 中国专利奖专项研究资产**

而不是主项目未来样本设计的默认模板。

---

## Public release — v0.1.0

首次正式版本发布前完成：

- README 完整化
- 数据字典
- 示例记录
- CONTRIBUTING
- CITATION.cff
- 多许可证边界确认
- 首批可复核 benchmark dataset
- 外部冷启动复现
- Schema freeze
- CI 全部通过
- Git tag + GitHub release
