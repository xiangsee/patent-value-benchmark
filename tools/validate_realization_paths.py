#!/usr/bin/env python3
"""Validate experimental Realization Path event logs and generated snapshots."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

import project_realization_paths as projector

ROOT = Path(__file__).resolve().parents[1]
EVENT_SCHEMA_PATH = ROOT / "schema" / "experimental" / "realization-path-events.schema.json"
SNAPSHOT_SCHEMA_PATH = ROOT / "schema" / "experimental" / "realization-path-snapshot.schema.json"
EVIDENCE_GLOB = "data/evidence/*.jsonl"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(pattern: str) -> list[tuple[Path, int, dict[str, Any]]]:
    rows: list[tuple[Path, int, dict[str, Any]]] = []
    for path in sorted(ROOT.glob(pattern)):
        if path.name == projector.GENERATED_NAME:
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip():
                rows.append((path, lineno, json.loads(line)))
    return rows


def schema_errors(record: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for err in sorted(validator.iter_errors(record), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in err.path) or "<root>"
        errors.append(f"schema error at {loc}: {err.message}")
    return errors


def validate_path_semantics(
    record: dict[str, Any],
    evidence_lookup: dict[str, dict[str, Any]],
) -> list[str]:
    errors: list[str] = []
    path_id = record.get("path_id", "<unknown>")

    try:
        as_of = date.fromisoformat(record["as_of_date"])
    except Exception:
        return errors

    event_ids: set[str] = set()

    for event in record.get("events", []):
        event_id = event.get("event_id")
        if event_id in event_ids:
            errors.append(f"{path_id}: duplicate event_id={event_id}")
        if isinstance(event_id, str):
            event_ids.add(event_id)

        precision = event.get("date_precision")
        event_date = event.get("event_date")
        if precision == "exact" and not event_date:
            errors.append(f"{path_id}: exact event {event_id} requires event_date")
        if event_date:
            try:
                event_dt = date.fromisoformat(event_date)
            except Exception:
                event_dt = None
            if event_dt and event_dt > as_of:
                errors.append(
                    f"{path_id}: event {event_id} occurs after as_of_date "
                    f"({event_dt} > {as_of})"
                )

        for evidence_id in event.get("evidence_ids", []):
            evidence = evidence_lookup.get(evidence_id)
            if evidence is None:
                errors.append(f"{path_id}: missing evidence_id {evidence_id}")
                continue
            observed_raw = evidence.get("observed_date")
            if observed_raw:
                try:
                    observed = date.fromisoformat(observed_raw)
                except Exception:
                    observed = None
                if observed and observed > as_of:
                    errors.append(
                        f"{path_id}: evidence {evidence_id} observed after as_of_date "
                        f"({observed} > {as_of})"
                    )

        amount = event.get("amount")
        if amount and amount.get("value", 0) < 0:
            errors.append(f"{path_id}: negative observed amount is not allowed")

    return errors


def main() -> int:
    event_schema = load_json(EVENT_SCHEMA_PATH)
    snapshot_schema = load_json(SNAPSHOT_SCHEMA_PATH)

    rows = load_jsonl(projector.INPUT_GLOB)
    evidence_rows = load_jsonl(EVIDENCE_GLOB)
    evidence_lookup = {
        obj["evidence_id"]: obj
        for _, _, obj in evidence_rows
        if isinstance(obj.get("evidence_id"), str)
    }

    errors: list[str] = []
    seen_paths: set[str] = set()

    for path, lineno, record in rows:
        path_id = record.get("path_id")
        if isinstance(path_id, str):
            if path_id in seen_paths:
                errors.append(f"{path}:{lineno}: duplicate path_id={path_id}")
            seen_paths.add(path_id)

        for err in schema_errors(record, event_schema):
            errors.append(f"{path}:{lineno}: {err}")
        if not schema_errors(record, event_schema):
            for err in validate_path_semantics(record, evidence_lookup):
                errors.append(f"{path}:{lineno}: {err}")

    # Validate deterministic projections as objects, independently of --check.
    for record in [obj for _, _, obj in rows]:
        snapshot = projector.project(record)
        for err in schema_errors(snapshot, snapshot_schema):
            errors.append(f"snapshot {record.get('path_id')}: {err}")

    if errors:
        print(f"Realization Path validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Realization Path validation passed: {len(rows)} path(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
