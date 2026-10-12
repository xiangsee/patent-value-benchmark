# Package B — Early-stage Option Value #2

## US4539507A / Tang–VanSlyke improved thin-film organic EL (Kodak)

日期：2026-10-12  
状态：Package B retrospective #2 — experimental; V0.7 remains adopted; V0.8 remains research-only  
关联：Issue #11

## 一、为什么选这件

Package B 要求：

1. T0 时为 **R0/R1**；
2. T0 信息不得使用后来成功结果；
3. 后来形成重大产品 / 标准 / 平台；
4. early T0 存在可观察的 option / future-value signals；
5. **PageRank 不计入**；
6. 相对 #1（mRNA / US8278036）应 **非生命科学** 以多样化。

US4539507A（Eastman Kodak；Tang & VanSlyke）满足这些约束：

- 预注册 early T0 = **1987-09-21**（APL《Organic electroluminescent diodes》发表日）时，公开记录是已授权工业专利 + 实验室二极管性能，而不是已上市 OLED 显示产品映射；
- 1982 前序专利 US4356429A 与 1985 本专利已给出有机 EL 平台连续性；1987 APL 给出低电压高亮度的可观察未来显示/发光平台信号；
- 后来（post-T0）Pioneer 1997 首款商用 OLED、以及手机/电视 OLED 大规模现实成功——但这只能写在回顾设计里，不能回填 early ledger。

## 二、Early T0 = 1987-09-21（APL 发表日）

Ledger：`data/ledgers/non-award-oled-us4539507-early-option.jsonl`

选择 APL 日而非授权日（1985-09-03）作为 T0，是为了在 **仍早于商业化约十年** 的前提下，纳入与 Package B #1 同构的 **同行评审 option signal**。授权已在 T0 之前完成，故 realization 仍从 Right Exists 起算。

### V0.7 能诚实记录的

| 维度 | 状态 |
|---|---|
| Realization stage | **R0 — Right Exists** |
| Knowledge origin | confirmed（Eastman Kodak corporate R&D） |
| Technical differentiation | strong_evidence（1982 平台前序；1985 效率改进权利要求；1987 APL 低电压高亮度） |
| Exact patent → marketed carrier | **unknown** |
| Patent-level attributable value | **unknown** |

### 在 T0 可观察的 option / future-value signals（不是 R3）

1. **Kodak 持有**的改进型薄膜有机 EL 专利（工业 R&D 来源清晰）；
2. **US4356429A（1982）**：同发明人/权利人有机 EL 电池平台前序；
3. **APL 1987**：双层有机薄膜 EL 二极管，<10 V 下亮度 >1000 cd/m²、约 1% EQE / 1.5 lm/W——面向未来低电压显示/发光平台的公开性能信号；
4. 专利文本本身以低驱动电压与功率转换效率改进描述可实用化装置方向。

这些信号说明：

> 在 realization 仍为 R0 时，资产已经具备可核验的未来期权特征。

它们**不能**被读成：

> 已经实现 R3+ 的上市 OLED 产品映射。

## 三、Post-T0 ground truth（仅用于回顾设计，不进入 early ledger）

Early ledger 设置 `post_t0_ground_truth_allowed=false`。

回顾设计需要知道“后来确实形成重大现实价值”，以便检验 H2c，但下列事实**不得**写入 T0=1987 ledger：

- Pioneer GD-F1（约 1997）等首批商用 OLED 产品；
- 此后手机 / 电视等大规模 OLED 显示采用；
- 后期许可、标准必要叙事或组合许可金额。

本回顾只要求：early T0 是干净的 R0/R1，且后来路径是重大现实成功。商用 OLED 路径满足“后来成功”条件，但属于 post-T0。

## 四、对 V0.7 / V0.8 的压力测试结果

### V0.7 做对了什么

- 拒绝把后来的 OLED 产业成功倒灌成 1987 的 R3/R4/R5；
- 允许 R0 同时保留装置/科学分化证据；
- Unknown ≠ 0：没有 exact mapping 就不抬阶段。

### V0.7 仍然说不清楚的

同一件专利在 early T0 的决策相关信息，很大一块是：

> **option / future-value horizon**

而不是当前 realization stage。

V0.7 可以把 1987 记成 R0，也可以（在另一个未来 ledger 中）把商用 OLED 后记成更高 R，但**缺少一个结构化对象**来表示：

- early option signals；
- remaining exclusivity / term；
- “低 realization ≠ 低期权价值”。

这与 Package B #1（mRNA）同构，并相对 #1 把样本扩到 **显示 / 光电非生命科学**：

| 样本 | 现象 |
|---|---|
| PageRank | 已是 R4，但两只钟（revealed vs remaining exclusivity）反向运动（**不计入** Package B） |
| US8278036 early T0 | 仍是 R0，生命科学 option signals 已可观察 |
| US4539507 early T0 | 仍是 R0，非生命科学（OLED 平台）option signals 已可观察 |

## 五、Package B 进度

| # | Case | Early T0 stage | Status |
|---|---|---|---|
| 1 | US8278036B2 modified-nucleoside RNA | R0 @ 2012-10-02 | complete |
| 2 | US4539507A Tang–VanSlyke thin-film organic EL | R0 @ 1987-09-21 | **complete（本 PR）** |
| 3 | TBD | | open |
| 4 | TBD | | open |

PageRank 不计入 Package B。

## 六、治理边界

- 不修改正式 Ledger Schema 1.0；
- 不把 option signals 偷偷塞进 R-stage；
- 不把 Pioneer / 手机 / 电视 OLED 成功回填 early T0；
- 不把 Kodak 企业价值或后期组合许可金额记成该专利在 1987 的内在价格；
- 不把 APL 实验室二极管性能读成 E3 上市产品映射。

V0.7 remains adopted.  
V0.8 remains research-only until Package B 4/4 与 Package C 剩余项完成后，再做新的 cross-case synthesis。
