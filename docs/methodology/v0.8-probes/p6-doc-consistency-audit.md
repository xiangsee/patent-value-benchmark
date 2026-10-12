# P6 — 文档一致性巡检

> 状态：**V0.8 probe — research-only；NOT frozen / NOT adopted**。正式面仍为 **V0.7 + schema 1.0**。本文件不改任何 schema / validator / ledger。来源：[`../model-v0.8-design-draft.md`](../model-v0.8-design-draft.md) §7。

检查范围：README、roadmap、research-tracks、cold-start-status、trap checklist、schema/README、schema/experimental/README、RC/RP/CF 导读、V0.8 agenda / design draft。

| 检查 | 结果 |
|---|---|
| 「V0.7 adopted / schema 1.0 frozen」横幅 | 全部一致 |
| 「V0.8 not adopted」 | 全部一致 |
| CF「无 schema」 | README、tracks、experimental README、CF 导读一致 |
| 普通扩样暂停 | status、roadmap、tracks、README（#47 起）一致 |
| design draft 指针 | roadmap、status、tracks、agenda、README、experimental README 均有 |
| 陈旧表述 | roadmap「Package A … 下一阶段转入 Package B/C 剩余验证」为历史叙述，保留不改 |

本 PR 唯一文档行为改动：design draft §7 增加探针结果链接。无链接断裂（本地 grep 校验）。
