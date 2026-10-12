# P3 — Value Horizon / Two Clocks 信号词典 v0（定性）

> 状态：**V0.8 probe — research-only；NOT frozen / NOT adopted**。正式面仍为 **V0.7 + schema 1.0**。本文件不改任何 schema / validator / ledger。来源：[`../model-v0.8-design-draft.md`](../model-v0.8-design-draft.md) §7。

来源：PageRank 双 T0、Package B ×4（mRNA / OLED / LIB / GMR）。

## 两只钟（仅描述，不打分）

| 钟 | 候选取值 | 说明 |
|---|---|---|
| `realized_history_clock` | 引用 V0.7 R-stage + 证据 id | 不新造等级；R 仍是唯一实现阶段 |
| `remaining_exclusivity_clock` | `term_remaining_years`（事实）/ `expired` / `unknown` | 仅法定期限事实；不折算价值 |

## Option / future 信号类别（≤T0、可核验、定性）

| code | 含义 | Package B 例 |
|---|---|---|
| `OS-SCI` | 同行评议科学论文支撑权利要求机制 | mRNA、GMR |
| `OS-INST` | 机构 IP / 技术转移办公室持有与营销 | Jülich、UPenn |
| `OS-USE` | 说明书声称的平台/架构性用途 | LIB、OLED |
| `OS-ADJ` | 同期相邻产业需求公开存在 | OLED 显示 |
| `OS-FAM` | 多辖区同族申请（筛选信号，**非**价值） | 多数 |
| `OS-NONE` | 寻而未得 | — |

## 纪律

- 每条信号需 evidence_id 且 date ≤ T0；post-T0 成功只可作 outcome label。
- **禁止**权重、合成分、「option value = X」。
- 信号存在 **不** 抬 R（四例均 R0）。
