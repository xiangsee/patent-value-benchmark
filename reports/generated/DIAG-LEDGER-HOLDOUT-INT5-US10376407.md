# Patent Value Diagnostic

**Patent:** US15/238,427 — Using wicking material to collect urine from a male for transport
**Ledger:** `LEDGER-HOLDOUT-INT5-US10376407`
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

- Value Carrier: **Sage PrimoFit (accused male external urine collection device)** (medical_device; confirmed)
- `US10376407B2` → `VC-HOLDOUT-INT5-PRIMOFIT` — **implemented_in** (confirmed)
- `VC-HOLDOUT-INT5-PRIMOFIT` → `COURT-ENFORCEMENT-DDEL-19-1508` — **validated_by** (confirmed)

## Observed Metrics

- **court-awarded reasonable royalty for infringement of US10376407**: 1799193 USD (final judgment 2023-10-27; D.Del. 1:19-cv-01508) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: Royalty is litigation-context; ongoing rate may change; not a market license schedule. (observability: `restricted`)
- **technical_comparison**: No field-normalized quality score beyond infringement. (observability: `public`)

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
