# Patent Value Diagnostic

**Patent:** US09/004,827 — Method for node ranking in a linked database
**Ledger:** `LEDGER-NA-PAGERANK-US6285999-T0-2004`
**Mode:** public

## Current State

- **Realization Stage:** R4 — Scaled Real-world Validation
- **Evidence Levels Present:** E1, E2, E3
- **Exact Patent → Value Carrier:** confirmed
- **Patent-level Attributable Value:** unknown

## Observability

- **enterprise:** disclosed_regulated
- **product_project:** disclosed_regulated
- **exact_patent_mapping:** disclosed_regulated
- **attributable_value:** unknown

## Confirmed Chain

- Value Carrier: **Google Web Search ranking system** (software_algorithm; confirmed)
- `US6285999` → `VC-PAGERANK-GOOGLE-SEARCH` — **implemented_in** (confirmed)

## Observed Metrics

- **Google total revenue**: 1465934000 USD (FY2003 (H1 2004 separately disclosed at USD 1.351835bn)) — scope=`enterprise`, attribution=`unknown`
- **licensed rights horizon**: exclusive license through 2011; patent stated to expire in 2017 (2004-07-26) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: Google's enterprise revenue, traffic and search scale cannot be apportioned to US6285999 from the public record. (observability: `restricted`)
- **other**: V0.7 does not separately represent accumulated revealed-value history, remaining exclusive-license duration, remaining patent term, or future option horizon; therefore two T0 states can both appear as R4 despite materially different asset horizons. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - patent-specific royalty economics
  - incremental search-performance contribution
  - counterfactual or apportionment analysis
- **TASK-02 → unknown**: 补齐Ledger列明的证据缺口
  - survival/revealed-value clock
  - remaining-exclusivity clock
  - value-horizon state

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.
- Historical diagnostic is frozen at T0=2004-07-26; post-T0 information must not be backfilled.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
