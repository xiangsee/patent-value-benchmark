# 第24届外部验证：Round 2 — 电力电子

日期：2026-09-24  
T0：**2022-10-31**  
模型：V0.7 Proposal（未 adopted）

## P24-POWER-001

Gold：
- ZL201410144513.X
- 《变频装置及其功率扩展方法》
- 中车株洲电力机车研究所有限公司

Silver：
- ZL201480005701.2
- 《一种MPPT集中模式退出、切换方法及其相关应用》
- 阳光电源股份有限公司

这不是完全相同的应用场景，但两者都处在电力电子变换 / 变频器控制层，申请时间接近，主体均为大型产业组织，因此适合作为 V0.7 的“证据层级继承”压力测试。

## 1. Gold：T0时能看到技术，但看不到完整价值链

Gold专利于2014-04-11申请，围绕模块化功率单元和不同功率等级组合实现变频装置功率扩展。

在本轮审阅到的 T0 前公开来源中，可以确认：
- exact patent；
- 技术结构；
- 专利已经授权。

但没有在 T0 前建立可靠的：
`Exact Patent → Named Product / Project → Scale → Attributable Value`

2023年获奖后的湖南政府材料则明确称，这项技术后来已经应用到轨道交通、工业变频、新能源发电，并参与复兴号、大兴机场等重点工程，产值上百亿元。

这些信息非常强，但**全部晚于T0**。

因此它只能作为 later ground truth：

> 事后证明这件专利确实具有巨大现实价值，但不能倒灌成“2022-10-31以前公开可观察”。

按 V0.7：
- Value State：现实中后来被证实很强；
- T0 Evidence / Observability：exact-patent商业链仍然 Unknown；
- T0 publicly defensible realization stage：R0。

## 2. Silver：公司产品规模非常大，但不能继承给具体专利

Silver专利解决光伏逆变器在不同光照条件下，如何兼顾整机转换效率与MPPT效率的问题。

到T0以前，阳光电源的现实产品规模已经非常大。

2021年年报披露：
- 光伏逆变器等电力转换设备收入约 **90.51亿元**；
- 光伏逆变器销售量 **47GW**；
- 公司已经形成很强的全球光伏逆变器市场地位。

而且在2022年9月，即国家奖T0之前，这件**具体专利**已经获得安徽省专利金奖。

但仍然缺少关键一跳：

`ZL201480005701.2 → 哪些具体逆变器产品 → 这些收入 / 性能中多少由该专利贡献`

因此不能写：

> “阳光电源逆变器卖了90亿元，所以这件Silver专利创造了90亿元价值。”

按 V0.7：
- E2：产品类别规模很强；
- E3：exact patent → product，Unknown；
- E4：patent-level attributable value，Unknown；
- exact patent 的公开 realization stage 仍只能保守停留在 R0；
- 产品类别本身则显然已经到 R4。

## 3. 这一组为什么重要

这一组同时出现两个过去非常容易犯的错误。

### 错误A：后见之明回填
Gold后来被政府材料证明有广泛应用和上百亿元产值。

但 T0 前看不到，就不能写进 T0 预测层。

### 错误B：层级自动继承
Silver公司的光伏逆变器业务已经极具规模。

但公司/产品类别的R4，不能自动继承给其中某一件专利。

所以 V0.7 的核心不是把 Gold / Silver 分出来，而是准确表达：

> **我们知道什么；这个事实属于企业、产品还是专利；以及在什么时间点能够知道。**

## 4. Round 2判断

**Public T0 evidence cannot distinguish Gold and Silver.**

但这一组对V0.7架构是强支持：

1. Value State 必须与 Observability 分开；
2. Product-level R4 不能自动继承为 Patent-level R4；
3. post-T0 ground truth 必须与 T0 evidence 分库存储；
4. Patent-level Attribution 仍然是核心缺口。

## 5. 当前第24届进度

目前累计3组：
- P24-PHARMA-001
- P24-SOFT-001
- P24-POWER-001

V0.7依然是 Proposal，不 adopted。

下一轮再寻找1–2组更强的“双方现实应用都成熟”的对照；达到4–6组后进行第一次跨届 V0.7 架构判断。
