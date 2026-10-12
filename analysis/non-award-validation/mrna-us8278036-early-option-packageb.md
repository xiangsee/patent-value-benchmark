# Package B — Early-stage Option Value #1

## US8278036B2 / Karikó–Weissman modified nucleoside RNA

日期：2026-10-12  
状态：Package B retrospective #1 — experimental; V0.7 remains adopted; V0.8 remains research-only  
关联：Issue #11

## 一、为什么选这件

Package B 要求：

1. T0 时为 **R0/R1**；
2. T0 信息不得使用后来成功结果；
3. 后来形成重大产品 / 标准 / 平台；
4. early T0 存在可观察的 option / future-value signals；
5. **PageRank 不计入**。

US8278036B2（University of Pennsylvania；Karikó & Weissman）满足这些约束：

- 授权日 **2012-10-02** 时，公开记录主要是专利权 + 机制科学，而不是已上市疫苗产品映射；
- 2005 / 2008 同行评审论文已给出可观察的未来治疗/疫苗使用信号；
- 后来（post-T0）该技术路线进入 COVID-19 mRNA 疫苗大规模现实成功——但这只能写在回顾设计里，不能回填 early ledger。

## 二、Early T0 = 2012-10-02（授权日）

Ledger：`data/ledgers/non-award-mrna-us8278036-early-option.jsonl`

### V0.7 能诚实记录的

| 维度 | 状态 |
|---|---|
| Realization stage | **R0 — Right Exists** |
| Knowledge origin | confirmed（Penn / NIH-supported university research） |
| Technical differentiation | strong_evidence（2005 TLR 抑制；2008 翻译↑ / 免疫原性↓） |
| Exact patent → marketed carrier | **unknown** |
| Patent-level attributable value | **unknown** |

### 在 T0 可观察的 option / future-value signals（不是 R3）

1. **大学持有、NIH 资助**的治疗性 RNA 专利（权利与研究来源清晰）；
2. **Immunity 2005**：修饰核苷可压制 TLR3/7/8 介导的 RNA 免疫激活；
3. **Molecular Therapy 2008**：假尿苷 mRNA 提高翻译、降低体内免疫原性，并明确写成 gene replacement **与 vaccination** 的有前景工具；
4. 专利文本本身描述治疗蛋白递送 / 降低免疫原性等未来用途。

这些信号说明：

> 在 realization 仍为 R0 时，资产已经具备可核验的未来期权特征。

它们**不能**被读成：

> 已经实现 R3+ 的上市产品映射。

## 三、Post-T0 ground truth（仅用于回顾设计，不进入 early ledger）

Early ledger 设置 `post_t0_ground_truth_allowed=false`。

回顾设计需要知道“后来确实形成重大现实价值”，以便检验 H2c，但下列事实**不得**写入 T0=2012 ledger：

- COVID-19 mRNA 疫苗的监管授权与大规模使用；
- 围绕 Penn / Cellscript / BioNTech / Moderna 等后续许可与商业化叙事；
- 后期权利金或大学收入报道。

本回顾只要求：early T0 是干净的 R0/R1，且后来路径是重大现实成功。COVID-era 结果满足“后来成功”条件，但属于 post-T0。

## 四、对 V0.7 / V0.8 的压力测试结果

### V0.7 做对了什么

- 拒绝把后来的疫苗成功倒灌成 2012 的 R3/R4/R5；
- 允许 R0 同时保留科学分化证据；
- Unknown ≠ 0：没有 exact mapping 就不抬阶段。

### V0.7 仍然说不清楚的

同一件专利在 early T0 的决策相关信息，很大一块是：

> **option / future-value horizon**

而不是当前 realization stage。

V0.7 可以把 2012 记成 R0，也可以（在另一个未来 ledger 中）把 COVID 后记成更高 R，但**缺少一个结构化对象**来表示：

- early option signals；
- remaining exclusivity / term；
- “低 realization ≠ 低期权价值”。

这正是 Package B / H2c 要复制的缺口，与 PageRank Two Clocks（同一 R4 下 horizon 不同）互补：

| 样本 | 现象 |
|---|---|
| PageRank | 已是 R4，但两只钟（revealed vs remaining exclusivity）反向运动 |
| US8278036 early T0 | 仍是 R0，但 option signals 已可观察 |

## 五、Package B 进度

| # | Case | Early T0 stage | Status |
|---|---|---|---|
| 1 | US8278036B2 modified-nucleoside RNA | R0 @ 2012-10-02 | **complete** |
| 2 | TBD | | open |
| 3 | TBD | | open |
| 4 | TBD | | open |

PageRank 不计入 Package B。

## 六、治理边界

- 不修改正式 Ledger Schema 1.0；
- 不把 option signals 偷偷塞进 R-stage；
- 不把 COVID 成功回填 early T0；
- 不把大学后期收入或组合许可金额记成该专利在 2012 的内在价格。

V0.7 remains adopted.  
V0.8 remains research-only until Package B 4/4 与 Package C 剩余项完成后，再做新的 cross-case synthesis。
