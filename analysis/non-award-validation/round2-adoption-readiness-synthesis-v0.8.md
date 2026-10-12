# V0.8 Round 2 — Adoption-Readiness Synthesis

日期：2026-10-12  
状态：**Round 2 minimum replication set complete; adoption-readiness documented; V0.8 NOT adopted**  
正式架构：**V0.7 remains adopted**  
Schema：**formal Ledger / Diagnostic remain `schema_version: "1.0"` (frozen at v0.1.0)**  
关联：Issue [#11](https://github.com/xiangsee/patent-value-benchmark/issues/11)（已关闭）

---

## 0. 一句话结论

> Round 2 证明：V0.7 仍然是正确的 **Evidence & Realization** 主干；V0.8 候选层（Rights Control / Value Horizon / Portfolio Network）在复制门槛上已达到「可以进入采纳讨论」的证据量，但 **不足以、也不应自动触发 adoption**。  
> **推荐：继续采用 V0.7；V0.8 保持 research-only，直到用户作出显式采纳决策。**

本文件是 adoption-readiness 综合，**不是** schema freeze、**不是** 方法基线切换、**不是** 实验对象升格为正式 schema。

---

## 1. Round 2 完成了什么

预注册最小复制集（Issue #11）已全部完成：

| Package | 门槛 | 结果 | 主机制 |
|---|---|---|---|
| **A — Rights Control** | 4 pairs | **4 / 4** | Claim-set 法律控制 ≠ R-stage |
| **B — Early option** | 4 cases | **4 / 4** | 早期 R0 可与 option signals 并存 |
| **C — Portfolio / licensing** | CRISPR + SEP/pool + 非生科复杂产品 | **3 / 3** | 网络对象不可压成单件 Ledger 字段 |

### 1.1 Package A — Rights Control（4 pairs）

| Pair | 样本 | Realization | Rights-control 对照要点 |
|---|---|---|---|
| 1 | i4i US5787449 × Amgen PCSK9 | R5 vs R4 | injunction/enforcement vs genus/enablement 失效 |
| 2 | Apple ’381 c19 × ’915 c8 | R4 vs R5 | reexam 确认 vs 不利 reexam 姿态 |
| 3 | SynQor ’702 c56 × ’021 c30 | **R4 vs R4** | 可专利性维持 vs obviousness 驳回确认 |
| 4 | Wirtgen ’309 c29 × Caterpillar ’693 c19 | **R4 vs R4** | IPR 存活 vs 不可专利 FWD + 仍有效的 ITC LEO |

稳定重复出现的最小信息：claim-set identity、scope、adjudication、finality、operative control。  
「valid / invalid」布尔不够；权利状态需要程序、终局性与可操作救济并存建模。

综合：`analysis/non-award-validation/rights-control-4pair-synthesis-v0.8.md`  
实验对象（**非**正式 schema）：`schema/experimental/claim-set-rights-control.schema.json`、`data/experimental/rights-control/`

### 1.2 Package B — Early-stage option retrospectives（4 cases）

| # | 专利 | Early T0 | V0.7 stage | 行业分化 |
|---|---|---|---|---|
| 1 | US8278036B2 Karikó–Weissman mRNA | 2012-10-02 | **R0** | 生物医药 RNA |
| 2 | US4539507A Tang–VanSlyke / Kodak OLED | 1987-09-21 | **R0** | 显示材料 |
| 3 | US4668595A Yoshino / Asahi Kasei LIB | 1987-05-26 | **R0** | 储能材料电化学 |
| 4 | US4949039A Grünberg / Jülich GMR | 1990-08-14 | **R0** | 自旋电子 / 磁存储传感 |

共同结果：

- early T0 诚实停在 **R0**；
- 同时存在可核验的 option / future-value signals（科学论文、机构 IP、架构声称用途等）；
- post-T0 重大成功（疫苗 / OLED / 商业锂电 / GMR 磁头等）**不得** 回填 early ledger；
- PageRank 仅计入 Two Clocks，**不计入** Package B。

H2c（clean early-stage option sample）达到预注册门槛；Package B 停止继续扩样，除非未来证据证伪 H2c。

### 1.3 Package C — Portfolio / licensing（含 CRISPR + SEP + 刀片非生科组合）

| 案例 | 锚点 | Stage | 网络形态 |
|---|---|---|---|
| CRISPR portfolio | US8697359 | R2 | 多权利人 / 许可栈 / 司法辖区网络 |
| SEP / patent pool | US6825782B2 ∈ Via LA AVC/H.264 | R2 | 多许可人专利池 + 标准映射；费率不随件数 |
| Blade non-LS product portfolio | CN110165116B（刀片 CTP 族） | R0 | **同权利人**复杂产品系统多专利栈（40+ 同日/同优先权族） |

三类机制互补：

1. CRISPR：跨主体许可与竞争/互补权利要求；
2. AVC pool：标准必要 + 池费率不可分摊到单件；
3. 刀片 CTP：同 assignee 产品平台成功 **≠** exact-patent → carrier；「300+ 专利」只是 program scope。

H3（Portfolio Dependency）在生命科学之外得到复制，且形态不同于池/多许可人网络。

### 1.4 与 Round 1 / 既有门槛的对齐

Round 1 已支持 H1（初对）、H2a、H2b、H3、H4；Round 2 完成 H1 复制门槛、H2c 门槛、以及 Package C 的 SEP/pool 与非生科产品组合。  
Two Clocks（PageRank）仍为 1/1。  
Realization Path（Issue #16 / #20）是 **exploratory**，**不计入** 本文件的 V0.8 adoption 门槛。

---

## 2. V0.7 不能充分表达的缺口

V0.7 **没有被推翻**。它继续正确回答：

> 在给定 T0，公开证据能把价值实现推进到哪一 R-stage，且 attribution / observability 如何约束该判断。

Round 2 重复暴露的是 **相邻层缺失**，不是 R-stage 设计错误：

### 2.1 Legal control beyond R-stage

- 同等或更高 realization，不蕴含更强可执行权利（Apple pair；SynQor / Wirtgen 同为 R4）。
- Claim-set 粒度、程序终局性、operative remedy（含 ITC LEO 与 PTAB FWD 并存）无法被 R0–R5 吸收。
- 诉讼损害赔偿 / 排除令是 **带 scope 的证据**，不是内在专利价格。

### 2.2 Value horizon / option

- R0 可以与可观察的未来期权信号共存（Package B ×4）。
- R-stage ≠ 价值大小 / 折旧评分；需要独立的 horizon / Two Clocks 对象，才能表达「已实现历史」与「剩余排他 / option」不同时钟。
- Outcome leakage 纪律在 early retrospective 中仍然是硬约束。

### 2.3 Portfolio / network objects

- 单件 Ledger 无法承载：池成员资格与标准映射、多许可人栈、同族互补 claim theme、program-scope「300+」叙事。
- Portfolio value ≠ Σ single-patent values；Jurisdiction A ≠ Jurisdiction B；pool royalty ≠ patent price。
- 实验性 network JSON（CRISPR / AVC / Blade）证明 **graph object** 增加决策信息，但也证明过早 schema 化会把未稳定字段冻进去。

### 2.4 明确不把下列内容塞进 V0.7

- design-around cost / blocking power 等 Counterfactual Control（仍缺系统复制）；
- Realization Path 的 event→snapshot 工程对象升格；
- 任何总分、Gold 概率、bibliometric→价值的短路。

---

## 3. 未来若讨论 V0.8 adoption，需要什么

### 3.1 已满足的预注册复制门槛（事实）

按 `docs/methodology/model-v0.8-research-agenda.md` 的 Adoption rule：

- Rights Control matched pairs：**4 / 4**
- Clean early-stage option retrospectives：**4 / 4**
- Portfolio case：**≥1**（CRISPR；另有 Blade 非生科复制）
- Two Clocks case：**1 / 1**
- SEP / patent-pool / cross-license：**1 / 1**（AVC）
- 本文件作为 **新的 cross-case synthesis**

门槛完成 **≠** 自动 adoption。门槛只解除「证据量不够、禁止讨论」的硬阻塞。

### 3.2 采纳前仍必须由用户显式决定的事项

1. **正式方法基线是否从 V0.7 切换**（默认：**否**）。
2. **哪些候选层进入正式 schema**（Rights Control / Horizon / Network 可分阶段，禁止一次塞全）。
3. **实验 schema 0.1 是否升格**，以及升格时的兼容策略（不得默默 bump 已冻结的 `1.0`）。
4. **Diagnostic / CI / CONTRIBUTING 的用户可见合同**如何改写（冷启动用户仍应以 V0.7 规则验收）。

### 3.3 仍开放的风险（未关闭则不应 adopt）

| 风险 | 说明 |
|---|---|
| Overfitting to famous cases | Round 2 样本虽跨行业，但仍偏「教科书级」叙事；普通冷启动专利的可操作性未同等验证 |
| Field explosion | Counterfactual Control、Realization Path、Screening Signals 若一并正式化，会破坏 v0.1.0 可用性 |
| False precision | 把 option signals 或 network 边写成伪定量分数 |
| Scope leakage | 池费率 / 产品收入 / 组合许可金再次漏进单件 R3+ |
| Dual-track confusion | 用户分不清 formal 1.0 Ledger 与 `schema/experimental/*` |
| Governance debt | 无显式「谁批准 adoption」与回滚标准 |

### 3.4 Non-goals（采纳讨论也不做这些）

- 生成总分或排名；
- 预测中国专利奖 Gold；
- 把 bibliometric proxy 当作直接价值；
- 用年龄做单向正/负指标；
- 把 portfolio / pool value 机械均分到成员专利；
- 把一司法辖区权利状态复制到其他国家；
- 把产品收入自动归因给 exact patent；
- **在用户决定前 bump schema 超过冻结的 1.0，或把默认方法从 V0.7 改掉。**

### 3.5 若用户将来批准 adoption，建议的最小路径（仅规划，本 PR 不实施）

1. 先只把 **Claim-set Rights Control** 的最小稳定字段升为 optional 并行对象（与 Ledger 1.0 并存，不破坏既有行）；
2. Horizon / Network 继续 research + 更多普通样本；
3. 新版本号与迁移说明；单独 release notes；保留 V0.7 作为可读默认；
4. 禁止在同一 PR 中「adoption + 大改字段 + 发版」捆绑。

---

## 4. 显式建议（给维护者 / 用户）

| 决策项 | 建议 |
|---|---|
| 正式研究架构 | **保持 V0.7 adopted** |
| V0.8 | **research-only** |
| Formal schema | **保持 `1.0`；不 bump** |
| Experimental schemas | 继续隔离在 `schema/experimental/` |
| Round 2 | 复制门槛完成；本综合关闭「缺 synthesis」项 |
| 下一步工程 | 工具链、更多普通样本、文档可用性——**不是** adoption |

**推荐决议文本（可供用户一键确认）：**

> 确认：在另行显式批准前，Xiangsee Patent Value Benchmark 继续以 V0.7 为正式方法；V0.8 仅作研究议程；Ledger/Diagnostic schema 保持冻结的 1.0。

---

## 5. 关键指针（main 上的分析与 Ledger）

### 5.1 综合与议程

| 文件 | 作用 |
|---|---|
| `analysis/non-award-validation/round1-cross-case-synthesis-v0.8.md` | Round 1 机制压力测试综合 |
| `analysis/non-award-validation/rights-control-4pair-synthesis-v0.8.md` | Package A 四对照综合 |
| `analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md` | **本文件** |
| `docs/methodology/model-v0.8-research-agenda.md` | V0.8 研究议程（not adopted） |
| `docs/methodology/model-v0.7.md` | 正式方法 |
| `docs/roadmap.md` | 进度与边界 |

### 5.2 Package A 分析与 Ledger

| 分析 | Ledger |
|---|---|
| `i4i-us5787449.md` / `amgen-sanofi-pcsk9.md` | `non-award-i4i-us5787449.jsonl` / `non-award-amgen-pcsk9.jsonl` |
| `apple-samsung-rights-control-pair2.md` | `non-award-apple-samsung-rights-pair2.jsonl` |
| `synqor-rights-control-pair3.md` | `non-award-synqor-rights-pair3.jsonl` |
| `road-milling-rights-control-pair4.md` | `non-award-road-milling-rights-pair4.jsonl` |

### 5.3 Package B

| 分析 | Ledger |
|---|---|
| `mrna-us8278036-early-option-packageb.md` | `non-award-mrna-us8278036-early-option.jsonl` |
| `oled-us4539507-early-option-packageb.md` | `non-award-oled-us4539507-early-option.jsonl` |
| `lib-us4668595-early-option-packageb.md` | `non-award-lib-us4668595-early-option.jsonl` |
| `gmr-us4949039-early-option-packageb.md` | `non-award-gmr-us4949039-early-option.jsonl` |

### 5.4 Package C / Round 1 portfolio & Two Clocks

| 分析 | Ledger / network |
|---|---|
| `crispr-portfolio-network.md` | `non-award-crispr-us8697359.jsonl` · `crispr-portfolio-network.json` |
| `avc-us6825782-sep-pool-packagec.md` | `non-award-avc-us6825782-sep-pool.jsonl` · `avc-sep-pool-network.json` |
| `byd-blade-cn110165116-portfolio-packagec.md` | `non-award-byd-blade-cn110165116-portfolio.jsonl` · `byd-blade-ctp-portfolio-network.json` |
| `pagerank-two-clocks.md` | `non-award-pagerank-two-t0.jsonl` |

路径前缀：分析在 `analysis/non-award-validation/`；Ledger 在 `data/ledgers/`。

### 5.5 相关但不计入本 adoption 门槛

- Realization Path：`analysis/non-award-validation/realization-path/`、`analysis/theory/patent-value-state-model-1.1-realization-path.md`
- 状态模型：`analysis/theory/patent-value-state-model-1.0.md`
- 外部冷启动（#2）：`data/ledgers/contrib-ZL201910544929.3.jsonl`（与刀片族兄弟专利对照，但属 v0.1.0 可用性，不是 V0.8 adoption 样本）

---

## 6. 变更边界（本 PR 遵守）

- ✅ 增加本综合文档，并同步 roadmap / research agenda / CHANGELOG 中 Round 2 完成状态；
- ✅ 明确 **不 adopt V0.8**；
- ❌ 不修改 `schema/patent-value-ledger.schema.json` 等正式 1.0；
- ❌ 不把 experimental schema 移入正式路径；
- ❌ 不改变默认方法论文档中的 V0.7 adopted 表述；
- ❌ 不提交「看起来像 freeze」的投机 schema 草稿。
