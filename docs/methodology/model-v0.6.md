# Patent Value Benchmark V0.6

状态：**Frozen for out-of-sample validation**

V0.6 在第 26 届中国专利奖 Gold / Silver 研究后冻结。冻结的目的，是避免继续根据已知结果不断增加变量，从而对历史样本过拟合。

## 两个引擎

### Engine A — Public Screening

仅使用外部可获得信息，用于从大规模专利组合中筛选值得深度核验的候选专利。

重点观察：
- 技术问题与相对技术差异
- 权利状态与专利族
- 产品 / 工艺 / 平台 / 工程线索
- 标准、临床、监管、工程应用线索
- 公开可见的规模与扩散证据

目标偏向 **Recall**：尽量不要漏掉潜在核心专利。

### Engine B — Internal Gold Readiness

在企业授权提供内部数据后进一步核验：
- Patent → Product / Process / Platform 是否能够证明
- 专利对应的核心性能贡献
- 销售、利润、成本、良率、效率等价值归因
- 工程项目、客户、许可、市场份额
- 审计、合同、监管、标准与第三方测试

目标偏向 **Precision**：判断专利是否已经形成可验证的高价值技术资产。

## Gold Readiness

V0.6 不采用简单 100 分制。首先判断四只“时钟”是否成熟：

1. 技术成熟度
2. 权利成熟度
3. 价值载体成熟度
4. 证据成熟度

专利年龄只可能是成熟度的代理变量，不等于成熟度本身。

## Gold Differentiation 候选观察维度

当前冻结观察维度：
- Relative Technological Differentiation
- Value Carrier Centrality
- Patent-level Attribution
- Real-world Validation Depth
- Scale & Diffusion
- Evidence Traceability
- Industry / Social Impact

这些维度目前是研究变量，不是官方评分，也不应被表述为获奖原因。

## 研究边界

中国专利奖的完整申报材料和逐项评委得分并不公开，因此公开数据模型存在天然观测上限。

项目的目标是建立 **高价值专利基准与诊断框架**，而不是声称可以精确复刻评审委员会。
