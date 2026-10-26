# Patent Value Diagnostic

**Patent:** KR20100140763A — Apparatus for virtual golf simulation providing amendment to decreasing rate of ball flight distance and method for the same
**Ledger:** `LEDGER-HOLDOUT-INT12-KR101031432`
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

- Value Carrier: **KakaoVX/SGM accused screen-golf simulators (products J/K/L)** (product_system; confirmed)
- `KR101031432B1` → `VC-HOLDOUT-INT12-ACCUSED-SGM` — **implemented_in** (confirmed)
- `VC-HOLDOUT-INT12-ACCUSED-SGM` → `COURT-ENFORCEMENT-KR-2021NA1510` — **validated_by** (confirmed)

## Observed Metrics

- **court-awarded Art.128⑦ damages for infringement of KR101031432**: 1313225245 KRW (특허법원 2021나1510 judgment 2023-04-12) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: Damages are litigation-context (Art.128⑦ discretion, 7% contribution); not a market license schedule. (observability: `restricted`)
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
