# T2 决策树走查：INT-5（PureWick）与 INT-9（Kerendia）

> Status: **research worked example**（2026-10-14 Asia/Shanghai）· 中文主述  
> Track: **T2** · 树：[`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md)  
> 编码合成：[`../analysis/non-award-validation/holdout-int-135-synthesis.md`](../../analysis/non-award-validation/holdout-int-135-synthesis.md) · [`holdout-int-7911-synthesis.md`](../../analysis/non-award-validation/holdout-int-7911-synthesis.md)  
> Formal: **V0.7 + schema 1.0** · T0=**2026-10-13** · **未** adopt V0.8 · **不**新编码  
> 建构对照：[`t1-construct-scenario-matrix.md`](t1-construct-scenario-matrix.md) · 判赔≠FMV：[`t1-frand-damages-vs-r5-fmv.md`](t1-frand-damages-vs-r5-fmv.md)

**目的：** 用两件**已编码** INT holdout，演示「主问题 → T2 枝 → V0.7 闸门 → 实际 R」；不是重审案件，也不是给费率建议。

---

## 例 A — INT-5 · US10376407B2 · PureWick（已编码 **R5**）

### A1. 认建构 / 主问题

| 项 | 本例取值 |
|---|---|
| 主问题（假设用户问法） | 「D.Del. 判了约 $1.80M royalty，这件专利是不是值这个数？能不能记 R5？」 |
| 正确建构拆分 | （1）**诉讼救济 / 合理许可费**；（2）若还要挂牌市价 → 另开 **FMV** 建构，勿混标签 |
| 错误建构 | 「判赔 = FMV = 自动 R5」 |

### A2. 走 T2 树

```text
主问题必须要货币？ → 是（救济金额）
场景类型？ → 侵权损害 / 合理许可费诉求
交接 → 诉讼损害层（判赔是救济建构）
GATE3：有本件 E3 + exact_patent 指标才可谈 R5？
        → 是（法院语境下映射与件级 royalty 指标齐备）
        → 可 R5；金额仍 = 争议情境（≠ 内在市价）
```

若用户**只**问「公开诊断走到哪」→ 树左枝「只用 V0.7」，仍得到 R5，但报告须标注金额来源=救济。

### A3. V0.7 闸门核对（与编码一致）

| 闸门 | INT-5 |
|---|---|
| E3 | confirmed（court） |
| E4 | 单件 royalty 指标 |
| R | **R5** |
| 金额标签 | 争议 / 裁判 royalty · **≠ FMV** |

### A4. 禁止偷换（本例）

- 不得把 ≈$1.80M 写成「公允市价」或 IVS 选定价值基础，除非另做价值类型声明的下游报告。  
- 不得因「有判赔」推广到「凡美医疗器械专利皆 R5」。

---

## 例 B — INT-9 · KR101614164B1 · Kerendia / Bayer（已编码 **R3**）

### B1. 认建构 / 主问题

| 项 | 本例取值 |
|---|---|
| 主问题（假设） | 「MFDS Green List 点名 10-1614164，药已上市，是不是可以估 ALP/市价并抬 R5？」 |
| 正确建构拆分 | （1）**已实现经营价值**诊断 → 先 V0.7 claims-check；（2）若要 ALP → **DEMPE/OECD** 另纸；（3）若要 FMV → **IVS** 另纸 |
| 错误建构 | 「Green List = Exploitation 完成 = E4/R5 = FMV」 |

### B2. 走 T2 树

```text
主问题只要状态 / 冷启动诊断？ → 先「只用 V0.7」
  claims-check：Green List + label 与 finerenone 物种对齐 → E3 PASS
  件级可归因金额？ → 无（本编码无 E4）
  → 停 R3；不交接金额继承

若用户坚持「必须要 ALP / 市价」：
  场景 → 关联方 TP 或融资估值
  交接 → OECD 或 IVS
  GATE：可信 E3？ → 是（有 E3）
  但回写 Ledger：仍无 exact_patent 经济指标 → E4 Unknown，R 保持 R3
  下游金额并列报告，禁止倒写假 E4 抬 R5
```

### B3. V0.7 闸门核对（与编码一致）

| 闸门 | INT-9 |
|---|---|
| E3 | PASS (strong) — Green List + 化合物对齐 |
| E4 | **无** |
| R | **R3** |
| 监管通道 | MFDS Green List ≈ 形态上的 US OB / CN NHSA 显式号；**≠ 自动 E4** |

### B4. 禁止偷换（本例）

- Green List / 上市 ≠ DEMPE 已定价，也 ≠ R5。  
- 不得把「可对 claim 的 API」直接写成件级销售收入归因。

---

## 两例对照（同一把树）

| 步骤 | INT-5 PureWick | INT-9 Kerendia |
|---|---|---|
| 树主枝 | 诉讼损害 → GATE3 | 先 V0.7；若要钱再 IVS/OECD → GATE |
| E3 | 有 | 有 |
| E4 | 有（单件裁判 royalty） | 无 |
| R | **R5** | **R3** |
| 金额能不能当 FMV | **不能**（救济） | 本 Ledger **无金额**；另开下游也不得倒写 E4 |
| 课堂句 | 闸门齐才 R5；R5 ≠ FMV | 监管 E3 可诚实抬；E3 ≠ E4 |

---

## 非目标

- 不重新编码、不改 R、不 adopt V0.8。  
- 不输出推荐费率、ALP 或市价数字。  
- EP/其他未编码 INT 不得套用本走查结论。
