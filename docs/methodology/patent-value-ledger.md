# Patent Value Ledger 1.0 Draft

Patent Value Ledger（专利价值账本）把 V0.7 从研究架构变成可以实际填写、审阅和持续更新的数据对象。

## 一张账本回答六个问题

1. **Knowledge Origin** — 这项技术从哪里来？
2. **Technology** — 它解决了什么问题，机制是什么，相对现有技术推进了多少？
3. **Patent** — 哪一件权利保护了什么？
4. **Value Carrier** — 它进入了什么产品、工艺、平台、药物、设备或工程？
5. **Real-world Validation** — 真实世界里是否已经使用、规模化、产生结果？
6. **Attributable Value** — 有多少性能、成本、收入或社会价值能够被归因到 exact patent？

## 核心链

```text
Knowledge
  → Technology
  → Patent
  → Value Carrier
  → Real-world Validation
  → Attributable Value
```

任何箭头都不得靠“企业很强”“产品卖得很多”自动补齐。

## Ledger 与 V0.7

每个 Ledger 必须包含四层状态：

- Value State
- Attribution / Evidence State
- Observability State
- Value Realization Stage (R0–R5)

### 重要规则

**企业价值不能自动继承给产品，产品价值不能自动继承给专利。**

例如：

```text
企业收入 100 亿
≠ 某产品价值 100 亿
≠ 某件专利价值 100 亿
```

要把产品价值进一步归因到 exact patent，需要 E3 / E4 证据。

## value_metrics 的作用

每个数值都必须标记 scope_level：

- `enterprise`
- `product_project`
- `exact_patent`

并单独标记 attribution_status。

这样“产品销售额30亿元”可以被安全记录，而不会被数据库误认为“该专利价值30亿元”。

## Public 与 Internal

### Public Ledger
只能写入可公开再利用、可以提供 source_id 的信息。

### Internal Ledger
企业内部可以进一步加入：
- 产品BOM/技术映射
- 技术评审
- 客户证明
- 合同
- 专项审计
- 成本/良率/性能贡献
- 许可和交易材料

Internal Ledger 不应未经授权进入公开仓库。

## 输出应该是什么

Ledger 的默认输出是：

- 当前价值实现阶段
- 已确认的专利→价值载体链
- 已确认的现实验证
- 证据等级
- Observability
- Evidence Gaps / Attribution Gaps

默认**不输出**：
- Gold概率
- 专利价值“拍脑袋金额”
- 无证据的排行榜
- 把 Unknown 当0的评分


## Evidence Levels are non-ordinal

E1–E5可以并存，不使用“最高证据等级”的表达。

例如：
- E2：产品已经产生销售
- E3：exact patent 已明确映射到产品
- E5：许可备案或监管文件提供独立核验

这三种证据回答不同问题，不能简单写成 E5 > E3 > E2。

Ledger 使用：
`evidence_levels_present`

## Realization Stage Evidence

R1–R5必须填写 `realization_stage_evidence_ids`。

原因是：
> “阶段”本身也必须是可追溯的事实判断。

例如R2必须能指向许可、转让或质押证据；不能只由研究者手工选择R2。
