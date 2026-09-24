# Cold-start Quick Reference

## Do

```text
Source → Evidence → Ledger → Diagnostic → Report
```

## Never inherit

```text
Enterprise value ≠ Product value ≠ Patent value
```

## Stages

- R0 Right exists
- R1 Intent to transfer/license
- R2 Rights transaction
- R3 Implemented in value carrier
- R4 Scaled real-world validation
- R5 Patent-level attributable value

## Evidence (can coexist)

- E1 Enterprise
- E2 Product / Project
- E3 Exact Patent → Value Carrier
- E4 Patent-level attributable value
- E5 Independent verification

## Stop rule

If evidence does not justify a higher stage:

> **Stop. Mark the gap. Keep Unknown.**

## Commands

```bash
python tools/validate_data.py
python tools/generate_diagnostics.py
python tools/render_reports.py

python tools/validate_data.py
python tools/generate_diagnostics.py --check
python tools/render_reports.py --check
```
