# V0.8 Design Draft — Architecture Shape (Research Only)

日期：2026-10-12  
状态：**Design draft — NOT frozen, NOT adopted**  
正式方法基线：**V0.7 (adopted)**  
正式数据表面：**Ledger / Diagnostic `schema_version: "1.0"`（[`v0.1.0`](https://github.com/xiangsee/patent-value-benchmark/releases/tag/v0.1.0) 已冻结）**  
前置议程：[`model-v0.8-research-agenda.md`](model-v0.8-research-agenda.md)  
Round 2 综合：[`../../analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`](../../analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md)

> **硬边界（全文适用）**  
> 本文是 **可评审的设计草案**，用于把 Round 2 之后「可以讨论」的候选形状写清楚。  
> - **不**冻结任何新 schema；**不** bump 正式 `1.0`；  
> - **不**把默认方法从 V0.7 切到 V0.8；  
> - **不**把 `schema/experimental/*` 移入正式路径；  
> - **不**新建 Counterfactual experimental schema；  
> - **不**开放普通冷启动扩样（维护平台期仍暂停）；  
> - 采纳 / freeze 仅在用户 **另行显式批准** 后才可启动。

---

## 1. Purpose & non-goals

### 1.1 Purpose

把 V0.8 从「研究议程 + Round 2 门槛清单」推进到一份 **可对照、可否决、可分阶段** 的设计形状，回答：

1. 若未来采纳，V0.8 相对 V0.7 **多回答哪些问题**？  
2. 哪些对象应 **并行**（旁路对象），哪些绝不能塞回 R0–R5？  
3. 与 Rights Control / Realization Path / Counterfactual Control 的关系是什么？  
4. 在什么决策门全部打勾之前，仓库应继续保持什么表面？

### 1.2 Non-goals（本草案明确不做）

| 不做 | 原因 |
|---|---|
| Schema freeze / bump beyond `1.0` | 正式表面已在 v0.1.0 冻结；freeze 需独立发布决策 |
| 切换默认方法到 V0.8 | Round 2 只解除「禁止讨论」；不触发自动 adoption |
| 生成总分 / Gold 概率 / 排名 | V0.7 与 Round 2 non-goals 均禁止 |
| 把 bibliometric proxy 当直接价值 | Screening Signals 必须留在价值事实之外 |
| 普通样本洪水 / 新 contrib ledger | 维护平台期：普通扩样暂停（见 [`cold-start-status.md`](../cold-start-status.md)） |
| 伪造 `design_around_cost_usd` / `blocking_score` / `rights_score` | False precision；CF 仍为 analysis-first |
| 把 CF / RP / Network 一次塞进同一正式对象 | Field explosion；破坏 v0.1.0 可用性 |
| 本 PR 附带「看起来像 adoption」的生产代码路径 | 避免假信号；工程变更另开决策 |

### 1.3 与已有文档的关系

| 文档 | 角色 |
|---|---|
| [`model-v0.8-research-agenda.md`](model-v0.8-research-agenda.md) | 假说、Package A/B/C、adoption 门槛（仍有效） |
| Round 2 synthesis | 门槛完成 ≠ 自动采纳的证据记录 |
| 本文件 | **设计形状草案**（候选字段/对象/迁移草图/决策门） |
| [`model-v0.7.md`](model-v0.7.md) | **现行正式架构**（不被本文件替换） |

---

## 2. What Round 2 / readiness already showed

摘要自 Round 2 synthesis 与 research agenda；此处只固定「设计必须尊重的事实」。

### 2.1 复制门槛（已满足）

| Package | 结果 | 对设计的含义 |
|---|---|---|
| **A Rights Control** 4/4 | 同 R 可不同法律控制；valid/invalid 不够 | 需要 **claim-set × 辖区 × T0** 旁路对象 |
| **B Early option** 4/4 | early T0 诚实 R0 + 可核验 option signals | R-stage ≠ 价值大小；需要 **Value Horizon / Two Clocks** |
| **C Portfolio** 3/3 | CRISPR / AVC pool / 刀片同 assignee 栈 | 需要 **graph / network 对象**，不能压成单件 Ledger 枚举 |
| **Two Clocks** 1/1 | PageRank 同专利双 T0 | Realization history ≠ remaining exclusivity |
| **Cross-case synthesis** | Round 2 文件本身 | 解除「缺 synthesis」阻塞，**不**等于 adopt |

### 2.2 V0.7 仍然正确的部分（不得推翻）

V0.7 继续正确回答：

> 在给定 T0，公开证据能把价值实现推进到哪一 R-stage，且 attribution / observability 如何约束该判断。

Non-inheritance、E3 精确映射、Unknown≠0、T0 / outcome leakage 纪律 **全部保留**。冷启动陷阱（同族误映射、R0+E2≠R3、300+ 不继承、他案点名≠E3、PP01≠R/RC、pre-filing E2 soft-warn）是 **正式表面可用性**，不是 V0.8 字段来源。

### 2.3 相邻层缺口（设计要覆盖、但勿塞回 R）

1. **Legal control beyond R-stage** — claim-set / adjudication / finality / operative remedy  
2. **Value horizon / option** — 已实现历史 vs 剩余排他 / option  
3. **Portfolio & jurisdiction network** — 池、许可栈、同族互补、program scope  
4. **（正交 exploratories）** Realization Path（事件→经济三分量）；Counterfactual（NIA / design-around / blocking scope）

### 2.4 实验轨道已存在的工程隔离（必须保持）

| 轨道 | 状态 | Schema | 校验 |
|---|---|---|---|
| Rights Control | experimental-0.1 | `schema/experimental/claim-set-rights-control.schema.json` | `validate_rights_control.py` |
| Realization Path | experimental-0.1 | events + snapshot schemas | `validate_realization_paths.py` + projector |
| Counterfactual Control | analysis-first；[#37](https://github.com/xiangsee/patent-value-benchmark/issues/37) 复制门关闭 | **无** | 人工 / PR |

通过实验 CI **≠** 升格为正式字段（见 [`schema/experimental/README.md`](../../schema/experimental/README.md)）。

### 2.5 Round 2 仍开放的风险（设计必须写进决策门）

- Overfitting to famous cases；普通冷启动可操作性未同等验证  
- Field explosion（RC+RP+CF+Network+Signals 一次正式化）  
- False precision（option / network 边写成伪分数）  
- Scope leakage（池费率 / 产品收入漏进单件 R3+）  
- Dual-track confusion（用户分不清 1.0 vs experimental）  
- Governance debt（无显式批准人与回滚标准）

---

## 3. Proposed V0.8 shape（候选；未冻结）

### 3.1 总览：并行层，而非替换 V0.7

```text
                    ┌─────────────────────────────────────┐
                    │  Value Construct（声明目标，可多选）   │
                    └─────────────────────────────────────┘
                                      │
     ┌────────────────────────────────┼────────────────────────────────┐
     │                                │                                │
     ▼                                ▼                                ▼
┌──────────────┐            ┌──────────────────┐            ┌────────────────────┐
│ Value Base   │            │ V0.7 Evidence &  │            │ Claim-set Rights   │
│ Tech + Prod  │            │ Realization      │            │ Control            │
│ (conceptual) │            │ R0–R5 + E + Obs  │            │ (experimental→?)   │
└──────────────┘            └──────────────────┘            └────────────────────┘
     │                                │                                │
     │                     ┌──────────┴──────────┐                     │
     │                     ▼                     ▼                     │
     │            ┌────────────────┐    ┌────────────────────┐         │
     │            │ Value Horizon  │    │ Realization Path   │         │
     │            │ / Two Clocks   │    │ (exploratory;      │         │
     │            │                │    │  orthogonal gate)  │         │
     │            └────────────────┘    └────────────────────┘         │
     │                                                                  │
     └──────────────┬───────────────────────────────┬───────────────────┘
                    ▼                               ▼
         ┌─────────────────────┐         ┌──────────────────────┐
         │ Portfolio &         │         │ Counterfactual       │
         │ Jurisdiction Network│         │ Control (no schema)  │
         └─────────────────────┘         └──────────────────────┘

Screening Signals —— 始终在价值事实之外
Cross-cutting: Time/T0 · Jurisdiction · Evidence/Observability · Enforcement Capacity (context only)
```

**原则：** 层与层 **并列、可链接、不可互相推导**。  
高 R ⇏ 强 Rights；有禁令 ⇏ 无 NIA；verdict ⇏ cash；池费率 ⇏ 单件价格。

### 3.2 Layer candidates（字段级草案 — 仅为讨论形状）

#### A. Value Construct（声明，非分数）

每次研究 / ledger 语境声明目标（可多选，必须区分）：

- `policy_statistical`  
- `technological_quality`  
- `private_asset`  
- `realized_operating`  
- `social_strategic`  

**开放问题 Q-A1：** 是否进入正式 Ledger 可选头字段，还是仅方法论要求写在 notes / analysis？

#### B. Claim-set Rights Control（最成熟的升格候选）

最小稳定信息（Package A 四对照重复出现）：

| 候选字段簇 | 意图 | 禁止 |
|---|---|---|
| `claim_set_id` / scope_type | 粒度 | 专利级 valid 布尔代替 |
| `jurisdiction` + `as_of` / T0 | 辖区-时间切片 | 跨国复制状态 |
| `adjudication_status` | 程序姿态 | 写成 score |
| `finality` | 终局 / 证书是否生效 | 忽略「FWD 不利但 LEO 仍 operative」 |
| `operative_control` / enforceability | 可操作救济 | 与 R-stage 合并 |
| `ownership_clarity` / encumbrance | 可选语境 | 自动抬 R |
| `value_carrier_mapping` | 链到 V0.7 E3 语境 | 反写正式 R |

**建议升格路径（若未来批准）：** 先把 experimental-0.1 的 **最小子集** 升为 **optional 并行对象**，与 Ledger 1.0 **并存**；不破坏既有行。  
**开放问题 Q-B1：** 升格时 `schema_version` 策略 — 新并行 schema `1.0-rc`？还是正式 minor 并保留 1.0 只读？  
**开放问题 Q-B2：** 冷启动贡献是否 **永远可选**（默认不填）？

#### C. Value Horizon / Two Clocks

候选区分：

- `realized_value_history`（已实现历史钟）  
- `remaining_exclusivity` / remaining term（剩余排他钟）  
- `option_future_signals`（早期可观察信号；**定性/结构化**，禁止伪定量总分）  

**开放问题 Q-C1：** Horizon 是否独立对象，还是 Diagnostic 只读注解？  
**开放问题 Q-C2：** Package B 的 option signals 词典如何最小化且可复核？

#### D. Portfolio & Jurisdiction Network

候选 graph 节点/边（研究 JSON 已存在于 CRISPR / AVC / Blade）：

- patents / claim sets / owners / licensees  
- complementary / blocking edges  
- SEP / pool / standard mapping  
- jurisdiction-specific rights state  
- time / procedural state  

硬规则草稿：

> Portfolio value ≠ Σ single-patent values.  
> Jurisdiction A ≠ Jurisdiction B.  
> Pool royalty ≠ patent price.  
> Program-scope「N+ 专利」≠ E3.

**开放问题 Q-D1：** Network 是否长期停留在 `analysis/` + 松散 JSON，直到有非教科书样本？  
**开放问题 Q-D2：** 与正式 Ledger 的链接键 — `patent_id` only，还是允许 `portfolio_id`？

#### E. Monetary evidence rule（跨层硬纪律）

Observed money = evidence with **scope, date, actor, legal context** — **not** intrinsic patent price.

必须区分：patent-level damages / single-patent license / portfolio license / field license / product revenue / enterprise revenue / transaction price。  
**不同 scope 不得互相继承。**

#### F. Screening Signals（明确排除在价值事实外）

citations、family size、claims、generality 等：可存筛选层；需 field/cohort/age/jurisdiction 归一化意识；**不得**短路为价值。

### 3.3 明确不进入「第一阶段 V0.8 形状」的内容

即使未来 adopt，第一阶段也建议 **排除**：

- Counterfactual 正式字段（仍 analysis-first）  
- Realization Path 升格（独立 gate；见 §4）  
- Enforcement Capacity 分数化  
- 任何统一 value score  

---

## 4. Relationship to RC / RP / CF

| 轨道 | 回答的问题 | 与未来 V0.8 | 当前动作 |
|---|---|---|---|
| **Rights Control (RC)** | claim-set 法律控制站在哪 | **核心候选层**；Round 2 Package A 已复制 | 保持 experimental-0.1；导读已稳定 |
| **Realization Path (RP)** | 沿什么事件路径拿到 cash/control/contractual | **正交 exploratory**；**不计入**既有 V0.8 adoption 门槛 | 保持 experimental-0.1；禁止并进 RC |
| **Counterfactual (CF)** | 若无此模式，替代与封锁范围 | **正交**；复制门 [#37](https://github.com/xiangsee/patent-value-benchmark/issues/37) 已关 | **仍无 schema**；replication-before-schema 纪律保持 |
| **V0.7 R0–R5** | 价值实现证据阶段 | **正式主干；不被替换** | 冷启动默认只碰 1.0 |

### 4.1 四者并列口令（对外一致）

> R0–R5：实现走到哪一证据阶段。  
> RC：法律控制站在哪。  
> RP：现金 / 控制 / 合同性未来价值沿什么路径发生。  
> CF：若无此模式，替代与封锁范围如何。  
> **四者并列，不能互相推导。**

### 4.2 CF 特殊纪律

- Issue #37 关闭 **只** 表示 matched 复制门完成；**不**授权建 `schema/experimental/counterfactual*`。  
- 禁令/终局 ∈ RC；金额事件 ∈ RP；NIA / redesign / blocking_scope ∈ CF。  
- 下一 CF 动作若有：更多 **普通/非教科书** 定性笔记或预注册扩展——**不是** schema。

### 4.3 RP 特殊纪律

- Events are facts；Snapshot is generated。  
- verdict ≠ cash；license cash 可无 infringement judgment；control 可 `cash=not_required`。  
- RP 若未来进入「正式家族」，需 **单独** 预注册门槛与用户批准，**不得**借 V0.8 adopt 顺带塞入。

---

## 5. Migration & compatibility sketch（仅草图）

> 本节在用户批准 adopt / freeze **之前** 不实施。

### 5.1 兼容目标

1. 已发布的 `schema_version: "1.0"` Ledger / Diagnostic / evidence / source **行继续合法**。  
2. 外部复现者按 Getting Started 仍以 **V0.7 + 1.0** 验收。  
3. Experimental 数据可继续在 `data/experimental/` 演进。  
4. 文档与 CI 步骤名继续区分 formal vs experimental。

### 5.2 可能的分阶段路径（讨论用）

| 阶段 | 内容 | 触发 |
|---|---|---|
| **Now（本草案）** | 设计文档 + 状态指针；research-only | 用户已启动设计草案 |
| **S1 — Optional RC parallel** | 最小 RC 字段并行对象；Ledger 1.0 不动；细则见 [`rights-control-optional-parallel-plan.md`](rights-control-optional-parallel-plan.md)（**本文件≠批准 S1**） | 用户显式批准「升格讨论→实施」 |
| **S2 — Horizon annotation** | Diagnostic 或并行 horizon 笔记；无总分 | S1 稳定 + 普通样本探针 |
| **S3 — Network research object** | 规范化 network JSON + 校验，仍非 Ledger 行内字段 | 非教科书复制 |
| **S4 — Method label** | 方法论可称「V0.8」；默认贡献合同仍写清 1.0 | 用户显式 adopt |
| **Never in same PR** | adoption + 大改字段 + 发版捆绑 | 禁止 |

### 5.3 回滚草图

- 并行对象可整目录弃用而不破坏 1.0。  
- 若错误 bump：保留 git tag `v0.1.0` 与 schema 1.0 为安全锚。  
- CONTRIBUTING / Getting Started 回滚到「只教 V0.7」。

### 5.4 版本号草图（未决定）

| 选项 | 含义 | 风险 |
|---|---|---|
| 保持方法名 V0.7；仅增 optional 对象 | 对外最清晰 | 「V0.8」品牌延迟 |
| 方法称 V0.8；schema 仍 1.0 + 并行 experimental→formal-optional | 需强横幅 | Dual-track 混淆 |
| schema 2.0 大版本 | 清晰断裂 | 过早；破坏冷启动合同 |

**开放问题 Q-M1：** 用户更倾向哪一种对外版本叙事？

---

## 6. Decision gates（采纳 / freeze 前必须为真）

下列全部为 **用户显式决策**；代理人或 PR 合并 **不能** 代替。

### 6.1 Gate 0 — 已满足（事实）

- [x] Round 2 预注册复制门槛（A/B/C + synthesis）  
- [x] Research agenda adoption rule 列表中的数量门槛  
- [x] Experimental RC / RP 与 formal 1.0 隔离横幅存在  

### 6.2 Gate 1 — 方法与治理（必须用户拍板）

- [ ] **正式方法基线是否从 V0.7 切换？**（默认：**否**）  
- [ ] **谁批准 adoption / freeze？** 回滚标准是什么？  
- [ ] **Diagnostic / CI / CONTRIBUTING 用户可见合同**如何改写？  
- [ ] 是否接受「V0.8 方法 + schema 仍 1.0 并行」的对外叙事？  

### 6.3 Gate 2 — 对象范围（禁止一次塞全）

- [ ] 第一阶段是否 **仅** optional Rights Control？  
- [ ] Horizon / Network 是否明确延后？  
- [ ] RP 是否保持独立 gate（默认：**是**）？  
- [ ] CF 是否保持无 schema（默认：**是**）？  

### 6.4 Gate 3 — 风险关闭（未关闭则不应 adopt）

- [ ] 至少一组 **普通冷启动型** 专利上演示 RC 并行对象不增加贡献摩擦  
- [ ] 无 score / 无 Gold 概率 / 无池费率继承进单件 R3+ 的 CI 或文档护栏已写明  
- [ ] Dual-track 文档（README / schema README / Getting Started）审查通过  
- [ ] Overfitting 风险被接受或被额外非教科书样本缓解  

### 6.5 Gate 4 — Freeze / release（独立于 adopt 方法标签）

- [ ] 明确要 freeze 的 schema 文件列表与 `schema_version` 字符串  
- [ ] 迁移说明 + 示例 + 外部复现清单  
- [ ] **单独** release notes；禁止与无关大改捆绑  
- [ ] 用户显式「批准 freeze」文本  

**推荐默认决议（与 Round 2 §4 一致，直到用户改口）：**

> 在另行显式批准前：继续以 V0.7 为正式方法；V0.8 仅研究 / 设计草案；Ledger/Diagnostic schema 保持冻结的 1.0。

---

## 7. Next research steps（小、可逆；无普通扩样洪水）

维护平台期约束下，只建议下列 **探针**（均需保持 research-only 横幅）：

| # | 探针 | 产出 | 不做 |
|---|---|---|---|
| P1 | RC 最小字段「升格清单」对照 experimental-0.1 | 一页 diff 表（字段 keep/drop/rename） | 改正式 schema |
| P2 | 用 **已有** 四域 contrib 之一做「RC 是否必要」负例笔记 | analysis 短文：普通 R0 案无需 RC | 新 ledger |
| P3 | Horizon 信号词典 v0（定性枚举草稿） | docs 附录或 agenda 补丁 | 分数公式 |
| P7 | Horizon worked example（mRNA） | [`v0.8-probes/p7-horizon-worked-example-mrna.md`](v0.8-probes/p7-horizon-worked-example-mrna.md) | schema / 分数 / adopt |
| P8 | Network relation vocabulary v0 | [`v0.8-probes/p8-network-relation-vocabulary-v0.md`](v0.8-probes/p8-network-relation-vocabulary-v0.md) | schema freeze / 回写自由文本 / adopt |
| P4 | Network JSON 三例（CRISPR/AVC/Blade）键名对齐草图 | 命名约定 md | 新 schema freeze |
| P5 | CF：可选一篇非教科书 qualitative note（若用户点名） | **已做**：刀片 CN110165116B → [`v0.8-probes/p5-cf-blade-nontextbook.md`](v0.8-probes/p5-cf-blade-nontextbook.md) / [`counterfactual-byd-blade-cn110165116.md`](../../analysis/non-award-validation/counterfactual-byd-blade-cn110165116.md)；analysis only | CF schema |
| P6 | 文档一致性巡检 | README / tracks / trap checklist 交叉链接 | 行为变更 |
| — | **外推 / 预测效度预注册**（评价工具下一步） | [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md)（研究**未启动**） | 假装已有外推证据 |

**探针结果（2026-10-12，research-only）：** 见 [`v0.8-probes/README.md`](v0.8-probes/README.md)。P5 已用刀片 CTP（无 CATL 材料，未回退 CRISPR）。

**外推预注册：** [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md) — 若要把模型当评价工具再推进一步，按该文档做小 N holdout；**合并该文档 ≠ 启动研究**。

**停止条件：** 任一探针开始暗示「默认贡献必须填 V0.8 字段」→ 立刻停，回到 Gate 1。

---

## 8. Document control

| 项 | 值 |
|---|---|
| 类型 | Design draft |
| 采纳状态 | **not adopted** |
| Schema | **not frozen**；formal 仍 `1.0` |
| 普通扩样 | **paused** |
| 维护者动作 | 评审本草案；需要时勾选 §6 gates；**不要**从本文件推断已 adopt |

修订时请同步：

- [`docs/roadmap.md`](../roadmap.md)  
- [`docs/cold-start-status.md`](../cold-start-status.md)  
- [`docs/research-tracks.md`](../research-tracks.md)  
- [`model-v0.8-research-agenda.md`](model-v0.8-research-agenda.md)（保留门槛真相来源）  
- [`CHANGELOG.md`](../../CHANGELOG.md) Unreleased research/docs theme  

