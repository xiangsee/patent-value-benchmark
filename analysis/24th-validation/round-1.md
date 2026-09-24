# 第24届外部验证：Round 1 — V0.7 Proposal

日期：2026-09-24  
第24届 T0：**2022-10-31**  
模型：**V0.7 Proposal（尚未 adopted）**

## 0. 研究纪律

第25届已经封存为 V0.7 架构的提出依据。

本轮开始：
- 不回头修改第25届 matched-pair 结果；
- 第24届作为新的跨届次验证集；
- 2022-10-31 之后的信息只能用于 award label 或 post-T0 ground-truth check；
- 不进入 T0 预测 / 诊断变量；
- 不做 Gold probability，也不做100分评分。

第24届最终名单为29项Gold、60项Silver。最终名单本身是 outcome label，不参与 T0 evidence。

## 1. P24-PHARMA-001：创新药

Gold：
- ZL201580045311.2
- 《EGFR抑制剂及其制备和应用》
- 豪森药业

Silver：
- ZL201310245354.8
- 《一类五元杂环并吡啶类化合物及其制备方法和用途》
- 上海药物所 / 海和药物

### Gold侧：产品成熟，但T0时专利映射公开度未必高

Gold专利本身在T0前已经公开、授权，涉及针对L858R、T790M和外显子19缺失等EGFR突变的抑制剂。

T0之前，豪森的阿美替尼已经：
- 2020年获批上市；
- 纳入医保；
- 2021年披露一线III期研究结果；
- 2021年一线适应症获批。

因此**产品 / 监管 / 临床层面的 Value State 很成熟**。

但是，在本轮已审阅的T0前公开来源中，没有找到像海和那样明确写出：

`ZL201580045311.2 → 阿美替尼`

的受监管文件。

2023年获奖后的豪森材料明确确认这件专利就是阿美替尼专利，但该材料晚于T0，只能作为 later ground truth，不能回填T0预测变量。

这正是 V0.7 Observability State 要解决的问题：

> 实际价值可能已经成熟，但 exact patent attribution 在公开层仍然不完整。

### Silver侧：专利映射更清楚，但产品还没上市

海和一侧非常有意思。

2021年的上交所披露法律文件已经明确把：
- 专利申请 201310245354.8 / CN104230922
- SCC244项目

直接连接起来，并说明海和负责该项目的临床开发、注册与商业化。

到T0之前：
- SCC244 / 谷美替尼已经完成关键II期研究；
- 2022年2月NDA获受理；
- 获优先审评；
- 但直到T0仍未正式获批上市。

所以Silver侧表现为：

`Exact Patent → Drug Candidate → Clinical / NDA`

映射非常可观察；

但 Value Realization Stage 仍低于已经上市的成熟药物。

### 第一项跨届次验证结果

这组不是简单支持“Gold比Silver证据更多”。

恰恰相反：

> **Silver 的 E3 / exact-patent traceability 在T0公开层反而更清楚；Gold 的产品现实成熟度更高。**

这说明 V0.7 把：
- Value State
- Attribution / Evidence State
- Observability State
- Realization Stage

拆开的方向，比把所有东西压成一个“Evidence Score”更合理。

本组**不用于声称为什么评审给Gold/Silver**。

## 2. P24-SOFT-001：软件基础设施

Gold：
- ZL201511034171.7
- 阿里云《一种分布式存储系统升级方法和装置》

Silver：
- ZL201510104674.0
- 中国联通《大数据分析挖掘管理面与业务面的关联方法及系统》

两件专利都属于大型平台 / 网络运营商的后台基础设施方法。

Gold解决：
- 分布式存储节点滚动升级；
- 在不中断上层服务的情况下完成升级；
- 降低数据丢失风险。

Silver解决：
- 大数据分析平台管理面与业务面关联；
- 数据需求方权限与结果输出安全；
- 支撑自动化数据服务。

但在T0前本轮公开来源中，两边都没有建立可靠的：

`Exact Patent → Named Product / Platform → Deployment Scale → Attributable Value`

因此按V0.7：

- 两边都不能写“价值低”；
- 两边只能写“公开观测到R0，R1–R5 Unknown”；
- Observability State 本身成为研究结果。

这与第25届通信、数据库、AI算法样本出现的结构一致。

## 3. Round 1 初步判断

V0.7 Proposal 的第一轮跨届测试**没有出现立即反例**，但远不足以 adopted。

目前出现两个积极信号：

1. **Value 与 Observability 分离是必要的。**  
   P24-PHARMA-001 里，Silver公开映射更完整，而Gold现实产品成熟度更高。

2. **Realization Stage 可以减少“产业化”这个模糊词。**  
   Silver药物到T0已是临床/NDA阶段，不能说“未转化”；但它与已经上市、医保、临床使用的产品也显然不是同一阶段。

软件组则再次证明：
- Unknown不是0；
- 公开不可见本身必须被编码。

## 4. 下一轮

继续第24届，但不急着铺样本。

优先增加：
- 电力电子：中车变频Gold vs 阳光电源MPPT Silver；
- 再寻找一组“双方都已规模应用、但证据制度不同”的强对照。

达到4–6组以后，再判断V0.7架构是否需要修订。
