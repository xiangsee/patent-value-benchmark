# Patent Value Diagnostic

**Patent:** US11/901,263 — High efficiency power converter
**Ledger:** `LEDGER-NA-SYNQOR-US7564702-C56-T0-2017`
**Mode:** public

## Current State

- **Realization Stage:** R4 — Scaled Real-world Validation
- **Evidence Levels Present:** E2, E3, E5
- **Exact Patent → Value Carrier:** confirmed
- **Patent-level Attributable Value:** unknown

## Observability

- **enterprise:** public
- **product_project:** public
- **exact_patent_mapping:** public
- **attributable_value:** unknown

## Confirmed Chain

- Value Carrier: **Commercial DC-DC converter systems adjudicated in SynQor v. Artesyn** (component; confirmed)
- `US7564702:claim56` → `VC-SYNQOR-702-C56-COMMERCIAL-CONVERTERS` — **implemented_in** (confirmed)

## Observed Metrics

- **commercial infringement / case scale**: multiple commercial power-converter defendants/products; mixed-patent judgment about USD 95.2m (2010 jury / 2011 court record) — scope=`product_project`, attribution=`unknown`

## Unresolved Gaps

- **patent_value_attribution**: The mixed 2010 damages judgment is not apportioned to this exact claim. (observability: `restricted`)
- **other**: V0.7 cannot separately encode that claim 56's challenged patentability was sustained in reexamination/appellate review at T0. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - claim-specific royalty/damages allocation
  - incremental technical contribution
  - claim-specific bargaining evidence
- **TASK-02 → unknown**: 补齐Ledger列明的证据缺口
  - claim-set patentability/adjudication state
  - procedure/finality state
  - enforceability and counterfactual control

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.
- Product/project metrics are available, but patent-level attributable value remains Unknown.
- R4 confirms scaled real-world validation; it does not establish R5 patent-level attributable value.
- Historical diagnostic is frozen at T0=2017-08-30; post-T0 information must not be backfilled.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
