# Rights Control Replication #3 — SynQor DC-DC power converters

日期：2026-09-26  
状态：Round 2 / Package A replication  
研究线：Track A — Patent Value Benchmark  
T0：2017-08-30

## 结论先行

第三组比前两组更接近“理想对照实验”。

两边是：

- 同一专利权人：SynQor
- 同一DC-DC电源转换技术家族
- 同一Intermediate Bus Architecture（IBA）技术脉络
- 同一批商业电源转换产品
- 同一场2010年陪审团侵权诉讼
- 两个claim都只有R4，没有单独可归因的专利金额

对照claims：

- **US7564702 claim 56**
- **US7272021 claim 30**

结果：

```text
Realization:
claim 56 → R4
claim 30 → R4

Rights Control at T0:
claim 56 → patentability sustained
claim 30 → obviousness rejection affirmed
```

因此：

# Pair #3 — Pass

而且这比“R5和R4倒置”更直接：

> **当Value Realization几乎被控制到相同状态时，Rights Control仍然产生material difference。**

## 一、共同的现实世界基础

2010年SynQor诉多家电源转换器厂商案件中，陪审团认定多个SynQor claims被直接或间接侵权。

其中包括：

- US7564702 **claim 56**
- US7272021 **claim 30**

法院随后记录，整个案件对多件专利、多名被告形成约：

> **USD 95.224m**

的混合损害赔偿判决，其中大部分为lost profits，其余为reasonable royalty。

但这个金额没有被可靠分配到：

- claim 56
- claim 30

所以两件Ledger都坚持：

> patent-level attributable value = Unknown

它们都停在：

> **R4 — Scaled Real-world Validation**

这是一个很重要的实验控制。

我们没有让金额证据把一边推到R5。

## 二、US7564702 claim 56：现实实施 + 再审后权利仍被维持

US7564702属于SynQor的高效DC-DC power converter技术。

2017年的Federal Circuit意见明确列明：

- claim 56属于Pressman-Kassakian prior-art combination所挑战的claims之一；
- Board此前撤销/拒绝了examiner的相关obviousness rejections；
- Federal Circuit最终**affirmed** Board的结论。

因此对claim 56，T0时可以记录：

```text
Implementation: Confirmed
Scale: Confirmed
Realization: R4
Rights Control:
  reexamination challenge survived
  patentability sustained
```

## 三、US7272021 claim 30：同样被商业实施，但再审结果相反

同一2010年侵权案件又确认：

> US7272021 claim 30进入了实际被控商业产品。

所以它在现实实现层面并不弱。

但2017年的Federal Circuit在另一份同日判决中明确处理：

> Rejection II — claims 23, 25, and 27–30

法院认为，这些电压范围限制属于普通技术人员针对具体应用环境进行的routine design choice，并明确：

> **affirmed the Board’s decision on rejection II**

因此claim 30在T0的Rights Control信号是：

```text
Implementation: Confirmed
Scale: Confirmed
Realization: R4
Rights Control:
  obviousness rejection affirmed
```

这里不需要推断。

claim 30就在法院明确列出的“27–30”范围内。

## 四、这组对照比Apple/Samsung还更干净

Apple/Samsung第二组中：

- ’381 claim 19 = R4
- ’915 claim 8 = R5

虽然已经能证明Rights Control不是R-stage函数，但两边realization仍有一点差异。

SynQor这一组把这个变量进一步压缩：

| 维度 | US7564702 claim 56 | US7272021 claim 30 |
|---|---|---|
| 权利人 | SynQor | SynQor |
| 技术领域 | DC-DC power conversion | DC-DC power conversion |
| 同一技术家族 | 是 | 是 |
| 同一侵权诉讼 | 是 | 是 |
| exact claim → commercial products | Confirmed | Confirmed |
| commercial scale | Confirmed | Confirmed |
| patent-level money attribution | Unknown | Unknown |
| V0.7 | **R4** | **R4** |
| Rights Control | **patentability sustained** | **obviousness rejection affirmed** |

所以：

> **相同R-stage并不意味着相同的专利资产控制力。**

这已经把H1从“相关性观察”推向更接近结构性独立维度。

## 五、为什么这对投资、许可和尽调是真实有意义的差别

如果企业只看：

- 已经实施；
- 有过侵权胜诉；
- 产品规模大；

那么两项claim看上去很相似。

但如果是：

### 许可谈判

claim 56与claim 30的可谈判控制位置显然不同。

### 并购/IP尽调

历史侵权记录不能替代当前可执行权利状态。

### 专利估值

不能因为两边都有商业实施，就给相同rights-control假设。

### 诉讼策略

claim 30已经有明确的不利obviousness裁判状态，不能只用历史侵权结果描述其当前地位。

所以这个维度不是“法律注释”。

它直接改变经济判断。

## 六、第三组复制带来的模型判断

现在已有：

1. i4i × Amgen
2. Apple ’381 claim 19 × ’915 claim 8
3. SynQor ’702 claim 56 × ’021 claim 30

三个样本横跨：

- 软件
- 生物医药
- 消费电子
- 电力电子/电源转换

而Rights Control仍重复提供V0.7无法表达的新增信息。

因此H1的可信度进一步上升。

但预注册门槛仍是4组。

所以当前进度：

> **Rights Control replication：3 / 4**

仍然：

> **V0.8 not adopted**

## 七、第三组还强化了一条原则

现在可以更明确地区分：

```text
Historical Realization
    ≠
Current Rights Control
```

一项claim曾经：
- 被实施；
- 被侵权；
- 参与形成损害赔偿；

并不能保证它在后续再审/无效程序后仍保留相同经济控制力。

所以未来估值时间点必须同时冻结：

- realization_as_of
- rights_control_as_of
- procedural_state_as_of

不能把不同年份的最佳事实拼成一张“超级专利画像”。

## 八、下一轮

Package A只剩最后一组。

为了做完4/4，我建议第四组不要再选诉讼高度密集的软件/电子。

优先找：

- 工业机械
- 汽车
- 能源装备
- 制造工艺

如果第四个完全不同产业仍然复制同样机制，就可以进入：

> **Rights Control 4/4 synthesis**

届时再决定Claim-set Rights Control是否达到进入V0.8候选Schema设计阶段的门槛。
