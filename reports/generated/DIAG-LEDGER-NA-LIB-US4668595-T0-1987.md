# Patent Value Diagnostic

**Patent:** US06/861,423 — Secondary battery
**Ledger:** `LEDGER-NA-LIB-US4668595-T0-1987`
**Mode:** public

## Current State

- **Realization Stage:** R0 — Right Exists
- **Evidence Levels Present:** E5
- **Exact Patent → Value Carrier:** unknown
- **Patent-level Attributable Value:** unknown

## Observability

- **enterprise:** public
- **product_project:** unknown
- **exact_patent_mapping:** unknown
- **attributable_value:** unknown

## Confirmed Chain

No non-Unknown patent-to-value-carrier chain is currently established.

## Observed Metrics

No value metric is currently recorded.

## Unresolved Gaps

- **exact_patent_mapping**: At T0=1987-05-26 there is no confirmed exact-patent → marketed Li-ion consumer / EV battery carrier link in this ledger. Lab/prototype cell performance and claimed secondary-battery uses are not implemented as a public commercial carrier here. (observability: `unknown`)
- **patent_value_attribution**: No public T0 evidence attributes royalty, incremental battery revenue, or cost/performance economics to this exact patent. (observability: `restricted`)
- **other**: V0.7 can record R0 plus electrochemical / materials differentiation, but has no structured field for early option/future-value horizon that is decision-relevant precisely when realization is still R0/R1. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E3**: 建立 exact patent → value carrier 映射
  - product disclosure naming US4668595
  - license / supply schedule tying this grant to a marketed battery
  - BOM / cell implementation mapping
- **TASK-02 → E4**: 建立专利级性能、成本或经济价值归因
  - single-patent or claim-family royalty economics
  - apportionment analysis
  - audited attributable-value disclosure
- **TASK-03 → unknown**: 补齐Ledger列明的证据缺口
  - value-horizon / option-value state
  - remaining-exclusivity clock
  - explicit separation of option signals from realized R-stage

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.
- Historical diagnostic is frozen at T0=1987-05-26; post-T0 information must not be backfilled.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
