#!/usr/bin/env python3
"""Create a cold-start contribution skeleton for one patent.

Example:
  python tools/scaffold_ledger.py \
    --application-number ZL202012345678.9 \
    --title "一种示例方法" \
    --assignee "权利人名称" \
    --publication-number CN123456789A \
    --grant-number CN123456789B \
    --filing-date 2020-06-22 \
    --grant-date 2024-02-02

Historical mode:
  python tools/scaffold_ledger.py \
    --application-number ZL202012345678.9 \
    --title "一种示例方法" \
    --t0 2024-02-05

Optional bibliographic flags (--publication-number, --grant-number,
--filing-date, --grant-date, --earliest-priority-date, --family-note) reduce
hand-fill. Look them up on Google Patents / CNIPA / USPTO — this tool does
not scrape patent offices.

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


def build_ledger(
    *,
    application_number: str,
    title: str,
    assignees: list[str],
    as_of_date: str,
    t0: str | None = None,
    publication_number: str | None = None,
    grant_number: str | None = None,
    filing_date: str | None = None,
    grant_date: str | None = None,
    earliest_priority_date: str | None = None,
    family_note: str | None = None,
) -> dict:
    """Build a conservative R0 ledger dict (no I/O)."""
    stem = safe_id(application_number)
    historical = bool(t0)
    missing_biblio = [
        name
        for name, value in (
            ("publication_number", publication_number),
            ("grant_number", grant_number),
            ("filing_date", filing_date),
            ("grant_date", grant_date),
        )
        if not value
    ]
    biblio_hint = (
        "Bibliographic fields still null — fill from patent literature "
        "(Google Patents / CNIPA / USPTO) or re-run scaffold with "
        "--publication-number / --grant-number / --filing-date / --grant-date. "
        if missing_biblio
        else "Bibliographic flags supplied at scaffold time. "
    )
    return {
        "ledger_id": f"LEDGER-{stem}",
        "schema_version": "1.0",
        "analysis_mode": "public",
        "patent": {
            "application_number": application_number,
            "publication_number": publication_number,
            "grant_number": grant_number,
            "title": title,
            "assignees": assignees,
            "filing_date": filing_date,
            "earliest_priority_date": earliest_priority_date,
            "grant_date": grant_date,
            "family_note": family_note,
        },
        "observation": {
            "as_of_date": as_of_date,
            "t0_date": t0 if historical else None,
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
            + biblio_hint
            + "evidence_levels_present: list only levels with status≠unknown support; "
            "sought-but-not-found E3 rows (status=unknown) may stay in evidence for audit "
            "but must NOT put E3 in evidence_levels_present. "
            "Traps: (1) sibling-family false mapping; (2) R0+E2 is allowed but does not raise R; "
            "(3) portfolio 300+ narratives do not inherit to this patent; "
            "(4) project/product news dated before this application filing ≈ nearly always another case. "
            "carrier_type hint: mechanical inventions often use equipment or component "
            "(also process/material/product_system/… — see schema enum; do not leave unknown forever once known). "
            "See docs/cold-start-trap-checklist.md."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Create a cold-start Source/Evidence/Ledger skeleton. "
            "Optional bibliographic flags reduce hand-fill; look up values on "
            "Google Patents / CNIPA / USPTO (no office scrapers)."
        )
    )
    parser.add_argument("--application-number", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--assignee", action="append", default=[])
    parser.add_argument("--t0", help="YYYY-MM-DD for historical cutoff mode")
    parser.add_argument(
        "--as-of-date",
        default=date.today().isoformat(),
        help="Observation date; defaults to today.",
    )
    parser.add_argument(
        "--publication-number",
        default=None,
        help="Optional. e.g. CN111859886A — from patent literature, not scraped.",
    )
    parser.add_argument(
        "--grant-number",
        default=None,
        help="Optional. e.g. CN111859886B / US8278036B2 — from patent literature.",
    )
    parser.add_argument(
        "--filing-date",
        default=None,
        help="Optional YYYY-MM-DD filing date from patent literature.",
    )
    parser.add_argument(
        "--grant-date",
        default=None,
        help="Optional YYYY-MM-DD grant date from patent literature.",
    )
    parser.add_argument(
        "--earliest-priority-date",
        default=None,
        help="Optional YYYY-MM-DD earliest priority date.",
    )
    parser.add_argument(
        "--family-note",
        default=None,
        help="Optional note about sibling/family peers to avoid false mapping.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    stem = safe_id(args.application_number)
    source_path = ROOT / "data" / "source-registry" / f"contrib-{stem}.jsonl"
    evidence_path = ROOT / "data" / "evidence" / f"contrib-{stem}.jsonl"
    ledger_path = ROOT / "data" / "ledgers" / f"contrib-{stem}.jsonl"

    for path in (source_path, evidence_path, ledger_path):
        ensure_new(path)
        path.parent.mkdir(parents=True, exist_ok=True)

    ledger = build_ledger(
        application_number=args.application_number,
        title=args.title,
        assignees=args.assignee,
        as_of_date=args.as_of_date,
        t0=args.t0,
        publication_number=args.publication_number,
        grant_number=args.grant_number,
        filing_date=args.filing_date,
        grant_date=args.grant_date,
        earliest_priority_date=args.earliest_priority_date,
        family_note=args.family_note,
    )

    source_path.write_text("", encoding="utf-8")
    evidence_path.write_text("", encoding="utf-8")
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False) + "\n", encoding="utf-8")

    missing = [
        flag
        for flag, value in (
            ("--publication-number", args.publication_number),
            ("--grant-number", args.grant_number),
            ("--filing-date", args.filing_date),
            ("--grant-date", args.grant_date),
        )
        if not value
    ]

    print("Created:")
    for path in (source_path, evidence_path, ledger_path):
        print(f"  - {path.relative_to(ROOT)}")
    print()
    if missing:
        print("Bibliographic fields left null (hand-fill or re-scaffold with flags):")
        for flag in missing:
            print(f"  - {flag}")
        print("  Hint: look up on Google Patents / CNIPA / USPTO — no scrapers in this tool.")
        print()
    print("Next:")
    print("  1. Add source records.")
    print("  2. Add evidence records.")
    print("     - Sought-but-not-found E3 may use status=unknown in the evidence file.")
    print("     - Do NOT put E3 in evidence_levels_present unless status≠unknown support exists.")
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
    print("  - evidence_levels_present: supporting levels only (status≠unknown); unknown-E3 ≠ present.")
    print("  - Project/product news dated BEFORE this application filing ≈ nearly always another case.")
    print("  carrier_type hint (mechanical stumble): prefer equipment or component when that fits;")
    print("    also process / material / product_system / software_algorithm / … (schema enum).")
    print("    Do not leave carrier_type=unknown forever once the carrier class is known.")
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
