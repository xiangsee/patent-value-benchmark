# V0.8 Non-award Pressure Test — Round 1 Cross-case Synthesis

日期：2026-09-26  
状态：Round 1 complete; V0.7 remains adopted; V0.8 remains research-only

## 一、这一轮真正完成了什么

四个样本不是为了证明“哪些专利价值最高”。

它们分别用不同的失败方式压力测试V0.7：

| Archetype | V0.7能表达 | V0.7不能表达 |
|---|---|---|
| i4i v. Microsoft | R5、exact mapping、专利级金额证据 | rights control / counterfactual control |
| Amgen v. Sanofi | R4、产品映射、规模 | claim-set validity / enforceability |
| PageRank | 两个T0均R4、实施/规模 | 同一R-stage下不同value horizon |
| CRISPR-Cas9 | 单件US8697359可记录R2 | portfolio / license / jurisdiction network |

因此V0.7并没有被推翻。

更准确地说：

> **V0.7解决的是Evidence & Realization，但Patent Value还需要另外几层。**

## 二、四个预注册假说的状态

### H1 — Rights Control adds information beyond Value Realization

**Supported in first contrasting pair.**

i4i与Amgen共同说明：
- 有realized value，不代表rights control相同；
- claim mapping和产品规模不能替代validity / enforceability；
- Rights Control需要至少下沉到claim / claim-set granularity。

仍缺更多matched pairs，不adopt。

### H2 — Value is date- and context-dependent

拆成三部分：

- **H2a Date/context dependence：Supported**
- **H2b Two Clocks：Supported**
- **H2c Clean early-stage option sample：Not yet tested**

PageRank拒绝配合原假说是一个有效反证：到可靠早期T0，它已经是R4，不应硬改成R0/R1。

### H3 — Portfolio context can dominate standalone analysis

**Supported.**

CRISPR表明单件专利模型会丢失：
- portfolio membership
- competing/complementary claim sets
- license stacking
- procedural status
- jurisdiction variance

而且Portfolio Context很可能不能只是一个字段，需要独立graph object。

### H4 — Monetary outcomes are evidence, not intrinsic price

**Supported across two different mechanisms.**

- i4i：USD 200m litigation damages是dispute-specific evidence，不是永恒专利价格。
- CRISPR：USD 50m portfolio/field-license upfront payment同样不能自动分配给US8697359。

因此：

> **Patent Value ≠ Litigation Award ≠ License Consideration ≠ Product Revenue**

这些金额都是价值证据，但scope不同。

## 三、第一轮之后的V0.8候选总结构

仍然只是candidate，不是adopted schema：

```text
VALUE CONSTRUCT
├─ policy/statistical
├─ technological quality
├─ private asset value
├─ realized operating value
└─ social/strategic value

        ↓

VALUE REALIZATION
R0 → R1 → R2 → R3 → R4 → R5

        +

ATTRIBUTION / EVIDENCE
E1 / E2 / E3 / E4 / E5

        +

OBSERVABILITY
public / regulated / internal / restricted / unknown

        +

CLAIM-SET RIGHTS CONTROL
├─ scope
├─ validity
├─ enforceability
├─ remaining term
├─ design-around
└─ blocking / counterfactual dependency

        +

VALUE HORIZON
├─ realized history
├─ survival / revealed-value clock
├─ remaining-exclusivity clock
└─ option / future value

        +

PORTFOLIO & JURISDICTION NETWORK
├─ patents / applications / claim sets
├─ owners / co-owners
├─ license / sublicense chains
├─ complementary / blocking rights
├─ disputes / proceedings
├─ product / process mapping
└─ jurisdiction-specific state

SCREENING SIGNALS remain outside value facts.
```

## 四、最重要的模型治理变化

第一轮之后有五条可以先视为硬规则，而不是等待V0.8才使用：

1. **Realization Stage ≠ Value Level**
2. **Patent-level analysis ≠ Claim-set rights analysis**
3. **Portfolio value ≠ sum of single-patent values**
4. **Jurisdiction A status ≠ Jurisdiction B status**
5. **Money observed ≠ intrinsic patent price**

这些规则不需要新schema才能先约束研究。

## 五、为什么现在还不能adopt V0.8

原research agenda设置了更高的adoption threshold。

目前完成度：

- Rights Control matched pairs：**1 / 4**
- clean early-stage option retrospectives：**0 / 4**
- portfolio case：**1 / 1**
- Two Clocks case：**1 / 1**
- SEP / complex licensing external test：**尚未独立完成**

所以第一轮的正确结论是：

> **Architecture direction strengthened; adoption threshold not met.**

不能因为四个故事都很漂亮，就提前冻结schema。

## 六、下一阶段应从“继续加字段”转成“最小验证集”

下一轮研究建议拆成三包：

### Package A — Rights Control Replication

再找3组：
- realization stage接近；
- rights control显著不同；
- 技术领域尽量异质。

验证claim-set Rights Control能否跨行业重复成立。

### Package B — Early-stage Option Value

重新寻找4个真正满足：
- T0时R0/R1；
- 当时不能使用后来成功信息；
- 后来形成重大产品/标准/平台；

的历史样本。

PageRank不计入。

### Package C — Portfolio / Licensing Replication

至少再做：
- 1个SEP / patent-pool / cross-license案例；
- 1个非生命科学复杂产品案例。

检验CRISPR是否只是生物技术特殊性。

## 七、Round 1 verdict

不是“V0.8已经完成”。

而是：

> **V0.7已经证明值得保留；同时，我们已经知道它的边界具体在哪里。**

这是比增加一个总分更重要的结果。
