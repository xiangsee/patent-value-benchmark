# Schema map

## Formal / frozen (v0.1.0)

These define the public contribution contract. Ledger & Diagnostic use
`schema_version: "1.0"`.

| File | Role |
|---|---|
| `patent-value-ledger.schema.json` | Patent Value Ledger 1.0 |
| `patent-value-diagnostic.schema.json` | Patent Value Diagnostic 1.0 |
| `v0.7-state.schema.json` | Embedded V0.7 state object |
| `evidence.schema.json` | Evidence records (structure-frozen) |
| `source-record.schema.json` | Source registry (structure-frozen) |
| `patent-record.schema.json` | Historical award/sample patent records |
| `matched-pair.schema.json` | Historical matched pairs |

Formal methodology: **V0.7 adopted**.  
Do **not** bump beyond `1.0` without an explicit freeze/release decision.

## Experimental / research-only

See [`experimental/README.md`](experimental/README.md).

> Objects under `schema/experimental/` are **not** part of formal schema 1.0.
> V0.8 remains research-only until explicitly adopted.

Validate formal data:

```bash
python tools/validate_data.py
python tools/generate_diagnostics.py --check
python tools/render_reports.py --check
```
