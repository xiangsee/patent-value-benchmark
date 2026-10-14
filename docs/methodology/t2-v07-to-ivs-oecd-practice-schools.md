# T2 深化备忘：V0.7 ↔ IVS 210 / OECD 无形资产 / 美欧中实务学派

> Status: **research comparison deepen v0**（2026-10-14 Asia/Shanghai）  
> Track: **T2** · 承接 [`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md) · 场景树 [`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md)  
> Formal: **V0.7** + **schema 1.0** · **未** adopt / freeze V0.8 · **不**输出美元总分  
> 引用纪律：下列来源均经公开网页 / PDF 核验；**无**伪造文献或页码。本页**不是**合规意见或估值结论。

## 0. 一句话

| 层 | 回答的问题 |
|---|---|
| **V0.7（本库正式面）** | 在固定 T0 与选定价值建构下，**证据能否把实现归因到这件专利**，以及仍停在何处 Unknown |
| **IVS / 中评协 / USPAP·SSVS 等金额学派** | 在选定价值基础与前提下，**值多少钱 / 何种费率** |
| **OECD 转让定价（Chapter VI）** | 关联方无形交易的**独立交易原则**条件（含 DEMPE / HTVI） |
| **诉讼 / FRAND 救济学派** | 争议情境下的**合理许可费或损害救济**（≠ 资产市值） |

V0.7 是**上游证据—实现闸门**；通过后才适合进入金额 / 费率测算。**不是** IVS 或 OECD 的替代品。

## 1. 对照表（一页核心）

| 轴 | V0.7 | IVS 210（无形资产） | OECD TPG Ch. VI | 美 / 欧 / 中实务学派（摘要） |
|---|---|---|---|---|
| **价值建构** | Value / Attribution / Observability / Realization（R0–R5）；Unknown≠0 | 按**价值基础**（如市场价值、投资价值等）与**使用意图**给出意见；市场 / 收益 / 成本路径 | **独立交易条件**；关注经济价值是否在关联方之间转移，而非标签 | 美：USPAP Std 9–10 + AICPA VS §100 估金额；欧：常叠 IVS + OECD TP，SEP 另走 FRAND；中：中评协指南按评估目的选价值类型并估金额 |
| **分析单元** | 件 ↔ 价值载体（E3）→ 件级可归因经济结果（E4） | 可识别无形资产（常含专利、商标、技术等；可单件或组合） | 无形及相关 DEMPE 功能 / 风险 / 资产；交易可含使用或转让 | 中评协明确专利**所有权 / 使用权**及许可形式；实务常与其他资产共同发挥作用 → 与本库「非继承」同向 |
| **T0 / 截止** | 显式 T0；禁 outcome leakage | 评估基准日 / 估值日清晰；预测需假设 | 交易时点事实；HTVI 允许在特定条件下用事后结果检验事前高度不确定假设 | 诉讼 / FRAND 以裁判与谈判时点为界；判赔≠内在市价（见 T4 INT-5） |
| **Unknown** | 一等公民；缺 E3 诚实 R0 | 缺可比则改方法、加折价或扩大假设披露；少把「未知」当输出态 | 无可比时用其他方法或估值技术；强调假设可验证 | 打分 / 引证学派常填补 → **Screening≠Proof** |
| **货币主张** | **正式面否**（金额可作 E4 线索） | **是**（金额） | **是**（ALP 价格 / 利润分割等） | **是**（评估报告 / 裁判费率） |
| **与 V0.7 接口** | — | **互补下游**：E3/E4 约束「收入/特许能否归本件」后再做 relief-from-royalty 等 | **互补平行**：DEMPE / 功能分析可提示「谁创造价值」，但**不能**替代件级 E3 | 许可可比、诉讼合理许可费 → E4/RC 语境输入；**不**自动抬 R5 |

## 2. 三所「金额学校」要点（核验摘要）

### 2.1 IVS 210 Intangible Assets（IVSC）

- **现行** IVS 含 Asset Standard **IVS 210**；现行版自 **2025-01-31** 生效（见 IVSC 2026 Exposure Draft *Basis for Conclusions* 对现行版的引用）。  
- **2026 征求意见稿**拟于 2027 发布、**2028-01-31** 强制适用；拟修订 IVS 210 结构以对齐 General Standards（框架、业务范围、数据与输入、模型、报告）。咨询页：IVSC。  
- WIPO（2026-05-05）公开致函确认：IVS 210 处于财务报告、转让定价、许可、诉讼与 IP 融资等语境的核心；并强调宜保持**目的中立**、勿过度绑定财务报告术语。  
- **映射**：IVS 先定 scope / basis of value / approach；V0.7 先定「有没有可复核的件↔载体与归因」。无 E3 时做 IVS 式收益法，易把企业/产品现金流**继承**到本件。

### 2.2 OECD 转让定价指南 Chapter VI（无形）

- *OECD Transfer Pricing Guidelines … 2022*，**Chapter VI Special considerations for intangibles**（官方 PDF，DOI `10.1787/0e655865-en`）：目标是关联方无形**使用或转让**的**独立交易条件**；功能分析须落到功能、资产与风险。  
- 补充：估值技术（含基于预测现金流折现）在缺乏可靠可比时可作工具；另有 **Hard-to-Value Intangibles (HTVI)** 专节及 2018 税局适用指引。  
- **映射**：OECD 问的是「集团内谁应按 ALP 得回报」；V0.7 问的是「公开证据能否把实现归到**这件专利**」。HTVI 的高度不确定性 ↔ 本库早 T0 / Unknown 纪律，但**税务事后调整权 ≠** 本库允许 outcome leakage 回填早年 R。

### 2.3 美 / 欧 / 中常见实务学派（非穷尽）

| 区域 | 可核验锚点 | 与 V0.7 |
|---|---|---|
| **美国** | The Appraisal Foundation：**USPAP**（2024 版起生效）覆盖含**无形资产**在内的商业评估学科；Standards **9–10** 规范商业/无形资产评估的开展与报告（见 USPAP 公开说明与标准文本）。AICPA：**VS Section 100 / SSVS**（估企业、权益、证券或**无形资产**并发表结论/计算价值时适用）。诉讼侧合理许可费（如 Georgia-Pacific 传统因素）属**救济建构**。 | 金额与救济 = 下游 / E4·RC 语境；**判赔 ≠** 资产公允价值 |
| **欧洲 / 跨境 SEP** | 实务常叠 **IVS** + **OECD TP**。SEP/FRAND：WIPO *FRAND Economics*（公开网络版）归纳——大陆欧洲多依 *Huawei v. ZTE* 审查**谈判行为与要约是否明显非 FRAND**，英/中等法域更常直接定费率；比较许可 / bottom-up / top-down 为常见方法族。 | FRAND 费率 = 标准必要组合与谈判建构；**禁止**当作单件内在价格或自动 R5 |
| **中国** | 中国资产评估协会：*知识产权资产评估指南*（**中评协〔2017〕44号**，2017-10-01 施行）与 *专利资产评估指导意见*（**中评协〔2017〕49号**）：明确评估目的（转让、许可、出资、质押、诉讼、财务报告等）、价值类型、市场/收益/成本法；专利对象含所有权与各类使用权；并强调知识产权常与其他资产**共同作用**、须恰当区分单件与组合。 | 与「非继承 / 先映射后金额」同向；中评协报告仍是**金额结论**，本库正式面仍停在证据—实现状态 |

另：**WIPO** *Intellectual Property Valuation Basics for Technology Transfer Professionals*（2025）面向早期技术转移，覆盖成本 / 市场 / 收益 / 实物期权，强调数据稀缺与假设可辩护——靠近本库 Package B「早 T0 停 R0」，仍属金额指南而非 R 阶梯。

## 3. 分工口诀（给编码与对外说明）

1. **先建构、再 T0、再证据**（V0.7）→ 再谈金额（IVS / 中评协 / SSVS）。  
2. **Orange Book / 说明书 / 判决点名** 可支撑 E3；**不等于** IVS 公允价值。  
3. **合理许可费 / 判赔 / FRAND 区间** 可作 E4 线索；**不等于** 专利资产市值，也**不**自动 R5（仍要 E3 + exact_patent 指标）。  
4. **OECD DEMPE** 解释集团回报分配；**不能**代替 claims-check。  
5. **引证 / ML 分** 仍是 Screening，落在矩阵「拒绝对齐」清单。

## 4. 非目标

- 不 adopt V0.8；不改 schema 1.0；不编码新 ledger。  
- 不声称本备忘可替代持证评估师 / 税务意见 / 法律意见。  
- 场景选用决策树：[`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md)（冷启动 / IVS / OECD TP / FRAND / 诉讼损害）。

## 5. 已核验来源（URL）

| # | 来源 | URL / 标识 |
|---|---|---|
| 1 | IVSC — IVS Exposure Draft consultation 2026（含 IVS 210 修订说明入口） | https://ivsc.org/consultations/ivs-exposure-draft-for-consultation-2026/ |
| 2 | IVSC — *Basis for Conclusions* PDF（引用现行 IVS effective 31 Jan 2025；IVS 210 修订动机） | https://ivsc.org/wp-content/uploads/2026/02/IVS-effective-31-January-2028-Exposure-Draft-Basis-for-Conclusions.pdf |
| 3 | WIPO 致 IVSC 函（2026-05-05）论 IVS 210 多目的适用 | https://www.wipo.int/documents/d/ip-financing/docs-letter-to-mr-nick-talbot.pdf |
| 4 | OECD Transfer Pricing Guidelines 2022（Ch. VI；DOI 10.1787/0e655865-en） | https://www.oecd.org/en/publications/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a.html |
| 5 | OECD — HTVI 税局适用指引（BEPS Action 8，2018） | https://www.oecd.org/en/publications/guidance-for-tax-administrations-on-the-application-of-the-approach-to-hard-to-value-intangibles-beps-action-8_5e402215-en.html |
| 6 | WIPO — IP Valuation Basics for Technology Transfer Professionals（2025） | https://www.wipo.int/publications/en/details.jsp?id=4805&plang=EN |
| 7 | WIPO — FRAND Economics（公开网络版，方法与法域差异） | https://www.wipo.int/web-publications/frand-economics-valuation-methods-in-licensing-standard-essential-patents/en/2-mutually-beneficial-terms-the-role-of-the-frand-undertaking-and-valuation-methodologies.html |
| 8 | The Appraisal Foundation — USPAP 概述（2024 版；含商业/无形资产学科） | https://appraisalfoundation.org/pages/uspap |
| 9 | AICPA — VS Section 100 / SSVS 说明页 | https://www.aicpa-cima.com/resources/article/statement-on-standards-for-valuation-services-vs-section-100 |
| 10 | 中国资产评估协会 —《知识产权资产评估指南》中评协〔2017〕44号（公开转载含全文） | https://www.chinaiprlaw.cn/index.php?id=4921 |
| 11 | 中国资产评估协会 —《专利资产评估指导意见》中评协〔2017〕49号（行业公开文本；与 44 号同日体系） | 见中评协体系公开转载，例如 https://docs.maoyanqing.com/appraisal/aas/aai/201749.html |

## 指针

- 矩阵：[`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md)  
- 场景树：[`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md)  
- T1：[`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md)  
- Formal：[`model-v0.7.md`](model-v0.7.md) · [`evidence-levels.md`](evidence-levels.md)  
- 四轨：[`world-class-roadmap.md`](world-class-roadmap.md)
