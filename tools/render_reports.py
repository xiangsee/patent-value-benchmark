#!/usr/bin/env python3
"""Render human-readable Markdown reports from generated diagnostics.

Usage:
  python tools/render_reports.py
  python tools/render_reports.py --check
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "diagnostics" / "generated.jsonl"
OUT_DIR = ROOT / "reports" / "generated"

def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value)
    return value.strip("-") or "diagnostic"

def fmt_value(metric: dict[str, Any]) -> str:
    value = metric.get("value")
    unit = metric.get("unit")
    period = metric.get("period")
    parts = [str(value)]
    if unit:
        parts.append(str(unit))
    if period:
        parts.append(f"({period})")
    return " ".join(parts)

def render(d: dict[str, Any]) -> str:
    state = d["current_state"]
    lines = [
        f"# Patent Value Diagnostic",
        "",
        f"**Patent:** {d['patent']['application_number']} — {d['patent']['title']}",
        f"**Ledger:** `{d['ledger_id']}`",
        f"**Mode:** {d['analysis_mode']}",
        "",
        "## Current State",
        "",
        f"- **Realization Stage:** {state['realization_stage']} — {state['stage_label']}",
        f"- **Evidence Levels Present:** {', '.join(state['evidence_levels_present']) if state['evidence_levels_present'] else 'None recorded'}",
        f"- **Exact Patent → Value Carrier:** {state['exact_patent_value_carrier_link']}",
        f"- **Patent-level Attributable Value:** {state['patent_level_attributable_value']}",
        "",
        "## Observability",
        "",
    ]
    for k, v in state["observability"].items():
        lines.append(f"- **{k}:** {v}")

    lines += ["", "## Confirmed Chain", ""]
    carriers = d["confirmed_chain"]["value_carriers"]
    links = d["confirmed_chain"]["links"]
    if not carriers and not links:
        lines.append("No non-Unknown patent-to-value-carrier chain is currently established.")
    else:
        for c in carriers:
            lines.append(f"- Value Carrier: **{c['name']}** ({c['carrier_type']}; {c['link_status']})")
        for l in links:
            lines.append(f"- `{l['from_node']}` → `{l['to_node']}` — **{l['relation']}** ({l['status']})")

    lines += ["", "## Observed Metrics", ""]
    if not d["observed_metrics"]:
        lines.append("No value metric is currently recorded.")
    else:
        for m in d["observed_metrics"]:
            lines.append(
                f"- **{m['metric_name']}**: {fmt_value(m)} — scope=`{m['scope_level']}`, attribution=`{m['attribution_status']}`"
            )

    lines += ["", "## Unresolved Gaps", ""]
    if not d["unresolved_gaps"]:
        lines.append("No unresolved gap is recorded.")
    else:
        for g in d["unresolved_gaps"]:
            lines.append(f"- **{g['gap_type']}**: {g['description']} (observability: `{g['observability']}`)")

    lines += ["", "## Next Evidence Tasks", ""]
    if not d["next_evidence_tasks"]:
        lines.append("No next evidence task is generated.")
    else:
        for t in d["next_evidence_tasks"]:
            lines.append(f"- **{t['task_id']} → {t['target_evidence_level']}**: {t['objective']}")
            for need in t["needed_evidence"]:
                lines.append(f"  - {need}")

    lines += ["", "## Warnings", ""]
    for warning in d["warnings"]:
        lines.append(f"- {warning}")

    lines += [
        "",
        "## Output Limits",
        "",
        "- Gold probability: **not produced**",
        "- Unsupported patent valuation amount: **not produced**",
        "- Automatic ranking: **not produced**",
        "",
        "---",
        "Generated deterministically from the Patent Value Ledger. Edit the Ledger/Evidence, not this report.",
        "",
    ]
    return "\n".join(lines)

def expected_files() -> dict[Path, str]:
    diagnostics = []
    for line in INPUT.read_text(encoding="utf-8").splitlines():
        if line.strip():
            diagnostics.append(json.loads(line))
    out = {}
    for d in diagnostics:
        path = OUT_DIR / f"{slug(d['diagnostic_id'])}.md"
        out[path] = render(d)
    return out

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = expected_files()

    if args.check:
        actual_paths = set(OUT_DIR.glob("*.md")) if OUT_DIR.exists() else set()
        if actual_paths != set(expected):
            print("Generated report file set is out of date. Run: python tools/render_reports.py", file=sys.stderr)
            return 1
        for path, content in expected.items():
            if path.read_text(encoding="utf-8") != content:
                print(f"Generated report is out of date: {path.relative_to(ROOT)}", file=sys.stderr)
                return 1
        print(f"Reports up to date: {len(expected)} report(s).")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in OUT_DIR.glob("*.md"):
        path.unlink()
    for path, content in expected.items():
        path.write_text(content, encoding="utf-8")
    print(f"Wrote {len(expected)} report(s) to {OUT_DIR.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
