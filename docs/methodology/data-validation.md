# Data Validation

The public dataset is validated on every relevant push and pull request.

Run locally:

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_data.py
```

The validator checks:

- JSON Schema conformance
- duplicate IDs
- source / evidence / patent / matched-pair cross references
- non-Unknown assessments without evidence
- evidence using non-T0-eligible sources
- T0 mismatches across paired records
- post-T0 public-availability leakage when dates are available

A passing validator means that the dataset is internally consistent. It does **not**
mean that the research conclusions are correct; substantive claims still require
source review and human judgment.


## Experimental Claim-set Rights Control

The experimental Rights Control object is validated separately from the formal
Patent Value Ledger:

```bash
python tools/validate_rights_control.py
python -m unittest discover -s tests -p "test_rights_control.py"
```

The validator checks:

- experimental JSON Schema conformance
- unique `rights_control_id`
- source Ledger existence
- Evidence ID integrity
- adjudication dates no later than T0
- evidence observation dates no later than T0
- evidence presence for non-Unknown mapping/finality/operative states
- deliberate support for contradictory-but-valid states

A canonical test fixture is Caterpillar US7140693 claim 19 at T0=2020-01-21:
an adverse PTAB FWD, no cancellation certificate yet, and an operative ITC
limited exclusion order are allowed to coexist.

Passing the experimental validator does **not** promote the object into the
formal v1 schema.
