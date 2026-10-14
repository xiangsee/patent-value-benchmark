# Patent Value Diagnostic

**Patent:** US13/422,494 — (Z)-2-cyano-3-hydroxy-but-2-enoic acid-(4'-trifluoromethylphenyl)-amide tablet formulations with improved stability
**Ledger:** `LEDGER-HOLDOUT-INT3-US8802735`
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

- Value Carrier: **Aubagio® (teriflunomide) tablets 7 mg / 14 mg** (drug_biologic; strong_evidence)
- `US8802735B2` → `VC-HOLDOUT-INT3-AUBAGIO` — **implemented_in** (strong_evidence)

## Observed Metrics

No value metric is currently recorded.

## Unresolved Gaps

- **patent_value_attribution**: No public E4 attributing revenue specifically to this formulation patent vs sibling use patents. (observability: `restricted`)
- **exact_patent_mapping**: Full quantitative wt% for every claim-1 band not on label (claims 36/37 give exact recipes). (observability: `restricted`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - Single-patent royalty/contribution analysis
- **TASK-02 → E3**: 建立 exact patent → value carrier 映射
  - Batch formula matching claim 36/37 mg

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
