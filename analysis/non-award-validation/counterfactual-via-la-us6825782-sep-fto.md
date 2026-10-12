# Counterfactual Control Case #3 (exploratory) — Via LA AVC SEP US6825782 (standard-lock + FRAND/pool FTO)

日期：2026-10-12  
状态：Issue [#37](https://github.com/xiangsee/patent-value-benchmark/issues/37) — **exploratory / different-R**；**不**计入 matched-pair #1×#2  
研究线：Track A — Patent Value Benchmark  
正式基线：**V0.7**；schema **1.0**；**无** Counterfactual schema；**不** adopt V0.8  
R 锚点（已有正式 Ledger，不新建行）：`data/ledgers/non-award-avc-us6825782-sep-pool.jsonl` → **R2** @ T0=2026-10-12  
姊妹：Package C 笔记 `avc-us6825782-sep-pool-packagec.md`；配对综合 `counterfactual-i4i-apple381-pair-synthesis.md`  
为何选 Via LA 而不是 ’915：公开池交叉表 / FAQ / 费率卡即可核验 standard-lock 与 FTO 路径，无需再拆 Apple lost-profits 意见书；且避免与 Rights Control Pair 2（’915 再审恶化）标签重贴。

---

## 一、这一例测什么（不是再讲一遍 R2 池许可）

Package C 笔记已经证明：单件 SEP 只能诚实停在 **R2**（pool membership + 标准映射），不能继承池费率或被许可人产品。

本笔记只补 Counterfactual 问题：

> 对 **要做 AVC/H.264 合规实现** 的实施者而言，公开记录如何描述 **next-best alternative** 与 **FTO 路径**？  
> 去掉本专利（或等价 essential claim theme）是否等于「换个 UI 反馈就能继续卖产品」，还是更接近 **退出该标准档位 / 走许可**？

答案（本案，定性）：

> **对合规 AVC 实现：标准级锁定强；设计绕开 ≈ 不做该标准档位。公开 FTO 路径是 Via LA（前 MPEG LA）AVC Patent Portfolio License（FRAND/池式组合许可），不是 feature-level redesign。**

这与 i4i / Apple ’381 的 **feature-level** 故事不同构——所以标为 exploratory，不假装 R2≈R4。

---

## 二、T0 与信息边界

| 项 | 值 |
|---|---|
| T0 | **2026-10-12**（与现有 Package C Ledger 一致；当前状态） |
| 专利 | [US6825782B2](https://patents.google.com/patent/US6825782B2/en)（NTT Docomo；Via LA Cross-Reference：claim **12** → H.264 **§9.3** CABAC 族） |
| V0.7 realization | **R2**（rights transaction via pool；exact product / patent-level $ = Unknown） |
| 本笔记新增 | Counterfactual：`blocking_scope≈standard` + `fto_path=pool/FRAND` |
| 信息规则 | 只用公开池清单、交叉表、FAQ/费率说明；**不**发明单件 redesign 美元；**不**把池费率当分给本专利的绕开成本 |

---

## 三、Counterfactual 结构化摘要（定性，无分数）

| 字段（候选名） | 本案观察 | 证据性质 |
|---|---|---|
| `next_best_alternative` | **做合规 AVC/H.264 实现时**：公开记录不提供「去掉 CABAC 相关 essential 映射仍自称同一标准档位」的产品级 NIA；现实替代是 **不实施该标准 / 改用其他编解码路线**（那是品类/标准选择，不是 feature patch） | 标准必要映射（池交叉表）+ 一般 SEP 结构事实；不发明技术绕开方案 |
| `design_around_feasibility` | **对「保持 AVC 合规」目标：低**；对「改做非 AVC 产品」目标：那是换标准，不是对本 claim 的 design-around | ≤T0 公开 essentiality chart（claim 12 → §9.3） |
| `performance_or_feature_loss_if_removed` | 若坚持无许可且避开映射条款：则 **无法声称完整依赖该条款族的 AVC 合规实现**；不等于「不能卖任何视频设备」 | blocking_scope 必须写 **standard-level**，禁止写成「消费电子产品线死亡」 |
| `blocking_scope` | **standard-level（对合规实现）** / product-line（否：非 AVC 路线仍可能存在） / feature-level（本案主叙事不适用） | 与 i4i/Apple 的 feature 轴对照 |
| `fto_path` | **Via LA AVC Patent Portfolio License**（多许可人池；公开 Licensee 名单；公开费率卡且 FAQ 表明费率 **不随 essential 专利件数增减**） | 公开池文件；FTO = 组合许可上下文，**不是**本专利单价 |

一句话：

> **R2 SEP + 标准级封锁叙事 + 池/FRAND FTO 路径** —— R 很低，但 Counterfactual 的 `blocking_scope` / `fto_path` 仍可比 feature 诉讼案更「硬」在标准轴上。

这正说明：Counterfactual **不能**从 R 单调推断；也说明过早写 schema 会把 feature 案与 SEP 案揉成同一伪精确字段。

---

## 四、与 Rights Control / Realization Path / R-stage / Portfolio 的强制拆分

| 问题 | 归属 | 本案怎么记 |
|---|---|---|
| 专利是否在池清单、是否有 licensor 路径 | **V0.7 R2 + Portfolio/network 笔记** | 已有 Package C Ledger / network JSON |
| 池费率是多少、enterprise cap | **Realization Path / H4 monetary context（program-scope）** | 费率 ≠ 本专利价格；**绝非** design-around cost |
| 禁令 / PTAB / 权利有效性争议 | **Rights Control** | 本案冷启动未主张 operative injunction；不把「在池里」写成禁令 |
| 合规实施者有没有公开 FTO 通道、绕开是否等于退标准 | **Counterfactual Control** | 本笔记核心 |

**禁止合并写法：**

- ❌ 「SEP ⇒ blocking_score=1」（发明分数）  
- ❌ 「池年费 ≈ 绕开成本」（把 program royalty 写成 redesign $）  
- ❌ 「R2 低 ⇒ 容易绕开」（R 只谈 realization 证据阶段）  
- ❌ 「有 FRAND ⇒ 无封锁」（FRAND 是 FTO **路径**，不是「标准可随意不实施」）

---

## 五、对 #1×#2 配对的增量（为何仍只算 exploratory）

| | i4i / Apple ’381（matched） | Via LA ’782（本 exploratory） |
|---|---|---|
| R 带 | R5 / R4 | **R2**（故意不同） |
| blocking_scope | feature | **standard（合规轴）** |
| fto_path | 许可谈判 / 金钱救济为主（无池式公开 FTO 卡） | **公开专利池 / FRAND 组合许可** |
| 能否计入 Issue #37 matched 最低门槛 | 是 | **否**（issue 原文：different R） |

增量价值：证明候选字段 `blocking_scope` 与 `fto_path` 在 SEP 上有独立观测面；  
**不**用来宣称「已有第三件 R4–R5 matched case」。

若未来要做 **同 R 带** 的第三 matched case，更干净的候选人仍是 Apple **’915 claim 8** 的 claim-scoped lost-profits NIA（需单独笔记，且严格与 Rights Control Pair 2 的再审故事拆开）——本轮不展开。

---

## 六、本轮明确不做

- 不新建 / 不改 formal Ledger 行  
- 不写 `schema/experimental/counterfactual*`  
- 不发明美元级 design-around cost，不把池费率分给本专利  
- 不宣布 V0.8 adoption  
- 不把本案算进 matched-pair 关闭条件的「第 3 件同 R 案」

Tracker：Issue #37（replication 门由 `counterfactual-i4i-apple381-pair-synthesis.md` 勾选；本文件为扩展观测）。
