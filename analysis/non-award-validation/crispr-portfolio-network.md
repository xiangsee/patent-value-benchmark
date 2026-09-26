# Non-award V0.8 Pressure Test — CRISPR-Cas9 Portfolio Dependency

日期：2026-09-26  
状态：Round 4 experimental — H3 pressure test complete; V0.8 not adopted  
研究线：Track A — Patent Value Benchmark  
T0：2026-08-05

## 结论先行

这一轮对H3的结果很清楚：

> **H3 — Portfolio context can dominate standalone-patent analysis：Supported。**

而且CRISPR样本把问题推进得比“加一个portfolio字段”更远。

真正需要表达的不是：

`Patent + Portfolio Name`

而是：

# Patent / Claim Set × Portfolio × License Chain × Jurisdiction Network

原因是同一项CRISPR-Cas9商业活动，同时受到：
- 多件专利；
- 多组相互竞争或互补的claims；
- 多个权利人；
- 多层许可与再许可；
- 美国、欧洲及其他司法辖区不同的权利状态；
- 干涉程序、异议、无效、侵权诉讼等不同法律程序

共同约束。

单件专利Ledger并没有“算错”，而是分析单位本身已经太小。

## 一、Interference 106,115本身就是一个portfolio案件

2026年3月26日PTAB Paper 2915的首页列出的不是：

> 一件Broad专利 v. 一件CVC专利

而是：
- **CVC：14件美国专利申请**
- **Broad：13件已授权美国专利 + 1件美国申请**

PTAB同时把Count 1具体锚定到：
- Broad `US8697359 claim 18`
- 或 CVC `15/981,807 claim 156`

二者都涉及能够在真核细胞中进行DNA切割/编辑的single-guide-RNA CRISPR-Cas9系统。

所以这里天然存在两个尺度：

```text
Claim-set dispute
        ↓
US8697359 claim 18
        vs.
CVC 15/981,807 claim 156

BUT the proceeding actually sits inside:

14 CVC applications
        vs.
13 Broad patents + 1 Broad application
```

只看代表性claim set，会看清“争的是什么”。

只看单件专利，却会看不清“权利网络有多大”。

## 二、2026年PTAB再次支持Broad，也没有把CVC portfolio清零

PTAB在联邦巡回法院发回后再次认定：

> CVC没有证明在Broad 2012年10月5日实际实施之前已经完成Count 1的conception。

这对争议Count的优先权非常重要。

但它不等于：

> Broad赢得“CRISPR-Cas9所有价值”。

两个原因。

第一，Editas在2026年第二季度10-Q中已经明确披露，CVC对3月26日的PTAB结果再次上诉，后续联邦巡回法院程序仍存在不确定性。

第二，UC Berkeley在决定当天披露，仍有：
- 超过60件CVC美国专利；
- 超过40件CVC非美国专利；

不受这次决定影响。

这组数字属于CVC一方的机构披露，因此我们不把它当成独立审计后的全球专利总数。

但它足以证明一件事：

> **一个interference count的胜负，不等于整个portfolio价值归零或归一。**

## 三、再往外一层，甚至不是Broad v. CVC两家

Editas 2026年Q2 10-Q披露的美国争议网络至少包括五组并行关系：

1. Broad ↔ CVC
2. Broad ↔ ToolGen
3. CVC ↔ ToolGen
4. Broad ↔ Sigma-Aldrich
5. CVC ↔ Sigma-Aldrich

而且在2026年3月Broad/CVC再次判决后：

- Broad ↔ ToolGen程序已经恢复；
- CVC ↔ ToolGen仍处暂停；
- Sigma相关程序仍存在；
- 某些Broad欧洲专利已经被撤销；
- 另一些欧洲专利以修改后的claims维持。

因此：

> **CRISPR的“权利状态”不是一个值，而是一张随时间变化的图。**

## 四、CASGEVY让这张图进入真实商业世界

如果CRISPR只有学术争议，Portfolio Context可能只是法律研究问题。

CASGEVY把它变成真实的经济问题。

Vertex在公开申报中说明，其CRISPR/CASGEVY知识产权位置同时涉及：
- CVC Group相关专利权；
- 通过Editas获得的Broad/Harvard CRISPR-Cas9非独占再许可；
- Vertex自己围绕CASGEVY的composition / manufacture / use专利及申请；
- ToolGen对CASGEVY制造相关专利提出的侵权主张。

这已经不是：

`Patent → Product`

而更接近：

```text
CVC portfolio ───────────┐
                         │
Broad/Harvard portfolio  ├──→ CASGEVY
        ↓                │
      Editas ────────────┤
                         │
Vertex own CASGEVY IP ───┤
                         │
ToolGen claims ──────────┘  (potential blocking / dispute)
```

## 五、金额证据再次说明：Portfolio Value ≠ Single Patent Value

2023年Editas与Vertex的CASGEVY相关Cas9许可公开了明确的经济条件：

- USD 50m upfront；
- potential additional USD 50m contingent upfront；
- through-2034 annual license fees；
- 其中与Broad/Harvard Cas9技术相关的收入，Editas还需要向Broad/Harvard支付mid-double-digit percentage。

到2026年第二季度，Vertex披露CASGEVY单季度产品收入：

> **USD 76.4m**

这两个数字都是真实价值证据。

但它们的正确单位分别是：

- **portfolio / field license transaction**
- **product-level realized value**

都不是：

> US8697359 = 5000万美元

或者：

> US8697359 = CASGEVY收入的某个比例

公开资料没有提供这样的apportionment。

因此这轮也把H4从“诉讼金额具有语境”扩展到了：

> **Portfolio license consideration同样具有语境。**

## 六、单件US8697359 Ledger为什么故意只停在R2

本轮专门建立了一个US8697359 standalone Ledger。

它能确认：
- 这件专利在PTAB portfolio set里；
- Editas披露该组Broad专利由其in-license；
- 因此存在真实rights transaction。

所以：

> **R2 — Rights Transaction**

但是公开资料不能确认：
- US8697359具体哪项claim被CASGEVY实施；
- 它在CASGEVY整体专利栈里的贡献比例；
- 5000万美元许可费中有多少属于这件专利；
- CASGEVY的7640万美元季度收入中有多少来自这件专利；
- 如果没有US8697359，是否必须重新许可、重新设计或者停产。

因此：
- exact patent → CASGEVY = Unknown
- patent-level attributable value = Unknown
- R3/R4/R5不得继承

结果看起来有一点反直觉：

> 一个与全球首批商业化CRISPR治疗产品处在同一许可网络里的核心基础专利，单件Ledger仍然只到R2。

但这恰恰是正确结果。

因为模型拒绝把portfolio/product事实自动分给一件专利。

## 七、问题不在Ledger，而在需要增加第二种分析单位

这轮说明未来模型至少需要两个并行对象。

### Object A — Patent / Claim-set Ledger

继续回答：
- 这件具体专利/claim控制什么？
- 有效性如何？
- exact mapping在哪里？
- 实现和归因到了哪一步？

### Object B — Portfolio & Jurisdiction Network

回答：
- 哪些专利/claims必须组合才能形成控制？
- 哪些是complementary，哪些是blocking？
- 谁许可给谁？
- 是否需要stacked licenses？
- 同一个产品在哪些国家受哪些权利约束？
- 某件专利失效以后是否有其他专利继续覆盖？
- 某一司法辖区失效以后，其他辖区是否仍然有效？

这两个对象不能互相替代。

## 八、CRISPR进一步修正了“portfolio context”的概念

原来V0.8研究议程写的是：

> standalone / complementary portfolio / blocking portfolio / cross-license / SEP / patent pool

现在看还不够。

CRISPR至少要求：

```text
PORTFOLIO & JURISDICTION NETWORK
├─ member patents / applications
├─ claim sets
├─ owners / co-owners
├─ licensees / sublicensees
├─ complementary rights
├─ blocking / competing rights
├─ interference / opposition / litigation edges
├─ jurisdiction-specific status
├─ product / process mapping
└─ time / procedural status
```

这已经不是一个普通“context field”。

它更接近一个graph object。

## 九、H3判定

Issue #5预注册标准是：

> H3 supported if standalone scoring loses material information in the CRISPR case.

现在满足。

单件US8697359 Ledger会丢失至少四类material information：

1. **Portfolio membership**  
   一场优先权程序本身涉及13件Broad专利+1申请和14件CVC申请。

2. **Competing portfolios**  
   CVC并没有因为Count 1结果而没有其他CRISPR权利；ToolGen和Sigma也在权利网络中。

3. **License stacking**  
   CASGEVY公开IP栈同时涉及CVC、Broad/Harvard/ Editas和Vertex自己的权利。

4. **Jurisdiction variance**  
   美国PTAB结果不能自动代表欧洲或其他国家；欧洲同一相关estate中已经出现撤销、修改维持等不同结果。

因此：

# H3 — Supported

## 十、这一轮仍然不修改Schema

虽然H1/H2/H3/H4现在都获得不同程度支持，但预注册的V0.8 adoption条件仍没有完成。

尤其还缺：
- 4组Rights Control matched pairs；
- 4个真正的early-stage option retrospectives；
- 更系统的portfolio/SEP外部验证。

所以：

> **V0.8 remains not adopted。**

正确动作不是马上把所有新字段塞进schema，而是先完成第一轮cross-case synthesis，再设计第二轮最小验证集。

