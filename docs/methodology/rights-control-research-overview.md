# Rights Control 研究导读（对外入口）

日期：2026-10-12  
状态：**research-only / experimental**  
正式方法基线：**V0.7 (adopted)**  
正式数据表面：**Ledger / Diagnostic schema 1.0（已冻结）**  
**V0.8：未采纳；本页任何内容都不构成采纳或升格。**

---

## 1. Rights Control 是什么

Rights Control 回答的是：

> 在某一 **T0**、某一 **司法辖区**，对某一 **claim / claim-set**，法律上的控制状态是什么？

它关心的是 **claim-set 粒度** 的：

- 裁决事件（adjudication）
- 终局 / 正式效果（finality）
- 当前是否仍有可执行的排除或执行能力（operative control）

它 **不** 回答：

- 专利“值多少钱”
- 技术有多先进
- 产品卖了多少
- 诉讼最终能收到多少现金
- 权利人资金或律师能力有多强

后几类问题分别属于 V0.7 Value Realization、Attribution、以及独立的 Realization Path / Enforcement Capacity 研究线。

一句话：

> **Value Realization（R0–R5）描述价值实现走到哪；Rights Control 描述法律控制此刻站在哪。二者并列，不能互相推导。**

---

## 2. 与 V0.7 Ledger / R-stage 的边界

| | V0.7 Ledger / Diagnostic（正式） | Claim-set Rights Control（实验） |
|---|---|---|
| 问题 | 价值状态、归因证据、可观察性、实现阶段 | claim-set 法律控制状态 |
| 粒度 | 专利 / ledger 行 | claim-set + 辖区 + T0 |
| Schema | `schema/*.schema.json`，`schema_version: "1.0"` | `schema/experimental/claim-set-rights-control.schema.json`，`experimental-0.1` |
| 数据位置 | `data/ledgers/`、`data/evidence/`、`data/source-registry/` | `data/experimental/rights-control/`（实验对象）；对照 ledger 仍在正式 ledgers 中供交叉引用 |
| 校验 | `tools/validate_data.py` 等 | **单独** `tools/validate_rights_control.py` |
| CI 含义 | 通过 = 正式数据表面一致 | 通过 = 实验对象可测试；**≠** 升格为正式字段 |

合法组合（四组对照实际观察到的世界）：

- R5 + 强权利控制
- R5 + 弱 / 不利权利控制
- R4 + 强权利控制
- R4 + 不利裁决但仍有 operative remedy

因此：**不能把 Rights Control 塞回 R0–R5**，也不要用 R-stage 代替 legal control。

---

## 3. 什么时候该看实验对象

适合打开本轨道的情形：

1. 你已经有一份 **V0.7 Ledger**，R-stage 相同或相近，但案例叙事暗示 **法律控制不同**（禁令、再审、IPR/PTAB、ITC、上诉终局性等）。
2. 你在读 Round 1 / Package A 的 matched pairs，想理解“同实现、不同权利控制”。
3. 你需要检查 **adverse adjudication + incomplete finality + operative remedy** 能否并存（不能压成 valid/invalid 布尔值）。
4. 你在评估 V0.8 research agenda 里 H1（Rights Control）的复制证据，而不是在填冷启动贡献。

冷启动 / 外部复现贡献（Getting Started、#2 类任务）**默认只碰正式 Ledger 1.0**；不必也不应把 Rights Control 字段写进 `schema_version: "1.0"` 的 ledger 行。

---

> **2026-10-12：** RC 对普通专利**永远可选**；允许**无裁决** RC 记录（见 [`claim-set-rights-control-experimental-0.1.md`](claim-set-rights-control-experimental-0.1.md)「No-ruling records」）。仍 experimental-0.1。
>
> **可选并行轨细则（research-only；未升格）：** [`rights-control-optional-parallel-plan.md`](rights-control-optional-parallel-plan.md)。

## 4. 什么时候 **不要** 升格进 schema 1.0

下列任一成立，就 **停止**，保持 experimental：

1. 想把 Rights Control 字段直接写进正式 Ledger / Diagnostic 行。
2. 想发明 `rights_control_score = 82` 这类单分数替代结构化状态。
3. 想把 Counterfactual Control（绕开成本、blocking power、FTO 等）未经独立复制就并进本对象。
4. 想把 Realization Path（损害赔偿路径、和解回款、诉讼融资等）并进 Rights Control。
5. 仅因为“CI 过了”或“4/4 门槛过了”就宣布 V0.8 adopted。
6. 没有用户 / 维护者对 **采纳 V0.8** 或 **解冻 schema 1.0** 的显式批准。

治理口令（保持有效）：

> **保持 V0.7 adopted；V0.8 research-only；formal schema 保持冻结的 1.0，直到另行显式批准。**

---

## 5. Round 2 四组对照如何服务研究问题

### 5.1 Package A 研究问题（H1）

预注册问题大意：

> Same realization / different rights-control 的对照，是否重复证明：**Value Realization 不能推导 Claim-set Rights Control**？

四组结果（详见 4-pair synthesis）：

| Pair | Realization | Rights-control 对照 | 新增信息 |
|---|---|---|---|
| i4i × Amgen | R5 vs R4 | 禁令/执行 vs genus claims 无效 | realization ≠ legal control |
| Apple ’381 c19 × ’915 c8 | R4 vs R5 | reexam 确认 vs 不利 reexam 态势 | 更高 realization ≠ 更强权利 |
| SynQor ’702 c56 × ’021 c30 | **R4 vs R4** | 可专利性维持 vs obviousness 维持驳回 | 同 R ≠ 同权利 |
| Wirtgen ’309 c29 × Caterpillar ’693 c19 | **R4 vs R4** | IPR 存活 vs unpatentable FWD + 仍有效的 ITC LEO | rights = adjudication + finality + operative remedy |

结论层级要分清：

- **H1 复制门槛：4/4 已满足** → 允许设计 **experimental schema 0.1**（已完成）。
- **≠ V0.8 adoption**。Round 2 综合明确：**保持 V0.7；不 adopt V0.8；schema 1.0 不变**。

### 5.2 与 Round 2 综合的关系

- Package A（Rights Control pairs）是 V0.8 research agenda 的一块；四组合成见 `rights-control-4pair-synthesis-v0.8.md`。
- Round 2 还覆盖 Package B（early-option retrospectives）与 Package C（SEP / 复杂产品组合等）；总门槛综合见 `round2-adoption-readiness-synthesis-v0.8.md`。
- 即使 Round 2 最低复现集已齐，**采纳仍是独立治理决策**，本仓库当前选择：**不采纳**。

---

## 6. 库存清单（Inventory）

### 6.1 Experimental schema

| 路径 | 角色 | `schema_version` |
|---|---|---|
| `schema/experimental/claim-set-rights-control.schema.json` | Claim-set 法律控制快照 | `experimental-0.1` |
| `schema/experimental/README.md` | 实验目录横幅与隔离规则 | — |

（同目录下的 Realization Path schemas 是 **另一条** 实验线，不要与 Rights Control 合并；导读：[`realization-path-research-overview.md`](realization-path-research-overview.md)。）

### 6.2 方法论文档

| 路径 | 角色 |
|---|---|
| **本页** `docs/methodology/rights-control-research-overview.md` | 对外入口：边界、何时看、何时不升格、库存 |
| `docs/methodology/claim-set-rights-control-experimental-0.1.md` | 实验对象设计说明 |
| `docs/methodology/claim-set-rights-control-data-dictionary.md` | 字段字典 |
| `docs/methodology/model-v0.8-research-agenda.md` | V0.8 研究议程（含 H1 / Package A） |
| `docs/methodology/data-validation.md` | 正式 + 实验校验入口 |

### 6.3 四组对照分析与合成

| 路径 | 角色 |
|---|---|
| `analysis/non-award-validation/i4i-us5787449.md` | Pair 语境（与 Amgen 对照） |
| `analysis/non-award-validation/amgen-sanofi-pcsk9.md` | Pair 语境 |
| `analysis/non-award-validation/apple-samsung-rights-control-pair2.md` | Pair #2 |
| `analysis/non-award-validation/synqor-rights-control-pair3.md` | Pair #3 |
| `analysis/non-award-validation/road-milling-rights-control-pair4.md` | Pair #4 |
| `analysis/non-award-validation/rights-control-4pair-synthesis-v0.8.md` | Package A 4/4 合成 |
| `analysis/non-award-validation/round1-cross-case-synthesis-v0.8.md` | Round 1 跨案 |
| `analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md` | Round 2 总门槛（**不 adopt**） |

### 6.4 正式 Ledger / Evidence / Source（对照用，仍属 1.0 表面）

Rights Control 实验记录通过 `source_ledger_id` / `evidence_ids` **引用** 这些正式对象；引用 ≠ 把 RC 字段写进 Ledger。

| 类型 | 路径模式 |
|---|---|
| Ledgers | `data/ledgers/non-award-*-rights-pair*.jsonl` 及 i4i / Amgen 等相关 ledger |
| Evidence | `data/evidence/non-award-v0.8-round2-rights-*.jsonl`、`experimental-rights-control-backfill.jsonl` 等 |
| Sources | `data/source-registry/non-award-v0.8-round2-rights-*.jsonl` 等 |

### 6.5 Experimental Rights Control 记录

| 路径 | 内容 |
|---|---|
| `data/experimental/rights-control/four-pair-backfill.jsonl` | 9 条 claim-set 快照（覆盖四组对照中的全部可用 claim-set） |

当前 `rights_control_id`：

1. `RC-I4I-US5787449-C14-18-20-T0-2010`
2. `RC-AMGEN-US8829165-C19-29-T0-2023`
3. `RC-AMGEN-US8859741-C7-T0-2023`
4. `RC-APPLE-US7469381-C19-T0-2017`
5. `RC-APPLE-US7844915-C8-T0-2017`
6. `RC-SYNQOR-US7564702-C56-T0-2017`
7. `RC-SYNQOR-US7272021-C30-T0-2017`
8. `RC-WIRTGEN-US7828309-C29-T0-2020`
9. `RC-CATERPILLAR-US7140693-C19-T0-2020`

### 6.6 Validators / tests

```bash
python tools/validate_rights_control.py
python -m unittest discover -s tests -p "test_rights_control.py"
```

关键不变量：

- 与正式 `validate_data.py` **隔离**
- 允许 “adverse PTAB FWD + 无 cancellation certificate + 仍有效的 ITC LEO” 并存
- **禁止** 用通过校验来暗示 schema 1.0 已包含本对象

正式冷启动仍只要求：

```bash
python tools/validate_data.py
python tools/generate_diagnostics.py --check
python tools/render_reports.py --check
```

---

## 7. 推荐阅读顺序

1. 本页（边界与库存）
2. `claim-set-rights-control-experimental-0.1.md`（对象形状）
3. `rights-control-4pair-synthesis-v0.8.md`（为何需要这些字段）
4. `schema/experimental/README.md`（隔离横幅）
5. `round2-adoption-readiness-synthesis-v0.8.md`（为何仍不 adopt V0.8）

---

## 8. 非目标（Non-goals）

- 不修改 formal schema 1.0
- 不采纳 V0.8
- 不提供 Rights Control 总分
- 不把本轨道当作冷启动必填项
- 不把 Realization Path / Counterfactual Control 静默并入本对象

姊妹研究线（独立对象，**无** schema）：Counterfactual Control — 导读 [`counterfactual-control-research-overview.md`](counterfactual-control-research-overview.md)；[#37](https://github.com/xiangsee/patent-value-benchmark/issues/37) **已关闭 / 复制门完成**；matched `counterfactual-i4i-us5787449.md` × `counterfactual-apple-us7469381-bounceback.md`；综合 `counterfactual-i4i-apple381-pair-synthesis.md`；exploratory `counterfactual-via-la-us6825782-sep-fto.md`。
