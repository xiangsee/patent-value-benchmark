# Patent Value Diagnostic

**Patent:** ZL201910544020.8 — 电池包、车辆和储能装置
**Ledger:** `LEDGER-NA-BYD-BLADE-CN110165116-T0-2026`
**Mode:** public

## Current State

- **Realization Stage:** R0 — Right Exists
- **Evidence Levels Present:** E1, E2
- **Exact Patent → Value Carrier:** unknown
- **Patent-level Attributable Value:** unknown

## Observability

- **enterprise:** public
- **product_project:** public
- **exact_patent_mapping:** unknown
- **attributable_value:** unknown

## Confirmed Chain

- Value Carrier: **比亚迪刀片电池 CTP 专利簇（同日/同优先权长单体与电池包族）** (protocol_platform; confirmed)
- `CN110165116B` → `VC-BYD-BLADE-CTP-PORTFOLIO` — **other** (confirmed)

## Observed Metrics

- **Media-reported Blade Battery core-patent portfolio size**: 300 patents_lower_bound_media (early-2020 media report of executive statement) — scope=`product_project`, attribution=`unknown`
- **Sibling pack claim volume-utilization threshold (CN110165115B)**: 55 percent_V1_over_V2_lower_bound (claim language as of 2019-12-20 grant) — scope=`product_project`, attribution=`unknown`

## Unresolved Gaps

- **exact_patent_mapping**: Official BYD disclosures establish Blade Battery → Han/Tang/Atto 3 platform fitment, and bibliographic sources place CN110165116B in the CTP patent cluster, but no public regulated disclosure maps CN110165116B individually to a named vehicle BOM or pack SKU. Secondary media citation of 116 is not treated as confirmed exact mapping. (observability: `restricted`)
- **patent_value_attribution**: Blade commercial success and media '>300 patents' framing are portfolio/product-system facts. No public apportionment assigns safety, range, cost, or revenue increments to CN110165116B versus siblings (115/118/cell patents) or later continuations. (observability: `restricted`)
- **other**: V0.7 can honestly stop at R0 for one CTP grant inside a commercially successful auto battery stack, but cannot represent the product-system object: complementary claim sets (structure vs utilization), sibling mis-mapping risk, cell-layer vs pack-layer patents, multi-vehicle platform edges, or portfolio-size narrative independent of any one grant. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E3**: 建立 exact patent → value carrier 映射
  - Official patent-product mapping list
  - Regulated disclosure naming CN110165116B / ZL201910544020.8
  - Claim chart from this grant to a shipped Blade pack
- **TASK-02 → E4**: 建立专利级性能、成本或经济价值归因
  - Single-patent contribution analysis
  - License/royalty attribution
  - Counterfactual if this grant alone were removed from the CTP cluster
- **TASK-03 → unknown**: 补齐Ledger列明的证据缺口
  - portfolio/product-system network object
  - claim-set complementarity graph
  - platform→vehicle edges separate from patent→platform edges

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.
- Product/project metrics are available, but patent-level attributable value remains Unknown.
- Historical diagnostic is frozen at T0=2026-10-12; post-T0 information must not be backfilled.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
