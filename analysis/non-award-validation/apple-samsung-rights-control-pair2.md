# Rights Control Replication #2 — Apple v. Samsung touchscreen claims

日期：2026-09-26  
状态：Round 2 / Package A replication  
研究线：Track A — Patent Value Benchmark  
T0：2017-04-14

## 结论先行

这一组比 i4i × Amgen 更严格。

因为它不是跨行业对照，而是：

- 同一权利人：Apple
- 同一被控侵权人：Samsung
- 同一智能手机商业场景
- 同一轮大型侵权诉讼
- 同类触控用户界面技术

对照的是两组具体claims：

- **US7469381 claim 19**
- **US7844915 claim 8**

现实实施都很强。

但到2017-04-14，Rights Control历史明显分化。

因此Package A的第二组复制测试：

> **Pass。**

## 一、为什么这是比第一组更强的复制

第一组 i4i × Amgen 可以被质疑：

> 软件专利和生物医药专利制度环境差异太大，Rights Control差异也许只是行业差异。

Apple v. Samsung 把这种解释压缩掉了。

这两组claims都来自同一个智能手机生态。

### US7469381 claim 19

核心是bounce-back / snap-back：

用户把电子文档滚动到边缘之外后，屏幕显示超出边缘的区域；用户松手后，内容反向回到正常位置。

### US7844915 claim 8

核心是scroll or gesture：

触摸系统依据单点输入与多点输入，区分scroll和gesture，并触发相应的滚动或缩放操作。

两者都不是实验室里的纸面权利。

它们进入了真实商业手机和大型侵权诉讼。

## 二、V0.7看到的现实价值状态

### ’381 claim 19

法院记录表明：
- Apple在该专利上最终只主张claim 19；
- 后续联邦巡回法院把’381列为Samsung智能手机侵权的Apple utility patent之一；
- 案件涉及多个/大量商业Samsung smartphone models。

因此：

- exact claim → product = Confirmed
- commercial implementation = Confirmed
- scale = Confirmed
- patent-level money attribution = Unknown

所以：

> **R4 — Scaled Real-world Validation**

### ’915 claim 8

现实实现甚至更强。

2015年Federal Circuit不仅确认：
- claim 8是具体争议claim；
- certain Samsung phones infringed the ’915 patent；

还专门讨论并维持：

> 某些侵权手机不存在可接受的non-infringing alternative，因此陪审团可以给予Apple lost-profits damages。

因此：

- exact claim → product = Confirmed
- commercial implementation = Confirmed
- scale = Confirmed
- patent-specific attributable monetary evidence = Confirmed

所以：

> **R5 — Patent-level Attributable Value**

如果只看Realization：

```text
'381 claim 19 → R4
'915 claim 8  → R5
```

甚至会自然产生一个错觉：

> ’915 claim 8似乎“更强”。

但Rights Control给出相反信号。

## 三、’381 claim 19：经过两轮再审仍然存活

US7469381经历过不止一次reexamination。

2013年7月23日第二次再审证书记载：

- claims 1–13、15、16、20 cancelled；
- **claims 14、17、18、19 patentability confirmed。**

因此，至少就本研究关注的claim 19：

> **它不是因为整个专利没被挑战才“看起来稳定”，而是在再审筛选以后仍被确认。**

这是一个非常有用的Rights Control信号：

```text
Realization: R4
Rights Control:
  claim 19 survived reexamination
  patentability confirmed
```

## 四、’915 claim 8：历史实现很强，但T0时权利状态已经明显恶化

这件专利的历史更有意思。

2015年侵权诉讼中，Federal Circuit面对Samsung的anticipation攻击，维持了陪审团关于claim 8未被Nomura预见的判断。

如果研究停在这里，Rights Control看起来也很强。

但是还有另一条独立程序线：

> ex parte reexamination。

PTO examiner在再审中reject了US7844915的全部claims，PTAB维持。

Apple随后上诉Federal Circuit。

2017年4月14日，Federal Circuit：

- 对核心 `scroll or gesture` limitation 的Board construction表示同意；
- 该分析直接覆盖claim 8这样的independent claim；
- 只对另外的 `rubberbanding` limitation认定Board解释错误，并就dependent claims 2、9、16发回。

因此本研究在T0记录：

> **claim 8处于adverse reexamination adjudication state。**

注意，我这里故意不写：

> “claim 8已经最终被取消。”

因为本轮现有证据建立的是2017-04-14的再审/上诉状态，而不是另外证明一个最终reexamination certificate已经取消claim 8。

这也是Rights Control为什么需要：

- validity status
- adjudication status
- procedural state

而不是只有一个：

`valid = true/false`

## 五、最重要的反转

现在把两件claims放在一起：

| 维度 | ’381 claim 19 | ’915 claim 8 |
|---|---|---|
| 同一商业手机生态 | 是 | 是 |
| exact claim → commercial product | Confirmed | Confirmed |
| commercial scale | Confirmed | Confirmed |
| V0.7 realization | R4 | **R5** |
| patent-specific money evidence | Unknown | **Confirmed** |
| reexamination signal | **patentability confirmed** | **adverse rejection posture** |
| Rights Control方向 | stronger | materially weaker / uncertain |

这组对照非常关键，因为：

> **实现价值更高的claim，反而可能拥有更弱的当前Rights Control。**

所以：

# Rights Control不是Realization的函数

不能写成：

`R5 > R4 → rights stronger`

也不能写成：

`历史上赚过钱 → 现在权利一定更强`

## 六、这次复制进一步修正了Rights Control结构

Amgen告诉我们：

> Rights Control必须下沉到claim set。

Apple/Samsung进一步告诉我们：

> Claim-set Rights Control还必须带procedural state。

候选结构应从：

```text
Claim Set
├─ validity
└─ enforceability
```

升级为：

```text
CLAIM-SET RIGHTS CONTROL
├─ claim_set_id
├─ scope_type
├─ patentability / validity state
├─ adjudication / procedure
│   ├─ original examination
│   ├─ reexamination / IPR / PGR
│   ├─ district court
│   └─ appellate status
├─ finality
├─ enforceability
├─ remaining term
├─ design-around
└─ counterfactual control
```

因为同一个claim完全可能同时具有：

- 历史侵权判决；
- 历史损害赔偿；
- 后来的PTO adverse decision；
- 尚未完全终结的程序状态。

单一valid/invalid字段会把时间和程序压扁。

## 七、还有一个重要发现：Rights Control是时间变量

这一组与PageRank的Two Clocks其实开始接上了。

’915 claim 8：

```text
2012/2015
litigation realization ↑
damages evidence ↑

2014–2017
reexamination challenge ↑
rights-control uncertainty ↑
```

也就是说：

> **同一claim的Realized Value History可以不断增加，而当前Rights Control可以同时下降。**

这说明未来Rights Control也必须带：

`as_of_date / T0`

不能做成一个永恒属性。

## 八、Pair #2判定

Package A预注册pass condition：

1. 两个claims的realization接近；
2. Rights Control有material difference；
3. 差异不能被V0.7现有字段表达；
4. 差异对真实决策有意义。

本组满足。

因此：

> **Rights Control replication progress：2 / 4**

这比第一组支持更强，因为行业、产品环境和诉讼背景高度接近。

## 九、但仍然不改Schema

现在有两组支持：

1. i4i × Amgen
2. Apple ’381 claim 19 × Apple ’915 claim 8

但adoption threshold要求4组。

因此继续：

> **V0.8 not adopted。**

下一轮Package A还需要两组。

优先应该离开软件/UI和医药领域，找：
- 半导体 / 电子器件；
- 工业设备 / 制造；
- 或机械/汽车。

这样才能检验Claim-set Rights Control是否真的是一般机制，而不是诉讼密集型软件/医药行业特征。
