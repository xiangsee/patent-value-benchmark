# V0.8 probes P1–P6（索引）

> 状态：**V0.8 probe — research-only；NOT frozen / NOT adopted**。正式面仍为 **V0.7 + schema 1.0**。本文件不改任何 schema / validator / ledger。来源：[`../model-v0.8-design-draft.md`](../model-v0.8-design-draft.md) §7。

| # | 探针 | 文件 | 结论（一句） | 是否触及 freeze/adopt 门 |
|---|---|---|---|---|
| P1 | RC 最小字段升格清单 | [p1-rc-field-promotion-diff.md](p1-rc-field-promotion-diff.md) | 14 个 required 中 8 个可作「最小核」，`adjudication_events minItems=1` 是普通专利的硬阻塞 | 否（清单仅供未来 Gate 2） |
| P2 | 普通 R0 案 RC 负例 | [p2-rc-negative-ordinary-r0.md](p2-rc-negative-ordinary-r0.md) | 天地和兴 ZL202110873119.X 无任何裁决 → RC 对象**不必要且不可构造**；支持「RC 永远可选」 | 否 |
| P3 | Horizon 信号词典 v0 | [p3-horizon-signal-dictionary-v0.md](p3-horizon-signal-dictionary-v0.md) | 两钟 + 6 类定性 option 信号；无分数、无权重 | 否 |
| P4 | Network JSON 键名对齐 | [p4-network-json-naming.md](p4-network-json-naming.md) | 三例节点/边键名基本一致，但 relation 词表三套互不相通（CRISPR 用自由文本） | 否（不建 schema） |
| P5 | CF 非教科书定性笔记 | [p5-cf-blade-nontextbook.md](p5-cf-blade-nontextbook.md) · [`counterfactual-byd-blade-cn110165116.md`](../../../analysis/non-award-validation/counterfactual-byd-blade-cn110165116.md) | 刀片 CN110165116B：R0 + portfolio-internal NIA=Unknown；仓库无 CATL 故未编造；仍无 CF schema | 否 |
| P6 | 文档一致性巡检 | [p6-doc-consistency-audit.md](p6-doc-consistency-audit.md) | 横幅一致；修 1 处陈旧表述（README「通用样本扩展」已在 #47 改为暂停） | 否 |

P1/P2 后续：用户已决定「RC 对普通专利永远可选 + 允许无裁决记录」，已在 RC experimental schema/validator 实施。

P5 已用刀片 CTP（仓库无 CATL 材料，未编造、未回退 CRISPR）；全文见 analysis CF Case #4。

停止条件未触发：没有任何探针需要默认贡献填写 V0.8 字段。
