# Package B — Early-stage Option Value #4

## US4949039A / Grünberg multilayer GMR-type magnetic-field sensor (KFA Jülich)

日期：2026-10-12  
状态：Package B retrospective #4 — experimental; V0.7 remains adopted; V0.8 remains research-only  
关联：Issue #11

## 一、为什么选这件

Package B 要求：

1. T0 时为 **R0/R1**；
2. T0 信息不得使用后来成功结果；
3. 后来形成重大产品 / 标准 / 平台；
4. early T0 存在可观察的 option / future-value signals；
5. **PageRank 不计入**；
6. 相对 #1（mRNA）、#2（OLED）、#3（LIB）应 **进一步多元化**（本案：自旋电子 / 磁存储传感，而非生命科学、有机显示或能源电化学）。

US4949039A（Kernforschungsanlage Jülich；Peter Grünberg）满足这些约束：

- 预注册 early T0 = **1990-08-14**（US 授权日）时，公开记录是已授权公共研究机构专利 + Fe/Cr 多层巨磁阻科学平台与权利要求，而不是已上市 GMR 硬盘读头映射；
- 1988 Fert 组 PRL 与 1989 Grünberg 组 PRB 给出 GMR 科学连续性；1990 本专利给出反平行铁磁多层 + 非铁磁中间层的磁场传感器架构 option signal，并明确面向磁存储读出；
- 后来（post-T0）IBM 约 1997 首款商用 GMR/spin-valve 硬盘读头、以及此后硬盘面密度跃升——但这只能写在回顾设计里，不能回填 early ledger；
- **不得**把约 1990 年的各向异性磁阻（AMR）读头当成 GMR 本专利的上市载体。

公开核验（2026-10-12）：

- Google Patents：[US4949039A](https://patents.google.com/patent/US4949039A/en) — grant 1990-08-14；filing 1989-06-14；priority DE 1988-06-16；inventor Peter Grünberg；assignee Kernforschungsanlage Jülich GmbH。
- DOI：[10.1103/PhysRevLett.61.2472](https://doi.org/10.1103/PhysRevLett.61.2472) — Baibich / Fert et al., *Phys. Rev. Lett.* 61, 2472–2475 (1988-11-21)。
- DOI：[10.1103/PhysRevB.39.4828](https://doi.org/10.1103/PhysRevB.39.4828) — Binasch / Grünberg et al., *Phys. Rev. B* 39, 4828(R) (1989-03-01)。

## 二、Early T0 = 1990-08-14（授权日）

Ledger：`data/ledgers/non-award-gmr-us4949039-early-option.jsonl`

选择授权日作为 T0，是因为该日 US 文本首次完整公开“反平行铁磁多层 + 适当非铁磁中间层”的磁场传感器架构，且仍早于 IBM 1997 商用 GMR 读头约七年。Fert/Grünberg 科学发现已在 T0 之前完成，故可作为平台前序，而 realization 仍从 Right Exists 起算。

### V0.7 能诚实记录的

| 维度 | 状态 |
|---|---|
| Realization stage | **R0 — Right Exists** |
| Knowledge origin | confirmed（KFA Jülich / Grünberg） |
| Technical differentiation | strong_evidence（1988/1989 GMR 科学平台；1990 传感器权利要求与相对 AMR 的增强 MR 叙述） |
| Exact patent → marketed carrier | **unknown** |
| Patent-level attributable value | **unknown** |

### 在 T0 可观察的 option / future-value signals（不是 R3）

1. **KFA Jülich 持有**的多层磁场传感器专利（公共研究机构来源清晰）；
2. **Fert 组 PRL 1988**：Fe/Cr 超晶格巨磁阻——面向未来高灵敏度磁传感的公开科学平台信号；
3. **Grünberg 组 PRB 1989**：Fe–Cr–Fe 层间反铁磁交换增强磁阻——与本专利发明人连续的平台前序；
4. **本专利装置架构**：反平行铁磁层 + 非铁磁中间层（厚度小于传导电子平均自由程），相对各向异性磁阻显著增大电阻变化——面向未来磁存储读出传感器的 option signal；
5. 专利文本本身以硬盘 / 软盘 / 磁带等磁存储读出及高空间分辨磁场测量描述可实用化装置方向。

这些信号说明：

> 在 realization 仍为 R0 时，资产已经具备可核验的未来期权特征。

它们**不能**被读成：

> 已经实现 R3+ 的上市 GMR 硬盘读头映射。

## 三、Post-T0 ground truth（仅用于回顾设计，不进入 early ledger）

Early ledger 设置 `post_t0_ground_truth_allowed=false`。

回顾设计需要知道“后来确实形成重大现实价值”，以便检验 H2c，但下列事实**不得**写入 T0=1990 ledger：

- IBM 约 1997 首款商用 GMR / spin-valve 硬盘读头；
- 此后硬盘面密度数量级跃升与 GMR→TMR 读头演进；
- 2007 诺贝尔物理学奖叙事；
- 任何把企业级硬盘业务收入直接归因给本专利的做法。

本回顾只要求：early T0 是干净的 R0/R1，且后来路径是重大现实成功。商用 GMR 读头路径满足“后来成功”条件，但属于 post-T0。

## 四、对 V0.7 / V0.8 的压力测试结果

### V0.7 做对了什么

- 拒绝把后来的 GMR 硬盘产业成功倒灌成 1990 的 R3/R4/R5；
- 允许 R0 同时保留自旋电子 / 磁阻分化证据；
- Unknown ≠ 0：没有 exact mapping 就不抬阶段；
- 明确区分约 1990 的 AMR 读头与本案 GMR 架构（避免伪映射）。

### V0.7 仍然说不清楚的

同一件专利在 early T0 的决策相关信息，很大一块是：

> **option / future-value horizon**

而不是当前 realization stage。

V0.7 可以把 1990 记成 R0，也可以（在另一个未来 ledger 中）把商用 GMR 读头后记成更高 R，但**缺少一个结构化对象**来表示：

- early option signals；
- remaining exclusivity / term；
- “低 realization ≠ 低期权价值”。

这与 Package B #1–#3 同构，并把样本扩到 **自旋电子 / 磁存储传感**：

| 样本 | 现象 |
|---|---|
| PageRank | 已是 R4，但两只钟（revealed vs remaining exclusivity）反向运动（**不计入** Package B） |
| US8278036 early T0 | 仍是 R0，生命科学 option signals 已可观察 |
| US4539507 early T0 | 仍是 R0，非生命科学（OLED 平台）option signals 已可观察 |
| US4668595 early T0 | 仍是 R0，能源存储（实用 Li-ion 架构）option signals 已可观察 |
| US4949039 early T0 | 仍是 R0，自旋电子（GMR 读传感）option signals 已可观察 |

## 五、Package B 进度

| # | Case | Early T0 stage | Status |
|---|---|---|---|
| 1 | US8278036B2 modified-nucleoside RNA | R0 @ 2012-10-02 | complete |
| 2 | US4539507A Tang–VanSlyke thin-film organic EL | R0 @ 1987-09-21 | complete |
| 3 | US4668595A Yoshino practical nonaqueous secondary battery | R0 @ 1987-05-26 | complete |
| 4 | US4949039A Grünberg multilayer GMR-type magnetic-field sensor | R0 @ 1990-08-14 | **complete（本 PR）** |

PageRank 不计入 Package B。**Package B 预注册阈值 4/4 已达到。**

## 六、治理边界

- 不修改正式 Ledger Schema 1.0；
- 不把 option signals 偷偷塞进 R-stage；
- 不把 IBM 1997 / 硬盘面密度成功回填 early T0；
- 不把 Jülich / IBM / 硬盘产业企业价值记成该专利在 1990 的内在价格；
- 不把约 1990 的 AMR 读头伪映射为本案 GMR 专利的 E3 载体；
- 不把 Fert 科学发现或诺贝尔叙事继承为本案在 T0 的 attributable value。

V0.7 remains adopted.  
V0.8 remains research-only until Package C 剩余项（SEP/pool/cross-license；非生命科学复杂组合）完成后，再做新的 cross-case synthesis。
