# Patent Value Diagnostic

**Patent:** US13/860,016 — Antigen binding proteins to proprotein convertase subtilisin kexin type 9 (PCSK9)
**Ledger:** `LEDGER-NA-AMGEN-US8829165`
**Mode:** public

## Current State

- **Realization Stage:** R4 — Scaled Real-world Validation
- **Evidence Levels Present:** E2, E3, E5
- **Exact Patent → Value Carrier:** confirmed
- **Patent-level Attributable Value:** unknown

## Observability

- **enterprise:** public
- **product_project:** disclosed_regulated
- **exact_patent_mapping:** public
- **attributable_value:** unknown

## Confirmed Chain

- Value Carrier: **Praluent (alirocumab)** (drug_biologic; confirmed)
- `US8829165B2:claims 19 and 29` → `VC-AMGEN-PRALUENT` — **implemented_in** (confirmed)
- `VC-AMGEN-PRALUENT` → `US-SALES-2022` — **validated_by** (confirmed)

## Observed Metrics

- **Praluent 2022 U.S. net product sales**: 130000000 USD (2022) — scope=`product_project`, attribution=`unknown`

## Unresolved Gaps

- **patent_value_attribution**: Praluent product sales and commercial scale cannot be apportioned to this patent or claim set from the public record. (observability: `restricted`)
- **other**: V0.7 records R4 implementation/scale but has no structured field showing that claims 19 and 29 was invalid for lack of enablement at T0. Claim-level rights-control status is therefore hidden in evidence/notes rather than represented as a comparable state. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - claim-specific royalty or damages evidence
  - apportionment analysis
  - patent-level economic contribution evidence
- **TASK-02 → unknown**: 补齐Ledger列明的证据缺口
  - claim-set rights-control state
  - validity/enforceability field keyed to claim set
  - scope-type field for functional genus claims

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.
- Product/project metrics are available, but patent-level attributable value remains Unknown.
- R4 confirms scaled real-world validation; it does not establish R5 patent-level attributable value.
- Historical diagnostic is frozen at T0=2023-05-18; post-T0 information must not be backfilled.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
