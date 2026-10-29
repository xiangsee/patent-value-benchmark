#!/usr/bin/env python3
"""Applied Assessment / Valuation Gate v0.2 — research-only.

Deliberately outputs NO patent dollar amount and NO V0.7 universal score.
This evaluator tests whether a context-specific award score or an indicative
valuation study is even allowed to proceed.

All fixtures in this public repository are synthetic; client records remain local.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"experimental"/"applied-gates"/"synthetic-fixtures.jsonl"
DIMENSIONS={"quality":.25,"technical":.25,"use_protection":.35,"social":.15}
GATES=tuple(f"G{i}" for i in range(5))

def _get_evidence(registry: list[dict], eid: str, subject: str, stage: str, t0: date)->bool:
    for rec in registry:
        if (rec.get("evidence_id")==eid and rec.get("subject_id")==subject
            and rec.get("stage")==stage and rec.get("verification_status")=="verified"
            and rec.get("verified_by") and rec.get("observed_date")):
            try:
                if date.fromisoformat(rec["observed_date"])<=t0:
                    return True
            except (ValueError,TypeError):
                pass
    return False

def evaluate(record: dict[str,Any])->dict[str,Any]:
    result={"case_id":record.get("case_id"),"assessment_status":"Not Ready",
            "award_score":None,"valuation_status":"L0: Not Valuation Ready",
            "value_amount":None,"warnings":[]}
    ctx=record.get("context") or {}
    subj=ctx.get("subject_id")
    try:t0=date.fromisoformat(ctx.get("as_of_date",""))
    except (TypeError,ValueError):t0=None
    reg=record.get("evidence_registry") or []
    if not subj or not t0:
        result["warnings"].append("G0: specific subject and as-of date required")
        return result

    # Award assessment: a context-specific, two-human-reviewed instrument,
    # not a universal patent quality or value score.
    a=record.get("assessment") or {}
    reviewers=a.get("reviewers") or []
    ids=[r.get("reviewer_id") for r in reviewers if r.get("independent_submission")]
    dims=a.get("dimensions") or {}
    all_dim_evidence=True
    weighted=0.0
    for name,weight in DIMENSIONS.items():
        d=dims.get(name) or {}
        score=d.get("score")
        if not isinstance(score,(int,float)) or isinstance(score,bool) or not (0<=score<=100):
            all_dim_evidence=False
            continue
        refs=d.get("evidence_ids") or []
        if not refs or not all(_get_evidence(reg,e,subj,"SCORE_"+name,t0) for e in refs):
            all_dim_evidence=False
        weighted+=weight*score
    reconciliation=a.get("reconciliation_evidence_id")
    recon_valid=(bool(reconciliation) and _get_evidence(reg,reconciliation,subj,"RECONCILIATION",t0))
    if (len(ids)>=2 and len(set(ids))==len(ids) and all_dim_evidence
        and recon_valid and a.get("evidence_complete") is True):
        result["assessment_status"]="Ready: Track B reviewed score"
        result["award_score"]=round(weighted,1)
    else:
        result["warnings"].append("Award score suppressed: independent reviews or evidence incomplete")

    # Monetary valuation requires a parallel gate; high award score is NEVER an input.
    v=record.get("valuation") or {}
    if not v:
        result["warnings"].append("Valuation not requested or defined")
        return result
    fields=("purpose","basis_of_value","rights_subject_type","method","economic_object")
    if not all(v.get(k) for k in fields):
        result["warnings"].append("G0: purpose, basis, method and rights object required")
        return result
    if v["economic_object"] != subj:
        result["warnings"].append("G2: economic object differs from subject")
        return result
    byid={g.get("gate_id"):g for g in v.get("gates") or []}
    for gid in GATES:
        gate=byid.get(gid) or {}
        refs=gate.get("evidence_ids") or []
        if (gate.get("status")!="passed" or gate.get("subject_id")!=subj
            or not gate.get("reviewer_id") or not refs
            or not all(_get_evidence(reg,eid,subj,gid,t0) for eid in refs)):
            result["warnings"].append(f"{gid}: unverified / subject mismatch / missing evidence")
            return result
    # Model cannot generate a number from just 'Passed'. An attributable
    # economic-input source must exist and be identified at the same scope.
    inputs=v.get("input_evidence_ids") or []
    if not inputs or not all(_get_evidence(reg,e,subj,"VALUATION_INPUT",t0) for e in inputs):
        result["warnings"].append("Economic parameter source is missing or cannot be attributed")
        return result
    result["valuation_status"]="L2: eligible to develop indicative range"
    result["warnings"].append("L2 is NOT a monetary valuation result or formal appraisal")
    return result

def main()->int:
    failed=0;count=0
    with DATA.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():continue
            record=json.loads(line); count+=1
            obs=evaluate(record)
            expected=record.get("expected",{})
            if obs["assessment_status"]!=expected.get("assessment_status") or obs["valuation_status"]!=expected.get("valuation_status"):
                failed+=1
                print("FAIL",obs["case_id"],obs,"expected",expected)
    if failed:
        print(f"Failed: {failed}/{count} synthetic fixtures")
        return 1
    print(f"Passed: {count} synthetic applied-gate fixtures; no monetary output generated.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
