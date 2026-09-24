# V0.6 Cross-pair Synthesis — 25th China Patent Award

日期：2026-09-24  
样本：第25届 10组 Gold–Silver matched pairs  
T0：2024-02-05  
模型状态：V0.6 frozen

## Executive finding

10组配对中：

- **2组：Yes** — 公开T0证据可以观察到明显差异
- **4组：No** — 公开T0证据无法区分
- **4组：Uncertain** — 有局部差异，但不足以稳定解释 Gold / Silver

因此：

> V0.6 可以帮助判断“高价值专利是否已经形成现实世界证据”，但不能被解释为一个可靠的 Gold-vs-Silver 预测器。

## Pair-level result matrix

| Pair | Domain | Result | Main observation |
|---|---|---|---|
| P25-LIFE-001 | Life science | Yes | Gold侧已跨入获批药物与临床使用；Silver侧公开T0产品验证未建立 |
| P25-EQUIP-001 | Semiconductor equipment / manufacturing | Uncertain | 两边产业化都强；Silver具有非常清楚的 exact-patent→core-tech 映射 |
| P25-MAT-001 | Advanced materials | Uncertain | Gold技术差异证据更强；Silver专利→核心技术映射更清楚 |
| P25-COMM-001 | Telecom | No | 标准、部署、许可价值在单件专利层面公开不可观察 |
| P25-MEDDEV-001 | Medical device | Yes | Gold形成 exact patent→product→approval→hospital→units→revenue 链 |
| P25-POWER-001 | Power digitalization | Uncertain | Gold许可备案生效；Silver公开许可竞价但流拍；不足以证明价值层级 |
| P25-SOFT-001 | Software infrastructure | No | 两边底层技术清楚，但 exact patent→product→value 链断裂 |
| P25-AI-001 | Robotics / autonomy | No | 算法控制闭环清楚，现实商业价值公开不可归因到具体专利 |
| P25-PHARMA-002 | Pharmaceuticals | Uncertain | 两边都已大规模商业化；Gold映射更直接，但规模本身不能区分 |
| P25-AI-002 | Mature AI algorithms | No | 两边均为成熟AI企业核心算法和跨国专利族，单件专利价值公开不可见 |

## 1. 被反例明确削弱的“简单规则”

### 1.1 产业化 ≠ Gold
华海清科 Silver、天岳先进 Silver、以岭药业 Silver 都具有非常强的现实运用或产品证据。

因此不能使用：

`产业化 = Gold`

### 1.2 大规模销售 ≠ Gold
P25-PHARMA-002 中，Gold 与 Silver 对应产品在 T0 前都已形成极大商业规模。

因此：

`Large Scale = Gold`

不成立。

### 1.3 Exact patent → product 映射 ≠ Gold
华海清科、天岳先进等 Silver 已经拥有非常清楚的 E3 证据。

因此 Centrality / Traceability 只能说明“这确实是一件重要专利”，不能单独区分 Gold / Silver。

### 1.4 头部企业 / 战略产业 / 发明专利 ≠ Gold
这些属性广泛存在于 Silver 样本，是进入高价值专利竞争的背景条件，而不是 Gold differentiation。

## 2. 仍然有用，但更像 Readiness 的变量

### Real-world Validation Depth
在 P25-LIFE-001 与 P25-MEDDEV-001 中具有明显区分力。

但当 Gold 和 Silver 两边都已经完成大规模验证时（如 P25-PHARMA-002、P25-EQUIP-001），区分力迅速下降。

因此更适合回答：

> 这项专利是否已经成熟到可以进入高价值专利深度评价？

而不是：

> 它为什么是 Gold 而不是 Silver？

### Value Carrier Centrality
对于判断“这是不是核心专利”非常重要。

但 Silver 反例证明它不是 Gold 的充分条件。

### Scale & Diffusion
可以证明现实世界影响，但不等价于奖项等级。

## 3. V0.6 中最大的公开数据缺口：Patent-level Attribution

在 **10/10 配对**中，公开T0信息都没有真正解决：

> 产品、收入、性能或社会价值中，到底有多少能够归因于这件具体专利？

即便存在：
- 产品销售额
- 医院数量
- 市场份额
- 许可行为
- 标准布局

也通常只能达到 E2 / E3。

真正的 E4：

`Patent → attributable performance / cost / revenue / profit`

几乎没有公开出现。

这可能是 Public Screening 与 Internal Gold Readiness 之间最重要的边界。

## 4. Evidence Traceability 是最常见的“可观察差异”，但不能当作价值本身

10组里，Evidence Traceability 是最频繁出现的可观察差异。

但方向并不稳定：

- 有些 Gold 的链条更完整；
- P25-MAT-001 中 Silver 的 exact-patent→core-tech 公开映射反而更清楚；
- 招股书、上市公司披露、药品监管等行业天然更容易留下结构化证据；
- 通信、数据库、AI底层算法则天然更难观察。

因此：

> Traceability 同时反映“价值证据质量”和“信息披露制度”。

必须把 **Value Evidence** 与 **Evidence Observability** 分开。

## 5. 行业具有不同的 Observability Regime

### 高可观察
- 上市公司制造业
- 医疗器械
- 药品 / 监管产品

原因：招股书、年报、注册审批、临床指南、产品收入等提供结构化公开证据。

### 低可观察
- 通信协议 / SEP
- 数据库基础设施
- AI底层算法

原因：价值常被组合进标准、平台、许可池和复杂产品系统，单件专利的贡献不对外披露。

因此同一个“Unknown”，在不同产业中的含义不同。

## 6. 三个模型应该彻底分开

### A. Patent Value Model
回答：

> 这项专利实际有没有形成技术、产品、市场或社会价值？

核心对象是现实状态。

### B. Patent Value Evidence Model
回答：

> 有什么证据允许我们把价值归因到这件专利？

核心对象是证据链与归因。

### C. Evidence Observability Model
回答：

> 这些证据是公开可见、企业内部可见，还是根本尚未形成？

核心对象是信息可得性。

Award level 应当放在三套模型之外，只作为 benchmark label，而不是偷偷进入解释变量。

## 7. V0.6 的正式判断

### 保留
V0.6 的：
- T0 cutoff
- Outcome Leakage control
- Unknown ≠ 0
- Public Screening / Internal Readiness 分离
- E1–E5 evidence hierarchy
- matched-pair method

全部保留。

### 不升级为“Gold prediction model”
10组结果不支持声称 V0.6 能稳定预测 Gold / Silver。

### 进入 V0.7 architecture proposal
V0.7 不增加一个新的评分项。

建议改为：
1. Value State
2. Attribution / Evidence State
3. Observability State
4. Value Realization Stage

这是架构升级，而不是分数升级。

## 8. 下一步

停止第25届扩样。

下一阶段：
1. 将 V0.7 候选架构形式化；
2. 选择第24届作为新的外部验证集；
3. 不回头修改第25届结果；
4. 测试新架构能否更好地区分“价值不足”和“价值不可观察”。

