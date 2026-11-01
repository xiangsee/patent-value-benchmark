#!/usr/bin/env python3
"""Conservative prior-publication screening for claim-scoped review.

Research only. The results cannot establish statutory prior art, validity,
infringement, E3/E4, or valuation. Uses synthetic fixture data in public CI.
"""
from __future__ import annotations
import json
from datetime import date
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
FIXTURES=ROOT/"data"/"experimental"/"prior-publication"/"synthetic-fixtures.jsonl"

def parse_date(value:Any)->date|None:
    try:return date.fromisoformat(value)
    except (ValueError,TypeError):return None

def audit_case(case:dict)->dict:
    out={"id":case.get("id"),"status":"UNTRACED","chronology_ok":False,
         "ready_for_claim_review":False,"legal_validity":None,
         "E3":"Unknown","E4":"Unknown","monetary_value":None,
         "reason":""}
    subject=case.get("subject") or {}
    item=case.get("comparator") or {}
    cutoff=parse_date(subject.get("claimed_priority_date"))
    publication_date=parse_date(item.get("publication_date"))
    if (not subject.get("grant_independent_claim_id") or not cutoff or
        not item.get("publication_id") or not publication_date or
        not str(item.get("source_url","")).startswith("https://")):
        out["reason"]="missing subject cutoff, claim, exact publication, publication date or source"
        return out
    if publication_date>cutoff:
        out["status"]="POST_CUTOFF"
        out["reason"]="cited publication version became public after subject cutoff; find earlier A only if its disclosed content actually matches"
        return out
    out["status"]="TIME_ELIGIBLE_UNMAPPED"
    out["chronology_ok"]=True
    element_map=item.get("element_map") or []
    reviewed=item.get("reviewed_by")
    if not reviewed or len(element_map)<2:
        out["reason"]="timely publication alone is not a documented grant-claim element comparison"
        return out
    seen=set()
    for entry in element_map:
        if not isinstance(entry,dict) or not entry.get("grant_element") or not entry.get("comparator_anchor") or not entry.get("difference_note"):
            out["reason"]="incomplete per-element mapping or missing source anchor"
            return out
        if entry["grant_element"] in seen:
            out["reason"]="duplicate grant element with no independent mapping"
            return out
        seen.add(entry["grant_element"])
    out["status"]="ELEMENT_MAPPED_REVIEW"
    out["ready_for_claim_review"]=True
    out["reason"]="temporal and element-mapping dossier ready for expert review; not a novelty/invalidity opinion"
    return out

def main()->int:
    rows=[json.loads(line) for line in FIXTURES.read_text(encoding="utf-8").splitlines() if line.strip()]
    fail=[]
    for row in rows:
        r=audit_case(row)
        if r["status"]!=row["expected_status"]:
            fail.append(f"{row['id']}: expected {row['expected_status']}, got {r['status']}")
        if r["legal_validity"] is not None or r["E3"]!="Unknown" or r["E4"]!="Unknown" or r["monetary_value"] is not None:
            fail.append(f"{row['id']}: unsafe legal or economic conclusion")
    if fail:
        print("\n".join(fail));return 1
    print(f"Prior-publication screening PASS: {len(rows)} synthetic cases; legal, E3/E4 and money remain Unknown/None")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
