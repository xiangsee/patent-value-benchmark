#!/usr/bin/env python3
"""Generate deterministic Patent Value Diagnostics from Patent Value Ledgers.

The generator adds no new evidence and performs no scoring.
It only transforms the ledger into a standardized diagnostic output.

Usage:
  python tools/generate_diagnostics.py
  python tools/generate_diagnostics.py --check
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LEDGER_GLOB = "data/ledgers/*.jsonl"
OUTPUT_PATH = ROOT / "data" / "diagnostics" / "generated.jsonl"

STAGE_LABELS = {
    "R0": "Right Exists",
    "R1": "Market / Transfer Intent",
    "R2": "Rights Transaction",
    "R3": "Implemented in Value Carrier",
    "R4": "Scaled Real-world Validation",
    "R5": "Patent-level Attributable Value",
    "unknown": "Unknown",
}

GAP_OBJECTIVES = {
    "knowledge_origin": ("补齐知识/技术来源链", "E1"),
    "technical_comparison": ("建立相对现有技术的可复核比较", "E5"),
    "exact_patent_mapping": ("建立 exact patent → value carrier 映射", "E3"),
    "implementation": ("证明专利已经实施到具体价值载体", "E3"),
    "scale_validation": ("补充规模化真实世界验证", "E2"),
    "patent_value_attribution": ("建立专利级性能、成本或经济价值归因", "E4"),
    "independent_verification": ("补充独立核验证据", "E5"),
    "other": ("补齐Ledger列明的证据缺口", "unknown"),
}

def load_jsonl(pattern: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(ROOT.glob(pattern)):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    return rows

def diagnostic_from_ledger(ledger: dict[str, Any]) -> dict[str, Any]:
    state = ledger["v0_7_state"]
    attr = state["attribution_evidence_state"]
    observability = state["observability_state"]
    stage = state["realization_stage"]

    carriers = [{
        "carrier_id": c["carrier_id"],
        "name": c["name"],
        "carrier_type": c["carrier_type"],
        "link_status": c["link_status"],
        "evidence_ids": c.get("evidence_ids", []),
    } for c in ledger.get("value_carriers", []) if c.get("link_status") != "unknown"]

    links = [{
        "link_id": l["link_id"],
        "from_node": l["from_node"],
        "to_node": l["to_node"],
        "relation": l["relation"],
        "status": l["status"],
        "evidence_ids": l.get("evidence_ids", []),
    } for l in ledger.get("value_links", []) if l.get("status") != "unknown"]

    metrics = [{
        "metric_id": m["metric_id"],
        "scope_level": m["scope_level"],
        "metric_name": m["metric_name"],
        "value": m.get("value"),
        "unit": m.get("unit"),
        "period": m.get("period"),
        "attribution_status": m["attribution_status"],
        "evidence_ids": m.get("evidence_ids", []),
    } for m in ledger.get("value_metrics", [])]

    gaps = []
    tasks = []
    for index, gap in enumerate(ledger.get("gaps", []), 1):
        gaps.append({
            "gap_type": gap["gap_type"],
            "description": gap["description"],
            "needed_evidence": gap.get("needed_evidence", []),
            "observability": gap["observability"],
        })
        objective, level = GAP_OBJECTIVES.get(gap["gap_type"], GAP_OBJECTIVES["other"])
        tasks.append({
            "task_id": f"TASK-{index:02d}",
            "gap_type": gap["gap_type"],
            "objective": objective,
            "target_evidence_level": level,
            "needed_evidence": gap.get("needed_evidence", []),
        })

    warnings = [
        "Enterprise or product value must not be automatically inherited by the exact patent.",
        "Unknown means unobserved or unresolved, not zero value.",
    ]
    product_metrics = [m for m in metrics if m["scope_level"] == "product_project"]
    exact_metrics = [m for m in metrics if m["scope_level"] == "exact_patent"]

    if product_metrics and attr["patent_level_attributable_value"] == "unknown":
        warnings.append("Product/project metrics are available, but patent-level attributable value remains Unknown.")
    if stage == "R4" and not exact_metrics:
        warnings.append("R4 confirms scaled real-world validation; it does not establish R5 patent-level attributable value.")
    if ledger["observation"]["time_policy"] == "historical_t0_cutoff":
        warnings.append(
            f"Historical diagnostic is frozen at T0={ledger['observation']['t0_date']}; post-T0 information must not be backfilled."
        )

    return {
        "diagnostic_id": f"DIAG-{ledger['ledger_id']}",
        "schema_version": "1.0-draft",
        "ledger_id": ledger["ledger_id"],
        "patent": {
            "application_number": ledger["patent"]["application_number"],
            "title": ledger["patent"]["title"],
        },
        "analysis_mode": ledger["analysis_mode"],
        "current_state": {
            "realization_stage": stage,
            "stage_label": STAGE_LABELS[stage],
            "evidence_levels_present": attr["evidence_levels_present"],
            "realization_stage_evidence_ids": state["realization_stage_evidence_ids"],
            "exact_patent_value_carrier_link": attr["exact_patent_value_carrier_link"],
            "patent_level_attributable_value": attr["patent_level_attributable_value"],
            "observability": observability,
        },
        "confirmed_chain": {"value_carriers": carriers, "links": links},
        "observed_metrics": metrics,
        "unresolved_gaps": gaps,
        "next_evidence_tasks": tasks,
        "warnings": warnings,
        "output_limits": {
            "gold_probability": False,
            "unsupported_patent_value_amount": False,
            "automatic_ranking": False,
        },
    }

def render(rows: list[dict[str, Any]]) -> str:
    diagnostics = [diagnostic_from_ledger(row) for row in rows]
    diagnostics.sort(key=lambda x: x["diagnostic_id"])
    return "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in diagnostics)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    ledgers = load_jsonl(LEDGER_GLOB)
    generated = render(ledgers)

    if args.check:
        current = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""
        if current != generated:
            print("Generated diagnostics are out of date. Run: python tools/generate_diagnostics.py", file=sys.stderr)
            return 1
        print(f"Diagnostics up to date: {len(ledgers)} ledger(s).")
        return 0

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(generated, encoding="utf-8")
    print(f"Wrote {len(ledgers)} diagnostic(s) to {OUTPUT_PATH.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
