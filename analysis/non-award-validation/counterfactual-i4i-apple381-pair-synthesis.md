# Counterfactual Control — short synthesis: i4i US5787449 × Apple US7469381 c19

日期：2026-10-12  
状态：Issue [#37](https://github.com/xiangsee/patent-value-benchmark/issues/37) **replication-gate checklist** — analysis-only  
正式基线：**V0.7**；Ledger / Diagnostic **schema 1.0**；**无** Counterfactual schema；**不** adopt V0.8  
案例笔记：`counterfactual-i4i-us5787449.md` × `counterfactual-apple-us7469381-bounceback.md`  
探索案（不同 R，不计入 matched pair）：`counterfactual-via-la-us6825782-sep-fto.md`

---

## 一、一页结论

两件都是诉讼已实现的商业软件 / UI 专利（R5 / R4），exact mapping 公开可核。  
**V0.7 R-stage 把它们放在同一「高 realization」带；Counterfactual 把它们拆开：**

| | i4i ’449 @ T0=2010-03-10 | Apple ’381 c19 @ CF观察日=2014-03-06 |
|---|---|---|
| V0.7 R 锚点 | **R5**（已有 Ledger） | **R4**（已有 Ledger；CF 证据截止早于 Ledger T0） |
| next_best_alternative | 提出的 NIA 对 **accused custom XML editor 用途** 不足 | 记录承认 rubberband / 边界反馈存在 **非侵权替代实现** |
| design_around_feasibility（保留功能时） | **低** → 现实路径是禁用功能 / 换 SKU | **相对高**（对整机竞争）→ 特征可省略且未证成驱动整机需求 |
| blocking_scope | **feature-level 强**；Word 产品类继续 | **feature-level 弱→中**；智能手机品类继续；永久禁令拒绝 |
| 决策差分（R 不变时） | 「要保留该功能 ⇒ 许可或合规禁用」 | 「去掉/替换该 UI 反馈 ≠ 退出智能手机市场」 |

**一句话：** Similar high R ≠ similar alternatives story. Counterfactual 在不改 R 的前提下改变「竞争者还能不能带着产品品类走」的判断。

---

## 二、Issue #37 Pass / fail — replication gate 勾选

### Pass（关闭本 tracker *replication* 门所需最低条）

| # | 标准 | 状态 | 依据 |
|---|---|---|---|
| 1 | ≥2 matched cases，similar R（偏 R4–R5），design-around / blocking **实质不同** | **满足** | i4i R5 × Apple ’381 R4；硬 feature NIA vs 有 NIA + 低产品封锁 |
| 2 | 每条 Counterfactual 主张引用 **公开源且日期 ≤ 各自 T0**（或显式标 post-T0 design-only） | **满足** | i4i：≤2010-03-10 Federal Circuit 重判路径；Apple：≤2014-03-06 N.D. Cal. renewed PI denial + Apple I 法理引用。两案均未发明 post-T0 绕开成本 |
| 3 | 每案至少展示一个 **R 不变、加上 Counterfactual 后决策改变** 的点 | **满足** | 见上表「决策差分」；配对表亦见两案笔记 §五 |
| 4 | 与 Rights Control 显式分离（禁令 / PTAB / 终局 ∈ Rights） | **满足** | i4i：禁令 operative → Rights；NIA 不足 → CF。Apple：禁令拒绝 → Rights；NIA / demand-driver → CF |
| 5 | 与 Realization Path 显式分离（损害赔偿 / 现金 / 和解 ∈ Path；不发明 redesign $） | **满足** | 两案均禁止把 verdict / damages 写成 design-around cost |

### Fail / stop（本轮确认未踩）

| 陷阱 | 本轮 |
|---|---|
| 发明 `design_around_cost_usd` / `blocking_score` | **未写** |
| 「有禁令 = Counterfactual」 | **拒绝**；禁令归 Rights |
| 写入 formal Ledger `schema_version: "1.0"` | **未写** |
| 宣布 V0.8 adopted / 解冻 schema 1.0 | **未做** |

### 关于「可选案 #3」

Issue 原文：案 #3 Via LA SEP 为 **exploratory / different-R**，**不要求**计入 matched-pair 最低门槛。  
本轮另交 `counterfactual-via-la-us6825782-sep-fto.md`（标准级封锁 + FRAND/池 FTO），用于扩展 `blocking_scope` / `fto_path` 观测面，**不**用来凑 R4–R5 配对。

---

## 三、仍不升级的理由（给未来 adoption 讨论预留）

复制门可以勾选，**不等于**该写 experimental schema：

1. 观测仍是 **定性结构表**，字段名未稳定到可校验；  
2. 尚无独立于诉讼裁判语言的「冷启动可填」操作定义；  
3. 探索案（SEP）说明 `blocking_scope=standard` + `fto_path=FRAND/pool` 与 feature 案不同构，过早冻字段会把 SEP 特例写死；  
4. Governance：**Keep V0.7; V0.8 research-only; schema 1.0 frozen.**

---

## 四、工件索引

| 文件 | 角色 |
|---|---|
| `counterfactual-i4i-us5787449.md` | Case #1 matched |
| `counterfactual-apple-us7469381-bounceback.md` | Case #2 matched |
| `counterfactual-via-la-us6825782-sep-fto.md` | Case #3 exploratory |
| 本文件 | replication-gate synthesis |
| [#37](https://github.com/xiangsee/patent-value-benchmark/issues/37) | tracker |

未创建：`schema/experimental/counterfactual*`、任何 formal Ledger 新行。
