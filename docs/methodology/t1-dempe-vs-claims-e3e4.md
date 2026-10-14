# T1 短备忘：OECD DEMPE ⊥ V0.7 claims-check / E3–E4

> Status: **research theory short memo**（2026-10-14 Asia/Shanghai）  
> Track: **T1** · 承接 [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md) · 对照 [`t2-v07-to-ivs-oecd-practice-schools.md`](t2-v07-to-ivs-oecd-practice-schools.md) §2.2 / 口诀 4  
> Formal: **V0.7** + **schema 1.0** · **未** adopt / freeze V0.8  
> 本页**不是**转让定价意见、估值意见或法律意见。

## 0. 一句话（正交）

| 框架 | 问的是什么 | 不问什么 |
|---|---|---|
| **OECD DEMPE**（TPG Ch. VI） | 关联方无形交易中，**谁执行** Development / Enhancement / Maintenance / Protection / Exploitation，从而谁应按**独立交易原则（ALP）**拿到经济回报 | 公开证据能否把**这件专利**钉到具体载体；本件是否已实现到 R3/R5 |
| **V0.7 claims-check → E3 → E4** | 在固定 **T0** 下，权利要求要素是否对得上公开载体（E3），以及是否存在**件级可归因**经济结果（E4） | 集团内功能/风险/资产如何分摊；税务上谁该拿 DEMPE 回报 |

二者**互补平行**，**不可互相替代**。  
口诀：**DEMPE 管「集团谁创造/谁回报」；claims-check / E3–E4 管「本件能不能对上、能不能归因」。**

## 1. 何时用哪一套

| 场景 | 优先用 | 仍要记得 |
|---|---|---|
| 关联方许可 / 成本分摊 / 利润分割 / 税局功能分析 | **DEMPE + ALP**（T2 / OECD） | 即使 DEMPE 指向「母公司研发中心」，也**不能**跳过本件 claims-check 把全集团收入写成 E4 |
| 冷启动诊断、holdout、公开 Ledger / Diagnostic | **V0.7**：claims-check → E3 →（有则）E4 → R | DEMPE 可作**叙事背景**，不得抬 `exact_patent_value_carrier_link` |
| IVS / 中评协金额报告 | 金额学派（下游） | 先过 E3/E4 闸门再谈 relief-from-royalty；见 T2 |
| 诉讼判赔 / 具名许可 | E4 线索 + RC 语境 | 判赔 ≠ DEMPE 回报分配，也 ≠ 自动 R5 |

选用树入口：[`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md)。

## 2. 防混淆对照（字段级）

| 若你看到… | 错误读法 | 正确读法 |
|---|---|---|
| 「母公司执行全部 DEMPE，子公司只是合约制造」 | 「母公司那件专利 = E3/R5」 | DEMPE 说**功能归属**；本件仍要独立 claims-check |
| Orange Book / Green List / NHSA 显式专利号 | 「DEMPE Exploitation 已完成 → 可估 ALP」 | 这是 **E3 监管映射**；金额仍属 IVS/OECD 下游 |
| 大合議 / D.Del. 单件判赔 | 「与 DEMPE Protection 同义」 | 这是 **E4（争议情境）+ E5**；救济建构 ≠ 集团 ALP |
| 品牌热销 + 同族 300+ | 「Exploitation 充分 → 抬 R3」 | **Screening / 非继承**；无 claims-check 则 R0（如 INT-7） |

## 3. 用本库 holdout 做反例（anti-conflation）

| Holdout | 若误用 DEMPE 会怎样 | V0.7 实际结果 | 教训 |
|---|---|---|---|
| **INT-7** JP6956213 / Style | 「MTG 自研自销全做 DEMPE → 专利已 Exploitation」 | **R0**：Style 叙事 ≠ claim 多区块垫+骶骨突起 | DEMPE 全做 ≠ E3 |
| **INT-1** TearLab Osmolarity | 「公司产品线即 Exploitation」 | **R0**：市售渗透压仪 ≠ 本专利 LFA 整合 claim | 产品环境 ≠ claims-check |
| **INT-9** Kerendia Green List | 「上市 = DEMPE 完成 = 可直接利润分割到本件」 | **R3**：监管 listing + 化合物对齐；**无 E4** | E3 ≠ E4；Green List ≠ ALP 金额 |
| **INT-3** Aubagio OB | 同上（US OB） | **R3**；不抬 R4/R5 | 监管 E3 仍无件级可归因金额 |
| **INT-11** ReFa 大合議 / **INT-5** PureWick royalty | 「判赔 = DEMPE Protection 的公允回报」 | **R5**：单件裁判 E3+E4；金额=**争议情境** | 救济 E4 ≠ 集团 DEMPE 回报，也 ≠ 内在市价 |
| **E4-N5** 具名许可捆服务费 | 「有许可即 Exploitation 已定价」 | **R2**：许可对价记服务费捆；无产品 E3 | 具名许可 ≠ 自动 E4/R5 |

完整编码表见：[`holdout-int-7911-synthesis.md`](../../analysis/non-award-validation/holdout-int-7911-synthesis.md) · [`holdout-int-135-synthesis.md`](../../analysis/non-award-validation/holdout-int-135-synthesis.md) · [`holdout-t4-phase-synthesis.md`](../../analysis/non-award-validation/holdout-t4-phase-synthesis.md)。

## 4. 最小工作流（避免偷换）

```text
① 写明场景：税务 ALP？公开诊断？金额报告？诉讼救济？
② 若税务 → DEMPE/功能分析另纸；结果不得直接写进 Ledger 的 E3/E4
③ 若诊断/编码 → 任何 E3 前 claims-check；不过则 link=unknown，停 R0/R2
④ 有 E3 仍无件级金额 → 停 R3（INT-3 / INT-9）
⑤ 有单件裁判/清晰特许金额 → 可记 E4；升 R5 仍须 E3 + exact_patent 指标
⑥ 需要「值多少钱 / ALP」→ 引用本 Ledger 归因边界，另开 IVS 或 OECD 工作纸（T2）
```

## 5. 非目标

- **不** adopt / freeze V0.8；**不**改 schema 1.0；**不**编码新 ledger。  
- **不**把本备忘当作 OECD 合规清单或 BEPS 实施方案。  
- DEMPE 五字展开仅作对照标签；细则以 OECD TPG Ch. VI 原文为准（见 T2 已核验来源）。

## 指针

| Doc | 角色 |
|---|---|
| [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md) | T1 主备忘：Construct / Two Clocks / RC⊥R / 纪律三原则 |
| [`t1-frand-damages-vs-r5-fmv.md`](t1-frand-damages-vs-r5-fmv.md) | T1 短备忘：FRAND/判赔 ≠ 自动 R5 / ≠ FMV |
| [`t2-v07-to-ivs-oecd-practice-schools.md`](t2-v07-to-ivs-oecd-practice-schools.md) | T2：V0.7 ↔ IVS 210 / OECD Ch. VI / 美欧中；DEMPE 不能代替 claims-check |
| [`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md) | 何时走 V0.7 vs IVS / OECD TP / FRAND / 判赔 |
| [`evidence-levels.md`](evidence-levels.md) · [`model-v0.7.md`](model-v0.7.md) | E1–E5 与正式架构 |
| [`world-class-roadmap.md`](world-class-roadmap.md) | 四轨总览 |
