#!/usr/bin/env python3
"""Claim Version Gate v0.3 - research-only, synthetic fixtures.

No legal validity decision, E3 upgrade, expert score or monetary value is returned.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

DATA=Path(__file__).resolve().parents[1]/"data"/"experimental"/"claim-version"/"synthetic-fixtures.jsonl"

def _date(value:Any)->date|None:
    try:
        return date.fromisoformat(value)
    except (ValueError,TypeError):
        return None

def _source(source:Any)->bool:
    return isinstance(source,dict) and source.get("doc_id") and str(source.get("url","")).startswith("https://")

def inspect_claim_version(case:dict)->dict:
    out={"case_id":case.get("case_id"),"status":"Blocked",
         "claim_scope_review_allowed":False,"legal_validity":None,
         "E3":"Unknown","E4":"Unknown","award_score":None,
         "monetary_value":None,"reason":""}
    ctx=case.get("context") or {}
    t0=_date(ctx.get("as_of_date"))
    priority=_date(ctx.get("priority_date"))
    grant_date=_date(ctx.get("grant_date"))
    if not all((ctx.get("application_id"),ctx.get("jurisdiction"),
                t0,priority,grant_date)):
        out["reason"]="CV0 missing identity, jurisdiction or dates"
        return out
    if t0<grant_date:
        out["reason"]="CV0 historical T0 predates grant; B cannot be backfilled"
        return out
    if priority>grant_date:
        out["reason"]="CV0 chronological inconsistency"
        return out
    a=case.get("publication_A")
    b=case.get("grant_B")
    if not _source(b) or b.get("kind")!="B":
        out["reason"]="CV1 no authoritative versioned B text source"
        return out
    if not _source(a) or a.get("kind")!="A":
        out.update(status="Preliminary",reason="CV1 A/B source pairing not complete")
        return out
    if a.get("application_id")!=ctx["application_id"] or b.get("application_id")!=ctx["application_id"]:
        out["reason"]="CV1 A/B documents do not belong to same exact application"
        return out
    if not b.get("independent_claim_ids") or not b.get("grant_claim_elements"):
        out.update(status="Preliminary",reason="CV2 B independent claims/elements not mapped")
        return out
    if not set(b["independent_claim_ids"]).issubset(set(b["grant_claim_elements"])):
        out["reason"]="CV2 elements do not map to each asserted independent grant claim"
        return out
    if not all(isinstance(b["grant_claim_elements"][cid],list) and
               len(b["grant_claim_elements"][cid])>=2
               for cid in b["independent_claim_ids"]):
        out.update(status="Preliminary",reason="CV2 insufficient element-by-element mapping")
        return out
    diff=case.get("comparison") or {}
    if (diff.get("comparison_type")!="element_level" or
        diff.get("reviewed") is not True or
        not isinstance(diff.get("material_change_notes"),list) or
        not diff.get("material_change_notes")):
        out.update(status="Preliminary",reason="CV2 counts/abstract are no substitute for A->B element comparison")
        return out
    prior=case.get("prior_art_candidates") or []
    if not prior:
        out.update(status="Preliminary",reason="CV3 no traceable technical comparison candidates")
        return out
    for item in prior:
        if not item.get("doc_id") or not str(item.get("url","")).startswith("https://"):
            out["reason"]="CV3 prior-art candidate has no traceable source"
            return out
        pubdate=_date(item.get("publication_date"))
        if not pubdate:
            out.update(status="Preliminary",reason="CV3 missing publication date")
            return out
        if item.get("role")=="pre_priority_baseline" and pubdate>priority:
            out["reason"]="CV3 post-priority publication cannot be used as pre-priority baseline"
            return out
    out.update(status="Claim-scoped research",claim_scope_review_allowed=True,
               reason="CV0-CV3 allow research; validity, E3/E4 and monetary value unverified")
    return out

def main()->int:
    fails=[]
    with DATA.open(encoding="utf-8") as f:
        lines=[json.loads(s) for s in f if s.strip()]
    for case in lines:
        outcome=inspect_claim_version(case)
        if outcome["status"] != case["expected_status"]:
            fails.append(f"{case['case_id']}: expected {case['expected_status']}, got {outcome['status']}: {outcome['reason']}")
        if outcome["legal_validity"] is not None or outcome["E3"]!="Unknown" or outcome["E4"]!="Unknown" or outcome["monetary_value"] is not None or outcome["award_score"] is not None:
            fails.append(f"{case['case_id']}: unsafe result leaked")
    if fails:
        print("\n".join(fails))
        return 1
    print(f"Claim Version Gate v0.3: {len(lines)} synthetic cases PASS; legal/score/money fields remain None/Unknown")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
