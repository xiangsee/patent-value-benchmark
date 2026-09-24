#!/usr/bin/env python3
"""Validate Xiangsee Patent Value Benchmark datasets.

The validator checks structural integrity, cross-file references, T0 discipline,
and the non-inheritance rules introduced by V0.7.

It intentionally does not score patents and does not infer missing facts.
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
    "ledgers": ROOT / "schema" / "patent-value-ledger.schema.json",
    "diagnostics": ROOT / "schema" / "patent-value-diagnostic.schema.json",
}

DATA_GLOBS = {
    "sources": "data/source-registry/*.jsonl",
    "patents": "data/patents/*.jsonl",
    "evidence": "data/evidence/*.jsonl",
    "pairs": "data/matched-pairs/*.jsonl",
    "ledgers": "data/ledgers/*.jsonl",
    "diagnostics": "data/diagnostics/*.jsonl",
}

ID_FIELDS = {
    "sources": "source_id",
    "patents": "record_id",
    "evidence": "evidence_id",
    "pairs": "pair_id",
    "ledgers": "ledger_id",
    "diagnostics": "diagnostic_id",
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


def collect_ledger_evidence_ids(item: dict[str, Any]) -> set[str]:
    ids: set[str] = set()

    ids.update(item.get("knowledge_origin", {}).get("evidence_ids", []))
    ids.update(item.get("technology", {}).get("evidence_ids", []))

    for carrier in item.get("value_carriers", []):
        ids.update(carrier.get("evidence_ids", []))

    for link in item.get("value_links", []):
        ids.update(link.get("evidence_ids", []))

    for metric in item.get("value_metrics", []):
        ids.update(metric.get("evidence_ids", []))

    ids.update(
        item.get("v0_7_state", {})
        .get("attribution_evidence_state", {})
        .get("evidence_ids", [])
    )
    return ids


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
    ledgers = lookups["ledgers"]
    diagnostics = lookups["diagnostics"]

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

    # Patent Value Ledger validation.
    for ledger_id, item in ledgers.items():
        for source_id in item.get("source_ids", []):
            if source_id not in sources:
                fail(errors, f"ledger {ledger_id}: missing source {source_id}")

        ledger_evidence_ids = collect_ledger_evidence_ids(item)
        for evidence_id in ledger_evidence_ids:
            if evidence_id not in evidence:
                fail(errors, f"ledger {ledger_id}: references missing evidence {evidence_id}")

        obs = item.get("observation", {})
        t0 = obs.get("t0_date")
        if obs.get("time_policy") == "historical_t0_cutoff" and not t0:
            fail(errors, f"ledger {ledger_id}: historical_t0_cutoff requires t0_date")

        # Check public-availability dates only for evidence actually used by this ledger.
        if t0:
            for evidence_id in ledger_evidence_ids:
                ev = evidence.get(evidence_id)
                if not ev:
                    continue
                src = sources.get(ev.get("source_id"), {})
                public_date = src.get("publicly_available_date")
                if public_date and public_date > t0:
                    fail(
                        errors,
                        f"ledger {ledger_id}: evidence {evidence_id} source public date "
                        f"{public_date} is after ledger T0 {t0}"
                    )

        state = item.get("v0_7_state", {})
        attr = state.get("attribution_evidence_state", {})
        stage = state.get("realization_stage")
        stage_evidence_ids = state.get("realization_stage_evidence_ids", [])
        exact_link = attr.get("exact_patent_value_carrier_link")
        patent_value = attr.get("patent_level_attributable_value")

        # Every claimed realization beyond R0 must cite evidence for that stage.
        if stage in {"R1", "R2", "R3", "R4", "R5"} and not stage_evidence_ids:
            fail(errors, f"ledger {ledger_id}: {stage} requires realization_stage_evidence_ids")
        for evidence_id in stage_evidence_ids:
            if evidence_id not in evidence:
                fail(errors, f"ledger {ledger_id}: realization stage references missing evidence {evidence_id}")

        # V0.7 non-inheritance rule:
        # Patent-level R3/R4/R5 requires at least a non-Unknown exact-patent link.
        if stage in {"R3", "R4", "R5"} and exact_link == "unknown":
            fail(
                errors,
                f"ledger {ledger_id}: {stage} requires a non-Unknown exact_patent_value_carrier_link"
            )

        # R5 specifically requires attributable patent-level value.
        if stage == "R5" and "E4" not in attr.get("evidence_levels_present", []):
            fail(errors, f"ledger {ledger_id}: R5 requires E4 in evidence_levels_present")

        if stage == "R5" and patent_value == "unknown":
            fail(
                errors,
                f"ledger {ledger_id}: R5 requires non-Unknown patent_level_attributable_value"
            )

        if stage == "R5":
            exact_metrics = [
                m for m in item.get("value_metrics", [])
                if m.get("scope_level") == "exact_patent"
                and m.get("attribution_status") != "unknown"
            ]
            if not exact_metrics:
                fail(
                    errors,
                    f"ledger {ledger_id}: R5 requires at least one attributable exact_patent value metric"
                )

    # Diagnostic -> Ledger / Evidence integrity.
    for diagnostic_id, item in diagnostics.items():
        ledger_id = item.get("ledger_id")
        if ledger_id not in ledgers:
            fail(errors, f"diagnostic {diagnostic_id}: missing ledger {ledger_id}")
            continue

        referenced_evidence: set[str] = set()
        for carrier in item.get("confirmed_chain", {}).get("value_carriers", []):
            referenced_evidence.update(carrier.get("evidence_ids", []))
        for link in item.get("confirmed_chain", {}).get("links", []):
            referenced_evidence.update(link.get("evidence_ids", []))
        for metric in item.get("observed_metrics", []):
            referenced_evidence.update(metric.get("evidence_ids", []))

        for evidence_id in referenced_evidence:
            if evidence_id not in evidence:
                fail(errors, f"diagnostic {diagnostic_id}: references missing evidence {evidence_id}")

        # Diagnostic current state must be a faithful projection of the Ledger.
        ledger_state = ledgers[ledger_id].get("v0_7_state", {})
        diag_state = item.get("current_state", {})
        if diag_state.get("realization_stage") != ledger_state.get("realization_stage"):
            fail(errors, f"diagnostic {diagnostic_id}: realization_stage differs from ledger {ledger_id}")

        ledger_attr = ledger_state.get("attribution_evidence_state", {})
        if diag_state.get("realization_stage_evidence_ids") != ledger_state.get("realization_stage_evidence_ids", []):
            fail(errors, f"diagnostic {diagnostic_id}: realization_stage_evidence_ids differ from ledger {ledger_id}")

        for field in (
            "evidence_levels_present",
            "exact_patent_value_carrier_link",
            "patent_level_attributable_value",
        ):
            if diag_state.get(field) != ledger_attr.get(field):
                fail(errors, f"diagnostic {diagnostic_id}: {field} differs from ledger {ledger_id}")

        if diag_state.get("observability") != ledger_state.get("observability_state"):
            fail(errors, f"diagnostic {diagnostic_id}: observability differs from ledger {ledger_id}")

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
