# Package B — Early-stage Option Value #3

## US4668595A / Yoshino practical nonaqueous secondary battery (Asahi Kasei)

日期：2026-10-12  
状态：Package B retrospective #3 — experimental; V0.7 remains adopted; V0.8 remains research-only  
关联：Issue #11

## 一、为什么选这件

Package B 要求：

1. T0 时为 **R0/R1**；
2. T0 信息不得使用后来成功结果；
3. 后来形成重大产品 / 标准 / 平台；
4. early T0 存在可观察的 option / future-value signals；
5. **PageRank 不计入**；
6. 相对 #1（mRNA）与 #2（OLED）应 **进一步多元化**（本案：能源存储 / 材料电化学，而非生命科学或有机显示）。

US4668595A（Asahi Kasei；Yoshino / Sanechika / Nakajima）满足这些约束：

- 预注册 early T0 = **1987-05-26**（US 授权日）时，公开记录是已授权工业专利 + 实验室/原型电池性能与权利要求，而不是已上市消费级锂离子电池映射；
- 1980 Mizushima–Goodenough *Mater. Res. Bull.* LixCoO2 阴极平台与 1981 US4302518A 给出前序阴极化学连续性；1987 本专利给出碳质负极窗口 + 层状复合氧化物的可实用二次电池架构 option signal；
- 后来（post-T0）Sony 约 1991 首款商用锂离子电池、以及手机/笔记本/电动车大规模 LIB 现实成功——但这只能写在回顾设计里，不能回填 early ledger。

公开核验（2026-10-12）：

- Google Patents：[US4668595A](https://patents.google.com/patent/US4668595A/en) — grant 1987-05-26；filing 1986-05-09；priority 1985-05-10；assignee Asahi Kasei Kogyo KK。
- Google Patents：[US4302518A](https://patents.google.com/patent/US4302518A/en) — Goodenough / Mizushima；grant 1981-11-24（仅作 pre-T0 阴极平台上下文）。
- DOI：[10.1016/0025-5408(80)90012-4](https://doi.org/10.1016/0025-5408(80)90012-4) — Mizushima et al., *Mater. Res. Bull.* 15, 783–789 (1980)。

## 二、Early T0 = 1987-05-26（授权日）

Ledger：`data/ledgers/non-award-lib-us4668595-early-option.jsonl`

选择授权日作为 T0，是因为该日 US 文本首次完整公开“层状复合氧化物 + 指定窗口碳质材料”的实用非水二次电池架构，且仍早于 Sony 1991 商用约四年。Goodenough/Mizushima 阴极科学已在 T0 之前完成，故可作为平台前序，而 realization 仍从 Right Exists 起算。

### V0.7 能诚实记录的

| 维度 | 状态 |
|---|---|
| Realization stage | **R0 — Right Exists** |
| Knowledge origin | confirmed（Asahi Kasei corporate R&D） |
| Technical differentiation | strong_evidence（1980/1981 LCO 阴极平台；1987 实用碳负极窗口 + 非水二次电池权利要求与实验室循环/能量密度示例） |
| Exact patent → marketed carrier | **unknown** |
| Patent-level attributable value | **unknown** |

### 在 T0 可观察的 option / future-value signals（不是 R3）

1. **Asahi Kasei 持有**的实用非水二次电池专利（工业 R&D 来源清晰）；
2. **Mizushima–Goodenough MRB 1980**：LixCoO2 高能量密度嵌入正极——面向未来高能量二次电池的公开科学平台信号；
3. **US4302518A（1981）**：同族阴极化学的专利平台前序；
4. **本专利实验室/原型示例**：可逆 Li+ 嵌入、多循环充放电、相对负极活性物质的高能量密度叙述——面向未来小型轻量可充电电池平台的 option signal；
5. 专利文本本身以相对铅酸/NiCd/金属锂方案的循环性、自放电与能量密度改进描述可实用化装置方向。

这些信号说明：

> 在 realization 仍为 R0 时，资产已经具备可核验的未来期权特征。

它们**不能**被读成：

> 已经实现 R3+ 的上市锂离子消费电池映射。

## 三、Post-T0 ground truth（仅用于回顾设计，不进入 early ledger）

Early ledger 设置 `post_t0_ground_truth_allowed=false`。

回顾设计需要知道“后来确实形成重大现实价值”，以便检验 H2c，但下列事实**不得**写入 T0=1987 ledger：

- Sony 约 1991 首款商用锂离子电池；
- 此后手机 / 笔记本 / 电动车等大规模 LIB 采用；
- 后期许可、Asahi–Sony 合作叙事或组合许可金额；
- 2019 诺贝尔化学奖叙事。

本回顾只要求：early T0 是干净的 R0/R1，且后来路径是重大现实成功。商用 LIB 路径满足“后来成功”条件，但属于 post-T0。

## 四、对 V0.7 / V0.8 的压力测试结果

### V0.7 做对了什么

- 拒绝把后来的锂离子产业成功倒灌成 1987 的 R3/R4/R5；
- 允许 R0 同时保留材料/电化学分化证据；
- Unknown ≠ 0：没有 exact mapping 就不抬阶段。

### V0.7 仍然说不清楚的

同一件专利在 early T0 的决策相关信息，很大一块是：

> **option / future-value horizon**

而不是当前 realization stage。

V0.7 可以把 1987 记成 R0，也可以（在另一个未来 ledger 中）把商用 LIB 后记成更高 R，但**缺少一个结构化对象**来表示：

- early option signals；
- remaining exclusivity / term；
- “低 realization ≠ 低期权价值”。

这与 Package B #1（mRNA）、#2（OLED）同构，并把样本扩到 **能源存储 / 材料电化学**：

| 样本 | 现象 |
|---|---|
| PageRank | 已是 R4，但两只钟（revealed vs remaining exclusivity）反向运动（**不计入** Package B） |
| US8278036 early T0 | 仍是 R0，生命科学 option signals 已可观察 |
| US4539507 early T0 | 仍是 R0，非生命科学（OLED 平台）option signals 已可观察 |
| US4668595 early T0 | 仍是 R0，能源存储（实用 Li-ion 架构）option signals 已可观察 |

## 五、Package B 进度

| # | Case | Early T0 stage | Status |
|---|---|---|---|
| 1 | US8278036B2 modified-nucleoside RNA | R0 @ 2012-10-02 | complete |
| 2 | US4539507A Tang–VanSlyke thin-film organic EL | R0 @ 1987-09-21 | complete |
| 3 | US4668595A Yoshino practical nonaqueous secondary battery | R0 @ 1987-05-26 | **complete（本 PR）** |
| 4 | TBD | | open |

PageRank 不计入 Package B。

## 六、治理边界

- 不修改正式 Ledger Schema 1.0；
- 不把 option signals 偷偷塞进 R-stage；
- 不把 Sony 1991 / 手机 / EV LIB 成功回填 early T0；
- 不把 Asahi 企业价值或后期组合许可金额记成该专利在 1987 的内在价格；
- 不把专利说明书中的实验室循环数据读成 E3 上市产品映射；
- 不把 Goodenough 阴极专利的价值继承为本案在 T0 的 attributable value。

V0.7 remains adopted.  
V0.8 remains research-only until Package B 4/4 与 Package C 剩余项完成后，再做新的 cross-case synthesis.
