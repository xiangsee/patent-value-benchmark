# Counterfactual Control 研究导读（对外入口）

日期：2026-10-12  
状态：**research-only / analysis-first（无 experimental schema）**  
正式方法基线：**V0.7 (adopted)**  
正式数据表面：**Ledger / Diagnostic schema 1.0（已冻结）**  
**V0.8：未采纳；本页任何内容都不构成采纳或升格。**

关联议题：[Issue #37](https://github.com/xiangsee/patent-value-benchmark/issues/37)（Counterfactual Control — replication before schema；**已关闭 / completed**）  
姊妹实验线入口：[`rights-control-research-overview.md`](rights-control-research-overview.md) · [`realization-path-research-overview.md`](realization-path-research-overview.md)

---

## 1. Counterfactual Control 是什么

Counterfactual Control 回答的是：

> 在某一 **T0**，若拿掉（或禁用）该专利所覆盖的模式，**竞争者还能不能带着同一产品品类 / 功能集合继续走？** 文档化的 **next-best alternative / design-around / blocking scope** 是什么？

它关心的是 **定性 / 结构化叙事**（复制阶段）的：

- `next_best_alternative`（去掉专利模式后还剩什么）
- `design_around_feasibility`（≤ T0 可文档化的 NIA / 重设路径）
- `performance_or_feature_loss_if_removed`（丢功能 vs 品类仍可继续）
- `blocking_scope`（feature / product-line / standard）
- `fto_path`（若有：如 FRAND / 池许可 — **仅作语境，不是分数**）

它 **不** 回答：

- 专利“值多少钱” / 损害赔偿该判多少（那是 **Realization Path** 的金额事件域）
- claim-set 法律控制此刻站在哪（禁令、PTAB、终局、operative remedy → **Rights Control**）
- V0.7 的 R0–R5 该升到哪（那是 **Value Realization Stage**）
- 绕开要花多少美元 / blocking 打多少分（**禁止**发明 `design_around_cost_usd` / `blocking_score`）

一句话：

> **R0–R5 描述价值实现走到哪一证据阶段；Rights Control 描述法律控制站在哪；Realization Path 描述现金 / 控制 / 合同性未来价值沿什么路径发生；Counterfactual Control 描述「若无此模式，替代与封锁范围如何」。四者并列，不能互相推导。**

---

## 2. Counterfactual Control 不是什么

| 常见误读 | 本轨道实际含义 |
|---|---|
| 高 R ⇒ 强 blocking | ❌ R 回答证据阶段，不回答替代方案 |
| 有禁令 = Counterfactual | ❌ 禁令 / 终局 / operative remedy ∈ **Rights Control**；NIA / redesign / demand-driver ∈ **Counterfactual** |
| lost-profits「无 NIA」⇒ 发明 redesign $ | ❌ 保持定性 / 有引用；不伪造损害赔偿 |
| Feature NIA = 产品品类死亡 | ❌ 必须记录 `blocking_scope`（feature / product / standard） |
| 池费率 / SEP 许可费 = redesign cost | ❌ 费率 ∈ Realization Path / 许可语境；≠ Counterfactual 美元成本 |
| 正式 Ledger 1.0 字段 / experimental JSON schema | ❌ **尚未**建 `schema/experimental/counterfactual*`；本轮只有 analysis notes |

---

## 3. 与 V0.7 Ledger / R-stage / RC / RP 的边界

| | V0.7 Ledger / Diagnostic（正式） | Rights Control（实验） | Realization Path（实验） | Counterfactual Control（研究） |
|---|---|---|---|---|
| 问题 | 价值状态、归因、可观察性、实现**阶段** | claim-set **法律控制** | 实现**路径**（事件 → 经济三分量） | **替代 / 绕开 / 封锁范围** |
| 粒度 | 专利 / ledger 行 | claim-set + 辖区 + T0 | rights_subject + path + as_of | 案例笔记中的结构化表（复制阶段） |
| Schema | `schema/*.schema.json`，`1.0` | `experimental-0.1` | `experimental-0.1` | **无**（故意不建） |
| 数据位置 | `data/ledgers/` 等 | `data/experimental/rights-control/` | `data/experimental/realization-path/` | `analysis/non-award-validation/counterfactual-*.md` |
| 校验 | `validate_data.py` 等 | `validate_rights_control.py` | `validate_realization_paths.py` | 人工 / PR 审查；**无**独立 validator |

合法观察（Issue #37 已复制）：

- **同属高 realization 带**（R5 / R4），但 **NIA / blocking_scope 实质不同**（i4i 硬 feature NIA vs Apple ’381 有 NIA + 低产品封锁）
- 禁令 operative ≠ 自动推出 Counterfactual；禁令拒绝 ≠ 自动推出「弱专利」——仍要分开记 Rights vs alternatives
- SEP 可出现 `blocking_scope=standard` + `fto_path=FRAND/pool`，与 feature 案 **不同构**（exploratory，不拿来凑 matched 门槛）

因此：**不能把 Counterfactual 塞回 R0–R5**，也不能并进 Rights Control 或 Realization Path 对象。

---

## 4. 什么时候该看本轨道

适合打开本轨道的情形：

1. 已有 **V0.7 Ledger**，R-stage 相同或相近，但叙事暗示 **替代方案 / 封锁范围不同**（feature 可删 vs 功能不得不禁；整机需求驱动 vs 标准锁定）。
2. 在读 [Issue #37](https://github.com/xiangsee/patent-value-benchmark/issues/37) 的 matched pair 或 pair synthesis。
3. 需要检查：**Similar high R ≠ similar alternatives story**；决策在 **不改 R** 时是否因 Counterfactual 改变。
4. 在评估 V0.8 research agenda §3（Counterfactual）的 **复制证据**，而不是在填冷启动贡献。

冷启动 / 外部复现贡献（Getting Started、#2 类任务）**默认只碰正式 Ledger 1.0**；不必也不应把 Counterfactual 字段写进 `schema_version: "1.0"` 的 ledger 行。

---

## 5. 什么时候 **不要** 升格进 schema（含 experimental）

下列任一成立，就 **停止**，保持 analysis-only：

1. 想把 Counterfactual 字段直接写进正式 Ledger / Diagnostic 行。
2. 想新建 `schema/experimental/counterfactual*` 仅因为「复制门勾选了」——复制门 **≠** 字段已稳定到可校验；Issue #37 关闭只关闭 **replication** tracker。
3. 想发明 `design_around_cost_usd`、`blocking_score` 或把池费率当成 redesign 成本。
4. 想把「有禁令」写成 Counterfactual，或把 NIA 叙事写进 Rights Control。
5. 想把损害赔偿 / 和解现金事件写进 Counterfactual（那是 Realization Path）。
6. 仅因为 Round 2 门槛齐了或本页存在就宣布 V0.8 adopted。
7. 没有用户 / 维护者对 **采纳 V0.8**、**解冻 schema 1.0**、或 **批准 Counterfactual experimental schema** 的显式批准。

治理口令（保持有效）：

> **保持 V0.7 adopted；V0.8 research-only；formal schema 保持冻结的 1.0，直到另行显式批准。**  
> **不建 Counterfactual experimental schema，除非另有显式批准。**

---

## 6. Issue #37 如何服务研究问题

### 6.1 预注册问题

> Holding **Value Realization stage roughly similar**（诉讼已实现的商业专利，偏 R4–R5），does documenting **next-best alternative / design-around feasibility / feature- vs product-level blocking** add decision-relevant information that neither V0.7 R-stage nor Claim-set Rights Control can express?

### 6.2 复制门结果（已关闭）

[Issue #37](https://github.com/xiangsee/patent-value-benchmark/issues/37) 状态：**closed / completed**（2026-10-12）。  
Pass 标准 1–5 由 pair synthesis 勾选为 **满足**（详见 `counterfactual-i4i-apple381-pair-synthesis.md`）。

| # | 案例 | R 锚点 | Counterfactual 对照 | 计入 matched？ |
|---|---|---|---|---|
| 1 | i4i / US5787449 @ T0=2010-03-10 | **R5** | 硬 feature-level NIA；现实路径多为禁用以保留 Word 产品类 | **是** |
| 2 | Apple / US7469381 c19 @ CF观察日=2014-03-06 | **R4** | 记录承认 NIA；因果关联不足 → 低产品级封锁；永久禁令拒绝 | **是** |
| 3 | Via LA AVC SEP US6825782 | **R2**（不同 R） | standard-lock + FRAND/pool FTO | **否**（exploratory） |

结论层级要分清：

- **Replication gate：已满足** → 允许继续用 analysis notes 讨论维度；**仍不**自动批准 experimental schema。
- **≠ V0.8 adoption**。本仓库当前选择：**保持 V0.7；不 adopt V0.8；schema 1.0 不变；不建 counterfactual schema。**

### 6.3 仍不升级的理由（摘自 synthesis）

1. 观测仍是定性结构表，字段名未稳定到可校验；  
2. 尚无独立于诉讼裁判语言的「冷启动可填」操作定义；  
3. SEP 探索案说明 `blocking_scope=standard` + `fto_path` 与 feature 案不同构，过早冻字段会把特例写死；  
4. Governance 口令如上。

---

## 7. 库存清单（Inventory）

### 7.1 Schema

| 路径 | 状态 |
|---|---|
| `schema/experimental/counterfactual*` | **不存在（故意）** |
| 正式 `schema/*.schema.json` | **1.0 冻结；无 Counterfactual 字段** |

### 7.2 方法论文档

| 路径 | 角色 |
|---|---|
| **本页** `docs/methodology/counterfactual-control-research-overview.md` | 对外入口：是什么/不是什么、边界、何时看、何时不升格、库存 |
| `docs/methodology/model-v0.8-research-agenda.md` §3 | V0.8 议程中的 Counterfactual 段 |
| `docs/methodology/rights-control-research-overview.md` | 姊妹线：法律控制（勿合并） |
| `docs/methodology/realization-path-research-overview.md` | 姊妹线：实现路径（勿合并） |
| `docs/research-tracks.md` | Track A 研究线清单 |

### 7.3 Issue #37 / #38 / #39 分析笔记

| 路径 | 角色 | 来源 |
|---|---|---|
| `analysis/non-award-validation/counterfactual-i4i-us5787449.md` | Case #1 matched | PR [#38](https://github.com/xiangsee/patent-value-benchmark/pull/38) |
| `analysis/non-award-validation/counterfactual-apple-us7469381-bounceback.md` | Case #2 matched | PR [#38](https://github.com/xiangsee/patent-value-benchmark/pull/38) |
| `analysis/non-award-validation/counterfactual-i4i-apple381-pair-synthesis.md` | Replication-gate synthesis（勾选 pass） | PR [#39](https://github.com/xiangsee/patent-value-benchmark/pull/39) |
| `analysis/non-award-validation/counterfactual-via-la-us6825782-sep-fto.md` | Case #3 exploratory（不同 R） | PR [#39](https://github.com/xiangsee/patent-value-benchmark/pull/39) |
| [#37](https://github.com/xiangsee/patent-value-benchmark/issues/37) | Tracker；**closed / completed** | 预注册 + 关闭评论 |

### 7.4 相关正式 Ledger（对照用，仍属 1.0）

Counterfactual 笔记 **引用** 既有 R 锚点 ledger；引用 ≠ 把 CF 字段写进 Ledger。

| 类型 | 路径模式 |
|---|---|
| i4i R5 | `data/ledgers/non-award-i4i-us5787449.jsonl` |
| Apple ’381 R4 | `data/ledgers/non-award-apple-samsung-rights-pair2.jsonl`（及相关 rights pair） |
| Via LA SEP R2 | `data/ledgers/non-award-avc-us6825782-sep-pool.jsonl` |

### 7.5 Validators

**无。** 正式冷启动仍只要求：

```bash
python tools/validate_data.py
python tools/generate_diagnostics.py --check
python tools/render_reports.py --check
```

Rights Control / Realization Path 的实验校验 **不** 覆盖本轨道，也 **不** 暗示应为本轨道建 schema。

---

## 8. 推荐阅读顺序

1. 本页（边界与库存）
2. `counterfactual-i4i-apple381-pair-synthesis.md`（为何 Similar R ≠ Similar alternatives）
3. `counterfactual-i4i-us5787449.md` 与 `counterfactual-apple-us7469381-bounceback.md`（matched 细节）
4. （可选）`counterfactual-via-la-us6825782-sep-fto.md`（standard + FTO 探索面）
5. `rights-control-research-overview.md` / `realization-path-research-overview.md`（姊妹边界）
6. `model-v0.8-research-agenda.md` §3 + `round2-adoption-readiness-synthesis-v0.8.md`（为何仍不 adopt）

---

## 9. 非目标（Non-goals）

- 不修改 formal schema 1.0
- 不采纳 V0.8
- **不**创建 `schema/experimental/counterfactual*`（除非另有显式批准）
- 不提供 Counterfactual 总分 / blocking score / 伪精确 redesign 美元
- 不把本轨道当作冷启动必填项
- 不把 Rights Control（禁令/终局）或 Realization Path（现金/和解）静默并入本对象
- 不把 Issue #37 关闭误读为「已批准升格」
