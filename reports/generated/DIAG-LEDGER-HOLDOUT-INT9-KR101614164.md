# Patent Value Diagnostic

**Patent:** KR20097017818A — Substituted 4-aryl-1,4-dihydro-1,6-naphthyridinamides and use thereof
**Ledger:** `LEDGER-HOLDOUT-INT9-KR101614164`
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

- Value Carrier: **Kerendia® (케렌디아정; finerenone) tablets 10 mg / 20 mg** (drug_biologic; strong_evidence)
- `KR101614164B1` → `VC-HOLDOUT-INT9-KERENDIA` — **implemented_in** (strong_evidence)

## Observed Metrics

No value metric is currently recorded.

## Unresolved Gaps

- **patent_value_attribution**: No public E4 attributing revenue specifically to this substance patent vs sibling process/crystal patents. (observability: `restricted`)
- **exact_patent_mapping**: Full Markush claim-chart to commercial API stereochemistry not published as a single chart. (observability: `restricted`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - Single-patent royalty/contribution analysis
- **TASK-02 → E3**: 建立 exact patent → value carrier 映射
  - Independent claim chart to finerenone species claim

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
