# 第25届样本外验证：Round 2

日期：2026-09-24  
模型：V0.6（继续冻结）  
T0：2024-02-05

## P25-COMM-001：华为 Gold vs 大唐移动 Silver

两件专利都直接面向 5G / NR 无线接口问题，并且都形成了多法域专利族。

华为专利解决 NR 与 LTE 共享载波时不同子载波映射方式可能导致的干扰；大唐专利解决 NR 上行传输中 SRS 与传输流配置带来的指示开销 / 负荷问题。

但在 T0 前公开来源中，本轮没有建立任一侧的：
- 具体专利 → 具体 3GPP 条款
- 具体专利 → 具体商用设备
- 具体专利 → 许可收入
- 具体专利 → 可归因经济价值

因此结果是：**public T0 evidence cannot distinguish the pair**。

这再次验证了“企业拥有大量 SEP”不能向下自动继承给某一件专利。

## 数据质量修正：不能再用申请号年份当专利年龄

华为 Gold 的奖项申请号是 ZL201910561574.9，表面像“2019 年申请”。

但专利文献记载：
- 申请日：2017-02-15
- 本国优先权：2017-01-26
- 分案原申请：201710082170.2

因此：

> application-number year ≠ filing date ≠ earliest priority date

此前把申请号前四位当作“专利年龄”的统计只能视为粗代理。正式数据必须优先使用真实申请日、最早优先权日，并记录分案 / PCT 来源。

这不是 V0.6 预测变量变化，而是数据治理修正。

## P25-MEDDEV-001：心脉医疗 Gold vs 迈瑞 Silver

这组技术载体并非完全一致，因此匹配质量弱于通信组；主要用于验证证据链完整度。

心脉医疗 2019 年招股书在 T0 前已经把 Gold 专利明确映射到胸主动脉覆膜支架系统的“分支支架制备技术”，同时披露 Castor：
- 2017 年获批并上市；
- 被描述为全球首款获批上市的分支型主动脉支架；
- 2018 年销售 480 个；
- 进入超过 120 家医院；
- 2018 年销售收入 2,347.89 万元。

因此公开资料形成了：

`Exact Patent → Core Technology → Approved Product → Hospitals → Units → Revenue`

迈瑞 Silver 专利在 T0 前公开资料能够确认具体专利技术内容、2022 年广东专利奖银奖，以及专利操作记录；但本轮没有建立同样明确的：

`Exact Patent → Named Commercial Product → Product Scale / Revenue`

本组在公开 T0 信息下可区分，主要差在：
- Value Carrier Centrality 的可观察证据
- Real-world Validation Depth
- Scale & Diffusion
- Evidence Traceability

仍然不能把这种公开证据差异解释成评审委员会给 Gold / Silver 的官方原因。

## Round 2 结论

1. **通信类的 Observability Ceiling 很高。**
2. **最有用的公开证据不是“公司很强”，而是 exact patent → value carrier 的连接。**
3. **产品收入仍然不能自动成为 E4 专利级价值归因。**
4. **专利年龄统计必须改用真实申请日 / 最早优先权日，不能使用申请号年份替代。**
5. V0.6 继续冻结。
