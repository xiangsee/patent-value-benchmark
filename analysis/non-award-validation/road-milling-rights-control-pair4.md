# Rights Control Replication #4 — Wirtgen × Caterpillar road-milling machines

日期：2026-09-26  
状态：Round 2 / Package A final replication  
研究线：Track A — Patent Value Benchmark  
T0：2020-01-21

## 结论先行

Rights Control 的预注册复制门槛：

> **4 / 4 达成。**

最后一组选在大型工业机械：

- Wirtgen **US7828309 claim 29**
- Caterpillar **US7140693 claim 19**

两个竞争者在同一个road-milling / cold-planer市场交叉起诉。

两边都满足：
- exact claim → commercial machine = Confirmed
- ITC真实侵权/排除救济 = Confirmed
- commercial enforcement / scale = Confirmed
- patent-level monetary value = Unknown
- V0.7 = **R4**

但到同一T0，Rights Control方向显著分化。

## 一、Wirtgen claim 29：R4 + IPR挑战未成功

2019年PTAB在IPR2017-02185中明确记录：
- ITC认定Caterpillar PM620 machine侵犯US7828309 claim 29；
- Commission对claim 29维持“不因obviousness无效”的判断；
- PTAB最终又认定Caterpillar没有以preponderance of evidence证明claims 29–32不可专利。

同年ITC发布LEO，覆盖侵犯claim 29的road-milling machines和components。

因此：

```text
US7828309 claim 29
Realization = R4
Rights Control at T0:
  infringement = confirmed
  exclusion remedy = operative
  IPR unpatentability = not established
```

注意：同一件’309 patent中的其他claims有不同结果。

所以仍然必须claim-set化，不能写成：

> “US7828309整件专利有效。”

## 二、Caterpillar claim 19：也是R4，但出现更复杂的权利状态

另一边，Caterpillar的US7140693 claim 19也绝不是纸面专利。

CBP的HQ H308232记录：
- ITC认定Wirtgen Series 1810 milling machines侵犯claim 19；
- 2019年6月27日发布LEO；
- 2019年12月CBP还实际排除了多台Wirtgen cold milling machines。

所以它同样是：

> **R4 — Scaled Real-world Validation**

但2019年12月13日，PTAB在IPR2018-01201中作出FWD：

> 包括claim 19在内的相关claims不可专利。

如果只有一个：

`validity_status = invalid`

模型就会立刻出错。

因为到本轮T0——2020年1月21日——CBP同时记录：

- USPTO尚未发出取消claim 19的certificate；
- ITC尚未修改或撤销LEO；
- 因而LEO仍然有效。

所以真实状态是：

```text
PTAB adjudication:
  unpatentable

BUT

USPTO cancellation:
  not yet issued

AND

ITC operative remedy:
  still in force
```

这就是为什么Rights Control必须记录**程序最终性**。

## 三、最后一组把valid / invalid二元模型彻底否掉

前三组已经让我们知道：

- claim-level重要；
- as-of date重要；
- reexamination/IPR程序重要。

最后一组进一步说明：

> **同一时点，可以同时存在“不利的可专利性裁判”和“仍然有效执行的排除救济”。**

因此Rights Control不能只有：

`valid / invalid`

至少需要同时区分：

1. **adjudication outcome**
2. **forum / proceeding**
3. **finality**
4. **cancellation / legal-effect state**
5. **operative enforcement / remedy state**

这些字段不是律师式细节。

它们直接改变：
- 是否还能排除竞争产品；
- 是否还能谈许可；
- 是否需要计提/调整资产价值；
- 是否存在上诉期权；
- 是否应当投资design-around。

## 四、这组为什么通过Pair #4

预注册标准要求：

1. realization stage接近；
2. rights-control状态显著不同；
3. V0.7无法表达该差异；
4. 差异对真实决策有经济意义。

本组是：

| 维度 | Wirtgen ’309 c29 | Caterpillar ’693 c19 |
|---|---|---|
| 产业 | 道路铣刨机 | 道路铣刨机 |
| exact claim → commercial machine | Confirmed | Confirmed |
| ITC remedy | LEO | LEO |
| V0.7 | **R4** | **R4** |
| patent-level money | Unknown | Unknown |
| PTAB方向 | unpatentability **not established** | **unpatentable FWD** |
| T0执行状态 | remedy operative | **remedy still operative** |
| procedural finality issue | lower | **material** |

这不是简单“强权利 vs 弱权利”。

更准确地说：

> **Rights Control是一组状态向量，而不是一个分数。**

## 五、4/4之后该停止继续扩样

现在已经完成：

1. i4i × Amgen
2. Apple ’381 c19 × ’915 c8
3. SynQor ’702 c56 × ’021 c30
4. Wirtgen ’309 c29 × Caterpillar ’693 c19

跨越：
- 软件
- 生物医药
- 消费电子
- 电力电子
- 工业机械

而Rights Control在每轮都提供V0.7无法表达、但对经济判断有实质影响的信息。

按照预注册规则：

# H1 / Package A replication threshold reached

正确动作不是继续找第5、第6组。

下一步应该进入：

> **Claim-set Rights Control candidate schema design**

但这里只意味着：
- 可以开始设计实验Schema；
- 不等于整个V0.8 adopted；
- 不等于直接改正式Ledger Schema。

因为V0.8整体仍缺：
- 4个early-stage option retrospectives；
- SEP/patent-pool/cross-license replication。

