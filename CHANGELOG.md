# Changelog

## Unreleased

### Theme: T3 P8 Network relation vocabulary v0

#### Added
- 约定稿：`docs/methodology/v0.8-probes/p8-network-relation-vocabulary-v0.md`（受控 snake_case relation + CRISPR 自由文本映射 + 边键约定）。

#### Changed
- 三例 network JSON **仅**增加顶层 `convention` 元数据（`legacy_preserved`）；**未**改写既有 `relation` 字符串。

#### Notes
- **未** adopt/freeze V0.8；**未**启动 S3；无 schema/validator。


### Theme: T4 phase synthesis + T3 P7 Horizon worked example

#### Added
- T4 合并笔记：`analysis/non-award-validation/holdout-t4-phase-synthesis.md`（H/E3/N/P/E4 纪律阶梯）。
- T3 探针 P7：`docs/methodology/v0.8-probes/p7-horizon-worked-example-mrna.md`（mRNA @2012-10-02 套用 P3 两钟+OS-*）。

#### Notes
- **未** adopt / freeze V0.8；**未**启动 S1/S2；不改 formal schema/ledger。


### Theme: T4 encode E4-N1/N2/N5（T0=2026-10-13）

#### Added
- Ledgers/evidence/sources：`holdout-E4N1-ZL201410204545.4`（汇顶判赔 → **R5**）、`holdout-E4N2-ZL200680012412.0`（维美德判赔 → **R5**）、`holdout-E4N5-ZL202010875349.5`（奥普具名许可 → **R2**）。
- Synthesis：`analysis/non-award-validation/holdout-e4-n125-synthesis.md`。

#### Notes
- 有判赔≠自动 R5：N1/N2 因单件 + 裁判 E3 + exact_patent 指标才升 R5；金额=争议情境。
- N2：法院采用侵权获利，**未**采信原告销售损失。
- N5：许可对价记服务费 + 四件捆 → 不升 E4/R5。
- **未** adopt V0.8。


### Theme: T4 E4 holdout nominees Round 1（nominate only）

#### Added
- E4 提名：`docs/methodology/e4-holdout-nominees-round1.md`（E4-N1–N5：汇顶判赔 / 维美德销售损失判赔 / 朗科许可+判赔 / 攀钢工艺判赔 / 光机所→奥普具名许可）。
- `world-class-roadmap.md` §4.1：H/E3/N/P 学习摘要 + E4 下一跳。

#### Notes
- **仅提名**；不编码；不 adopt V0.8。E3≠E4；避开已编码 holdout/ledger 集合。


### Theme: Encode E3-P1/P3/P4 holdouts（T0=2026-10-13；claims PASS plausible → R3）

#### Added
- E3-P1 复立坦 / ZL202111620840.4 → **R3**；E3-P3 小儿紫贝宣肺 / ZL200810100459.3 → **R3**；E3-P4 芪防鼻通 / ZL202110966782.4 → **R3**。
- Case notes + synthesis：`analysis/non-award-validation/holdout/E3P*.md` · `holdout-e3-p134-synthesis.md`。

#### Changed
- `e3-holdout-nominees-round3.md`：标记 P1/P3/P4 已编码。

#### Notes
- 3/3 claims-check **PASS (plausible)**（NHSA 显式 ZL + 规格/处方对齐；定量 wt%/份量仍缺口）。**不** auto-R4/R5（无 E4）。不 adopt V0.8。


### Theme: T4 E3-P nominees Round 3（PASS-oriented；nominate only）

#### Added
- Round 3 holdout 提名：`docs/methodology/e3-holdout-nominees-round3.md`（E3-P1–P6；复立坦 / 益气通窍 / 小儿紫贝宣肺 / 芪防鼻通 / 九味止咳 / 阿利沙坦酯吲达帕胺用途权）。
- 含 N1/N2/N5 失败原因说明 + Round 3 选案过滤器（显式 ZL + 规格/处方/说明书要素）。

#### Changed
- `world-class-roadmap.md` / `docs/roadmap.md`：T4 Round 3 提名指针。

#### Notes
- **仅提名**；不编码；不 adopt V0.8；不冻 schema。避开 H/E3-N 与既有 ledgers。


### Theme: T1 theory memo v0（Value Construct / Two Clocks / RC⊥R）

#### Added
- T1 短理论备忘：`docs/methodology/t1-theory-memo-value-construct.md`（建构、双时钟、RC⊥R、Screening≠Proof、Unknown≠0、非继承；对照 T2 IVS/引证学校）。

#### Changed
- `world-class-roadmap.md` / `docs/roadmap.md` / T2 矩阵：T1 v0 指针。

#### Notes
- 不编码；不 adopt V0.8；不冻 schema。


### Theme: Encode E3-N1/N2/N5 holdouts（T0=2026-10-13；claims check FAIL → R0）

#### Added
- E3-N1 绽妍三重蛋白 / ZL202210708835.7 → **R0**；E3-N2 焦点福瑞达酶切HA / ZL202110767111.5 → **R0**；E3-N5 奥普特手眼标定 / ZL201810828154.8 → **R0**。
- Case notes + synthesis：`analysis/non-award-validation/holdout/E3N*.md` · `holdout-e3-n125-synthesis.md`。

#### Notes
- 3/3 claims-check **FAIL**（配方量/工艺参数/迭代加权算法公开不足）。品牌点名或功能类叙事 = E2 ≠ E3；**不** auto-R3。不 adopt V0.8。


### Theme: T2 existing-models comparison matrix v0（research/docs）

#### Added
- 既有估值/评估族系 vs V0.7 一页矩阵：`docs/methodology/existing-models-comparison-matrix.md`（IVS/特许/成本/引证/ML打分/奖项/诉讼损害/期权）。

#### Changed
- `world-class-roadmap.md` / `docs/roadmap.md`：T2 v0 完成指针。

#### Notes
- 不编码；不 adopt V0.8；不冻 schema。


### Theme: World-class roadmap + E3-N nominees Round 2（research/docs；未编码）

#### Added
- 世界级评估四轨路线：`docs/methodology/world-class-roadmap.md`（理论 / 既有模型比较 / 自有创新测试 / 实效验证；formal=V0.7+schema1.0；**未** adopt/freeze V0.8）。
- E3 holdout 提名 Round 2：`docs/methodology/e3-holdout-nominees-round2.md`（E3-N1–N6；iphouse 核验授权 B；**提名 only**）。

#### Changed
- README / roadmap / cold-start-status：轻量指针。

#### Notes
- 不编码新 ledger；不 adopt V0.8；不冻 schema。确认名单后再编码。


### Theme: Holdout E3-probe E3-A/B/C（T0=2026-10-13；claims check）

#### Added
- E3-A 诺欣顺 / ZL201710337622.7 → **R3**（strong_evidence）；E3-B 迈瑞 CrozFusion / ZL201310419886.9 → **R3**；E3-C 玻麦妍 / ZL202310277767.8 → **R0**（claims check FAIL）。
- 预注册附录 B；`holdout-e3-abc-synthesis.md`。

#### Notes
- 有 E3 ≠ 自动 R3+：A/B 停 R3；C 贴纸未过权利要求核验。不 adopt V0.8。


### Theme: External extrapolation holdout H1–H9（T0=2026-10-13；研究编码）

#### Added
- Holdout H1–H9 formal ledgers / evidence / sources（`data/*/holdout-ZL*.jsonl`）；case notes `analysis/non-award-validation/holdout/`；synthesis `holdout-extrapolation-synthesis.md`。
- L3 H9 optional RC：`data/experimental/rights-control/holdout-H9-ZL201910958076.8.jsonl`（experimental；formal 仍 R0）。
- 预注册附录 A：确认名单 + 每案 R0 结果（`docs/methodology/external-extrapolation-preregistration.md`）。

#### Notes
- 9/9 **R0**；Unknown≠0；无假 E3/R3+；不 adopt V0.8；不发明 gold/美元。主成功=过程纪律支持；H-E3 弱 / H-E5 inconclusive（见 synthesis）。


Maintenance plateau（2026-10-12）：**V0.7 / schema 1.0 稳定**；V0.8 / RC / RP / CF 仅 research；**普通冷启动扩样暂停**。采纳 V0.8 需显式决策。状态见 [`docs/cold-start-status.md`](docs/cold-start-status.md) · [`docs/roadmap.md`](docs/roadmap.md)。

### Theme: External extrapolation pre-registration（预注册；holdout 已编码见上）

#### Added
- 外推 / 预测效度预注册：`docs/methodology/external-extrapolation-preregistration.md`（holdout vs in-sample、假设、成败标准、小 N 普通/非教科书设计、标签边界、泄漏、与 V0.7/RC 关系、启动前决策门）。**不** freeze；**不**默认 adopt V0.8；**不**发明 gold/美元指标。

### Theme: RC optional parallel-track plan（research/docs；未升格）

#### Added
- RC 可选并行轨实施细则：`docs/methodology/rights-control-optional-parallel-plan.md`（反映 #49：永远可选、无裁决、mapping 可选；并存规则；S1 迁移草图；Gate 1–4）。**不** freeze / **不** adopt V0.8。

### Theme: Counterfactual P5 — Blade non-textbook note（analysis-only；无 CF schema）

#### Added
- Exploratory CF Case #4：`analysis/non-award-validation/counterfactual-byd-blade-cn110165116.md`（刀片 CN110165116B；R0；portfolio-internal NIA=Unknown）。仓库无 CATL 材料，未编造。
- P5 指针：`docs/methodology/v0.8-probes/p5-cf-blade-nontextbook.md`；CF 导读 / design draft / experimental README 交叉链接。

### Theme: Rights Control experimental — optional & no-ruling records（未冻结 / 未采纳）

#### Changed
- `claim-set-rights-control.schema.json`（experimental-0.1）：`adjudication_events` 可为空；`finality_state.status` 增 `not_applicable`；`scope_type` 增 `all_granted_claims`；`value_carrier_mapping` 改为可选。
- `validate_rights_control.py`：无裁决记录须 finality = `not_applicable`；有裁决时禁止 `not_applicable`。
- 测试：无裁决 fixture、可选 mapping、普通 ledger 无需 RC。RC 对普通专利**永远可选**。formal schema 1.0 / V0.7 不变。

### Theme: V0.8 design draft（research/docs；未冻结 / 未采纳）

#### Added
- V0.8 设计草案：`docs/methodology/model-v0.8-design-draft.md`（目的与非目标、Round 2 事实、候选形状、RC/RP/CF 关系、迁移草图、决策门、可逆探针）。**不** freeze schema；**不** adopt V0.8；formal 仍为 V0.7 + schema 1.0。

#### Changed
- Roadmap / cold-start-status / research-tracks / V0.8 research agenda：增加「design draft in progress / research-only」指针。
- V0.8 probes P1–P4、P6（docs only）：`docs/methodology/v0.8-probes/`；P5 待点名。未改 schema / validator / ledger。

### Theme: Round 2 V0.8 replication（#24–#30；research-only，未采纳）

#### Added
- Package B early-stage option retrospectives（各停在 R0）：US8278036B2（#24）、US4539507A（#25）、US4668595A（#26）、US4949039A（#27）→ **B 4/4**。
- Package C：Via LA AVC/H.264 池 SEP US6825782B2 停在 R2（#28）；非生科复杂产品组合 CN110165116B Blade CTP 停在 R0（#29）→ **C 完成**。
- Round 2 adoption-readiness 综合：`analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`（#30）。明确复制门槛已满 **≠** 自动采纳 V0.8。

#### Changed
- Roadmap / V0.8 research agenda：Package B/C 进度填满；Round 2 最小集完成。
- 澄清：正式方法仍为 V0.7；formal schema 仍冻结在 1.0。

### Theme: Cold-start quality & ordinary samples（#31–#34、#32、#40–#45）

#### Added
- Cold-start trap checklist：`docs/cold-start-trap-checklist.md`（同族误映射、R0+E2、300+ 组合不继承）（#31）。
- `schema/README.md` / `schema/experimental/README.md`：experimental ≠ formal 1.0（#31）。
- 普通冷启动 contrib（均 R0；扩样现已暂停）：远光 ZL202010574036.6（#32）、天地和兴 ZL202110873119.X（#40）、科达 ZL201911041536.7（#41）、威远 ZL202011377891.4（#42）、中晶 ZL202010866038.2（#44）。
- Scaffold 可选著录项 flags；CI harden（`.venv` 提示、`compileall`、统一 unittest、`workflow_dispatch`）（#33–#34）。
- `validate_data.py`：cold-start consistency levers + **pre-filing E2 soft warning**（exit 0）（#31/#43）。
- Track A 状态页：`docs/cold-start-status.md`；Getting Started §6.1 soft-warn UX（#45）。

#### Changed
- Scaffold 打印冷启动陷阱 / gap 提示；`carrier_type` 与 soft-warn 提示（#33/#42/#44）。
- Getting Started / quick-ref / trap checklist / README：unknown-E3、`.venv`、soft warn、状态页链接。
- GitHub Actions：`tools/**` path filter；步骤名区分 formal 1.0 vs experimental。

### Theme: Research overviews — RC / RP / CF（#35–#40；无 CF schema）

#### Added
- Rights Control 研究导读 + inventory（#35）：`docs/methodology/rights-control-research-overview.md`。
- Realization Path 研究导读 + inventory（#36）：`docs/methodology/realization-path-research-overview.md`。
- Counterfactual Control：预注册 [#37](https://github.com/xiangsee/patent-value-benchmark/issues/37)（已关）；配对笔记 i4i × Apple ’381（#38）；综合 + Via LA exploratory #3（#39）；导读 `counterfactual-control-research-overview.md`（#40）。**不**建 CF experimental schema。

#### Changed
- `docs/research-tracks.md`：RC / RP / CF 导读与复制门状态交叉链接。

---

## [0.1.0] - 2026-10-12

### Added
- Freeze Patent Value Ledger / Diagnostic schemas at `schema_version: "1.0"` for v0.1.0.
- Mark Evidence / Source Registry schemas structure-frozen with the release.
- Complete external cold-start reproduction (#2 / PR #22): BYD ZL201910544929.3 stopped at R0.
- Add v0.1.0 release notes and update readiness checklist to Released.
- Document sibling-patent / R0+E2 / portfolio non-inheritance cold-start pitfalls from #22 feedback.

### Changed
- CITATION.cff version `0.1.0-draft` → `0.1.0`.
- README / Data Dictionary / methodology titles drop “Draft” for Ledger & Diagnostic 1.0.

### Historical notes (pre-freeze development)

- 初始化 Xiangsee Patent Value Benchmark 公共研究库。
- 冻结 Patent Value Benchmark V0.6，开始第 25 届样本外验证。
- 建立 E1–E5 证据等级。
- 建立 T0 截断与 Outcome Leakage 控制规范。
- 明确 Unknown ≠ 0。
- 明确 Public Screening / Internal Gold Readiness 双引擎结构。
- 建立 Patent Record / Evidence / Matched Pair / Source Registry 四类 JSON Schema。
- 第 25 届结构化预览数据已扩展至：20 条专利记录、14 条证据记录、10 组 Gold–Silver matched pairs。
- 增加数据完整性验证脚本 `tools/validate_data.py`。
- 增加 GitHub Actions 自动校验工作流；Round 1–3 数据提交均通过 CI 验证。
- 增加 `publicly_available_date`，严格区分事件发生日期与信息公开可得日期。

### Changed
- “专利年龄”不再以申请号前四位作为正式代理；后续统一优先使用真实申请日与最早优先权日，并记录分案 / PCT 来源。
- 对非 Unknown 的分析判断，要求至少引用一个 evidence record。

- Milestone A 达到 10 组 matched pairs，暂停第25届扩样，进入 Cross-pair Synthesis。

- 完成第25届 V0.6 Cross-pair Synthesis：10组中 2 Yes / 4 No / 4 Uncertain。
- 确认公开T0证据在 10/10 配对中均无法解决 patent-level attribution。
- 提出 V0.7 架构候选：Value State / Attribution-Evidence State / Observability State / Value Realization Stage。
- V0.7 暂不 adopted，计划使用第24届进行外部验证。

- 启动第24届跨届次外部验证，T0=2022-10-31。
- 新增 V0.7 External Validation Protocol。
- 第24届 Round 1 完成2组：创新药与软件基础设施。
- 初步验证 Value State / Evidence / Observability / Realization Stage 分层具有解释价值，但 V0.7 仍未 adopted。

- 第24届 Round 2 新增 P24-POWER-001（中车变频 Gold vs 阳光电源 MPPT Silver）。
- 电力电子组强化两条 V0.7 规则：产品类别价值不得自动继承给 exact patent；post-T0 ground truth 不得回填 T0 evidence。
- 第24届当前累计3组外部验证配对，V0.7 仍为 Proposal。

- 第24届 Round 3 新增 P24-BIOLOGIC-001（艾可宁 Gold vs 北京生物新冠灭活疫苗 Silver）。
- 第24届达到4组跨届次验证最低门槛。
- V0.7 正式 adopted 为 Patent Value Benchmark research architecture。
- 明确：V0.7不宣称Gold/Silver预测能力，不输出获奖概率。
- 新增 V0.7 状态Schema，正式分离 Value / Attribution-Evidence / Observability / Realization Stage。

- Patent Value Ledger 1.0 Draft 上线：新增 Schema、方法文档、模板、贡献协议和首个公开示例（艾可宁）。
- Ledger CI 新增跨引用校验与V0.7 Non-inheritance硬规则：R3/R4/R5必须有exact-patent link，R5必须有专利级可归因价值。
- 将第24届Ledger示例Evidence从第25届预览数据中拆分，保持数据集语义边界。

- Patent Value Diagnostic 1.0 Draft 上线：新增Schema、确定性生成器、艾可宁人类可读示例和generated dataset。
- CI新增Diagnostic→Ledger一致性校验、Diagnostic证据引用校验和生成文件漂移检查。
- Diagnostic明确禁止Gold概率、无E4支持的专利金额估值和自动排名。

- E1–E5 从“最高等级”语义迁移为可并存的 `evidence_levels_present`，避免误读为单调评分阶梯。
- R1–R5新增 `realization_stage_evidence_ids`，要求价值实现阶段本身可追溯。
- 新增R0（华为无线通信）、R2（电网专利许可）验收Ledger，与艾可宁R4组成R0/R2/R4三阶段测试集。
- 新增Data Dictionary、CITATION.cff、许可证策略说明和v0.1.0 readiness checklist。
- 新增Markdown报告渲染器并纳入CI漂移检查。

- 许可证决策完成：代码/CI/JSON Schema 使用 Apache-2.0；原创文档与原创结构化数据使用 CC BY 4.0。
- 新增多许可证边界说明、NOTICE、代码/数据/文档许可证说明；第三方来源材料不被本仓库重新授权。

- 新增30分钟冷启动指南、单页速查、Ledger脚手架工具和冷启动PR模板。
- Issue #2 已改写为可直接执行的外部复现任务；无需历史聊天或额外口头说明。
- CI新增Python工具编译检查，冷启动脚手架、数据、Diagnostic与Markdown报告全链路通过。

- 启动V0.8理论研究线，但V0.7继续为正式架构。
- 完成“高价值专利”Value Construct拆分：Policy / Technological Quality / Private Asset / Realized Operating / Social-Strategic。
- 将citations、family size、claims、renewal、litigation等定位为Screening Signals，而非直接Value Proof。
- 提出候选新层：Rights Control、Counterfactual Control、Value Horizon / Option Value、Portfolio Context。
- 提出Patent Age“两只钟”解释：长期维持体现revealed value，但剩余排他期随年龄缩短。
