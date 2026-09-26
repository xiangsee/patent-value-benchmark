# Patent Value Diagnostic

**Patent:** US14/054,414 — CRISPR-Cas systems and methods for altering expression of gene products
**Ledger:** `LEDGER-NA-CRISPR-US8697359-T0-2026`
**Mode:** public

## Current State

- **Realization Stage:** R2 — Rights Transaction
- **Evidence Levels Present:** E1, E2, E5
- **Exact Patent → Value Carrier:** unknown
- **Patent-level Attributable Value:** unknown

## Observability

- **enterprise:** disclosed_regulated
- **product_project:** disclosed_regulated
- **exact_patent_mapping:** unknown
- **attributable_value:** unknown

## Confirmed Chain

- Value Carrier: **Editas in-licensed Broad Cas9 patent estate** (protocol_platform; confirmed)
- `US8697359` → `VC-CRISPR-EDITAS-BROAD-CAS9-ESTATE` — **licensed_to** (confirmed)

## Observed Metrics

- **CASGEVY Q2 2026 product revenue**: 76400000 USD (Q2 2026) — scope=`product_project`, attribution=`unknown`
- **CASGEVY-related Editas Cas9 license upfront payment**: 50000000 USD (2023 license) — scope=`product_project`, attribution=`unknown`

## Unresolved Gaps

- **exact_patent_mapping**: Public records establish that US8697359 sits inside an in-licensed Broad Cas9 patent estate and that CASGEVY is covered by a broader multi-portfolio licensing stack, but do not establish the exact US8697359 → CASGEVY implementation/contribution link. (observability: `restricted`)
- **patent_value_attribution**: CASGEVY revenue and the Editas-Vertex portfolio license consideration cannot be apportioned to US8697359 from public evidence. (observability: `restricted`)
- **other**: V0.7 cannot represent that the economic/legal position depends on a network spanning multiple Broad patents, CVC patents/applications, ToolGen and Sigma claims, multiple licenses, ongoing appeals/interferences, and jurisdiction-specific validity outcomes. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E3**: 建立 exact patent → value carrier 映射
  - patent schedule for the CASGEVY sublicense
  - claim chart to CASGEVY editing/manufacturing steps
  - license scope identifying US8697359 individually
- **TASK-02 → E4**: 建立专利级性能、成本或经济价值归因
  - portfolio-to-patent apportionment
  - patent-specific royalty allocation
  - counterfactual bargaining contribution
- **TASK-03 → unknown**: 补齐Ledger列明的证据缺口
  - portfolio membership graph
  - claim-set overlap graph
  - license-chain graph
  - jurisdiction-specific rights state

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.
- Product/project metrics are available, but patent-level attributable value remains Unknown.
- Historical diagnostic is frozen at T0=2026-08-05; post-T0 information must not be backfilled.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
