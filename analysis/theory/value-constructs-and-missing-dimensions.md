# From “High-Value Patent” to Patent Value Constructs

日期：2026-09-24  
状态：Research synthesis — V0.7 remains adopted; V0.8 not adopted

## Executive conclusion

“高价值专利”不是一个单一、稳定、自然存在的变量。

至少需要区分五种不同的 value construct：

1. **Policy / Statistical Value** — 政策统计意义上的“高价值”
2. **Technological Quality** — 技术影响、质量与重要性
3. **Private Rights / Asset Value** — 专利权作为排他性资产的私人价值
4. **Realized Operating Value** — 产品、工艺、许可、市场中的现实价值
5. **Social / Strategic Value** — 公共健康、产业链安全、基础设施等外部价值

如果不先说明研究的 value construct，任何“专利价值评分”都可能把不同对象混成一个分数。

---

## 1. 中国“高价值发明专利”首先是政策统计口径

“十四五”规划把满足任一条件的有效发明专利纳入统计：

- 战略性新兴产业
- 海外同族专利权
- 维持年限超过10年
- 较高质押融资金额
- 国家科技奖或中国专利奖

到2026年“十五五”相关解读中，国家知识产权局当前列出的统计口径变为四类：

- 战略性新兴产业
- 海外同族
- 维持超过10年
- 国家科技奖或中国专利奖

高额质押融资不再出现在这份四类说明中。

### 研究含义

这说明：

> **Policy High Value 是治理和统计构造，不是专利的“内在经济价值”定义。**

它有明确政策目的：
- 引导战略产业
- 鼓励国际布局
- 鼓励长期维持
- 奖励标志性成果

因此本项目以后必须把：

`policy_high_value`

与：

`economic/private/realized value`

彻底分开。

---

## 2. OECD / 经典文献研究的是“质量/价值代理指标”

OECD的实验性Patent Quality Index使用：

- forward citations
- patent family size
- number of claims
- generality
- backward citations
- grant lag

而且按照年份和技术领域进行归一化。

Lanjouw & Schankerman则把：

- claims
- forward citations
- backward citations
- family size

看作一个潜在“quality”变量的多个噪声代理，并验证其与后续renewal、litigation有关。

### 研究含义

这些指标非常适合：

> **Public Screening**

但不等价于：

> **Patent-level Attributable Value**

例如：
- 被引很多，可能说明技术影响力大；
- 家族很大，可能说明申请人愿意支付全球布局成本；
- claims很多，可能与保护结构有关；

但这些都不能直接证明：

> “这件专利为某产品创造了5000万元利润。”

因此V0.8不应该把bibliometric/administrative indicators塞进R0–R5作为价值事实。

更合适的位置是：

# Screening Signals

它们是候选专利筛选信号，不是价值证明本身。

---

## 3. “专利权资产价值”与“技术/产品价值”也不是一回事

Harhoff、Scherer、Vopel特别区分：

- renewal protection value
- patent-right asset value

他们的asset value包含战略性和blocking power。

关键反事实是：

> 如果把这项专利权卖给竞争对手，原权利人可能失去什么？

对于覆盖关键产品/工艺特征的宽专利，竞争对手获得专利后可能：
- 阻止原企业继续实施；
- 迫使其支付许可费；
- 迫使其承担invent-around成本；
- 威胁产品所产生的quasi-rents。

这与我们现在的 **Value Carrier Centrality** 接近，但并不相同。

### 一个重要区别

一项专利可能：

**在当前产品中很核心，但非常容易绕开。**

另一项专利可能：

**自己没有直接产生销售额，但具有很强blocking / bargaining power。**

因此：

`Product Centrality ≠ Rights Control Power`

---

## 4. WIPO提醒我们：IP价值的根来自Exclusivity和Future Benefits

WIPO目前的IP valuation框架强调：

- 排除竞争者的权利
- 可测量的经济利益
- 与其他资产协同增值
- 未来经济利益
- 产品内直接实施
- 销售/许可
- 建立进入壁垒
- 降低替代威胁

同时估值需要考虑：
- legal status
- ownership
- claims
- remaining useful lifetime
- family / geography
- litigation
- commercialization impediments

### V0.7的缺项

V0.7目前擅长描述：

> **价值已经走到哪里，证据在哪里。**

但对“权利本身控制了什么”描述还不够。

---

# 5. V0.7缺失的四个候选维度

## A. Rights Control State

建议研究一套独立的“权利控制状态”：

- legal status / enforceability
- ownership clarity
- encumbrances
- claim scope
- validity resilience
- jurisdiction coverage
- remaining term

这不是E5。

E5是证据独立核验属性。

Rights Control是专利资产本身的法律控制能力。

---

## B. Counterfactual Dependency / Design-around Cost

提出一个新的候选问题：

> **如果权利人失去这件专利，或者竞争者获得这件专利，现实价值链会发生什么？**

可研究：

- 产品是否必须重新设计？
- 是否存在next-best alternative？
- 绕开成本多少？
- 需要多长时间？
- 会失去什么性能？
- 是否会失去Freedom to Operate？
- 是否具有blocking power？

暂定名称：

# Counterfactual Control

它比“产品中心度”更接近专利权资产价值。

---

## C. Value Horizon / Option Value

Pakes、Schankerman的renewal研究把专利看成带不确定性的未来收益权/期权。

这揭示V0.7的一个潜在偏差：

> R0可能只是“尚未实现”，不等于“价值低”。

年轻的前沿技术专利可能：
- 当前没有产品收入；
- 但拥有很大的未来商业选择权。

因此需要区别：

- **Realized Value**
- **Option / Future Value**

---

## D. Portfolio Context

单件专利的价值可能高度依赖于：

- 技术相关专利组合
- patent fence
- cross-license
- SEP portfolio
- 标准组合
- Freedom to Operate

WIPO在SEP语境中明确指出，许可谈判通常围绕跨多个国家的众多SEP，而不是某一件单一国家专利。

因此必须有：

`standalone patent context`

和：

`portfolio-dependent value`

之分。

---

# 6. 一个非常重要的“年龄悖论”

这是本轮最值得保留的发现之一。

中国政策统计中：

> **维持年限超过10年**

被作为高价值发明专利的一类。

这背后的逻辑是：

> 权利人长期愿意支付维护成本，是revealed value的信号。

但WIPO技术转移估值指南又指出：

> 剩余有效期越长，一般越有利于未来交易价值；只有1年剩余期的专利通常不如还有10年保护期的专利。

于是同一个“年龄”出现两个方向完全不同的含义。

## Patent Age必须拆成“两只钟”

### Survival / Revealed-value Clock

年龄越长且持续维持：

> 对过去价值和权利人持续付费意愿的证据越强。

### Remaining-exclusivity Clock

年龄越长：

> 剩余排他期越短，未来可捕获现金流窗口可能越小。

因此以后绝不能出现：

`older patent = higher value`

或：

`younger patent = higher value`

这种单向规则。

---

# 7. Patent Value ≠ Patent Price

WIPO强调Price和Value应区分。

同一专利对不同主体的价值可能不同，因为：

- 产品组合不同
- 市场位置不同
- 是否拥有互补know-how不同
- 是否需要Freedom to Operate不同
- 是否能实现协同不同

因此：

> **Patent value is actor- and context-dependent.**

未来如果做货币估值，Ledger必须记录：

- valuation purpose
- valuation date
- valuation subject
- assumed owner/user
- market context

不能存在脱离主体和目的的“永恒专利价格”。

---

# 8. 对V0.7的判断

V0.7不需要推翻。

它解决的是：

> **State + Evidence + Observability + Realization**

这些仍然成立。

但它还不是完整的Patent Value Model。

更准确地说：

> **V0.7是Patent Value Evidence & Realization Architecture。**

它回答：
- 价值走到了哪里？
- 我们能证明到哪里？
- 哪些证据看得到？
- 哪些不能归因？

下一步研究需要补：

- Value Construct
- Rights Control
- Future / Option Value
- Portfolio Context

---

# 9. 一个新的总结构候选

暂不作为V0.8正式模型，仅作为研究假说：

```text
                      VALUE CONSTRUCT
          ┌──────────────┼──────────────┐
   Technological     Private Asset    Social/Strategic
      Quality            Value             Value
          │                │                 │
          └──────────────┬─┴─────────────────┘
                         │
                  RIGHTS CONTROL
            scope / validity / term /
            geography / blocking power
                         │
                 VALUE REALIZATION
                 R0 → R1 → ... → R5
                         │
                 ATTRIBUTION / EVIDENCE
                    E1 / E2 / E3 / E4
                         │
                    OBSERVABILITY
          public / regulated / internal / restricted
                         │
                     HORIZON
                realized / option value

                 + PORTFOLIO CONTEXT
```

## Screening Signals位于体系之外

例如：
- citations
- family size
- claims
- renewal age
- generality
- grant lag
- litigation/opposition

它们首先是：

> **signals / proxies**

不能未经进一步证据直接变成：

> value facts。

---

# 10. 下一轮研究假说

V0.8暂不adopt。

下一步优先验证四个假说：

### H1 — Rights Control
在R4程度相近的专利中，权利范围/稳定性/绕开难度是否显著解释私人资产价值差异？

### H2 — Two Clocks
长年维持是否提高revealed-value证据，但同时降低remaining-exclusivity future value？

### H3 — Portfolio Dependency
通信、半导体等复杂行业中，单专利价值是否必须在portfolio / cross-license语境下评价？

### H4 — Screening vs Proof
citations/family/claims等public signals能否提高高价值候选的Recall，但不能替代E3/E4？

只有这些假说经过样本验证，才讨论V0.8。
