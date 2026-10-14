# Patent Value Diagnostic

**Patent:** EP07004772 — Stable pharmaceutical solution formulations for pressurised metered dose inhalers
**Ledger:** `LEDGER-HOLDOUT-INT15-EP1787639`
**Mode:** public

## Current State

- **Realization Stage:** R3 — Implemented in Value Carrier
- **Evidence Levels Present:** E2, E3
- **Exact Patent → Value Carrier:** strong_evidence
- **Patent-level Attributable Value:** unknown

## Observability

- **enterprise:** public
- **product_project:** disclosed_regulated
- **exact_patent_mapping:** disclosed_regulated
- **attributable_value:** unknown

## Confirmed Chain

- Value Carrier: **Fostair® / Formodual® (beclometasone dipropionate + formoterol fumarate dihydrate) pMDI solution** (drug_biologic; strong_evidence)
- `EP1787639B1` → `VC-HOLDOUT-INT15-FOSTAIR` — **implemented_in** (strong_evidence)

## Observed Metrics

No value metric is currently recorded.

## Unresolved Gaps

- **patent_value_attribution**: No public E4 attributing revenue specifically to this formulation patent vs sibling patents; SPC exclusivity expired before T0. (observability: `restricted`)
- **exact_patent_mapping**: Full quantitative ethanol/acid/pH recipe matching claim 11 not on SmPC. (observability: `restricted`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - Single-patent royalty/contribution analysis
- **TASK-02 → E3**: 建立 exact patent → value carrier 映射
  - Batch formula matching claim 11 bands

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
