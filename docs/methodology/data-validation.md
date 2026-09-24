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
