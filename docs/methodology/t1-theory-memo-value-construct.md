# T1 理论备忘：Value Construct · Two Clocks · RC⊥R · 纪律三原则

> Status: **research theory memo v0**（2026-10-14 Asia/Shanghai）  
> Track: 世界级四轨路线 **T1** · [`world-class-roadmap.md`](world-class-roadmap.md)  
> Formal: **V0.7 adopted** + **schema 1.0** · **未** adopt / freeze V0.8  
> 对照：[`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md)（T2）· [`model-v0.7.md`](model-v0.7.md)

## 0. 一句话

先定**谈的是哪一种价值**（Value Construct），再在固定 **T0** 下分别记录：现实走到哪（Value / R）、证据能不能归因到这件专利（Attribution）、外人看不看得见（Observability）。  
**金额、打分、引证、奖项、权利强弱**可以进入对话，但不能偷偷替换上述问题。

## 1. Value Construct（价值建构）

「专利价值」不是单一标量。至少先分清：

| 建构（示例） | 问的是什么 | V0.7 中的位置 |
|---|---|---|
| 技术分化 / 载体中心性 | 相对现有方案差在哪、是否卡在关键载体上 | Value State |
| 已实现经营价值 | 产品/工艺/平台是否已落地并可归因 | Realization R0–R5 + E3/E4 |
| 权利控制力 | claim 是否可执行、稳定、终局 | **RC（研究层；⊥R）** |
| 未来选择权 / Horizon | 早 T0 时的期权，而非已实现现金 | Two Clocks / Package B 纪律 |
| 交易或报告公允价值 | 「值多少钱」 | **IVS 等下游**；非 V0.7 正式输出 |
| 政策/奖项标签 | 评审或统计口径 | Track B；≠ 通用价值 |

建构×场景选用短表：[`t1-construct-scenario-matrix.md`](t1-construct-scenario-matrix.md)。

规则：**换建构 = 换问题**。把 IVS 金额、引证分、金奖结果直接叫作「专利价值」，属于建构偷换。

## 2. Two Clocks（双时钟）

同一件专利可以有两套时间轴：

1. **评估时钟（T0）**：只允许使用 ≤ T0 的信息；禁止用后来的畅销、判赔、后授引证倒推早年价值（防 outcome leakage）。  
2. **实现时钟**：价值载体在现实中的推进（R0→R5）。R 高只说明「实现走得远」，不自动等于「当年在 T0 就该判高价值」。

PageRank 式「同专利、两 T0」与 Package B「早 T0 诚实停 R0」都服务同一纪律：  
**期权叙事 ≠ 已实现价值**；早年 Unknown 合法。

## 3. RC ⊥ R（权利控制 ⊥ 实现阶段）

| | Realization（R） | Rights Control（RC） |
|---|---|---|
| 问 | 价值是否已实现到载体 / 经济结果 | 权利是否可控、可执行、终局如何 |
| 单元 | 件 ↔ 载体映射（E3/E4） | 常需 claim-set 粒度 |
| 与金额 | R5 仍可能缺分摊 | 判赔/禁令是 RC 与 E4 的语境，不是 R 的别名 |

因此：

- **高 R ≠ 强 RC**（产品大卖但权利脆弱）。  
- **强 RC ≠ 高 R**（权利要求稳但尚未落到可核对载体）。  
- RC 对普通专利**永远可选**；无裁决可建 `not_applicable` 记录（研究层）。  
- **不**因 Round 2 / 探针完成而自动 adopt V0.8。

## 4. 纪律三原则（正式面硬约束）

1. **Screening ≠ Proof**  
   引证、族大小、权利要求数、ML 分、维持年限 → **筛选信号**。  
   不能单独把 `exact_patent_value_carrier_link` 抬成 strong_evidence，也不能抬 R3+。

2. **Unknown ≠ 0**  
   公开信息缺失记 Unknown，不填 0 以便打总分。  
   E3-C / E3-N1–N5 的 R0 是成功的诚实停机，不是模型失败。

3. **No inheritance（非继承）**  
   企业规模、产品热销、组合 300+、同族他案、品牌叙事 **不**自动传给本件。  
   需要本件的 E3（claims-check 后）才谈载体映射；E4 才谈件级可归因经济结果。

另：**T0 cutoff** 贯穿全部编码。

## 5. 对照 T2：我们站在哪两所「学校」旁边

用 [`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md) 定位：

| 学校 | 他们优化什么 | 与本备忘的关系 |
|---|---|---|
| **IVS / 特许费率 / 成本法** | 在选定价值基础上给出**金额或费率** | **互补下游**。V0.7 先回答「能不能把收入/许可归到这件专利」；通过后才适合进入 IVS 式测算。V0.7 **不是** IVS 替代品，也**不**输出美元总分。 |
| **引证 / 文献计量 / 多数 ML 打分** | 用可规模化代理做**排序或质量分** | 落在 **Screening**。可提高冷启动召回，**禁止**短路为 Proof 或 R3+。缺引证 ≠ 价值为 0（Unknown≠0）。 |
| 诉讼损害 / 奖项 / 期权叙事 | 救济对价、政策标签、未来选择权 | 分别服务 RC·E4、Track B、Two Clocks；均不可单列成通用「价值分」。 |

**分工口诀：**

> 引证学校帮你**找候选**；V0.7 帮你**证映射与实现**；IVS 学校在映射成立后帮你**谈价钱**。

## 6. 最小工作流（编码时）

```text
① 写明 Value Construct + T0
② Value / Observability 如实填；缺则 Unknown
③ 任何 E3 前做 claims-check；不过 → link=unknown，R 停住
④ 不把 Screening 信号、企业/产品事实继承为本件 E3/E4
⑤ RC 仅在有研究需要时可选填写；不与 R 互相推导
⑥ 需要金额时 → 另开 IVS/特许工作纸，并引用本 Ledger 的归因边界
```

## 7. 非目标

- 不 adopt V0.8；不冻新 schema；不改正式 1.0 字段。  
- 不宣称本备忘已证明预测效度或美元精度。  
- 下一版 T1：可补「建构 × 场景」选用表（许可谈判 / 侵权 / 融资披露 / 冷启动诊断）。DEMPE ⊥ E3–E4 短备忘已出 → [`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md)。

## 指针

- Formal：[`model-v0.7.md`](model-v0.7.md) · [`evidence-levels.md`](evidence-levels.md) · [`time-cutoff-and-outcome-leakage.md`](time-cutoff-and-outcome-leakage.md)  
- T1 短备忘：[`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md)（DEMPE ⊥ claims-check / E3–E4）  
- T2：[`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md) · [`t2-v07-to-ivs-oecd-practice-schools.md`](t2-v07-to-ivs-oecd-practice-schools.md)  
- Research：[`model-v0.8-design-draft.md`](model-v0.8-design-draft.md) · [`rights-control-research-overview.md`](rights-control-research-overview.md)  
- 更深建构讨论：[`../../analysis/theory/value-constructs-and-missing-dimensions.md`](../../analysis/theory/value-constructs-and-missing-dimensions.md)
