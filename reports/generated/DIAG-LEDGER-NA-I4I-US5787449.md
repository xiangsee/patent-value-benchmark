# Patent Value Diagnostic

**Patent:** US08/253,263 — Method and system for manipulating the architecture and the content of a document separately from each other
**Ledger:** `LEDGER-NA-I4I-US5787449`
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

- Value Carrier: **Microsoft Word custom XML editor** (software_algorithm; confirmed)
- `US5787449` → `VC-I4I-WORD-CUSTOM-XML` — **implemented_in** (confirmed)
- `VC-I4I-WORD-CUSTOM-XML` → `COURT-ENFORCEMENT-2010` — **validated_by** (confirmed)

## Observed Metrics

- **jury-awarded patent infringement damages**: 200000000 USD (judgment affirmed as of 2010-03-10) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **technical_comparison**: The litigation record establishes infringement and enforcement outcomes but this ledger does not yet construct a field-normalized technological-quality comparison. (observability: `public`)
- **other**: V0.7 can record R5/E4 and the injunction as evidence, but cannot explicitly model rights-control dimensions such as claim scope, validity resilience, remaining term, design-around conditions and counterfactual blocking power. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E5**: 建立相对现有技术的可复核比较
  - contemporaneous prior-art comparison
  - field-normalized technical-quality evidence
- **TASK-02 → unknown**: 补齐Ledger列明的证据缺口
  - rights-control experimental fields
  - design-around/counterfactual evidence
  - remaining-term context

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.
- Historical diagnostic is frozen at T0=2010-03-10; post-T0 information must not be backfilled.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
