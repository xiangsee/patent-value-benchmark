# Patent Value Diagnostic

**Patent:** US11/885,460 — Road-building machine
**Ledger:** `LEDGER-NA-WIRTGEN-US7828309-C29-T0-2020`
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

- Value Carrier: **Caterpillar commercial road-milling machines covered in ITC 337-TA-1067** (equipment; confirmed)
- `US7828309:claim29` → `VC-ROAD-WIRTGEN-CAT-MILLING` — **implemented_in** (confirmed)

## Observed Metrics

- **commercial exclusion-remedy scale**: ITC limited exclusion order covering infringing Caterpillar road-milling machines and components (2019) — scope=`product_project`, attribution=`unknown`

## Unresolved Gaps

- **patent_value_attribution**: The public ITC/IPR record does not apportion product economics or a monetary amount specifically to US7828309 claim 29. (observability: `restricted`)
- **other**: V0.7 cannot encode that PTAB failed to establish claim 29 unpatentable while an ITC exclusion remedy was operating; these are claim-set Rights Control facts separate from R4. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - claim-29-specific royalty/damages allocation
  - incremental technical contribution
  - claim-specific bargaining value
- **TASK-02 → unknown**: 补齐Ledger列明的证据缺口
  - claim-set adjudication state
  - procedural finality
  - operative remedy/enforcement state

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
