# Patent Value Diagnostic

**Patent:** ZL201410204545.4 — 基于指纹识别的终端及其待机状态下的登录方法、系统
**Ledger:** `LEDGER-HOLDOUT-E4N1-ZL201410204545.4`
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

- Value Carrier: **思立微被控指纹芯片产品（裁判认定侵权）** (component; confirmed)
- `ZL201410204545.4` → `VC-HOLDOUT-E4N1-SILICONITY-FP-CHIPS` — **implemented_in** (confirmed)
- `VC-HOLDOUT-E4N1-SILICONITY-FP-CHIPS` → `COURT-ENFORCEMENT-YUE03-3258` — **validated_by** (confirmed)

## Observed Metrics

- **court-awarded patent infringement damages (incl. costs components in judgment_amount)**: 40069871.66 CNY (judgment 2020-02-18; (2018)粤03民初3258号) — scope=`exact_patent`, attribution=`confirmed`

## Unresolved Gaps

- **patent_value_attribution**: Damages rest on discretionary infringer-profit apportionment (fingerprint-chip line share / multi-year narrative), not audited lost profits of Goodix own product. (observability: `restricted`)
- **technical_comparison**: No field-normalized technical-quality benchmark beyond infringement finding. (observability: `public`)

## Next Evidence Tasks

- **TASK-01 → E4**: 建立专利级性能、成本或经济价值归因
  - Full audit trail of profit base
  - Rightsholder product-level lost sales tied to this ZL
- **TASK-02 → E5**: 建立相对现有技术的可复核比较
  - Prior-art / design-around comparison

## Warnings

- Enterprise or product value must not be automatically inherited by the exact patent.
- Unknown means unobserved or unresolved, not zero value.

## Output Limits

- Gold probability: **not produced**
- Unsupported patent valuation amount: **not produced**
- Automatic ranking: **not produced**

---
Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.
