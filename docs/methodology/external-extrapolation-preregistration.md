# External Extrapolation / Predictive-Validity Pre-registration

日期：2026-10-13  
状态：**Holdout H1–H9 encoded (T0=2026-10-13)；pre-reg locked；NOT a schema freeze；NOT V0.8 adoption**  
正式方法基线：**V0.7 (adopted)** + **schema 1.0 / v0.1.0**  
研究语境：Round 2 复制门槛已满但仍偏教科书案；冷启动可用性已证；**外推 / 预测效度尚未评价**  
关联：[`round2-adoption-readiness-synthesis-v0.8.md`](../../analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md) · [`v0.7-validation-protocol.md`](v0.7-validation-protocol.md) · [`time-cutoff-and-outcome-leakage.md`](time-cutoff-and-outcome-leakage.md) · [`model-v0.8-design-draft.md`](model-v0.8-design-draft.md) · [`cold-start-status.md`](../cold-start-status.md)

> **一句话：下一步若要把「评价工具」推进一步，不是再写维护文档，而是按本预注册跑一小轮诚实的外推检验——看 V0.7 诊断在未见过的普通专利上是否仍减少混淆、是否可操作；不宣称美元准、不默认 adopt V0.8。**

---

## 0. What would make the model “better” as an evaluation tool

按优先级（本预注册只承诺做得到的，不发明虚假精度）：

| 优先级 | 「更好」的含义 | 本预注册是否覆盖 |
|---|---|---|
| **P0** | 在 **未见过 / 普通 / 非教科书** 专利上，编码器仍能诚实停在正确 R、不假抬、不混淆产品与专利 | **是（主目标）** |
| **P1** | 外部新人按 Getting Started 能在时限内完成可复核 Ledger，陷阱率可控 | **是（可用性外推）** |
| **P2** | 当法律控制叙事出现时，可选 RC 并行是否增加决策信息且不强迫填写 | **可选附带；不默认升格** |
| **P3** | Horizon / Network / CF 在普通案上是否有增量 | **探索性记录；不计入主成功标准** |
| **不在此列** | 预测 Gold、估计许可金/诉讼金额、输出总分排名 | **明确排除** |

「更好」= **外推下的诊断纪律与可操作性**，不是分数更高。

---

## 1. Purpose & non-goals

### 1.1 Purpose

预注册并（在用户批准启动后）执行一轮 **小 N、高纪律** 的外部外推研究，回答：

1. **Holdout 混淆减少：** 在未用于 V0.7 形成/Round 2 教科书复制的样本上，四层分离（Value / Evidence / Observability / Realization）是否仍减少「低价值 vs 看不见 / 产品 vs 专利 / 意图 vs 实施」类错误？  
2. **普通专利可操作性：** 非诉讼明星、非奖项金样本上，公开证据能否支撑完整 Ledger + Diagnostic，且默认停在证据允许的 R（常为 R0）？  
3. **假抬失败模式：** 同族热度、「N+ 专利」、他案点名、pre-filing E2 是否仍被软警告/陷阱清单挡住？  
4. **（可选）RC 增量：** 仅当样本确有裁决叙事时，可选 RC 是否改变「同 R 不同控制」的阅读——且无裁决案保持不填。

### 1.2 Non-goals（硬）

| 不做 | 原因 |
|---|---|
| 宣称或检验「专利值多少钱」 | H4：金额是带 scope 的证据，不是内在价格 |
| 默认采纳 V0.8 / freeze 新 schema | 外推成功 ≠ adoption；需另门决策 |
| 发明 gold label 或伪精确分数 | 无人类金标准则记 Unknown / 定性 |
| 预测中国专利奖 Gold / 排名 | V0.7 明确不宣称 |
| 大 N 流水线爬取 | 小 N 诚实优先；防样本洪水 |
| 把 holdout 失败偷偷改成训练叙事 | 预注册锁定成败标准 |
| 本预注册文件本身改 formal 1.0 | 仅文档；启动研究另开 PR |

---

## 2. Hypotheses（预注册；启动前锁定）

### H-E1 — Extrapolation of non-inheritance（主）

在 holdout 普通专利上，**无 E3 则不得出现 R3+**；产品/平台成功叙事不得自动抬 R。  
**预期：** 通过率高；失败 = 编码器在 T0 材料下仍写出 R3+ 而无 exact-patent 点名。

### H-E2 — Unknown ≠ 0 外推

公开看不见 exact mapping 时，Ledger 保持 `exact_patent_value_carrier_link = unknown` 与诚实 gaps，而不是填 0 或编造 E3。  
**预期：** holdout 中「成功产品 + unknown mapping」组合可稳定出现且 Diagnostic 不假装已归因。

### H-E3 — Cold-start operability

不熟悉仓库历史的编码者（或同一代理换新案）按 Getting Started，在约定时限内产出通过 `validate_data.py` 的 R0–R2 级 Ledger（视证据而定）。  
**预期：** ≥ 预设比例的案次一次 PR 即 CI 绿，或仅需文档级修正；不需要实验 schema。

**双编码盲评协议（落实本假设 + §6.3）：** [`t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md) — 样本、盲法、分歧裁断、R/E3 一致率；**docs only，默认未开跑**。

### H-E4 — Trap surface still bites

至少一类已知陷阱（同族误映射 / 他案点名 / 300+ 不继承 / pre-filing E2 / PP01≠R）在 holdout 中被触发并正确处理（停住或 soft-warn）。  
**预期：** 陷阱被挡住 = 支持；陷阱被写进 R3+ = 主失败。

### H-E5 — Optional RC non-friction（附带，不挡主结论）

无裁决 holdout：**不**创建 RC 仍算完整。有裁决子集：可选 RC 记录可校验，且不改变 formal R。  
**预期：** 与 [#49](https://github.com/xiangsee/patent-value-benchmark/pull/49) / 并行细则一致；RC 缺失永不导致 formal CI 失败。

### Non-hypotheses（不检验）

- 许可金/判决金额预测误差  
- Gold 概率  
- bibliometric → 价值回归 R²  
- V0.8 字段提升「准确率」

---

## 3. In-sample vs holdout

### 3.1 In-sample（已用；本轮 **禁止** 再当成功证据）

| 集合 | 角色 | 外推研究中的地位 |
|---|---|---|
| 第25届 10 pairs | V0.6/V0.7 形成 | **训练/形成集** — 不得计入外推成功 |
| 第24届 4 pairs | V0.7 采纳压力测试 | **已用验证集** — 可作基线对照，不算本轮新外推 |
| Round 1/2 教科书机制案（i4i、Amgen、Apple、Package B 四杰、CRISPR、AVC、刀片锚点等） | V0.8 复制 | **机制 in-sample** — 可引用为「已知能表达」，不计入 H-E1–E4 通过数 |
| 现有四域 contrib + #2 | 可用性 | **可用性校准集** — 设计陷阱与 soft-warn 的来源；本轮 holdout **不得重复同一申请号** |

### 3.2 Holdout（本预注册的评价集）

**定义：** 申请号 / 专利号 **未** 出现在上表任一已发表 ledger 或 Round 2 主分析标题中的新案。

**分层（小 N，预注册锁定目标数量；启动前由用户确认最终 N）：**

| 层 | 目标 N（建议） | 特征 |
|---|---|---|
| L1 普通当前态 | **4–6** | 中小权利人、非诉讼明星；软件/机械/化工或材料/电气各尽量覆盖；预期多数 R0 |
| L2 非教科书机制 | **2–3** | 有公开产品叙事但 **无** 名官司；或同族拥挤；用于压 H-E1/E4 |
| L3（可选）有裁决 | **0–2** | 仅当公开可核验 claim-set 程序；用于 H-E5；**不**为凑 RC 而选著名案 |

**总 N 建议上限：8–10。** 超过则另开预注册修正，禁止静默扩容。

### 3.3 分配规则

1. 先锁定 holdout 名单与 T0（每案一个 T0），再编码。  
2. 名单公开在研究 issue / 本文件附录（启动 PR 填入）；编码中不得因「不好写」替换名单，除非预注册修订。  
3. Round 2 综合已点名的过拟合风险（famous-case bias）——holdout **优先讨厌的普通案**。

---

## 4. Success / fail criteria（主研究）

### 4.1 主成功（全部满足才称「外推支持 V0.7 作为评价工具」）

1. **Holdout 完成率：** 锁定名单中 ≥80% 产出通过 formal CI 的 Ledger（+ 自动 Diagnostic）。  
2. **H-E1：** 无 E3 的 holdout 案 **0 件** 出现 R3+。  
3. **H-E2：** 凡产品叙事强但无 exact 点名的案，mapping 保持 unknown，且 notes/gaps 显式记录。  
4. **H-E4：** ≥1 件 holdout 触发已知陷阱类并正确处理；**0 件** 因陷阱假抬成功混入「通过」。  
5. **综合笔记：** 一篇 cross-case note 写明失败模式；不得只报喜。

### 4.2 主失败（任一即「外推未支持 / 需改工具或文档」）

- 编码者普遍无法在无内部知识下完成（H-E3 崩溃）。  
- 多个 holdout 在无 E3 时仍写入 R3+ 或伪造 E3。  
- 必须依赖 experimental schema 才能让 formal 表面「好看」。  
- 事后用 post-T0 成功回填 T0 状态（泄漏）。

### 4.3 弱支持 / 不确定

- 完成但陷阱从未出现（可能选样过「干净」）→ 补 1–2 件高陷阱风险案或降级结论。  
- RC 附带假设样本不足 → H-E5 标 inconclusive，**不影响**主成功判定。

### 4.4 与 V0.8 / freeze 的关系

| 结果 | 允许的下一步 | 不允许 |
|---|---|---|
| 主成功 | 宣称「V0.7 在小 N 普通 holdout 上外推纪律成立」；可讨论文档/脚手架硬化 | 自动 adopt V0.8；自动 freeze |
| 主失败 | 修 Getting Started / validate soft rules / 陷阱清单；或限制宣称范围 | 假装 Round 2 已证明外推 |
| 仅 H-E5 亮 | 推进 RC 并行轨讨论（仍 optional） | 把 RC 塞进 1.0 必填 |

---

## 5. Sample design details

### 5.1 纳入

- 公开可核验著录项（申请号/公开号/授权号、权利人、日期）。  
- 至少能写 R0（权利存在）的公开源。  
- 中文或英文公开源均可；优先中国发明普通案以延续冷启动路径，可混入 1–2 件非 CN 以测文档是否绑死司法辖区。

### 5.2 排除

- 已在 in-sample 列表中的专利号。  
- 仅为「凑 R5」而选的天价诉讼/奖项金样本（可另册，不进主成功计数）。  
- 无法设定 T0 或公开源全在防火墙后且无任何 public 层证据的案（Observability 全 Restricted 且无公开著录——极罕见；若遇则记 skipped + 原因）。

### 5.3 每案最低交付物

1. `data/ledgers/…` formal 1.0 行（或启动后约定的 holdout 目录，仍 schema 1.0）  
2. 所需 evidence / source  
3. 生成 Diagnostic + report（CI）  
4. 一页 case note：T0、R、是否触发陷阱、是否写 RC（默认否）  
5. **禁止** 为本轮新建 CF/Horizon schema

---

## 6. Labels：what exists vs what needs human gold

### 6.1 已有、可作 outcome / 对照的标签（慎用）

| 标签 | 来源 | 本预注册用法 |
|---|---|---|
| 奖项 Gold/Silver | Track B 历史 | **不作** 本轮预测目标；最多 post-hoc 描述 |
| 公开诉讼结果 / 禁令 | 裁判文书 | 仅 L3 可选；属 RC/RP 域，不是 R 的 gold |
| 产品是否上市 | 公司披露 | **产品层** outcome；**禁止** 无 E3 时当作专利 R gold |
| Package B 事后成功 | 历史回顾 | 仅说明 early R0 纪律；holdout 不用同一专利 |

### 6.2 本轮 **不发明** 的 gold

- 「真实专利价值」美元  
- 「正确 R」的专家分数（除非用户另行组织盲审协议）  
- blocking_score / option_score  

### 6.3 若用户要人类 gold（可选加门，默认关闭）

仅当用户显式批准时，可增加：

- **盲审协议：** 两名编码者独立写 R 与 mapping；第三人裁分歧。  
- **一致率报告：** 只报一致/分歧类型，不把一致率吹成准确率。  
- **仍不** 产生美元或总分 gold。

可执行细则（样本 / 盲法 / 裁断 / 指标 / 不宣称）：[`t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md)。

无此门时：成功标准只用 §4 的 **过程纪律与可操作性**，不用「命中真值」。

---

## 7. Leakage rules

沿用并收紧 [`time-cutoff-and-outcome-leakage.md`](time-cutoff-and-outcome-leakage.md)：

1. 每案锁定 **T0**（日历日）；公开可得日 `publicly_available_date` ≤ T0 才可进 T0 evidence。  
2. post-T0 仅可：确认后来产品/诉讼/奖项作 **outcome label**；**不可** 抬 T0 的 R / E / Observability。  
3. 编码器写作时不得打开「后来成功」维基叙事再倒推 E3（Package B 纪律外推到 holdout）。  
4. 预注册名单与成败标准在编码开始前冻结；改标准必须修订本文件并注明日期。  
5. soft-warn（pre-filing E2）保持 exit 0；**不得** 为通过「好看」而删警告源。

---

## 8. Relation to V0.7 and experimental layers

```text
Holdout 主路径（必须）
  V0.7 Ledger 1.0 → Diagnostic → traps / soft-warn
       │
       ├─ 成功/失败 → 评价「作为评价工具的外推」
       │
       └─ 可选支路（不挡主结论）
            ├─ RC experimental（仅 L3 或显式无裁决注记）
            ├─ Horizon 定性信号（P3 词典；无分数）
            ├─ Network 草图（仅当组合叙事强；松散 JSON/笔记）
            └─ CF 一页定性（仅当 NIA 文书存在；无 schema）
```

| 层 | 本预注册角色 |
|---|---|
| V0.7 R0–R5 + E + Obs | **主评价对象** |
| RC optional parallel | 附带 H-E5；细则见 [`rights-control-optional-parallel-plan.md`](rights-control-optional-parallel-plan.md) |
| Horizon / Network / CF / RP | 最多探索记录；**不计入** §4.1 |
| V0.8 adopt / schema freeze | **出口决策另议**；本预注册出口最多到「外推结论」 |

---

## 9. Decision gates（启动研究前必须用户拍板）

本文件合并 **≠** 启动编码。启动前需用户显式确认：

| # | 决策 | 默认建议 |
|---|---|---|
| D1 | 是否批准按本预注册 **启动** holdout 编码？ | **已确认启动（2026-10-13）** |
| D2 | 最终 N 与分层（L1/L2/L3）？ | L1=4–6, L2=2–3, L3=0–1 |
| D3 | Holdout **具体名单** 谁定？（用户指定 / 代理提名后你确认） | **用户已确认附录 A 名单** |
| D4 | 每案 T0 规则：统一「编码日」还是「各自事件日」？ | **统一编码日 T0=2026-10-13** |
| D5 | 是否开启人类盲审 gold 门（§6.3）？ | **默认关** |
| D6 | 失败时是否允许立即改 validate/脚手架（另 PR）？ | 建议允许文档/软规则，不允许改 1.0 必填语义充数 |
| D7 | 外推成功后是否进入 V0.8 S1 讨论？ | **默认否**；成功只支持 V0.7 外推声明 |

---

## 10. Execution checklist（批准启动后）

1. 开 GitHub Issue 挂本预注册链接 + 锁定名单表。  
2. 一案一分支/PR；formal CI 绿。  
3. 全部完成后写 `analysis/non-award-validation/holdout-extrapolation-synthesis.md`（名可微调）。  
4. 对照 §4 勾选成功/失败；**禁止** 事后改标准。  
5. 若失败：列出工具/文档补丁清单；若成功：更新 roadmap 一句「小 N 普通外推：支持/不支持」，仍不 adopt V0.8。

---

## 11. Document control

| 项 | 值 |
|---|---|
| 类型 | Predictive-validity / external-extrapolation **pre-registration** |
| 研究状态 | **已启动并完成 H1–H9 编码（见附录 A）** |
| Schema | formal 1.0 不动；无新 freeze |
| 虚假指标 | 无；不报告编造的准确率 |

修订必须追加日期与变更说明；启动后改成败标准视为新预注册。

---

## Appendix A — Confirmed holdout list (locked 2026-10-13)

**User confirmation:** encode full H1–H9; **T0 = 2026-10-13** (uniform encoding-day cutoff); nominated ZL numbers as listed; honest cold-start (Unknown≠0, no inheritance, no fake E3/R3+); L3 H9 optional RC only with evidence ≤T0.

**Study status after this appendix:** **started / encoded** (this PR). Formal baseline remains V0.7 + schema 1.0. Not V0.8 adoption.

| ID | Layer | Application (ZL) | Grant | Title (short) | Assignee (short) | Domain | Formal R | E present | Mapping | Optional RC |
|---|---|---|---|---|---|---|---|---|---|---|
| H1 | L1 | ZL202111562464.8 | CN114297223B | 中小企业信息化服务平台 | 深圳空间数字科技 | software | **R0** | [] | unknown | no |
| H2 | L1 | ZL201910471967.0 | CN110162936B | 软件内容使用授权方法 | 北京比特安索 | software | **R0** | [] | unknown | no |
| H3 | L1 | ZL202011067792.6 | CN112240323B | 液压摆线马达 | 邢台中威卓特液压 | mechanical | **R0** | [] | unknown | no |
| H4 | L1 | ZL202011166628.0 | CN112177941B | 新型膏体泵 | 成都博磊化工机械 | chemical_equipment | **R0** | [] | unknown | no |
| H5 | L1 | ZL202110513769.3 | CN113200747B | 低温烧结氮化铝陶瓷 | 山东鼎鼎 / 深圳鼎鼎 | materials | **R0** | [] | unknown | no |
| H6 | L2 | ZL202110686604.6 | CN113553338B | RPA+AI 许可证生成 | 来也网络 / 来也科技 | software | **R0** | [E2] | unknown | no |
| H7 | L2 | ZL202110448799.0 | CN113182524B | 钛基金属陶瓷及刀具 | 赣州澳克泰 / 崇义章源钨业 | materials | **R0** | [E2] | unknown | no |
| H8 | L2 | ZL202010875322.6 | CN112012978B | 负载敏感充液阀/装载机液压 | 广西柳工机械 | mechanical | **R0** | [E2] | unknown | no |
| H9 | L3 | ZL201910958076.8 | CN110660074B | 废钢等级划分神经网络 | 北京同创信通 | software | **R0** | [E2] | unknown | **yes** (experimental) |

**Counts:** L1=5, L2=3, L3=1; total N=9 (within pre-reg 8–10 cap).

**Ledger IDs:** `LEDGER-HOLDOUT-H{n}-ZL…` (prefix distinguishes holdout from ordinary `LEDGER-ZL…` contrib so RC-optional tests stay honest).

**Artifacts:** `data/ledgers|evidence|source-registry/holdout-ZL*.jsonl`; case notes `analysis/non-award-validation/holdout/H*-….md`; synthesis `analysis/non-award-validation/holdout-extrapolation-synthesis.md`; H9 RC `data/experimental/rights-control/holdout-H9-ZL201910958076.8.jsonl`.

**Decision gates closed by user for this run:** D1 start=yes; D2 N/layers=as table; D3 list=confirmed nominations; D4 T0=uniform 2026-10-13; D5 human gold=off; D7 V0.8=not this PR.

---

## Appendix B — Confirmed E3-probe holdout (E3-A/B/C; locked 2026-10-13)

**User confirmation:** encode E3-A `ZL201710337622.7`, E3-B `ZL201310419886.9`, E3-C `ZL202310277767.8`; **T0=2026-10-13**; E3 only if exact patent→carrier holds after **claims check**; **no auto R3+**.

| ID | ZL | Title (short) | Assignee | Claims check | Formal R | E present | Mapping |
|---|---|---|---|---|---|---|---|
| E3-A | ZL201710337622.7 | 助产用凝胶及其制备方法 → 诺欣顺® | 成都英诺新 | **PASS** (plausible) | **R3** | E2+E3 | strong_evidence |
| E3-B | ZL201310419886.9 | 监护设备生理参数处理 → CrozFusion®/N系列 | 深圳迈瑞 | **PASS** (plausible) | **R3** | E2+E3 | strong_evidence |
| E3-C | ZL202310277767.8 | 美白抗衰护肤组合物及应用 → 玻麦妍塑颜水 | 江苏仅三 | **FAIL** | **R0** | E2 only | unknown |

**Honesty notes:** E3-C marketing patent sticker ≠ E3 after granted-claim vs public-ingredient check. E3-A/B reach R3 (implemented) only; **no** R4/R5 without E4. Not V0.8 adoption.

**Artifacts:** `data/*/holdout-E3{A,B,C}-ZL*.jsonl`; notes `analysis/non-award-validation/holdout/E3*-….md`.
