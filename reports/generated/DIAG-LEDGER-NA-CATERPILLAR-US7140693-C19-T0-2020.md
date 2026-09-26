# Patent Value Diagnostic

**Patent:** US10/476,206 — Milling machine with re-entering back wheels
**Ledger:** `LEDGER-NA-CATERPILLAR-US7140693-C19-T0-2020`
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

- Value Carrier: **Wirtgen Series 1810 road-milling machines covered in ITC 337-TA-1088** (equipment; confirmed)
- `US7140693:claim19` → `VC-ROAD-CAT-WIRTGEN-1810` — **implemented_in** (confirmed)

## Observed Metrics

- **commercial exclusion-remedy scale**: ITC limited exclusion order remained in effect; CBP excluded multiple Wirtgen cold-milling machines (2019–2020) — scope=`product_project`, attribution=`unknown`

## Unresolved Gaps

- **patent_value_attribution**: The ITC/CBP record does not apportion a monetary value specifically to US7140693 claim 19. (observability: `restricted`)
- **other**: V0.7 cannot encode the split T0 state: PTAB had found claim 19 unpatentable, yet no cancellation certificate had issued and the ITC exclusion order remained operative. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - claim-19-specific royalty/damages allocation
  - incremental technical contribution
  - claim-specific bargaining value
- **TASK-02 → unknown**: 补齐Ledger列明的证据缺口
  - claim-set adjudication state
  - finality/cancellation state
  - operative enforcement/remedy state

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.
- Product/project metrics are available, but patent-level attributable value remains Unknown.
- R4 confirms scaled real-world validation; it does not establish R5 patent-level attributable value.
- Historical diagnostic is frozen at T0=2020-01-21; post-T0 information must not be backfilled.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
