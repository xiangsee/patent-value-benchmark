# T1 短备忘：FRAND / 诉讼判赔 ≠ 自动 R5 · ≠ 公允市价（FMV）

> Status: **research theory short memo**（2026-10-14 Asia/Shanghai）  
> Track: **T1** · 承接 [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md) · 对照 [`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md)  
> 选用树：[`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md)（FRAND / 判赔节点）  
> Formal: **V0.7** + **schema 1.0** · **未** adopt / freeze V0.8  
> 本页**不是**诉讼策略、FRAND 定价意见或持证估值意见。

## 0. 一句话（正交）

| 建构 | 问的是什么 | 不问什么 |
|---|---|---|
| **诉讼损害 / 合理许可费判赔** | 在特定争议、当事人、管辖与救济规则下，法院（或和解）给出的**救济金额** | 该专利在公开市场上的公允市价；本件是否自动到达 R5 |
| **FRAND（SEP）** | 标准必要专利组合在「公平、合理、无歧视」约束下的**许可条件 / 行为边界**（法域或重行为、或重定费率） | 单件专利的内在价格；把组合费率直接写成单件 E4/R5 |
| **V0.7 E4 → R5 闸门** | 固定 **T0** 下：是否已有 **E3**（本件 claim↔载体）+ **件级可归因**经济结果（E4，常带 `scope_level=exact_patent` 指标） | 判赔或 FRAND 数字本身是否「公道」；组合许可是否该按件拆分到账本一行 |

口诀：**判赔 / FRAND = 争议或监管约束下的对价建构；R5 = 本件证据闸门过关后的实现阶。前者永不自动等于后者，也永不自动等于 FMV。**

## 1. 映射到 V0.7 闸门（E4 / R5）

```text
有公开「金额」叙事（判赔 / FRAND 费率 / 合理许可费）
        │
        ├─ 缺本件 E3（claims-check FAIL / unknown）
        │     → 可记 E5 / 笔记 /（可选）RC；**R 不升 R5**
        │
        ├─ 有 E3，但金额是组合 / 捆包 / 非 exact_patent 指标
        │     → E4 常保持 Unknown；R 常停 R2–R3（视映射）
        │
        └─ 有 E3 + 单件（或明确件级）裁判/特许指标
              → 可记 E4；**在同时满足 exact_patent 指标时可 R5**
              → 金额写入 gaps / notes 为 **争议情境**，不作内在 FMV
```

| 闸门 | 通过条件（摘要） | 失败时 |
|---|---|---|
| **E3** | 公开材料把**本件** claim 要素钉到载体 | 品牌、标准、组合热销 ≠ E3 |
| **E4** | 件级可归因经济结果（常来自单件裁判或清晰件级特许） | 组合 FRAND、多件捆许可、服务费科目 → 通常 **不是** 本件 E4 |
| **R5** | E3 + E4（及 schema 要求的 exact_patent 级指标） | **有判赔数字 ≠ 自动 R5** |

与 DEMPE 备忘一致：税务 ALP、IVS FMV、诉讼救济是**下游平行建构**；见 T2 树「交接 ≠ 替换」。

## 2. 映射到 T2 决策树

| T2 节点（主问题） | 交接层 | 回写 V0.7 时的硬停 |
|---|---|---|
| SEP / 要 FRAND 区间或行为判断 | **FRAND 层** | 未区分组合 vs 单件；把 FRAND 费率写成单件市价或自动 R5 |
| 侵权损害 / 合理许可费诉求 | **诉讼损害层** | 把判赔当资产 FMV；缺 E3 / exact_patent 却抬 R5 |
| 融资·出资·质押·要金额 | **IVS / 中评协等** | 用判赔或 FRAND 数字直接当选定价值基础的市价，而不另做价值类型声明 |

树入口：[`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md) §1–§2（`GATE2` / `GATE3`）。

## 3. Holdout 例（条件满足才 R5 —— 仍 ≠ FMV）

下列四案 **均已编码 R5**，恰恰用来说明：「能过闸」与「金额=公允市价」必须拆开。

| ID | 法域 / 机制 | 为何可 R5（闸门） | 为何仍 ≠ FMV / ≠「自动」 |
|---|---|---|---|
| **E4-N1** | CN · 思立微指纹芯片 · 单件判赔 ≈¥40.07M | 裁判确认 E3 + 件级侵权获利指标 | 酌定侵权获利 = **救济建构**；争议情境写入 gaps；不是公开市场成交价 |
| **E4-N2** | CN · 盘壳 · 单件判赔 ≈¥40M | claim 比对 E3 + 法院采用的侵权获利 | 提名「销售损失」被法院否定——编码以裁判为准；更说明金额随救济规则变，**不是**稳定 FMV |
| **INT-5** | US · PureWick · D.Del. 单件 royalty ≈$1.80M | 法院语境下本件 E3 + exact_patent 指标 | 合理许可费 / 裁判 royalty ≠ 资产挂牌市价；换管辖或比较许可集可能不同 |
| **INT-11** | JP · ReFa · 知財高裁大合議 特許２ · ≈¥4.4006亿 | 单件判赔 + E3 + exact_patent 指标 | 大合議救济逻辑服务本案当事人与争点；**不得**外推为「美容器专利全球 FMV」 |

对照合成：[`holdout-e4-n125-synthesis.md`](../../analysis/non-award-validation/holdout-e4-n125-synthesis.md) · [`holdout-int-135-synthesis.md`](../../analysis/non-award-validation/holdout-int-135-synthesis.md) · [`holdout-int-7911-synthesis.md`](../../analysis/non-award-validation/holdout-int-7911-synthesis.md)。

**反例（有金额叙事却不该自动 R5）：** E4-N5 具名许可但服务费捆 → **R2**；仅有组合 FRAND 费率、无单件 E3 → 停在 V0.7 记录争议语境，**不**升 R5（见 T2 反例 2–3）。

## 4. 防混淆对照

| 若你看到… | 错误读法 | 正确读法 |
|---|---|---|
| 「法院判了 X 元」 | 「该专利值 X = FMV；自动 R5」 | 先查 E3 + 指标是否件级；金额=救济；R5 是闸门结果 |
| 「SEP 组合 FRAND 费率 y%」 | 「组合内每件都按 y% 记 E4/R5」 | FRAND 是组合/行为建构；单件仍要 claims-check；费率 ≠ 单件内在价 |
| 「合理许可费与 IVS 收入法很像」 | 「两个数字应相等」 | 价值类型、假设、当事人约束不同；只可并列报告 |
| 「四案都是 R5，所以判赔总能抬 R」 | 「有判赔就编码 R5」 | 四案是 **闸门碰巧齐备** 的正例；缺 E3 则停 |

## 5. 最小工作流

```text
① 主问题是救济 / FRAND / 还是 FMV？→ 先走 T2 树选层
② 任何回写 Ledger 前：本件 claims-check（E3）
③ 金额来源标注建构：诉讼救济 / FRAND 组合 / IVS 选定价值基础（勿混标签）
④ 仅当 E3 + exact_patent 级 E4 指标齐备 → 才讨论 R5
⑤ 金额进 gaps/notes：争议或许可情境；声明 ≠ FMV（除非另开 IVS 工作纸且价值类型一致）
⑥ 需要组合 FRAND 行为判断 → 另纸；不要把组合结果摊进单件 R5
```

## 6. 非目标

- **不** adopt / freeze V0.8；**不**改 schema 1.0；**不**编码新 ledger。  
- **不**推荐具体 FRAND 费率、判赔公式或管辖策略。  
- **不**宣称 INT-5/11、E4-N1/N2 的金额可外推为行业基准价。

## 指针

| Doc | 角色 |
|---|---|
| [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md) | Construct / Two Clocks / RC⊥R |
| [`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md) | DEMPE ⊥ E3–E4（税务平行建构） |
| [`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md) | 何时交接 FRAND / 判赔 / IVS |
| [`t2-v07-to-ivs-oecd-practice-schools.md`](t2-v07-to-ivs-oecd-practice-schools.md) | 学派对照与来源 |
| [`evidence-levels.md`](evidence-levels.md) · [`model-v0.7.md`](model-v0.7.md) | E1–E5 / R 阶正式定义 |
| [`world-class-roadmap.md`](world-class-roadmap.md) | 四轨总览 |
