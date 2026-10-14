# Roadmap

## Research Preview — current

当前正式研究架构：**V0.7 adopted**

主项目目标是建立可复核、可反驳、可持续更新的 **Patent Value Benchmark**，而不是预测任何奖项。

从2026-09-24起，研究分为两条线：

- **Track A — Patent Value Benchmark**：通用专利价值主干
- **Track B — China Patent Award Research**：中国专利奖专项模块

两条线共享证据纪律、T0规则和数据治理，但不共享目标变量。

详见 `docs/research-tracks.md`。

---

## Track A — Patent Value Benchmark

> **维护平台期**：正式方法 V0.7 + schema 1.0；V0.8 research-only；普通样本扩样暂停。详见 [`cold-start-status.md`](cold-start-status.md)。
>
> **V0.8 design draft in progress / research-only；formal = V0.7 + schema 1.0** → [`methodology/model-v0.8-design-draft.md`](methodology/model-v0.8-design-draft.md)（**未**冻结、**未**采纳）。
>
> RC 可选并行轨细则（research-only；**未**启动 S1 升格）：[`methodology/rights-control-optional-parallel-plan.md`](methodology/rights-control-optional-parallel-plan.md)。
>
> **外推 E3-probe E3-A/B/C**（T0=2026-10-13；A/B=R3，C=R0 claims-fail）：预注册附录 B。
>
> **外推 holdout H1–H9**（T0=2026-10-13；已编码；主成功=纪律支持；**未** adopt V0.8）：[`methodology/external-extrapolation-preregistration.md`](methodology/external-extrapolation-preregistration.md) · [`../analysis/non-award-validation/holdout-extrapolation-synthesis.md`](../analysis/non-award-validation/holdout-extrapolation-synthesis.md)。
>
> **世界级四轨路线 + E3-N 提名**（research；**未**编码；**未** adopt V0.8）：[`methodology/world-class-roadmap.md`](methodology/world-class-roadmap.md) · [`methodology/e3-holdout-nominees-round2.md`](methodology/e3-holdout-nominees-round2.md)。
>
> **T2 既有模型比较矩阵 v0**（research）：[`methodology/existing-models-comparison-matrix.md`](methodology/existing-models-comparison-matrix.md)。
>
> **E3-N1/N2/N5 已编码**（T0=2026-10-13；3/3 R0 claims-fail）：[`../analysis/non-award-validation/holdout-e3-n125-synthesis.md`](../analysis/non-award-validation/holdout-e3-n125-synthesis.md)。
>
> **T1 理论备忘 v0**（research）：[`methodology/t1-theory-memo-value-construct.md`](methodology/t1-theory-memo-value-construct.md)。

> **E3-P Round 3**：**P1/P3/P4 已编码**（T0=2026-10-13；3/3 R3）：[`methodology/e3-holdout-nominees-round3.md`](methodology/e3-holdout-nominees-round3.md) · [`../analysis/non-award-validation/holdout-e3-p134-synthesis.md`](../analysis/non-award-validation/holdout-e3-p134-synthesis.md)。

> **E4 Round 1 提名**（判赔/销售损失/具名许可；**未**编码）：[`methodology/e4-holdout-nominees-round1.md`](methodology/e4-holdout-nominees-round1.md)。

### 当前正式架构：V0.7

已采用：

- Value State
- Attribution / Evidence State
- Observability State
- Value Realization Stage (R0–R5)

V0.7不输出总分，也不预测Gold。

### V0.8 Research — Round 1 complete, not adopted

第一轮完全不依赖中国专利奖标签的机制型压力测试已完成：

| Archetype | Tested mechanism | Main result |
|---|---|---|
| i4i v. Microsoft | Litigation value / enforcement | R5仍不能替代Rights Control |
| Amgen v. Sanofi | Claim-set validity | Rights Control需要claim-set granularity |
| PageRank | Same patent / two T0s | Two Clocks成立；R-stage不是价值等级 |
| CRISPR-Cas9 | Portfolio dependency | 单件专利Ledger之外需要Portfolio & Jurisdiction Network |

Round 1综合：

`analysis/non-award-validation/round1-cross-case-synthesis-v0.8.md`

当前假说状态：

- H1 Rights Control：第一组对照支持，仍需复制
- H2a Date/context dependence：支持
- H2b Two Clocks：支持
- H2c Clean early-stage option sample：4 个干净回顾完成（mRNA + OLED + Yoshino LIB + Grünberg GMR）；**4 / 4**
- H3 Portfolio Dependency：支持
- H4 Monetary evidence is contextual：跨诉讼/组合许可两类场景支持

### V0.8 adoption progress

- Rights Control matched pairs：**4 / 4（完成）**
- clean early-stage option retrospectives：**4 / 4**
- portfolio case：**1 / 1**（CRISPR；另有 Blade 非生科产品组合复制）
- Two Clocks case：**1 / 1**
- SEP / patent-pool / cross-license replication：**1 / 1**（US6825782B2 / Via LA AVC pool）
- non-life-science complex product portfolio：**1 / 1**（CN110165116B Blade CTP）
- Round 2 cross-case synthesis：**完成** → `analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`

因此：

> **预注册复制门槛已满足，但 V0.8 remains not adopted。**  
> 正式方法仍为 V0.7；formal schema 仍为冻结的 1.0。采纳与否由用户显式决定。

Round 2 已结束扩样。

**维护平台期（2026-10-12）**：Track A 正式表面稳定（V0.7 + schema 1.0）。普通冷启动扩样 **已暂停**。V0.8 / RC / RP / CF 保持 research-only；采纳需显式决策。允许文档/校验维护；普通 contrib 扩样仍暂停。**例外：** 预注册锁定的外推 holdout H1–H9（2026-10-13）已入库。状态快照：[`docs/cold-start-status.md`](cold-start-status.md)。

#### Package A — Rights Control Replication
**已完成4/4：**
1. i4i × Amgen
2. Apple ’381 claim 19 × Apple ’915 claim 8
3. SynQor ’702 claim 56 × ’021 claim 30
4. Wirtgen ’309 claim 29 × Caterpillar ’693 claim 19

第四组进入工业道路铣刨机械，并出现“PTAB不利FWD但取消尚未生效、ITC排除令仍在执行”的并存状态，证明Rights Control不能压成valid/invalid布尔值。

Package A停止继续扩样。实验性 Claim-set Rights Control Schema 0.1 已实现并接入CI，但仍与正式v1 Ledger Schema隔离。下一阶段转入Package B/C剩余验证，以及Issue #16的Realization Path复制研究。

#### Package B — Early-stage Option Value
寻找4个真正T0=R0/R1、后来形成重大现实价值的历史专利。PageRank不计入。

当前进度：**4 / 4（完成）**
1. US8278036B2（Karikó–Weissman modified nucleoside RNA）— early T0=2012-10-02 停在 **R0**；分析见 `analysis/non-award-validation/mrna-us8278036-early-option-packageb.md`。
2. US4539507A（Tang–VanSlyke / Kodak thin-film organic EL）— early T0=1987-09-21 停在 **R0**；分析见 `analysis/non-award-validation/oled-us4539507-early-option-packageb.md`。
3. US4668595A（Yoshino / Asahi Kasei practical nonaqueous secondary battery）— early T0=1987-05-26 停在 **R0**；分析见 `analysis/non-award-validation/lib-us4668595-early-option-packageb.md`。
4. US4949039A（Grünberg / KFA Jülich multilayer GMR-type magnetic-field sensor）— early T0=1990-08-14 停在 **R0**；分析见 `analysis/non-award-validation/gmr-us4949039-early-option-packageb.md`。

Package B 停止继续扩样（除非未来证据证伪 H2c）。PageRank 仍仅计入 Two Clocks，不计入 Package B。

#### Package C — Portfolio / Licensing Replication

**已完成 3 / 3：**
- CRISPR portfolio case（US8697359，R2）
- **SEP / patent-pool external replication：US6825782B2（NTT Docomo）∈ Via LA AVC/H.264 Patent Portfolio License，T0=2026-10-12，R2**
- **非生命科学复杂产品组合：CN110165116B（比亚迪刀片电池 CTP 族锚点），T0=2026-10-12，R0**

分析：
- `analysis/non-award-validation/avc-us6825782-sep-pool-packagec.md`
- `analysis/non-award-validation/byd-blade-cn110165116-portfolio-packagec.md`

Round 2 最小复制集已完成。Adoption-readiness 综合见：

`analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`

> **V0.8 remains not adopted.** Schema 1.0 unchanged. Default methodology remains V0.7.

### Candidate architecture after Round 1 + Taction state-model refinement

```text
Value Base
├─ Technology State
└─ Product State

        +

V0.7 Realization / Evidence
R0 → R5

        +

Claim-set Rights Control

        +

Realization Path
├─ Infringement State
├─ Remedy State
└─ Cash / Economic Realization State

        +

Value Horizon / Two Clocks

        +

Portfolio & Jurisdiction Network

Cross-cutting:
Time/T0 · Jurisdiction · Evidence/Observability · Enforcement Capacity

Screening Signals remain outside value facts.
```

Taction带来的Realization Path目前只是exploratory dimension，不修改现有V0.8 adoption threshold；需要单独预注册验证。

---

## Patent Value Ledger + Diagnostic

状态：**核心输入/输出闭环已建立**

已完成：

- Patent Value Ledger 1.0 Draft
- Patent Value Diagnostic 1.0 Draft
- Ledger → Diagnostic 确定性生成器
- Diagnostic → Markdown report 渲染
- CI校验 non-inheritance、cross-reference、T0 和版本一致性
- R0 / R2 / R4 / R5公开样例
- 非奖项机制样本已进入同一数据链

下一步：

- 外部冷启动复现
- 根据复现结果修正文档 / schema
- 在V0.8研究与v0.1.0基础设施release之间保持版本边界
- Schema freeze
- v0.1.0 release

---

## Track B — China Patent Award Research

中国专利奖研究作为独立长期模块保留。

### 已完成的历史研究

#### 第25届
- 10组 Gold–Silver matched pairs
- Cross-pair Synthesis
- V0.6 的主要形成样本

#### 第24届
- 4组跨届压力测试
- 创新药、软件基础设施、电力电子、生物制品
- 用于V0.7外部验证

这些记录继续保存在：
- `analysis/25th-validation/`
- `analysis/24th-validation/`

专项入口：
- `analysis/china-patent-award/README.md`

### 后续独立议程

逐步扩展：
- 历届 Gold / Silver / Excellent
- 评奖标准与结果的制度史
- 同届同领域匹配研究
- 获奖后技术、市场、许可、诉讼、标准、产业化表现
- 金奖是否对某些 value constructs 提供稳定外部信号

历史数据必须区分当时的评奖制度与当前制度，避免跨制度直接横比。

---

## Historical provenance — V0.6 / V0.7

项目早期曾以中国专利奖样本为主要现实世界验证入口。

### V0.6 Cross-pair Synthesis

第25届10组 matched pairs：

- Yes: 2
- No: 4
- Uncertain: 4

得到的关键结论不是“能预测Gold”，而是：

- 单一readiness分数无法稳定区分奖项结果；
- 必须拆开价值、归因、可观察性和实现阶段；
- 不能用事后故事修补 Unknown。

### V0.7 External Validation

第24届4组跨届压力测试达到预设最低门槛。

正式采用：

- Value State
- Attribution / Evidence State
- Observability State
- Value Realization Stage (R0–R5)

这些结果现在被视为：

> **通用架构的历史形成证据 + 中国专利奖专项研究资产**

而不是主项目未来样本设计的默认模板。

---

## Public release — v0.1.0

首次正式版本发布前完成：

- README 完整化
- 数据字典
- 示例记录
- CONTRIBUTING
- CITATION.cff
- 多许可证边界确认
- 首批可复核 benchmark dataset
- 外部冷启动复现
- Schema freeze
- CI 全部通过
- Git tag + GitHub release


---

## Realization Path — three-path replication complete

Issue #16预注册复制已完成：

1. **Taction v. Apple** — litigation → damages verdict → cash unresolved
2. **Editas → Vertex → DRI** — license → upfront cash → recurring fee → receivable monetization
3. **Wirtgen ITC** — infringement → exclusion order → continuing control realization

主要修正：

- Infringement不是所有路径的必经节点；
- Remedy State改为更一般的 **Realization Mechanism**；
- Cash Realization改为 **Economic Realization State**；
- Realization Path采用 **Event Log → deterministic Snapshot**；
- rights subject需要支持claim set / patent / portfolio / field rights / receivable。

研究结论见：
- `analysis/non-award-validation/realization-path/three-path-synthesis.md`
- `analysis/theory/patent-value-state-model-1.1-realization-path.md`

下一步允许设计Experimental Realization Path Schema 0.1，但V0.8仍未adopt。


## Experimental Realization Path 0.1 — implemented

Issue #20已完成工程化：

- event-log schema
- generated snapshot schema
- three-path structured backfill
- deterministic projector
- validator
- unit tests
- CI integration
- data dictionary / design note

Canonical rule:

> **Events are facts; Snapshot is generated.**

三个canonical fixtures在CI中固定为：

- Taction：jury verdict存在，但cash realization仍为unresolved；
- Editas：无merits infringement judgment，仍可通过license实现现金并进一步货币化应收款；
- Wirtgen：通过ITC exclusion order实现control，cash = not_required。

Experimental 0.1仍与formal v1 Ledger Schema隔离，也不改变V0.8 adoption threshold。
