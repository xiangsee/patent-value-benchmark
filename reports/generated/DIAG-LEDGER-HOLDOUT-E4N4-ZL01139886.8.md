# Patent Value Diagnostic

**Patent:** ZL01139886.8 — 氮化钒的生产方法
**Ledger:** `LEDGER-HOLDOUT-E4N4-ZL01139886.8`
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

- Value Carrier: **渝鑫被控氮化钒生产方法及直接获得产品（裁判认定侵权）** (process; confirmed)
- `ZL01139886.8` → `VC-HOLDOUT-E4N4-YUXIN-VN-PROCESS` — **implemented_in** (confirmed)
- `VC-HOLDOUT-E4N4-YUXIN-VN-PROCESS` → `COURT-ENFORCEMENT-CDIPC-505` — **validated_by** (confirmed)

## Observed Metrics

- **court-awarded patent infringement damages and costs (all defendants)**: 29648800.5 CNY (judgment 2021-11-25; (2020)川01知民初505号) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: Relative to T0=2026-10-13 the invention expired 2021-12-04 (days after judgment); E4 is historical damages realization with discretionary contribution-rate/profit-band apportionment, not a live royalty or audited plant-level patent price. (observability: `restricted`)
- **technical_comparison**: No independent field-normalized quality score beyond infringement; defendant raised ZL201010284583.7 as alternative process narrative (defense only). (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - Plant-level profit audit tied to claim elements
  - Live named-ZL royalty (none post-expiry)
- **TASK-02 → E5**: 建立相对现有技术的可复核比较
  - Independent process benchmark / design-around study

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
