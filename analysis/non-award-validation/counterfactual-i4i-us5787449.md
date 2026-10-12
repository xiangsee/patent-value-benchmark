# Counterfactual Control Case #1 — i4i / US5787449 (hard feature-level NIA)

日期：2026-10-12  
状态：Issue #37 pre-registration — **analysis-first**; not an adopted model change  
研究线：Track A — Patent Value Benchmark  
正式基线：**V0.7**；schema **1.0** 不变；**无** Counterfactual schema  
关联：[#37](https://github.com/xiangsee/patent-value-benchmark/issues/37)；姊妹笔记 `counterfactual-apple-us7469381-bounceback.md`  
R 锚点（已有正式 Ledger，不新建行）：`data/ledgers/non-award-i4i-us5787449.jsonl` → **R5** @ T0=2010-03-10

---

## 一、这一例测什么（不是再讲一遍 R5）

Round 1 笔记 `i4i-us5787449.md` 已经证明：V0.7 能诚实记下 R5 / E3–E5 / 禁令证据，但 **design-around / blocking** 只能挤进 notes。

本笔记只补 Issue #37 的 Counterfactual 问题：

> 在 realization 已经很高时，公开记录能否单独说明：**去掉或禁用该专利覆盖的功能后，竞争者的 next-best alternative 是否仍然“商业上够用”？**

答案（本案）：**不够用**——至少对 Microsoft 想保留的 **Word custom XML editor 能力** 而言。

---

## 二、T0 与信息边界

| 项 | 值 |
|---|---|
| T0 | **2010-03-10**（Federal Circuit 重新判决日；与现有 Ledger 一致） |
| 产品载体 | Microsoft Word 中的 custom XML editor |
| V0.7 realization | **R5**（exact mapping + patent-level damages + enforcement 证据链） |
| 本笔记新增对象 | Counterfactual Control（叙事结构）；**不**改 Ledger 字段 |

只使用 T0 及以前公开裁判记录。不把后来 Word 产品演进倒灌成 2010 的绕开成本数字。

---

## 三、Counterfactual 结构化摘要（定性，无分数）

| 字段（候选名） | 本案观察 | 证据性质 |
|---|---|---|
| `next_best_alternative` | Microsoft 提出的“非侵权使用”：binary `.doc` 存储、无内容 XML、仅创建表单类流程等 | 诉讼记录中的 **提出的 NIA**，被法院/陪审团路径视为对 **accused custom XML editor 用途** 不充分 |
| `design_around_feasibility` | **低（对保留该功能而言）**：公开评论与裁判语境表明可行路径是 **禁用 custom XML 功能 / 换 SKU**，而不是在保持同等动态 custom XML 编辑能力下轻松绕开 | ≤T0 公开裁判 + 同期公开报道（禁用功能路径） |
| `performance_or_feature_loss_if_removed` | **功能层损失**：新销售/许可副本上的 custom XML editor 能力被禁令覆盖；**产品层**：Word 作为文字处理产品类别仍可继续销售（禁令被裁成窄范围） | 禁令范围本身就是“feature-level block, not kill Word”的公开结构 |
| `blocking_scope` | **feature-level（强）** / product-line（弱：Word 本体未整体禁售） | 禁令文本：针对含 custom XML 打开/编辑能力的 Word，且主要约束禁令生效后的新购买/许可副本 |
| `fto_path` | 本案记录中未见 FRAND/池式 FTO；现实路径是合规禁用或许可谈判（谈判结果不作估值） | 缺省 = Unknown，不发明许可金 |

一句话：

> **高 R + 强 feature blocking + 对“保留该功能”而言 NIA 不足；同时不等于“Word 产品线死亡”。**

这正是 V0.7 R-stage 表达不了、又不能偷换成 Rights Control 布尔值的信息。

---

## 四、与 Rights Control / Realization Path / R-stage 的强制拆分

| 问题 | 归属 | 本案怎么记 |
|---|---|---|
| 禁令是否发出、是否仍 operative | **Rights Control / remedy** | Federal Circuit 维持永久禁令（调整生效日）→ 法律控制侧事实 |
| 2 亿美元是不是专利价格 | **Realization Path / H4 monetary context** | dispute-specific damages；**不是** design-around 成本 |
| R5 是否成立 | **V0.7 Value Realization** | 已由现有 Ledger 固定 |
| custom XML 有没有“商业上可接受的非侵权替代用法” | **Counterfactual Control** | 本案核心；法院路径拒绝把 Microsoft 列举的用途当成充分 NIA |

**禁止合并写法：**

- ❌ “有禁令 ⇒ blocking_score 高”（把 remedy 当成 Counterfactual）
- ❌ “R5 ⇒ 绕不开”（把 realization 当成 alternatives）
- ❌ “2 亿美元 ≈ 绕开成本”（发明 damages）

---

## 五、对研究问题的贡献（相对配对案）

与 `counterfactual-apple-us7469381-bounceback.md` 对照：

| | i4i ’449 | Apple ’381 c19 |
|---|---|---|
| 相近 realization | **R5** | **R4**（同为诉讼已实现、exact mapping 商业软件/UI） |
| Feature NIA | 记录显示 **不足**（对 accused editor 用途） | 记录承认 **存在** rubberband/边界反馈的非侵权替代实现 |
| Product-level blocking | Word 产品可继续；**功能**被强排除 | 智能手机品类继续；**未**获得永久禁令；因果关联未证明 feature 驱动整机需求 |
| V0.7 单独能说清吗？ | 只能到 R5 + notes | 只能到 R4 + notes |

**初步结论（单案，不触发 schema）：**

> Same-ish high realization 下，Counterfactual 仍可显著分化：**“功能级强封锁” vs “功能可省略/可替代且整机需求不被该功能驱动”。**

---

## 六、本轮明确不做

- 不新建 / 不改 formal Ledger 行  
- 不写 `schema/experimental/counterfactual*`  
- 不发明美元级 design-around cost  
- 不宣布 V0.8 adoption  

下一动作见配对案与 Issue #37 tracker。
