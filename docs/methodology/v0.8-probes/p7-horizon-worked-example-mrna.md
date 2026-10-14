# P7 — Value Horizon 信号 worked example（mRNA / US8278036 @ T0=2012-10-02）

> 状态：**V0.8 probe — research-only；NOT frozen / NOT adopted**。正式面仍为 **V0.7 + schema 1.0**。  
> 本文件 **不**改 schema / validator / ledger。  
> 词典：[`p3-horizon-signal-dictionary-v0.md`](p3-horizon-signal-dictionary-v0.md)  
> 案例源：[`../../../analysis/non-award-validation/mrna-us8278036-early-option-packageb.md`](../../../analysis/non-award-validation/mrna-us8278036-early-option-packageb.md) · Ledger `LEDGER-NA-MRNA-US8278036-T0-2012`

来源：设计草案 [`../model-v0.8-design-draft.md`](../model-v0.8-design-draft.md) §3.2C / §5 **S2 预备**（本探针 ≠ 批准 S2）。

---

## 1. Purpose

把 P3 定性词典 **套到一件已有 Package B 样本**，示范：

> 在 formal **R0** 时，如何用两只钟 + option 信号描述「决策相关的未来视界」，而不抬 R、不发明分数。

非目标：不新建 Horizon schema；不回填 COVID 成功；不改 mRNA ledger。

---

## 2. Two clocks（仅描述）

| 钟 | P3 字段 | 本例取值（T0=2012-10-02） | 依据 |
|---|---|---|---|
| 已实现历史钟 | `realized_history_clock` | **R0** + evidence refs on origin/mechanism（非新等级） | Ledger `realization_stage=R0`；无 E3 上市映射 |
| 剩余排他钟 | `remaining_exclusivity_clock` | `term_remaining_years` ≈ **~15+**（从 2012 授权日起算至届满；精确日待年费/期限表复核时可标 `unknown` 细位） / 非 `expired` | 授权日 2012-10-02；T0 时权利有效（公开专利记录） |

纪律：剩余年限是 **法定期限事实**，不折算美元 option。

---

## 3. Option / future 信号（P3 codes ≤ T0）

| code | 本例？ | 可核验锚（≤T0） | 不解读成 |
|---|---|---|---|
| **OS-SCI** | **是** | Immunity 2005 TLR 抑制；Mol Therapy 2008 翻译↑/免疫原性↓（`E-MRNA-036-MECH-TLR-2005` / `E-MRNA-036-OPTION-SIGNAL-2008`） | 已上市产品 |
| **OS-INST** | **是** | Penn 持有；NIH 资助与政府权利保留（`E-MRNA-036-ORIGIN-PENN-NIH`） | 大学持有 ⇒ R3 |
| **OS-USE** | **是** | 授权文本 / 说明书层治疗蛋白递送与 vaccination 用途（`E-MRNA-036-CLAIMED-USES-GRANT`） | 用途声称 = E3 映射 |
| **OS-ADJ** | 弱/未单列 | 2012 前 RNA 治疗叙事存在，但本 ledger 未另建独立产业需求证据行 → 宁标未用 | 编造相邻市场热度 |
| **OS-FAM** | 可记筛选 | PCT/同族存在（family_note）— **筛选信号，非价值** | family size ⇒ 价值 |
| **OS-NONE** | 否 | — | — |

汇总（定性，无权重）：

```text
horizon_annotation_v0 (research-only):
  realized_history_clock: R0
  remaining_exclusivity_clock: term_remaining (non-expired at T0)
  option_signals_present: [OS-SCI, OS-INST, OS-USE] (+ OS-FAM as screening-only)
  option_signals_absent_or_unused: [OS-ADJ]
  forbids: score, weights, "option_value_usd", R-stage uplift
```

---

## 4. 与 V0.7 的边界（本例证明）

| 问题 | 答案 |
|---|---|
| Horizon 注解能否代替 R？ | **否** — R0 不变 |
| 信号能否继承为 E3/E4？ | **否** — exact mapping / attributable value 仍 Unknown |
| Post-T0 COVID 疫苗成功？ | **仅** outcome label；禁止回填本 T0 注解抬升 |
| 是否需要新 schema？ | **本探针不需要**；S2 若将来批准，再谈 Diagnostic 只读注 vs 并行对象（Q-C1） |

---

## 5. 对 S2 的启示（仍未批准）

1. **最小注解形状**可先是：两钟引用 + `option_signals[]` 枚举 + evidence_ids — 与 P3 一致。  
2. Worked example 可复核：**每条信号都有 ≤T0 evidence_id**。  
3. 普通冷启动 **永远不要求**填 Horizon（与 RC 可选同构）。  
4. 下一步若继续 T3：可再做一件「OS-NONE 主导」负例，或 PageRank 双 T0 的两钟对照 worked example — **仍**不要 adopt。

---

## 6. 停止条件

- 未引入分数/权重/美元 option。  
- 未改 formal ledger / schema 1.0。  
- 未宣称 V0.8 adopt 或 S2 启动。
