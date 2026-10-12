# Realization Path 研究导读（对外入口）

日期：2026-10-12  
状态：**research-only / experimental**  
正式方法基线：**V0.7 (adopted)**  
正式数据表面：**Ledger / Diagnostic schema 1.0（已冻结）**  
**V0.8：未采纳；本页任何内容都不构成采纳或升格。**

关联议题：[Issue #16](https://github.com/xiangsee/patent-value-benchmark/issues/16)（三路径复制预注册；已关闭 / completed）  
姊妹实验线入口：[`rights-control-research-overview.md`](rights-control-research-overview.md)

---

## 1. Realization Path 是什么

Realization Path 回答的是：

> 在某一 **as_of / T0**，权利人 **实际上沿什么路径** 取得（或不取得）经济结果？

它关心的是 **事件驱动** 的：

- 权益来源（entitlement：侵权裁决、合同、许可等）
- 实现机制（license / settlement / damages_verdict / exclusion_order / …）
- 经济结果三分量：**cash / control / contractual_future_value**
- 观察到的金额事件（按 scope 保存，**不**自动加总成「专利价值」）

它 **不** 回答：

- 专利“值多少钱”（intrinsic price）
- 技术有多先进 / 产品卖了多少（Value Base）
- claim-set 法律控制此刻站在哪（那是 **Rights Control**）
- V0.7 的 R0–R5 阶段该升到哪（那是 **Value Realization Stage**）
- 诉讼融资 / 律师能力有多强（Enforcement Capacity 仅作可选 context，**无分数**）

一句话：

> **R0–R5 描述价值实现走到哪一证据阶段；Rights Control 描述法律控制站在哪；Realization Path 描述权利人沿什么事件路径拿到（或尚未拿到）现金 / 控制 / 合同性未来价值。三者并列，不能互相推导。**

---

## 2. Realization Path 不是什么

| 常见误读 | 本对象实际含义 |
|---|---|
| jury verdict = 已实现现金 | ❌ verdict amount 与 `cash.status` 分离；Taction 固定为 `cash=unresolved` |
| 许可金额 = 单件专利价值 | ❌ portfolio / field rights 金额 **不** 机械继承给成员专利 |
| Infringement → Remedy → Cash 流水线 | ❌ Editas 无 merits 侵权裁决仍可收现；Wirtgen 以 control 为主、cash 可 `not_required` |
| Realization Score | ❌ 实验 schema **拒绝** score 字段 |
| 正式 Ledger 1.0 字段 | ❌ 数据在 `data/experimental/realization-path/`，单独校验 |

---

## 3. 与 V0.7 Ledger / R-stage 的边界

| | V0.7 Ledger / Diagnostic（正式） | Realization Path（实验） |
|---|---|---|
| 问题 | 价值状态、归因证据、可观察性、实现**阶段**（R0–R5） | 实现**路径**：事件 → 确定性 snapshot |
| 粒度 | 专利 / ledger 行 | `rights_subject`（claim_set / patent / portfolio / field_rights / receivable）+ 路径 + as_of |
| Schema | `schema/*.schema.json`，`schema_version: "1.0"` | `realization-path-events.schema.json` + `realization-path-snapshot.schema.json`，`experimental-0.1` |
| 数据位置 | `data/ledgers/`、`data/evidence/`、`data/source-registry/` | `data/experimental/realization-path/`；证据/来源仍可用正式 surface 交叉引用 |
| 校验 | `tools/validate_data.py` 等 | **单独** `validate_realization_paths.py` + `project_realization_paths.py --check` |
| CI 含义 | 通过 = 正式数据表面一致 | 通过 = 事件源可投影且可测试；**≠** 升格为正式字段 |

合法组合（三路径实际观察到的世界）：

- 高额 damages verdict + **cash unresolved**（Taction）
- **无** infringement judgment + cash received（Editas–Vertex）
- exclusion order **operative** + cash `not_required`（Wirtgen ITC）

因此：**不能把 Realization Path 塞回 R0–R5**，也不要用 R-stage 代替 cash/control/contractual 状态。

与 Rights Control 的边界：

- Rights Control：claim-set **法律控制**（裁决 / 终局 / operative remedy）
- Realization Path：权利人 **经济实现路径**（机制 + 经济三分量）
- 二者可互相链接（例如同一 Wirtgen LEO 语境），**禁止合并**为一个对象

---

## 4. 什么时候该看实验对象

适合打开本轨道的情形：

1. 已有 **V0.7 Ledger**，但叙事涉及 **裁决额 / 和解 / 许可 / 排除令**，需要区分「判了多少」与「收到多少 / 控制是否生效」。
2. 在读 [Issue #16](https://github.com/xiangsee/patent-value-benchmark/issues/16) 三路径复制或 Taction 状态迁移笔记。
3. 需要验证：**verdict ≠ cash**、**license without merits**、**control without cash** 等不变量。
4. 在评估 Realization Path experimental 0.1 的复制证据，而不是在填冷启动贡献。

冷启动 / 外部复现贡献（Getting Started、#2 类任务）**默认只碰正式 Ledger 1.0**；不必也不应把 Realization Path 字段写进 `schema_version: "1.0"` 的 ledger 行。

---

## 5. 什么时候 **不要** 升格进 schema 1.0

下列任一成立，就 **停止**，保持 experimental：

1. 想把 Realization Path 字段直接写进正式 Ledger / Diagnostic 行。
2. 想发明 `realization_score = 82` 或把 `observed_amount_events` 加总成 intrinsic patent value。
3. 想把 jury verdict 写成已实现现金 / 专利价格。
4. 想把 Rights Control 或 Counterfactual Control 静默并进本对象。
5. 想把 Enforcement Capacity 冻成 financing / counsel / expert **分数**。
6. 仅因为“CI 过了”或“三路径门槛过了”就宣布 V0.8 adopted。
7. 没有用户 / 维护者对 **采纳 V0.8** 或 **解冻 schema 1.0** 的显式批准。

治理口令（保持有效）：

> **保持 V0.7 adopted；V0.8 research-only；formal schema 保持冻结的 1.0，直到另行显式批准。**

---

## 6. Issue #16 三路径如何服务研究问题

### 6.1 预注册问题

[Issue #16](https://github.com/xiangsee/patent-value-benchmark/issues/16) 要求在提出实验 schema 前，至少复制三条异质路径，并至少一条含重大事件后的后续变化：

| Path | 案例 | 类型 | Snapshot 必须得到 |
|---|---|---|---|
| A | **Taction** v. Apple | litigation → merits → damages verdict | `mechanism=damages_verdict`；amount ≈ USD 5.7bn；**`cash=unresolved`** |
| B | **Editas** → Vertex → DRI | voluntary license → cash → receivable monetization | `entitlement=contractual`；`license` + `receivable_monetization`；**`cash=received`** |
| C | **Wirtgen** ITC LEO | infringement → exclusion → continuing control | `mechanism=exclusion_order`；**`control=operative`**；`cash=not_required` |

结论层级要分清：

- **三路径复制门槛：已满足** → 允许设计 **experimental schema 0.1**（已完成；事件源 + 确定性投影）。
- **≠ V0.8 adoption**。本仓库当前选择：**保持 V0.7；不 adopt V0.8；schema 1.0 不变**。

### 6.2 与 Taction 锚点的关系

- 案例笔记：`analysis/non-award-validation/taction-state-migration-2026.md`
- 状态迁移：2023 SJ 非侵权 → 2025 CAFC vacatur → 2026 证据争议 → 2026-09-25 ≈$5.7bn verdict → **收款 unresolved**
- 用途：证明「状态可编码」且 **禁止** 把 verdict 误写成 realized value；**不足以**单独支撑升格。

### 6.3 与 Round 2 / V0.8 agenda 的关系

- Realization Path 是 Package A（Rights Control）之后发现的 **exploratory** 维度；预注册独立于既有 V0.8 adoption 门槛。
- Round 2 综合见 `round2-adoption-readiness-synthesis-v0.8.md`：**仍不 adopt**。
- 议程说明见 `model-v0.8-research-agenda.md`（Exploratory dimension / experimental 0.1 status）。

---

## 7. 库存清单（Inventory）

### 7.1 Experimental schema

| 路径 | 角色 | `schema_version` |
|---|---|---|
| `schema/experimental/realization-path-events.schema.json` | Canonical event log（人工维护） | `experimental-0.1` |
| `schema/experimental/realization-path-snapshot.schema.json` | Generated snapshot（**禁止手改**） | `experimental-0.1` |
| `schema/experimental/README.md` | 实验目录横幅与隔离规则 | — |

（同目录下的 Claim-set Rights Control schema 是 **另一条** 实验线，不要与 Realization Path 合并。）

### 7.2 方法论文档

| 路径 | 角色 |
|---|---|
| **本页** `docs/methodology/realization-path-research-overview.md` | 对外入口：边界、何时看、何时不升格、库存 |
| `docs/methodology/realization-path-experimental-0.1.md` | 实验对象设计说明 |
| `docs/methodology/realization-path-data-dictionary.md` | 字段字典 |
| `docs/methodology/rights-control-research-overview.md` | 姊妹线：法律控制（勿合并） |
| `docs/methodology/model-v0.8-research-agenda.md` | V0.8 研究议程（含 exploratory RP） |
| `docs/methodology/data-validation.md` | 正式 + 实验校验入口 |

### 7.3 三路径分析与合成

| 路径 | 角色 |
|---|---|
| `analysis/non-award-validation/taction-state-migration-2026.md` | Taction 状态迁移锚点 |
| `analysis/non-award-validation/realization-path/editas-vertex-license.md` | Path B 写记 |
| `analysis/non-award-validation/realization-path/wirtgen-exclusion-control.md` | Path C 写记 |
| `analysis/non-award-validation/realization-path/three-path-synthesis.md` | Issue #16 三路径合成 |
| `analysis/non-award-validation/realization-path/round1-events.json` | 事件素材（研究侧） |
| `analysis/theory/patent-value-state-model-1.1-realization-path.md` | 理论侧状态模型笔记 |
| `analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md` | Round 2 总门槛（**不 adopt**） |

### 7.4 正式 Evidence / Source（交叉引用，仍属 1.0 表面）

Realization Path 事件通过 `evidence_ids` **引用** 这些正式对象；引用 ≠ 把 RP 字段写进 Ledger。

| 类型 | 路径 |
|---|---|
| Evidence | `data/evidence/realization-path-round1.jsonl` |
| Sources | `data/source-registry/realization-path-round1.jsonl` |

### 7.5 Experimental Realization Path 记录

| 路径 | 内容 |
|---|---|
| `data/experimental/realization-path/three-path-backfill.jsonl` | 3 条 canonical event-log 路径 |
| `data/experimental/realization-path/generated-snapshots.jsonl` | 由投影器生成的 snapshot（`--check` 校验一致性） |

当前 `path_id`：

1. `RP-TACTION-APPLE-2026` — litigation_damages；verdict ≠ cash
2. `RP-EDITAS-VERTEX-CAS9-2024` — voluntary_license；cash without merits
3. `RP-WIRTGEN-CAT-309-LEO-2026` — exclusion_control；control without cash

### 7.6 Validators / tests / projector

```bash
python tools/validate_realization_paths.py
python tools/project_realization_paths.py --check
python -m unittest discover -s tests -p "test_realization_paths.py"
```

关键不变量：

- 与正式 `validate_data.py` **隔离**
- 事件是唯一事实源；snapshot 必须可由 `project_realization_paths.py` 重放
- 允许 “大额 verdict + cash unresolved”
- 允许 “无 infringement judgment + cash received”
- 允许 “exclusion operative + cash not_required”
- **禁止** realization score；**禁止** 把 observed amounts 加总成 intrinsic value
- **禁止** 用通过校验来暗示 schema 1.0 已包含本对象

正式冷启动仍只要求：

```bash
python tools/validate_data.py
python tools/generate_diagnostics.py --check
python tools/render_reports.py --check
```

---

## 8. 推荐阅读顺序

1. 本页（边界与库存）
2. `realization-path-experimental-0.1.md`（对象形状：Event Log → Snapshot）
3. `realization-path/three-path-synthesis.md`（为何否定线性 Infringement→Remedy→Cash）
4. `taction-state-migration-2026.md`（verdict ≠ cash 的锚点）
5. `schema/experimental/README.md`（隔离横幅）
6. `rights-control-research-overview.md`（姊妹线边界）
7. `round2-adoption-readiness-synthesis-v0.8.md`（为何仍不 adopt V0.8）

---

## 9. 非目标（Non-goals）

- 不修改 formal schema 1.0
- 不采纳 V0.8
- 不提供 Realization Score / 专利总价值加总
- 不把本轨道当作冷启动必填项
- 不把 Rights Control / Counterfactual Control / Enforcement Capacity scores 静默并入本对象

姊妹研究线（独立对象，**无** schema）：Counterfactual Control — 导读 [`counterfactual-control-research-overview.md`](counterfactual-control-research-overview.md)；[#37](https://github.com/xiangsee/patent-value-benchmark/issues/37) **已关闭 / 复制门完成**；综合 `counterfactual-i4i-apple381-pair-synthesis.md`；案例见 `analysis/non-award-validation/counterfactual-*.md`。NIA / design-around ≠ cash/verdict；池费率 ≠ redesign cost。
- 不把手改 `generated-snapshots.jsonl` 当成合法更新路径
