#!/usr/bin/env python3
"""Create a cold-start contribution skeleton for one patent.

Example:
  python tools/scaffold_ledger.py \
    --application-number ZL202012345678.9 \
    --title "一种示例方法"

Historical mode:
  python tools/scaffold_ledger.py \
    --application-number ZL202012345678.9 \
    --title "一种示例方法" \
    --t0 2024-02-05

The script creates three contribution files:
- data/source-registry/contrib-<patent>.jsonl
- data/evidence/contrib-<patent>.jsonl
- data/ledgers/contrib-<patent>.jsonl

The Source and Evidence files start empty. The Ledger starts conservatively at R0.
Unknown is intentional and valid.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def safe_id(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")


def ensure_new(path: Path) -> None:
    if path.exists():
        raise FileExistsError(
            f"{path.relative_to(ROOT)} already exists. "
            "Choose a different patent number or remove the draft explicitly."
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--application-number", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--assignee", action="append", default=[])
    parser.add_argument("--t0", help="YYYY-MM-DD for historical cutoff mode")
    parser.add_argument(
        "--as-of-date",
        default=date.today().isoformat(),
        help="Observation date; defaults to today.",
    )
    args = parser.parse_args()

    stem = safe_id(args.application_number)
    source_path = ROOT / "data" / "source-registry" / f"contrib-{stem}.jsonl"
    evidence_path = ROOT / "data" / "evidence" / f"contrib-{stem}.jsonl"
    ledger_path = ROOT / "data" / "ledgers" / f"contrib-{stem}.jsonl"

    for path in (source_path, evidence_path, ledger_path):
        ensure_new(path)
        path.parent.mkdir(parents=True, exist_ok=True)

    historical = bool(args.t0)
    ledger = {
        "ledger_id": f"LEDGER-{stem}",
        "schema_version": "1.0",
        "analysis_mode": "public",
        "patent": {
            "application_number": args.application_number,
            "publication_number": None,
            "grant_number": None,
            "title": args.title,
            "assignees": args.assignee,
            "filing_date": None,
            "earliest_priority_date": None,
            "grant_date": None,
            "family_note": None,
        },
        "observation": {
            "as_of_date": args.as_of_date,
            "t0_date": args.t0 if historical else None,
            "time_policy": "historical_t0_cutoff" if historical else "current_state",
            "post_t0_ground_truth_allowed": False,
        },
        "knowledge_origin": {
            "status": "unknown",
            "description": None,
            "origin_types": ["unknown"],
            "evidence_ids": [],
        },
        "technology": {
            "problem": "TODO: describe the concrete technical problem.",
            "mechanism": "TODO: describe the claimed technical mechanism.",
            "relative_differentiation": "unknown",
            "comparison_baseline": None,
            "evidence_ids": [],
        },
        "value_carriers": [
            {
                "carrier_id": f"VC-{stem}-1",
                "carrier_type": "unknown",
                "name": "待确认价值载体",
                "link_status": "unknown",
                "description": None,
                "evidence_ids": [],
            }
        ],
        "value_links": [],
        "value_metrics": [],
        "v0_7_state": {
            "value_state": {
                "technical_differentiation": "unknown",
                "value_carrier_centrality": "unknown",
                "real_world_validation": "unknown",
                "scale_diffusion": "unknown",
                "industry_social_impact": "unknown",
            },
            "attribution_evidence_state": {
                "evidence_levels_present": [],
                "exact_patent_value_carrier_link": "unknown",
                "patent_level_attributable_value": "unknown",
                "evidence_ids": [],
            },
            "observability_state": {
                "enterprise": "unknown",
                "product_project": "unknown",
                "exact_patent_mapping": "unknown",
                "attributable_value": "unknown",
            },
            "realization_stage": "R0",
            "realization_stage_evidence_ids": [],
        },
        "gaps": [
            {
                "gap_type": "technical_comparison",
                "description": "Need a reproducible comparison against relevant prior/baseline technology.",
                "needed_evidence": ["prior-art comparison", "technical benchmark or independent technical source"],
                "observability": "unknown",
            },
            {
                "gap_type": "exact_patent_mapping",
                "description": (
                    "Need to determine whether THIS exact patent number maps to a specific value carrier. "
                    "Do not inherit mapping from a sibling/same-day family patent cited in secondary sources."
                ),
                "needed_evidence": [
                    "product/patent mapping that names this patent number",
                    "regulated disclosure",
                    "technical documentation",
                    "implementation proof",
                ],
                "observability": "unknown",
            },
            {
                "gap_type": "patent_value_attribution",
                "description": (
                    "Portfolio / program narratives (e.g. '300+ patents supporting the product') are "
                    "enterprise/product scope. Do not auto-upgrade this single patent to R3+/R5."
                ),
                "needed_evidence": [
                    "E3 naming this patent number",
                    "optional E4 for patent-level attributable value",
                ],
                "observability": "unknown",
            },
        ],
        "source_ids": [],
        "review_status": "draft",
        "notes": (
            "Cold-start scaffold. Keep Unknown where evidence is not yet sufficient. "
            "Traps: (1) sibling-family false mapping; (2) R0+E2 is allowed but does not raise R; "
            "(3) portfolio 300+ narratives do not inherit to this patent. "
            "See docs/cold-start-trap-checklist.md."
        ),
    }

    source_path.write_text("", encoding="utf-8")
    evidence_path.write_text("", encoding="utf-8")
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False) + "\n", encoding="utf-8")

    print("Created:")
    for path in (source_path, evidence_path, ledger_path):
        print(f"  - {path.relative_to(ROOT)}")
    print()
    print("Next:")
    print("  1. Add source records.")
    print("  2. Add evidence records.")
    print("  3. Update the Ledger only as far as evidence allows.")
    print("  4. Run: python tools/validate_data.py")
    print("  5. Run: python tools/generate_diagnostics.py")
    print("  6. Run: python tools/render_reports.py")
    print("  7. Re-run validation/checks before opening a PR.")
    print()
    print("Cold-start traps (do not skip):")
    print("  - Sibling / same-day family patents: never inherit exact mapping from a peer number.")
    print("  - R0 + E2 is allowed; R0 + E2 ≠ R3 (product-layer evidence does not raise R alone).")
    print("  - '300+ patent portfolio' narratives are product/enterprise scope — no auto R3+/R5.")
    print("  Checklist: docs/cold-start-trap-checklist.md")
    print("  Round 2 synthesis (V0.8 NOT adopted):")
    print("    analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except FileExistsError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)
