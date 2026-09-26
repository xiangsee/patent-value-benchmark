#!/usr/bin/env python3
"""Validate experimental Claim-set Rights Control records.

This validator is intentionally separate from the formal Patent Value Ledger
validator. It validates the experimental object without promoting it into the
formal v1 schema.

Checks:
- JSON Schema conformance
- unique rights_control_id
- evidence cross-references
- T0 discipline for adjudication events and evidence
- source Ledger references
- required evidence for value-carrier mapping / finality / operative control

It deliberately allows contradictory-but-valid legal states, for example:
an adverse PTAB FWD + no cancellation certificate + an operative ITC LEO.
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "experimental" / "claim-set-rights-control.schema.json"
DATA_GLOB = "data/experimental/rights-control/*.jsonl"
EVIDENCE_GLOB = "data/evidence/*.jsonl"
LEDGER_GLOB = "data/ledgers/*.jsonl"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(pattern: str) -> list[tuple[Path, int, dict[str, Any]]]:
    rows: list[tuple[Path, int, dict[str, Any]]] = []
    for path in sorted(ROOT.glob(pattern)):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            rows.append((path, lineno, json.loads(line)))
    return rows


def collect_evidence_ids(record: dict[str, Any]) -> set[str]:
    ids = set(record.get("evidence_ids", []))
    ids.update(record.get("value_carrier_mapping", {}).get("evidence_ids", []))
    for event in record.get("adjudication_events", []):
        ids.update(event.get("evidence_ids", []))
    ids.update(record.get("finality_state", {}).get("evidence_ids", []))
    ids.update(record.get("operative_control", {}).get("evidence_ids", []))
    return ids


def validate_semantics(
    record: dict[str, Any],
    evidence_lookup: dict[str, dict[str, Any]],
    ledger_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    rid = record.get("rights_control_id", "<unknown>")
    as_of_raw = record.get("as_of_date")
    try:
        as_of = date.fromisoformat(as_of_raw)
    except Exception:
        return errors  # schema validator reports malformed dates.

    for ledger_id in record.get("source_ledger_ids", []):
        if ledger_id not in ledger_ids:
            errors.append(f"{rid}: source_ledger_id does not exist: {ledger_id}")

    for event in record.get("adjudication_events", []):
        try:
            decision_date = date.fromisoformat(event["decision_date"])
        except Exception:
            continue
        if decision_date > as_of:
            errors.append(
                f"{rid}: adjudication event {event.get('event_id')} occurs after T0 "
                f"({decision_date} > {as_of})"
            )

    referenced = collect_evidence_ids(record)
    for evidence_id in sorted(referenced):
        ev = evidence_lookup.get(evidence_id)
        if ev is None:
            errors.append(f"{rid}: missing evidence_id {evidence_id}")
            continue
        observed_raw = ev.get("observed_date")
        if observed_raw:
            try:
                observed = date.fromisoformat(observed_raw)
            except Exception:
                continue
            if observed > as_of:
                errors.append(
                    f"{rid}: evidence {evidence_id} observed after T0 "
                    f"({observed} > {as_of})"
                )

    mapping = record.get("value_carrier_mapping", {})
    if mapping.get("status") != "unknown" and not mapping.get("evidence_ids"):
        errors.append(f"{rid}: non-Unknown value_carrier_mapping requires evidence")

    finality = record.get("finality_state", {})
    if not finality.get("evidence_ids"):
        errors.append(f"{rid}: finality_state requires evidence")

    operative = record.get("operative_control", {})
    if operative.get("enforceability_state") != "unknown" and not operative.get("evidence_ids"):
        errors.append(f"{rid}: non-Unknown operative_control requires evidence")

    # Intentionally no rule that collapses adjudication into enforceability.
    # Example: adverse PTAB FWD + no cancellation certificate + operative ITC LEO
    # is a valid, important state that the schema must preserve.

    return errors


def validate_record(
    record: dict[str, Any],
    schema: dict[str, Any],
    evidence_lookup: dict[str, dict[str, Any]],
    ledger_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for err in sorted(validator.iter_errors(record), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in err.path) or "<root>"
        errors.append(f"schema error at {loc}: {err.message}")
    if not errors:
        errors.extend(validate_semantics(record, evidence_lookup, ledger_ids))
    return errors


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    rows = load_jsonl(DATA_GLOB)
    evidence_rows = load_jsonl(EVIDENCE_GLOB)
    ledger_rows = load_jsonl(LEDGER_GLOB)

    evidence_lookup = {
        obj["evidence_id"]: obj
        for _, _, obj in evidence_rows
        if isinstance(obj.get("evidence_id"), str)
    }
    ledger_ids = {
        obj["ledger_id"]
        for _, _, obj in ledger_rows
        if isinstance(obj.get("ledger_id"), str)
    }

    errors: list[str] = []
    seen: set[str] = set()

    for path, lineno, record in rows:
        rid = record.get("rights_control_id")
        if isinstance(rid, str):
            if rid in seen:
                errors.append(f"{path}:{lineno}: duplicate rights_control_id={rid}")
            seen.add(rid)

        for error in validate_record(record, schema, evidence_lookup, ledger_ids):
            errors.append(f"{path}:{lineno}: {error}")

    if errors:
        print(f"Rights Control validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Rights Control validation passed: {len(rows)} experimental record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
