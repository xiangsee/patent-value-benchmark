# Patent Value Diagnostic

**Patent:** EP02767896 — Ceric oxide and method for production thereof, and catalyst for exhaust gas clarification
**Ledger:** `LEDGER-HOLDOUT-INT18-EP1435338`
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

- Value Carrier: **Rhodia HSA20 high-surface-area ceria (plaintiff) / Neo C100N (accused)** (product_system; confirmed)
- `EP1435338B1` → `VC-HOLDOUT-INT18-HSA20` — **implemented_in** (confirmed)
- `VC-HOLDOUT-INT18-HSA20` → `COURT-ENFORCEMENT-EWHC-ANAN-NEO` — **validated_by** (confirmed)

## Observed Metrics

- **settled UK Head 1 damages for infringement of EP(UK)1435338**: 85000 GBP (settlement late 2020; recorded in [2022] EWHC 708 (Pat)) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: E4 is a small UK-head settlement (face value of goods); overseas heads dismissed — teaches territoriality. Not a market license schedule or FMV. (observability: `restricted`)
- **technical_comparison**: No field-normalized quality score beyond infringement finding. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - Arms-length license comps
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
