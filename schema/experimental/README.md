# Experimental schemas — NOT formal schema 1.0

> **BANNER / 横幅**
>
> 本目录下的 JSON Schema 全部是 **experimental / research-only**。  
> 它们 **不是** 正式 Patent Value Ledger / Diagnostic **schema 1.0** 的一部分。  
> 正式方法基线仍是 **V0.7 (adopted)**。  
> **V0.8 尚未采纳**；通过实验校验 **不会** 把对象升格为正式字段。

| Formal (frozen 1.0) | Experimental (this folder) |
|---|---|
| `schema/patent-value-ledger.schema.json` | `claim-set-rights-control.schema.json` |
| `schema/patent-value-diagnostic.schema.json` | `realization-path-events.schema.json` |
| `schema/evidence.schema.json` | `realization-path-snapshot.schema.json` |
| `schema/source-record.schema.json` | |
| `schema/v0.7-state.schema.json` | |

## Rules

1. Do **not** add these fields into Ledger / Diagnostic rows under `schema_version: "1.0"`.
2. Experimental data lives under `data/experimental/` and is validated by **separate** tools:
   - `python tools/validate_rights_control.py`
   - `python tools/validate_realization_paths.py`
3. Cold-start / CI acceptance for public contributions is still:
   - `python tools/validate_data.py`
   - `python tools/generate_diagnostics.py --check`
   - `python tools/render_reports.py --check`
4. Round 2 adoption-readiness synthesis explicitly keeps these research-only:
   - `analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`

## Files

| File | Role | `schema_version` const |
|---|---|---|
| `claim-set-rights-control.schema.json` | Claim-set legal control state | `experimental-0.1` |
| `realization-path-events.schema.json` | Canonical event log | `experimental-0.1` |
| `realization-path-snapshot.schema.json` | Generated snapshot (do not hand-edit) | `experimental-0.1` |

Methodology notes:

- `docs/methodology/claim-set-rights-control-experimental-0.1.md`
- `docs/methodology/realization-path-experimental-0.1.md`
- `docs/methodology/data-validation.md`
