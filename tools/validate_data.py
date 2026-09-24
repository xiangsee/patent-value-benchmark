#!/usr/bin/env python3
"""Validate Xiangsee Patent Value Benchmark JSONL datasets.

Checks:
1. JSON syntax and JSON Schema conformance.
2. Unique IDs within each entity class.
3. Cross-file references (sources, evidence, matched-pair patent IDs).
4. Non-Unknown assessments must cite at least one evidence record.
5. Evidence records must use T0-eligible sources.
6. T0-eligible sources with known public-availability dates must not be post-T0
   when they are used as evidence for the current validation dataset.

This script intentionally does not score patents or infer missing facts.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

SCHEMAS = {
    "sources": ROOT / "schema" / "source-record.schema.json",
    "patents": ROOT / "schema" / "patent-record.schema.json",
    "evidence": ROOT / "schema" / "evidence.schema.json",
    "pairs": ROOT / "schema" / "matched-pair.schema.json",
}

DATA_GLOBS = {
    "sources": "data/source-registry/*.jsonl",
    "patents": "data/patents/*.jsonl",
    "evidence": "data/evidence/*.jsonl",
    "pairs": "data/matched-pairs/*.jsonl",
}

ID_FIELDS = {
    "sources": "source_id",
    "patents": "record_id",
    "evidence": "evidence_id",
    "pairs": "pair_id",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(paths: list[Path]) -> list[tuple[Path, int, dict[str, Any]]]:
    rows: list[tuple[Path, int, dict[str, Any]]] = []
    for path in paths:
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{lineno}: invalid JSON: {exc}") from exc
            rows.append((path, lineno, obj))
    return rows


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    datasets: dict[str, list[tuple[Path, int, dict[str, Any]]]] = {}

    for kind, pattern in DATA_GLOBS.items():
        paths = sorted(ROOT.glob(pattern))
        datasets[kind] = load_jsonl(paths) if paths else []

    # Schema validation.
    for kind, rows in datasets.items():
        schema = load_json(SCHEMAS[kind])
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for path, lineno, obj in rows:
            for err in sorted(validator.iter_errors(obj), key=lambda e: list(e.path)):
                loc = ".".join(str(p) for p in err.path) or "<root>"
                fail(errors, f"{path}:{lineno}: schema error at {loc}: {err.message}")

    # Unique IDs and lookup maps.
    lookups: dict[str, dict[str, dict[str, Any]]] = {}
    for kind, rows in datasets.items():
        field = ID_FIELDS[kind]
        lookup: dict[str, dict[str, Any]] = {}
        for path, lineno, obj in rows:
            value = obj.get(field)
            if not isinstance(value, str) or not value:
                continue
            if value in lookup:
                fail(errors, f"{path}:{lineno}: duplicate {field}={value}")
            lookup[value] = obj
        lookups[kind] = lookup

    sources = lookups["sources"]
    patents = lookups["patents"]
    evidence = lookups["evidence"]

    # Evidence -> source integrity.
    for evidence_id, item in evidence.items():
        source_id = item.get("source_id")
        if source_id not in sources:
            fail(errors, f"evidence {evidence_id}: missing source_id {source_id}")
            continue
        src = sources[source_id]
        if not src.get("t0_eligible", False):
            fail(errors, f"evidence {evidence_id}: source {source_id} is not T0-eligible")

    # Patent -> sources/evidence integrity.
    for record_id, item in patents.items():
        for source_id in item.get("sources", []):
            if source_id not in sources:
                fail(errors, f"patent {record_id}: missing source {source_id}")

        award_source = item.get("award", {}).get("official_list_source_id")
        if award_source and award_source not in sources:
            fail(errors, f"patent {record_id}: missing award source {award_source}")

        assessment = item.get("assessment", {})
        for dimension, value in assessment.items():
            status = value.get("status")
            evidence_ids = value.get("evidence_ids", [])
            if status != "unknown" and not evidence_ids:
                fail(errors, f"patent {record_id}: {dimension}={status} but has no evidence_ids")
            for evidence_id in evidence_ids:
                if evidence_id not in evidence:
                    fail(errors, f"patent {record_id}: {dimension} references missing evidence {evidence_id}")

    # Pair -> patent integrity and T0 consistency.
    for pair_id, item in lookups["pairs"].items():
        for key in ("gold_record_id", "comparison_record_id"):
            rid = item.get(key)
            if rid not in patents:
                fail(errors, f"pair {pair_id}: {key} references missing patent {rid}")
                continue
            patent_t0 = patents[rid].get("cutoff", {}).get("t0_date")
            if patent_t0 and patent_t0 != item.get("t0_date"):
                fail(errors, f"pair {pair_id}: T0 mismatch for {rid}: pair={item.get('t0_date')} patent={patent_t0}")

    # Public-availability sanity check for evidence used by 25th records.
    t0_dates = {
        item.get("cutoff", {}).get("t0_date")
        for item in patents.values()
        if item.get("cutoff", {}).get("t0_date")
    }
    if len(t0_dates) == 1:
        t0 = next(iter(t0_dates))
        for evidence_id, item in evidence.items():
            source_id = item.get("source_id")
            src = sources.get(source_id, {})
            public_date = src.get("publicly_available_date")
            if item.get("t0_eligible") and public_date and public_date > t0:
                fail(errors, f"evidence {evidence_id}: source {source_id} public date {public_date} is after T0 {t0}")

    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    counts = {kind: len(rows) for kind, rows in datasets.items()}
    print("Validation passed.")
    print(json.dumps(counts, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
