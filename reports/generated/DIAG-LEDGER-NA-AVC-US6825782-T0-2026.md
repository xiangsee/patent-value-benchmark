# Patent Value Diagnostic

**Patent:** US10/665,638 — Method and apparatus for arithmetic coding and termination
**Ledger:** `LEDGER-NA-AVC-US6825782-T0-2026`
**Mode:** public

## Current State

- **Realization Stage:** R2 — Rights Transaction
- **Evidence Levels Present:** E1, E2, E5
- **Exact Patent → Value Carrier:** unknown
- **Patent-level Attributable Value:** unknown

## Observability

- **enterprise:** public
- **product_project:** public
- **exact_patent_mapping:** unknown
- **attributable_value:** unknown

## Confirmed Chain

- Value Carrier: **AVC/H.264 Patent Portfolio License (Via LA / formerly MPEG LA)** (protocol_platform; confirmed)
- Value Carrier: **AVC / H.264 (ISO/IEC 14496-10 / ITU-T H.264) digital video coding standard** (standard; confirmed)
- `US6825782` → `VC-AVC-VIA-LA-PORTFOLIO-LICENSE` — **licensed_to** (confirmed)
- `US6825782` → `VC-AVC-H264-STANDARD` — **standardized_in** (confirmed)

## Observed Metrics

- **AVC Patent Portfolio License OEM decoder/encoder unit royalty schedule**: 0.2 USD_per_unit_mid_tier (public schedule as of 2026-10-12 (mid tier $0.20; high tier $0.10; first 100k free)) — scope=`product_project`, attribution=`unknown`
- **AVC Patent Portfolio License annual enterprise royalty cap (2017 and after)**: 9750000 USD (annual; 2017 and after (public schedule)) — scope=`enterprise`, attribution=`unknown`

## Unresolved Gaps

- **exact_patent_mapping**: Public sources confirm US6825782 claim 12 is mapped into the AVC pool / H.264 §9.3 CABAC sections, and that a large licensee ecosystem exists under the portfolio license, but they do not establish an exact US6825782 → named product/service implementation link. (observability: `restricted`)
- **patent_value_attribution**: Published AVC pool royalties and enterprise caps are program-level consideration. Via LA FAQ states royalties do not change with the number of essential patents. No public apportionment assigns any share of the pool rate card to US6825782. (observability: `restricted`)
- **other**: V0.7 can record R2 for a single SEP inside a pool, plus standard essentiality evidence, but cannot represent the pool as a first-class network object: multi-licensor membership, rate-card independence from patent count, grant-back, licensee graph, essential-counterpart jurisdictions, or the difference between pool licensing and bilateral SEP cross-licenses. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E3**: 建立 exact patent → value carrier 映射
  - product or codec disclosure naming US6825782
  - licensee patent schedule identifying this patent
  - claim chart from claim 12 to a specific shipped encoder/decoder
- **TASK-02 → E4**: 建立专利级性能、成本或经济价值归因
  - pool-to-patent royalty allocation
  - bilateral FRAND comparable for this claim family
  - counterfactual bargaining contribution of claim 12
- **TASK-03 → unknown**: 补齐Ledger列明的证据缺口
  - portfolio/pool membership graph
  - licensor–licensee–standard edges
  - jurisdiction-specific essential-counterpart state
  - explicit pool vs bilateral licensing construct

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
