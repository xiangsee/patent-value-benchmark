# Patent Value Diagnostic

**Patent:** ZL99117225.6 — 用于数据处理系统的快闪电子式外存储方法及其装置
**Ledger:** `LEDGER-HOLDOUT-E4N3-ZL99117225.6`
**Mode:** public

## Current State

- **Realization Stage:** R5 — Patent-level Attributable Value
- **Evidence Levels Present:** E3, E4, E5
- **Exact Patent → Value Carrier:** confirmed
- **Patent-level Attributable Value:** confirmed

## Observability

- **enterprise:** public
- **product_project:** public
- **exact_patent_mapping:** public
- **attributable_value:** public

## Confirmed Chain

- Value Carrier: **晶天电子被控 USB 快闪外存储产品（裁判认定侵权）** (product_system; confirmed)
- `ZL99117225.6` → `VC-HOLDOUT-E4N3-JINGTIAN-USB-FLASH` — **implemented_in** (confirmed)
- `VC-HOLDOUT-E4N3-JINGTIAN-USB-FLASH` → `COURT-ENFORCEMENT-SZIPC-510` — **validated_by** (confirmed)

## Observed Metrics

- **court-awarded patent infringement damages and costs (judgment item 二)**: 7663438.43 CNY (judgment 2017-04-07; (2014)深中法知民初字第510号) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: Relative to T0=2026-10-13 the invention term expired 2019-11-14; E4 is historical damages realization, not a live royalty stream. Soft 朗科「专利授权许可收入」is pool/business-line and is demoted (not single-patent E4). (observability: `restricted`)
- **technical_comparison**: No field-normalized technical-quality benchmark beyond claim-1 infringement finding. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - Live named-ZL royalty schedule post-expiry (none expected)
  - Audited single-ZL license fee
- **TASK-02 → E5**: 建立相对现有技术的可复核比较
  - Prior-art / design-around comparison

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
