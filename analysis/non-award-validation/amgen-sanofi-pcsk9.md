# Non-award V0.8 Pressure Test — Amgen v. Sanofi / PCSK9 genus claims

日期：2026-09-25  
状态：Round 2 experimental — not an adopted model change  
研究线：Track A — Patent Value Benchmark  
T0：2023-05-18

## 这一轮真正测试什么

i4i样本告诉我们：

> 一件专利可以已经走到R5，出现专利级损害赔偿和禁令，但Value Realization仍然不能代替Rights Control。

Amgen v. Sanofi提供了反方向的压力：

> **一组权利要求可以真实映射到商业产品、甚至曾经成立侵权，但最终仍然失去法律控制力。**

因此这轮不是研究PCSK9药物本身是否“有价值”。

研究问题是：

> **Product / implementation / scale已经存在时，专利权利要求的有效性与可执行性是否仍然构成独立的价值维度？**

## 一、事实链非常干净

### 1. 争议不是“有没有真实产品”

Federal Circuit记录，`US8829165`与`US8859741`共享说明书，公开26个抗体序列，其中包括21B12；21B12就是evolocumab，也就是Amgen上市的Repatha。

这意味着技术并不是纸面概念。

### 2. 争议也不是“有没有exact claim → product映射”

Federal Circuit同时记录，Amgen与Sanofi曾经约定：

- `US8829165` claims 19 and 29 构成侵权；
- `US8859741` claim 7 构成侵权。

因此这三个claim set拥有比普通“产品疑似使用该专利”强得多的映射证据。

### 3. 商业规模也是真实存在的

Regeneron 2022年Form 10-K披露，Praluent在美国的2022年净产品销售额为：

> **USD 130 million**

在V0.7语言里，这足以形成：
- E3 exact claim-set → value carrier
- E2 product-scale validation
- R4 scaled real-world validation

但不能形成：
- E4 patent-level attributable value
- R5

因为产品销售额不能自动归因给某一件专利，更不能在两件覆盖同一产品的专利之间重复计价。

## 二、然后发生了关键反转：Rights Control坍塌

2023年5月18日，美国最高法院一致维持下级法院结论：

- `US8829165` claims 19 and 29；
- `US8859741` claim 7；

因未满足enablement要求而无效。

争议权利要求不是针对一个特定氨基酸序列，而是试图覆盖一个按功能定义的广泛抗体属：

1. 与PCSK9特定残基/区域结合；
2. 阻断PCSK9与LDL受体结合。

Amgen公开了26个抗体实例和两类发现其他抗体的方法，但法院认为，这不足以enable其所主张的广泛功能性范围。

## 三、这暴露出V0.7一个真正的结构性缺口

把这两件专利输入现有Ledger后，会得到一个看起来完全合理的结果：

> **R4 — Scaled Real-world Validation**

因为：
- exact mapping存在；
- 商业实施存在；
- 产品销售规模存在。

但同一T0下还有另一个同样重要的事实：

> **用于建立这种广泛控制的核心claim set已经无效。**

V0.7没有字段能够同时表达这两件事。

于是出现：

```text
Value Realization: R4
        +
Exact mapping: Confirmed
        +
Product scale: Confirmed

BUT

Rights Control of relevant claims:
INVALID — lack of enablement
```

这不是V0.7“算错了”。

而是说明：

> **Realization Stage和Rights Control描述的是两个不同维度。**

## 四、比“增加validity字段”更重要的发现：Rights Control必须下沉到claim set

这一轮最重要的新发现不是：

> 给专利增加一个valid/invalid字段。

因为那仍然太粗。

最高法院判的是：
- ’165的claims 19、29；
- ’741的claim 7。

不能把这个结论粗暴写成：

> “整个US8829165都无效”
>
> “整个US8859741都无效”

同一件专利中的不同权利要求可能拥有不同的：
- 有效性；
- 范围；
- 侵权映射；
- 剩余期限；
- 可执行性；
- 绕开难度。

因此V0.8真正需要研究的不是简单的：

`Patent Rights Control`

而更可能是：

# Claim / Claim-set Rights Control

候选结构：

```text
Patent
  └─ Claim / Claim Set
       ├─ scope_type
       ├─ validity_status
       ├─ adjudication_status
       ├─ enforceability
       ├─ value_carrier_mapping
       ├─ design_around
       └─ remaining_term
```

这一点是i4i单个案例没有暴露出来的。

## 五、又出现一个portfolio层面的警告

最高法院还专门区分：

- Amgen针对Repatha具体抗体的2011 sequence-specific patent；
- Sanofi针对Praluent具体抗体的2011 patent；

与本案争议的2014 broad genus patents。

法院明确说：

> **那两件具体抗体专利不在本案争议范围内。**

因此：

> **广泛属权利要求失效 ≠ 产品失去全部专利保护。**

这也意味着，以后评估“一个产品的专利价值”时，不能只抓一件专利。

需要至少区分：
- sequence / composition protection
- genus / platform protection
- formulation
- method of treatment
- manufacturing
- device / delivery
- portfolio interaction

本轮只把它记录为Portfolio Context警告；H3仍留给预注册的CRISPR案例正式检验。

## 六、i4i × Amgen：H1现在有了真正的对照

| 机制 | i4i v. Microsoft | Amgen v. Sanofi |
|---|---|---|
| exact patent/claim → product | confirmed | confirmed |
| 现实实施 | confirmed | confirmed |
| 规模/金额证据 | USD 200m诉讼赔偿 | Praluent 2022美国销售USD 130m（产品级） |
| V0.7阶段 | R5 | R4 |
| Rights Control关键事实 | 禁令得到维持 | 核心claim set因enablement不足无效 |
| 单靠R-stage是否足够 | 否 | 否 |

因此，按Issue #5预注册的H1判定标准：

> **H1 — Rights Control adds information beyond Value Realization**

本轮可以从：

**Provisional support**

升级为：

# Supported in the first contrasting pair

但这仍然不等于：

> V0.8 adopted。

我们仍然要完成剩余预注册样本，并检验这个维度是否跨技术、跨场景稳定。

## 七、这一轮对模型的暂定结论

### 保留

1. V0.7的R0–R5继续保留。
2. Non-inheritance继续保留。
3. Product revenue不进入patent-level value。
4. E3/E4/E5与R-stage继续分层。

### 新增研究假说

**H1a — Rights Control需要claim-set granularity。**

如果只在patent level记录valid/invalid，可能产生新的错误。

### 暂不做

这一轮仍然：
- 不修改Schema；
- 不新增总分；
- 不把invalidity变成简单负分；
- 不把Repatha或Praluent销售额归给任何单一专利；
- 不把失效的三个claim推广为整件专利全部失效。

## 八、下一轮

按预注册顺序，下一例进入：

# PageRank / Stanford → Google

它要测试的是另一类问题：

> **同一件专利，在不同时间点可能从“尚未实现的option value”，变成“已实现的重大商业价值”，再变成“剩余排他期限不断缩短的成熟资产”。**

也就是H2：

**Value is date- and context-dependent.**
