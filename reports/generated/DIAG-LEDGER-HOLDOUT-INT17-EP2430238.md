# Patent Value Diagnostic

**Patent:** EP10721044 — Trackbed liner and related methods
**Ledger:** `LEDGER-HOLDOUT-INT17-EP2430238`
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

- Value Carrier: **Geofabrics Tracktex trackbed liner (plaintiff commercial embodiment)** (product_system; confirmed)
- `EP2430238B1` → `VC-HOLDOUT-INT17-TRACKTEX` — **implemented_in** (confirmed)
- `VC-HOLDOUT-INT17-TRACKTEX` → `COURT-ENFORCEMENT-EWHC-HP2018-000003` — **validated_by** (confirmed)

## Observed Metrics

- **court damages inquiry quantum for infringement of EP(UK)2430238**: 13400000 GBP (EWHC damages inquiry 2022-09-27; HP-2018-000003) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: Damages are litigation-context (counterfactual lost profits, price depression); not a market license schedule or FMV. (observability: `restricted`)
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
