# P2 — 负例：普通 R0 专利不需要 RC 对象

> 状态：**V0.8 probe — research-only；NOT frozen / NOT adopted**。正式面仍为 **V0.7 + schema 1.0**。本文件不改任何 schema / validator / ledger。来源：[`../model-v0.8-design-draft.md`](../model-v0.8-design-draft.md) §7。

样本（**已有**，不新建 ledger）：`data/ledgers/contrib-ZL202110873119.X.jsonl`（天地和兴，`software_algorithm`，R0，E2 only）。

## 检查

| 问题 | 结果 |
|---|---|
| 有无无效/复审/诉讼/ITC 裁决？ | 公开记录中无 |
| 能否按 experimental-0.1 构造 RC 记录？ | **不能**：`adjudication_events` minItems=1、`finality_state.status` 无 `not_applicable` |
| RC 若可构造，会增加决策信息吗？ | 否：唯一法律语境是 PP01 保全，陷阱清单 E 已规定 PP01 ≠ R/RC |
| 贡献摩擦 | 若强制填写，冷启动者需编造空裁决 → 违反 Unknown≠0 精神 |

## 结论

- 支持 Q-B2：**RC 对未经裁决的普通专利应永远可选、默认不填**。
- Gate 3 第一项（「普通型专利上 RC 不增摩擦」）在「可选」前提下成立；在「必填」前提下**不成立**。
- 是否允许「无裁决 RC 记录」（P1 minItems 0）是范围决策，留给用户。

## 后续（2026-10-12 用户决定，已实施）

RC 对普通专利永远可选；无裁决记录被允许。测试用内存 fixture（基于本 ledger）验证通过，**未**新增数据文件或 ledger。
