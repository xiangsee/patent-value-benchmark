#!/usr/bin/env python3
"""Compare independent reviewer CSV exports. Research-only, no score prediction.

Export the '独立评分' sheet from each separate reviewer workbook to two CSVs.
No arguments => explicit Not Run; never pretend independent reviewers existed.
"""
from __future__ import annotations
import argparse, csv, json, math
from pathlib import Path
from typing import Any

CASE="编码"
CATS=("权项/对比核验","产业实施核验")
SCORES=("质量(0-100)","技术(0-100)","运用保护(0-100)","社会(0-100)","综合分（合格后）")

def read_csv(path:Path)->dict[str,dict[str,str]]:
    out={}
    with path.open("r",encoding="utf-8-sig",newline="") as f:
        for row in csv.DictReader(f):
            case=(row.get(CASE) or "").strip()
            if not case:continue
            if case in out:raise ValueError(f"duplicate case id: {case}")
            out[case]={k:(v or "").strip() for k,v in row.items() if k}
    return out

def kappa(labels_a:list[str],labels_b:list[str])->float|None:
    if len(labels_a)!=len(labels_b) or not labels_a:return None
    values=sorted(set(labels_a)|set(labels_b))
    obs=sum(a==b for a,b in zip(labels_a,labels_b))/len(labels_a)
    expected=sum((labels_a.count(v)/len(labels_a))*(labels_b.count(v)/len(labels_b)) for v in values)
    if math.isclose(expected,1.0):
        return None # all responses in one category: κ undefined, not 1
    return round((obs-expected)/(1-expected),4)

def compare(a:dict[str,dict[str,str]],b:dict[str,dict[str,str]])->dict[str,Any]:
    ids=sorted(set(a)&set(b))
    if not ids:
        return {"status":"Not Run","reason":"no matched submissions","matched_cases":0}
    # Check independent identities. Do not report a fake two-rater agreement.
    identities_a={a[x].get("评委内部编码","") for x in ids if a[x].get("评委内部编码")}
    identities_b={b[x].get("评委内部编码","") for x in ids if b[x].get("评委内部编码")}
    if not identities_a or not identities_b:
        return {"status":"Not Run","reason":"reviewer identities not submitted","matched_cases":len(ids)}
    if identities_a&identities_b:
        return {"status":"Invalid","reason":"reviewer identities overlap; independent review not established","matched_cases":len(ids)}
    result={"status":"Pilot only—not population inference","matched_cases":len(ids),
            "coverage":{"A":len(a),"B":len(b)},"categorical":{},"score_mae":{}}
    for key in CATS:
        pairs=[(a[x].get(key),b[x].get(key)) for x in ids if a[x].get(key) and b[x].get(key)]
        if not pairs:
            result["categorical"][key]={"pairs":0,"agreement":None,"cohen_kappa":None}
            continue
        la=[x[0] for x in pairs];lb=[x[1] for x in pairs]
        result["categorical"][key]={"pairs":len(pairs),
            "agreement":round(sum(x==y for x,y in pairs)/len(pairs),4),
            "cohen_kappa":kappa(la,lb)}
    for key in SCORES:
        pairs=[]
        for x in ids:
            try:
                if a[x].get(key) and b[x].get(key):
                    v1=float(a[x][key]);v2=float(b[x][key])
                    if 0<=v1<=100 and 0<=v2<=100:pairs.append((v1,v2))
            except ValueError:
                pass
        result["score_mae"][key]={
            "pairs":len(pairs),
            "mean_abs_difference":round(sum(abs(x-y) for x,y in pairs)/len(pairs),2) if pairs else None}
    return result

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--a",type=Path);ap.add_argument("--b",type=Path)
    args=ap.parse_args()
    if not args.a or not args.b:
        print(json.dumps({"status":"Not Run","reason":"two independent reviewer CSVs not yet supplied"},ensure_ascii=False))
        return 0
    if args.a.resolve()==args.b.resolve():
        raise SystemExit("Cannot compare a reviewer file to itself")
    print(json.dumps(compare(read_csv(args.a),read_csv(args.b)),ensure_ascii=False,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
