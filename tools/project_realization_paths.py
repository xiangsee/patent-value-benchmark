#!/usr/bin/env python3
"""Project experimental Realization Path event logs into deterministic snapshots.

Canonical source of truth:
  data/experimental/realization-path/*.jsonl

Generated output:
  data/experimental/realization-path/generated-snapshots.jsonl

Do not hand-edit generated snapshots.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INPUT_GLOB = "data/experimental/realization-path/*.jsonl"
OUTPUT_PATH = ROOT / "data" / "experimental" / "realization-path" / "generated-snapshots.jsonl"

# Avoid recursively loading the generated file as an input.
GENERATED_NAME = OUTPUT_PATH.name

MECHANISM_ORDER = [
    "license",
    "settlement",
    "damages_verdict",
    "judgment",
    "injunction",
    "exclusion_order",
    "assignment",
    "sale",
    "receivable_monetization",
]

FUTURE_VALUE_ORDER = [
    "recurring_fee_right",
    "royalty_right",
    "contingent_payment_right",
    "receivable",
    "receivable_sold",
]

MECHANISM_EVENTS = {
    "license_executed": "license",
    "settlement_executed": "settlement",
    "jury_verdict": "damages_verdict",
    "judgment_entered": "judgment",
    "injunction_issued": "injunction",
    "exclusion_order_issued": "exclusion_order",
    "remedy_outstanding": "exclusion_order",
    "assignment": "assignment",
    "sale": "sale",
    "receivable_monetized": "receivable_monetization",
}

ENTITLEMENT_EVENTS = {
    "rights_available": "rights_available",
    "assertion": "asserted",
    "infringement_alleged": "asserted",
    "adverse_merits_decision": "adverse",
    "appeal": "unresolved",
    "vacatur_remand": "unresolved",
    "reopened": "unresolved",
    "infringement_established": "established",
    "jury_verdict": "established",
    "license_executed": "contractual",
    "settlement_executed": "contractual",
    "assignment": "contractual",
    "sale": "contractual",
}

CONTROL_EVENTS = {
    "injunction_issued": "operative",
    "exclusion_order_issued": "operative",
    "remedy_outstanding": "operative",
    "remedy_stayed": "stayed",
    "remedy_modified": "modified",
    "remedy_vacated": "vacated",
    "remedy_expired": "expired",
}

CASH_STATUS_PRIORITY = {
    "none": 0,
    "not_required": 0,
    "unknown": 1,
    "due": 2,
    "contingent": 2,
    "unresolved": 3,
    "partial": 4,
    "received": 5,
    "written_off": 5,
    "mixed": 6,
}


def load_paths() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(ROOT.glob(INPUT_GLOB)):
        if path.name == GENERATED_NAME:
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    return rows


def add_unique(items: list[str], value: str, order: list[str] | None = None) -> None:
    if value not in items:
        items.append(value)
    if order is not None:
        rank = {item: i for i, item in enumerate(order)}
        items.sort(key=lambda x: rank.get(x, len(rank)))


def merge_cash_status(current: str, new: str) -> str:
    if current == "none":
        return new
    if current == new:
        return current
    if {current, new} <= {"received", "partial"}:
        return "partial" if "partial" in {current, new} else "received"
    if current == "received" and new in {"due", "contingent", "unresolved", "written_off"}:
        return "mixed"
    if new == "received" and current in {"due", "contingent", "unresolved", "written_off"}:
        return "mixed"
    if current == "mixed" or new == "mixed":
        return "mixed"
    return new if CASH_STATUS_PRIORITY.get(new, 0) >= CASH_STATUS_PRIORITY.get(current, 0) else current


def project(record: dict[str, Any]) -> dict[str, Any]:
    entitlement = "unknown"
    mechanisms: list[str] = []
    cash_status = "none"
    cash_event_ids: list[str] = []
    control_status = "not_applicable"
    control_event_ids: list[str] = []
    future_states: list[str] = []
    future_event_ids: list[str] = []
    observed_amounts: list[dict[str, Any]] = []
    evidence_ids: list[str] = []

    for event in record["events"]:
        event_id = event["event_id"]
        event_type = event["event_type"]

        for evidence_id in event.get("evidence_ids", []):
            add_unique(evidence_ids, evidence_id)

        if event_type in ENTITLEMENT_EVENTS:
            entitlement = ENTITLEMENT_EVENTS[event_type]

        mechanism = MECHANISM_EVENTS.get(event_type)
        if mechanism:
            add_unique(mechanisms, mechanism, MECHANISM_ORDER)

        control = CONTROL_EVENTS.get(event_type)
        if control:
            control_status = control
            add_unique(control_event_ids, event_id)

        for future_state in event.get("contractual_future_effects", []):
            add_unique(future_states, future_state, FUTURE_VALUE_ORDER)
            add_unique(future_event_ids, event_id)

        amount = event.get("amount")
        if amount:
            observed_amounts.append({
                "event_id": event_id,
                "value": amount["value"],
                "currency": amount["currency"],
                "amount_scope": amount["amount_scope"],
                "payment_status": amount["payment_status"],
                "economic_object": amount["economic_object"],
            })
            payment_status = amount["payment_status"]
            if payment_status == "received":
                cash_status = merge_cash_status(cash_status, "received")
                add_unique(cash_event_ids, event_id)
            elif payment_status == "partial":
                cash_status = merge_cash_status(cash_status, "partial")
                add_unique(cash_event_ids, event_id)
            elif payment_status == "due":
                cash_status = merge_cash_status(cash_status, "due")
                add_unique(cash_event_ids, event_id)
            elif payment_status == "contingent":
                cash_status = merge_cash_status(cash_status, "contingent")
                add_unique(cash_event_ids, event_id)
            elif payment_status == "unresolved":
                cash_status = merge_cash_status(cash_status, "unresolved")
                add_unique(cash_event_ids, event_id)
            elif payment_status == "written_off":
                cash_status = merge_cash_status(cash_status, "written_off")
                add_unique(cash_event_ids, event_id)
            else:
                cash_status = merge_cash_status(cash_status, "unknown")
                add_unique(cash_event_ids, event_id)

    if cash_status == "none":
        if control_status in {"operative", "stayed", "modified", "vacated", "expired"}:
            cash_status = "not_required"
        elif any(m in mechanisms for m in {"license", "settlement", "damages_verdict", "judgment", "assignment", "sale", "receivable_monetization"}):
            cash_status = "unknown"

    warnings = [
        "Observed amount events preserve their legal/transaction scope and are not summed into intrinsic patent value.",
        "Snapshot is generated from canonical events; edit the event log, not this file.",
    ]
    if "damages_verdict" in mechanisms and cash_status in {"unresolved", "unknown", "due", "contingent"}:
        warnings.append("Verdict or judgment amount is not realized cash.")
    if control_status == "operative" and cash_status == "not_required":
        warnings.append("Economic realization may occur through operative control without cash receipt.")
    if "license" in mechanisms:
        warnings.append("License economics remain at contractual/portfolio/field scope unless separately apportioned.")

    return {
        "snapshot_id": f"SNAP-{record['path_id']}",
        "schema_version": "experimental-0.1",
        "path_id": record["path_id"],
        "as_of_date": record["as_of_date"],
        "entitlement_state": entitlement,
        "realization_mechanisms": mechanisms,
        "economic_realization": {
            "cash": {"status": cash_status, "event_ids": cash_event_ids},
            "control": {"status": control_status, "event_ids": control_event_ids},
            "contractual_future_value": {
                "states": future_states,
                "event_ids": future_event_ids,
            },
        },
        "observed_amount_events": observed_amounts,
        "evidence_ids": evidence_ids,
        "warnings": warnings,
    }


def render(rows: list[dict[str, Any]]) -> str:
    snapshots = [project(row) for row in rows]
    snapshots.sort(key=lambda x: x["snapshot_id"])
    return "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
        for row in snapshots
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    generated = render(load_paths())

    if args.check:
        current = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""
        if current != generated:
            print(
                "Generated Realization Path snapshots are out of date. "
                "Run: python tools/project_realization_paths.py",
                file=sys.stderr,
            )
            return 1
        print("Realization Path snapshots are up to date.")
        return 0

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(generated, encoding="utf-8")
    print(f"Wrote Realization Path snapshots to {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
