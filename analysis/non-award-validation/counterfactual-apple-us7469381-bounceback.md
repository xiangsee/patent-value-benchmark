# Counterfactual Control Case #2 — Apple US7469381 claim 19 (bounce-back / documented NIA)

日期：2026-10-12  
状态：Issue #37 pre-registration — **analysis-first**; not an adopted model change  
研究线：Track A — Patent Value Benchmark  
正式基线：**V0.7**；schema **1.0** 不变；**无** Counterfactual schema  
关联：[#37](https://github.com/xiangsee/patent-value-benchmark/issues/37)；配对案 `counterfactual-i4i-us5787449.md`  
R 锚点（已有正式 Ledger，不新建行）：`data/ledgers/non-award-apple-samsung-rights-pair2.jsonl` 中 **US7469381 / claim 19** → **R4**（Ledger T0=2017-04-14，Rights Control 复制用）  
本笔记 Counterfactual 观察日：**2014-03-06**（N.D. Cal. 拒绝 Apple 基于 utility patents 的 renewed permanent injunction）

---

## 一、为什么用 ’381，而不是再写一遍 Rights Control Pair 2

`apple-samsung-rights-control-pair2.md` 回答的是：

> 同案、同生态下，claim-set **法律控制**如何分化（’381 再审存活 vs ’915 不利再审态势）。

本笔记回答 Issue #37：

> 在 **R4 级诉讼已实现** 的前提下，公开记录是否显示 **bounce-back / rubberband 功能** 存在可记录的 next-best alternative，以及去掉该功能是否等于竞争者退出智能手机市场？

答案（本案）：**存在 NIA 叙事；去掉该功能 ≠ 产品品类封锁。**

---

## 二、T0 策略（避免和 Rights Control Ledger 打架）

| 用途 | 日期 | 说明 |
|---|---|---|
| V0.7 R 锚点 | Ledger `t0_date=2017-04-14` | 已确认 **R4**、exact claim→Samsung phones；**不改 Ledger** |
| Counterfactual 证据截止 | **2014-03-06** | Koh 法官 *Order Denying Apple’s Renewed Motion for Permanent Injunction*（11-CV-01846） |
| 信息规则 | 2014-03-06 及以前公开裁判 | 2017 再审相关事实留给 Rights Control 笔记，不塞进本 Counterfactual 结论 |

R4 在 2014 年禁令动议时已经由侵权/商业规模支撑；本笔记不重新打 R 分，只引用已有锚点。

---

## 三、Counterfactual 结构化摘要（定性，无分数）

| 字段（候选名） | 本案观察 | 证据性质 |
|---|---|---|
| `next_best_alternative` | 卷宗与专家语境承认：存在 **非侵权的边界提示 / rubberband 替代实现**（并非“有滚动就必侵 ’381”） | ≤2014-03-06 公开禁令令与相关专家声明引用 |
| `design_around_feasibility` | **相对高（对整机竞争而言）**：法院在因果关联分析中强调——若消费者购买原因与 patented feature **无关**，则即使去掉侵权特征，销售仍可能发生；并批评 survey 对 NIA 呈现不足 | Apple I/II/IV 因果关联法理 + 2014 令 |
| `performance_or_feature_loss_if_removed` | **UI 反馈层损失**（snap-back / 过边界显示）；**不是**“不能做智能手机” | 专利本身覆盖特定 touchscreen 文档滚动反馈，而非整机架构 |
| `blocking_scope` | **feature-level（弱→中）**；**product-line blocking 未获支持**（永久禁令拒绝） | eBay 四要素 + causal nexus 失败 |
| `fto_path` | 金钱赔偿路径被法院认为更合适；不把许可谈判金额写成绕开成本 | Realization Path / adequacy of damages — **不**并入 Counterfactual 金额 |

Federal Circuit 在 Apple I 中的关键表述（被 2014 令反复引用）：

> 若 patented feature **并不驱动** 产品需求，则即使没有该侵权特征，销售仍会失去——因此无法证明禁令所需的不可弥补损害因果链。

这对 Counterfactual 的翻译是：

> **功能可缺省 / 可替代的公开司法认定，与“高 realization”可以并存。**

---

## 四、与 Rights Control 的边界（本案最容易混）

2014-03-06 令 **拒绝永久禁令**。这首先是：

- **Rights Control / remedy**：operative exclusion **未**获得  
- **Realization Path**：损害赔偿仍可能是主要路径  

Counterfactual **额外**要保存的是令文与上诉法理中的 **NIA / demand-driver** 内容，例如：

1. 复杂消费电子产品含数百特征；三个 utility 特征未被证明驱动整机需求；  
2. 公开消费者调研几乎不问 rubberband 等具体专利特征；  
3. 法院明确讨论 **noninfringing alternatives** 在因果关联与 survey 设计中的位置；  
4. 公共利益权衡：不宜因有限非核心特征剥夺大量非侵权功能的产品选择。

**禁止写法：**

- ❌ “没拿到禁令 ⇒ design_around_score 高”（把 remedy 结果直接当 Counterfactual 分数）  
- ❌ “R4 较低 ⇒ 容易绕开”（R4 只说明 realization 证据阶段）  
- ❌ 把 jury damages / 9 亿美元量级数字写成绕开成本  

---

## 五、与 i4i 配对后的解释力

| 决策问题 | 只看 V0.7 R | 加上 Counterfactual |
|---|---|---|
| 两件都是“打赢过的商业软件/UI 专利”吗？ | 都是高 realization（R5 / R4） | 仍成立 |
| 竞争者能否在 **保留产品品类** 的前提下处理该功能？ | 说不清 | i4i：禁用 custom XML；Apple ’381：整机品类继续 + NIA/需求驱动未证成 |
| 该不该把“排除能力”写进同一格子？ | 容易和 R 混 | 拆成 Rights（禁令/否）+ Counterfactual（NIA/blocking_scope） |

**配对结论（预注册，不升格）：**

> **Similar R / different design-around & blocking-scope** 在公开记录上可复制。  
> 这支持 Issue #37：Counterfactual 值得独立预注册复制；**仍不**值得此时写 experimental schema。

---

## 六、与 ’915 claim 8 的一句话防混淆

同一 Apple v. Samsung 案中，’915 侧曾出现 **lost-profits / “某些机型缺乏可接受 NIA”** 的损害赔偿推理（见 Rights Control Pair 2 → R5）。

那是 **另一 claim-set** 的 Counterfactual 候选信号，**不要**自动继承给 ’381 claim 19。

Issue #37 第一对只用：

- i4i ’449（硬 feature NIA）  
- Apple ’381 c19（NIA + 低产品封锁）  

’915 可作为后续第三对照，而不是把 Pair 2 的 Rights 故事重贴标签。

---

## 七、本轮明确不做

- 不新建 formal Ledger 行（R4 锚点已存在）  
- 不写 Counterfactual schema / validator  
- 不发明 redesign 美元成本  
- 不宣布 V0.8 adoption  

Tracker：Issue #37（保持 open，直至复制门槛被显式勾选）。
