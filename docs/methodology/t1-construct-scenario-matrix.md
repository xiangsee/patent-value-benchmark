# T1 短表：价值建构 × 场景选用对照

> Status: **research cheat-sheet**（2026-10-14 Asia/Shanghai）· 中文主述  
> Track: **T1** · 承接 [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md)  
> 场景树：[`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md)  
> Formal: **V0.7 + schema 1.0** · **未** adopt V0.8  
> 记分卡下一刀落实：[`t1-t4-executive-scorecard.md`](t1-t4-executive-scorecard.md)

**用法：** 先认「谈的是哪一种建构」，再看 T2 树该走哪一枝；表右列是**禁止偷换**句。本表不是估值或法律意见。

---

## 对照总表

| 价值建构 | 主问题 | T2 树优先枝 | V0.7 内怎么记 | 禁止偷换 |
|---|---|---|---|---|
| **技术分化 / 载体中心性** | 相对基线差在哪、是否卡住关键载体 | **只用 V0.7** | Value State；无 E3 不抬 R3+ | 引证分 / ML 分 ≠ Proof |
| **已实现经营价值** | 本件是否落到可核对载体与经济结果 | **先 V0.7**；要金额再交接 IVS | R0–R5 + E3/E4；Unknown≠0 | 产品热销 / 品牌叙事 ≠ 自动 E3 |
| **权利控制力（RC）** | claim-set 是否可控、终局、可执行 | V0.7 +（可选）RC 研究层；诉讼语境可交接判赔枝记 RC 语境 | RC ⊥ R；普通案可空；无裁决可 `not_applicable` | 无效维持 / 禁令 ≠ 自动抬 R |
| **未来选择权 / Horizon** | 早 T0 下的期权叙事 | **只用 V0.7**（停 R0/R1）；实物期权仅并列研究 | Two Clocks；Package B 纪律 | 后来畅销倒推早年 R |
| **交易 / 报告公允价值（FMV）** | 选定价值基础上「值多少钱」 | V0.7 闸门 → **交接 IVS / 中评协 / USPAP·SSVS** | Ledger 不输出美元总分；金额在下游报告 | 判赔 / FRAND 费率 ≠ FMV |
| **关联方 ALP / DEMPE 回报** | 集团谁执行 DEMPE、独立交易对价 | V0.7（公开侧）→ **交接 OECD TPG Ch.VI** | DEMPE ⊥ E3–E4（[`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md)） | 功能分析完成 ≠ 本件 E3/R5 |
| **FRAND（SEP 组合）** | 公平合理无歧视许可条件 / 行为 | V0.7（件与组合分开）→ **交接 FRAND 层** | 组合结果记争议/许可语境 | 组合费率摊成单件 R5 / 内在价 |
| **诉讼救济 / 合理许可费** | 特定争议下的损害或许可费救济 | V0.7 → **交接诉讼损害层**；回写须过 E3+exact_patent 才谈 R5 | E4/E5/RC 语境；金额=争议情境 | 有判赔 = FMV 或自动 R5（[`t1-frand-damages-vs-r5-fmv.md`](t1-frand-damages-vs-r5-fmv.md)） |
| **政策 / 奖项 / 高价值库标签** | 评审或统计口径是否命中 | Track B 信号；**勿交接金额当通用价值** | 可笔记；不抬 `exact_patent…` | 金奖 / 入库 = 通用经济价值或 R3+ |

---

## 三步口诀

```text
① 写明建构（上表左列选一行，可并列但标签分开）
② 主问题要状态还是要金额/ALP/FRAND/救济？→ 进 T2 树
③ 任何下游数字回写前：本件 E3；缺则 Unknown / 停 R，禁止倒写
```

## 与已编码例的快速锚（不展开）

| 建构误用风险 | 反锚 holdout |
|---|---|
| 经营价值假抬 | INT-1 / INT-7 / E3-N → R0 |
| 监管 listing 当 FMV | INT-3 / INT-9 → R3、无 E4 |
| 判赔当 FMV / 忘闸门 | INT-5 / INT-11 / E4-N1/N2 → R5 仅因闸门齐；金额仍争议情境 |
| 许可捆包当 E4 | E4-N5 → R2 |

走树详例：[`t2-decision-tree-walkthrough-int5-int9.md`](t2-decision-tree-walkthrough-int5-int9.md)。

## 非目标

- 不 adopt V0.8；不改 schema；不编码。  
- 不替代持证评估、税务或诉讼意见。
