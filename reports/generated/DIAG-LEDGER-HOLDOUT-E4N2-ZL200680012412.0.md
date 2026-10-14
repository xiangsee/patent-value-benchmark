# Patent Value Diagnostic

**Patent:** ZL200680012412.0 — 盘壳
**Ledger:** `LEDGER-HOLDOUT-E4N2-ZL200680012412.0`
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

- Value Carrier: **镇江中福马被诉热磨机盘壳（BM 系列等）** (component; confirmed)
- `ZL200680012412.0` → `VC-HOLDOUT-E4N2-ZHONGFUMA-DISC-HOUSING` — **implemented_in** (confirmed)
- `VC-HOLDOUT-E4N2-ZHONGFUMA-DISC-HOUSING` → `COURT-ENFORCEMENT-SU01-1204` — **validated_by** (confirmed)

## Observed Metrics

- **court-awarded patent infringement damages and costs**: 40000000 CNY (judgment 2021-06-04; (2020)苏01民初1204号) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: Award uses discretionary per-unit infringer profit on systems that include more than the patented disc housing; plaintiff named sales contracts were held insufficient for actual-loss proof. (observability: `restricted`)
- **technical_comparison**: No separate field-normalized quality score beyond infringement. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - Component-level profit apportionment
  - Independent lost-profits proof
- **TASK-02 → E5**: 建立相对现有技术的可复核比较
  - Design-around / prior-art comparison

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
