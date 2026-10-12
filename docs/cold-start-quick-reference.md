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

`evidence_levels_present`: only levels with **status≠unknown** support.
Sought-but-not-found E3 (`status=unknown`) may stay in the evidence file — **do not** list `"E3"` as present.

## Stop rule

If evidence does not justify a higher stage:

> **Stop. Mark the gap. Keep Unknown.**

## Commands

Prefer `.venv` (see Getting Started) if system Python lacks `jsonschema`:

```bash
source .venv/bin/activate
python tools/validate_data.py
python tools/generate_diagnostics.py
python tools/render_reports.py

python tools/validate_data.py
python tools/generate_diagnostics.py --check
python tools/render_reports.py --check
```

## Pitfalls (#2 / PR #22 / PR #32)

- Sibling / same-day family patents: do **not** inherit mapping from a peer patent number.
- **R0 + E2 is allowed; R0 + E2 ≠ R3.**
- “300+ patent portfolio” narratives are product/enterprise scope — never auto-upgrade a single patent to R3+/R5.
- **unknown-E3 ≠ present:** sought-but-not-found E3 rows do not go into `evidence_levels_present`.
- **他案点名 ≠ 本案 E3:** company news naming *other* patent numbers (or only filing counts) is not E3 for *this* patent.
- **PP01 ≠ R / RC:** legal-status flags (e.g. patent-right preservation) are context only — do not raise R or invent Rights Control fields.
- Scaffold bibliographic flags (`--publication-number`, `--grant-number`, `--filing-date`, `--grant-date`) reduce hand-fill; no office scrapers.

## Further reading

- Trap checklist: [`docs/cold-start-trap-checklist.md`](cold-start-trap-checklist.md)
- Round 2 synthesis (V0.8 **NOT** adopted; formal = V0.7 / schema 1.0):
  [`analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`](../analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md)
- Experimental schemas (not formal 1.0): [`schema/experimental/README.md`](../schema/experimental/README.md)
- Rights Control research overview (do **not** put into Ledger 1.0): [`docs/methodology/rights-control-research-overview.md`](methodology/rights-control-research-overview.md)
- Realization Path research overview (do **not** put into Ledger 1.0): [`docs/methodology/realization-path-research-overview.md`](methodology/realization-path-research-overview.md)

