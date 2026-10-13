# Counterfactual Control Case #4 (exploratory, non-textbook) — BYD Blade CTP CN110165116B

日期：2026-10-13  
状态：**analysis-first / research-only**；**无** Counterfactual schema；**不**计入 Issue #37 matched 门槛  
正式方法：**V0.7**；正式 schema：**1.0**；**不**采纳 V0.8  
关联：Package C [`byd-blade-cn110165116-portfolio-packagec.md`](byd-blade-cn110165116-portfolio-packagec.md) · network [`byd-blade-ctp-portfolio-network.json`](byd-blade-ctp-portfolio-network.json) · Issue #2 sibling [`contrib-ZL201910544929.3`](../../data/ledgers/contrib-ZL201910544929.3.jsonl) · CF 导读 [`docs/methodology/counterfactual-control-research-overview.md`](../../docs/methodology/counterfactual-control-research-overview.md) · P5 指针 [`docs/methodology/v0.8-probes/p5-cf-blade-nontextbook.md`](../../docs/methodology/v0.8-probes/p5-cf-blade-nontextbook.md)

---

## 0. 为何选刀片、为何不算「宁德时代案」

用户点名「刀片电池 / CATL相关」做 P5 非教科书笔记。仓库检索结果：

- **有** 比亚迪刀片 CTP 族（CN110165116B 锚点 + 115/118 兄弟 + 产品平台网络 + Package C 分析 + Issue #2 冷启动兄弟）。
- **无** 宁德时代 / CATL 诉讼、许可或 FTO 结构化材料。

因此本笔记 **只用已有刀片材料**，**不**发明 CATL 绕开成本、竞品 CTP 对照或跨公司禁令叙事。刀片材料足够支撑一条与 feature-NIA / SEP-FTO **不同构** 的 Counterfactual 观测；无需回退 CRISPR。

「非教科书」含义：无法院 NIA 意见书、无禁令四要素、无 SEP essentiality chart；公开面是产品平台叙事 + 同族互补栈 + 诚实 R0。

---

## 1. Counterfactual 问题（本案）

> 在 T0=2026-10-12，若拿掉（或禁用）**CN110165116B** 所覆盖的结构/支撑模式，  
> **（A）比亚迪刀片 CTP 产品平台是否仍可能带着 115 / 118 / 电芯层等兄弟权利商业化？**  
> **（B）外部竞争者能否在不实施本授权号的前提下继续做动力电池包 / CTP 品类？**

答案（诚实摘要）：

> **（A）公开记录无法确认 exact practiced subset → portfolio-internal NIA = Unknown；互补 claim theme 只说明「可能有兄弟替代路径」，不是替代已证明。**  
> **（B）外部竞争者绕开/封锁范围 = Unknown；不得从装车成功或「300+ 专利」叙事推出产品线级 blocking。**

---

## 2. 结构化表（定性；无分数 / 无美元）

| 字段 | 本案记录 | 证据边界 |
|---|---|---|
| `next_best_alternative` | **对「去掉 116、保留同族」**：公开记录提示 **可能的** 兄弟路径（115 体积利用率主题、118 同日结构兄弟、电芯层未在本网络穷尽），但 **未** 证明任一兄弟可替代 116 的 practiced 模式；**对外部竞争者**：无 ≤T0 公开 NIA 目录 | Package C §二「不能确认」第 3 点；network `complementary_claim_theme` / `sibling_mis_mapping_risk` |
| `design_around_feasibility` | **对保留 Blade 平台商业化且坚持 exact 116**：Unknown（无实施映射则无「绕开什么」）；**对「只用兄弟主题」**：定性上 **可能**（互补起草），**非** 已验证高可行性 | exact patent → carrier = unknown（Ledger R0） |
| `performance_or_feature_loss_if_removed` | Unknown：若 116 未被实施，去掉它可能 **零产品损失**；若它是某结构主题的唯一 practiced 件，损失未知——**禁止**写成「刀片品类死亡」 | Unknown ≠ 0；也 ≠ 高价值 |
| `blocking_scope` | **不可主张** product-line / feature-level / standard-level；最多记 **`unknown`（portfolio-internal claim-theme 候选）** | 无禁令、无 essentiality、无法院 NIA |
| `fto_path` | 无 FRAND/池式公开 FTO；缺省 **Unknown**；不发明许可金 | 与 Via LA exploratory 对照 |

一句话：

> **低 R（R0）+ 强产品叙事 ≠ 强 Counterfactual blocking；兄弟互补边属于 Network，不能自动填成 NIA 已证明。**

---

## 3. 与既有 CF 案的对照（扩展观测面，不凑 matched）

| | #1 i4i | #2 Apple ’381 | #3 Via LA SEP | **#4 Blade 116（本笔记）** |
|---|---|---|---|---|
| R（V0.7） | R5 | R4 | R2 | **R0** |
| 主机制 | 硬 feature NIA | 有 NIA + 低产品封锁 | standard-lock + 池 FTO | **portfolio-internal 替代不确定性** |
| 公开 NIA 文书 | 有（诉讼） | 有（诉讼/因果关联） | 标准交叉表 | **无** |
| blocking_scope | feature 强 | feature 弱→中 | standard | **unknown** |
| 计入 #37 matched？ | 是 | 是 | 否（exploratory） | **否（exploratory / 非教科书）** |

设计含义：Counterfactual 若过早冻字段，会默认「总有诉讼级 NIA 文书」；本案证明普通/产品栈专利上 CF 仍可做，但答案常是 **Unknown + 结构化理由**。

---

## 4. 边界：CF ≠ Network ≠ RC ≠ RP ≠ R

| 对象 | 本案放哪里 |
|---|---|
| R0 + E2 平台装车、不升 R3 | **V0.7 Ledger**（已有） |
| 115↔116 complementary、116↔118 sibling mis-map、300+ not_apportioned | **Portfolio Network**（已有 JSON） |
| 「去掉 116 后产品能否继续」 | **Counterfactual**（本笔记） |
| PP01 / 无效宣告 / 禁令 | **Rights Control**（本案无；且 RC 对普通专利永远可选） |
| 销量、许可金、池费率 | **Realization Path / monetary scope**（本案不写 redesign $） |

硬禁止：

- ❌ 发明 `design_around_cost_usd` / `blocking_score`
- ❌ 把「300+ 专利」或汉 EV 成功写成 blocking
- ❌ 把 network 的 `complementary_claim_theme` 直接标成「NIA 已确认」
- ❌ 引入仓库中不存在的 CATL 事实
- ❌ 建 `schema/experimental/counterfactual*`

---

## 5. 对决策的增量（在不改 R 的前提下）

仅看 V0.7：R0 + Unknown mapping → 「单件归因不够」。  
加上 Network：看见兄弟互补与误映射风险。  
加上本 CF 笔记：明确 **「平台成功」不能翻译成「对本授权号的强封锁」**；内部替代是否成立仍是 Unknown，且必须与 network 边分开记账。

这对冷启动贡献者的含义：P5 级普通案 **不需要** CF schema；用一页定性表即可，且大量格子合法为 Unknown。

---

## 6. 变更边界

- ✅ 本分析笔记 + 导读/探针指针  
- ❌ 不改 formal 1.0 / V0.7 scoring  
- ❌ 不建 CF schema；不 adopt V0.8；不 freeze  
- ❌ 不新增 ordinary ledger / 不扩样  
