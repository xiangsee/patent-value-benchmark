# Patent Value Diagnostic

**Patent:** JP2014197056A — 美容器
**Ledger:** `LEDGER-HOLDOUT-INT11-JP5847904`
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

- Value Carrier: **MTG ReFa-line beauty roller (plaintiff product; court embodiment of Invention 2)** (product_system; confirmed)
- `JP5847904B2` → `VC-HOLDOUT-INT11-REFA` — **implemented_in** (confirmed)
- `VC-HOLDOUT-INT11-REFA` → `COURT-ENFORCEMENT-IPHC-31NE10003` — **validated_by** (confirmed)

## Observed Metrics

- **court-awarded Art.102(1) damages for infringement of JP5847904 (Patent 2)**: 440060000 JPY (IPHC Grand Panel judgment 2020-02-28; Heisei 31 (Ne) 10003) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: Damages are litigation-context (Art.102 presumptions, contribution/unsaleable reductions); not a market license schedule. (observability: `restricted`)
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
