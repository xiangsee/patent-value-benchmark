# Patent Value Diagnostic

**Patent:** US11/620,717 — Application programming interfaces for scrolling operations
**Ledger:** `LEDGER-NA-APPLE-US7844915-C8-T0-2017`
**Mode:** public

## Current State

- **Realization Stage:** R5 — Patent-level Attributable Value
- **Evidence Levels Present:** E2, E3, E4, E5
- **Exact Patent → Value Carrier:** confirmed
- **Patent-level Attributable Value:** confirmed

## Observability

- **enterprise:** public
- **product_project:** public
- **exact_patent_mapping:** public
- **attributable_value:** public

## Confirmed Chain

- Value Carrier: **Samsung smartphone scroll-or-gesture touchscreen implementations adjudicated in Apple v. Samsung** (product_system; confirmed)
- `US7844915:claim8` → `VC-APPLE-915-SAMSUNG-PHONES` — **implemented_in** (confirmed)

## Observed Metrics

- **commercial infringement scale**: multiple Samsung smartphone products in the litigation (2012–2015 litigation record) — scope=`product_project`, attribution=`unknown`
- **patent-specific lost-profits damages evidence**: lost-profits damages awarded for certain phones infringing the '915 patent; standalone amount not isolated here (2015 appellate record) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **other**: V0.7 shows stronger realization (R5) but cannot represent that claim 8 simultaneously had an adverse reexamination adjudication posture at T0, demonstrating that realized value and current rights control can diverge. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → unknown**: 补齐Ledger列明的证据缺口
  - claim-set reexamination/adjudication state
  - final cancellation/survival state if later established
  - enforceability and design-around implications

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.
- Historical diagnostic is frozen at T0=2017-04-14; post-T0 information must not be backfilled.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
