# World-Class Patent Value Assessment — Research Roadmap

> Status: **research program document** (2026-10-14 Asia/Shanghai)  
> Formal surface: **V0.7 adopted** + **schema 1.0 frozen** ([v0.1.0](https://github.com/xiangsee/patent-value-benchmark/releases/tag/v0.1.0))  
> V0.8: design draft + probes + optional RC parallel plan — **not adopted, schema not frozen**  
> This page does **not** authorize adopt / freeze / S1 promotion / ordinary contrib expansion.

## 1. Ambition (honest)

Goal: extend Xiangsee Patent Value Benchmark toward a **world-class, evidence-first patent value assessment model** — globally usable, falsifiable, and better than score-only or citation-only systems at answering:

> What value is claimed, for which construct, under which T0, with which attribution, and what remains Unknown?

“World-class” here means **discipline + external validity + comparative transparency**, not a marketing claim of dollar accuracy or universal ranking.

## 2. Four ongoing tracks

| Track | Question | Near-term work | Maps to |
|---|---|---|---|
| **T1 Theory research** | What *kinds* of patent value exist, and which layers must stay separate? | **memo v0** → [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md)；**DEMPE⊥E3–E4** → [`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md) | Formal: V0.7 four layers. Research: design draft + RC/RP/CF overviews |
| **T2 Comparison of existing models** | How do IVS / royalty / citation / ML score / award proxies / litigation damages differ from us? | **v0 matrix** → [`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md)；**deepen** → [`t2-v07-to-ivs-oecd-practice-schools.md`](t2-v07-to-ivs-oecd-practice-schools.md)；**场景树** → [`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md) | Docs under `docs/methodology/` + `analysis/theory/`；not schema |
| **T3 Own innovation testing** | Do RC / RP / Network / Horizon / optional parallel RC improve diagnosis without false inheritance? | P1–P8（+ **P7 Horizon** / **P8 Network vocabulary**）；optional RC plan (Gate 0)；**no-ruling fixture** `data/experimental/rights-control/fixture-no-ruling-ordinary-r0.jsonl`；**no** V0.8 adopt | Research / experimental schemas only |
| **T4 Real-world effect validation** | On unseen patents, does the model refuse false R3+ and allow honest R3 when E3 maps—and can it reach **E4** without inheritance? | H/E3/E4 + INT R1/R2 已编码；**跨法域合成** → [`holdout-t4-cross-jurisdiction-synthesis.md`](../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md)（CN/US/JP/KR；INT-2/4/6/8/10/12 仍提名） | Formal V0.7 when encoding; prereg: [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md) |

Tracks are **parallel**. Winning on T3 probes does not auto-adopt V0.8. Winning on T4 discipline does not equal prediction of future cash.

## 3. Formal vs research surface

```text
FORMAL (ship / reproduce / cold-start)
  V0.7 Evidence & Realization Architecture
  Ledger + Diagnostic schema 1.0
  Unknown ≠ 0 · non-inheritance · T0 cutoff · Screening ≠ Proof

RESEARCH (docs / experimental / analysis)
  V0.8 design draft · RC experimental-0.1 · RP experimental-0.1
  CF analysis-only (no CF schema)
  Extrapolation holdouts · E3 probes · world-class roadmap (this page)
```

Promotion rule: **explicit user decision** for adopt / freeze / S1. Round 2 readiness ≠ adopt. Extrapolation success ≠ adopt.

## 4. Near-term milestones (next 1–2 cycles)

1. **T4 nominations / encode** — CN 波已完成（见 phase synthesis）。International Round 1：**INT-1/3/5 已编码**（R0/R3/R5）；INT-2/4/6 仍提名 → [`t4-international-holdout-nominees-round1.md`](t4-international-holdout-nominees-round1.md)。**Round 2 JP/KR**：**INT-7/9/11 已编码**（R0/R3/R5）；INT-8/10/12 仍提名 → [`t4-international-holdout-nominees-round2.md`](t4-international-holdout-nominees-round2.md)。**跨法域合并** → [`../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md`](../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md)。
2. **T2 comparison** — matrix v0 → [`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md)；深化备忘 → [`t2-v07-to-ivs-oecd-practice-schools.md`](t2-v07-to-ivs-oecd-practice-schools.md)；**场景选用决策树** → [`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md)（2026-10-14）。
3. **T1 theory memo** — [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md)；**DEMPE ⊥ claims-check / E3–E4** → [`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md)（2026-10-14）。下一版：建构 × 场景选用表。
4. **T3 next step** — P7 Horizon + **P8 Network relation vocabulary** → [`v0.8-probes/p8-network-relation-vocabulary-v0.md`](v0.8-probes/p8-network-relation-vocabulary-v0.md)；RC 仍可选；**no-ruling on-disk fixture**（#49 规则）已落地；**不**启动 S1/S2/S3；**不** adopt V0.8。
5. **T4 H-E3 inter-rater** — dual-coder blind protocol → [`t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md)（docs only；开跑需另批案表）。
6. **Data hygiene** — keep formal CI green; experimental validators separate; no silent schema drift.

## 4.0 T1–T4 progress board（through PR #72）

> Snapshot date: **2026-10-14**（Asia/Shanghai）。Formal: **V0.7 + schema 1.0**。**V0.8 not adopted.**

| Track | Status | Delivered (PR) | Next (not authorized here) |
|---|---|---|---|
| **T1 Theory** | **memo v0 + DEMPE⊥E3–E4 done** | [#58](https://github.com/xiangsee/patent-value-benchmark/pull/58) Construct / Two Clocks / RC⊥R；[#72](https://github.com/xiangsee/patent-value-benchmark/pull/72) DEMPE ⊥ claims-check / E3–E4 | Construct × scenario selection table；no V0.8 |
| **T2 Comparison** | **matrix + deepen + scenario tree done** | [#56](https://github.com/xiangsee/patent-value-benchmark/pull/56) matrix v0；[#67](https://github.com/xiangsee/patent-value-benchmark/pull/67) IVS/OECD/practice schools；[#68](https://github.com/xiangsee/patent-value-benchmark/pull/68) scenario decision tree | Optional worked examples only；not schema |
| **T3 Innovation probes** | **P1–P8 + optional RC plan；no-ruling fixture** | [#49](https://github.com/xiangsee/patent-value-benchmark/pull/49) RC optional + no-ruling rules；[#51](https://github.com/xiangsee/patent-value-benchmark/pull/51) parallel plan；[#50](https://github.com/xiangsee/patent-value-benchmark/pull/50) P5 CF note；[#63](https://github.com/xiangsee/patent-value-benchmark/pull/63) P7 Horizon；[#64](https://github.com/xiangsee/patent-value-benchmark/pull/64) P8 Network vocab；**this PR** on-disk no-ruling RC fixture | Gate 0 only；**no** S1/S2/S3；**no** V0.8 adopt / freeze |
| **T4 Extrapolation** | **CN + INT R1/R2 encoded；跨法域合成已写** | [#52](https://github.com/xiangsee/patent-value-benchmark/pull/52) prereg；[#53](https://github.com/xiangsee/patent-value-benchmark/pull/53) H1–H9 R0；[#54](https://github.com/xiangsee/patent-value-benchmark/pull/54)–[#62](https://github.com/xiangsee/patent-value-benchmark/pull/62) E3/E4 waves；[#65](https://github.com/xiangsee/patent-value-benchmark/pull/65)/[#66](https://github.com/xiangsee/patent-value-benchmark/pull/66) INT-1/3/5；[#69](https://github.com/xiangsee/patent-value-benchmark/pull/69)/[#71](https://github.com/xiangsee/patent-value-benchmark/pull/71) INT-7/9/11；[#70](https://github.com/xiangsee/patent-value-benchmark/pull/70) roadmap pointers | INT-2/4/6、INT-8/10/12 nominate-only；H-E3 盲评协议已稿、未开跑；no auto R5 |

**PR spine #49 → #72（research / encode / docs；none adopt V0.8）**

| Band | PRs | Theme |
|---|---|---|
| RC optional | #49–#51 | no-ruling rules；parallel plan；CF note |
| T4 CN holdouts | #52–#63 | prereg → H → E3 → E4 + phase synthesis / P7 |
| T3 Network | #64 | P8 relation vocabulary v0 |
| T4 INT | #65–#71 | Round 1 US/EP encode；Round 2 JP/KR nominate+encode；roadmap pointers |
| T1 / T2 | #56–#58, #67–#68, #72 | matrix；theory memo；deepen；scenario tree；DEMPE⊥E3–E4 |

Hard stops this board does **not** lift: V0.8 adopt · schema freeze · S1 promotion · ordinary contrib flood · inventing adjudications.

## 4.1 T4 status snapshot（H / E3 / N / P / E4 / INT）

**CN 波合并：** [`../../analysis/non-award-validation/holdout-t4-phase-synthesis.md`](../../analysis/non-award-validation/holdout-t4-phase-synthesis.md)  
**跨法域（CN/US/JP/KR）：** [`../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md`](../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md)

```text
H1–H9     → R0 ×9     discipline: refuse false lift
E3-A/B/C  → R3/R3/R0  claims-check works both ways
E3-N1/2/5 → R0 ×3     narrative ≠ claim elements
E3-P1/3/4 → R3 ×3     NHSA ZL + 规格/处方 → honest E3 (still no E4)
E4-N1/N2  → R5 ×2     single-ZL court E3+E4 (damages≠intrinsic price)
E4-N5     → R2        named license but service-fee bundle; no product E3
INT-1/3/5 → R0/R3/R5  TearLab / Aubagio OB / PureWick royalty (INT-2/4/6 still nominate)
INT-7/9/11 → R0/R3/R5  Style / Kerendia Green List / ReFa Art.102 (INT-8/10/12 still nominate)
```

Rule reinforced: **E3 ≠ E4**. Mapping ≠ attributable value. Judgment ≠ auto R5. Named license ≠ auto E4. Encode only with user-confirmed IDs and T0.

## 5. What not to claim yet

- Not a **universal dollar valuation engine** (no gold-standard price backtest).
- Not a **prediction model** for award / IPO / M&A / litigation win.
- Not **auto-R3+** from product stickers, brand fame, or portfolio size.
- Not **V0.8 adopted** or schema 1.x extension without explicit freeze.
- Not proven **inter-rater reliability** for cold-start newcomers (H-E3 still weak；补测协议 → [`t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md)，**未**开跑).
- Not global coverage parity (CN holdouts ≠ multi-jurisdiction validity).

## 6. Evidence already in hand (baseline)

| Result | What it supports | What it does not |
|---|---|---|
| V0.7 adopted after award-pair + cross-cohort stress | Structure / non-inheritance | Universal quality score |
| v0.1.0 schema 1.0 + CI | Reproducible ledger/diagnostic | Predictive accuracy |
| Round 2 RC/RP/SEP/portfolio packages | Mechanism pressure for V0.8 *research* | Auto-adopt V0.8 |
| H1–H9 all R0 | Process discipline on ordinary/semi cases | Discrimination when true E3 exists |
| E3-A/B → R3; E3-C → R0 | Claims-check can pass **and** fail | R4/R5 |
| E3-N1/N2/N5 → R0 | Brand/process/feature ≠ claim elements | Mid-tier E3 density |
| E3-P1/P3/P4 → R3 (plausible) | Explicit ZL + dose/处方 can clear E3 | **Still no E4** (no attributable ¥) |
| E4-N1/N2 → R5; E4-N5 → R2 | Court E4 can clear R5 **with** E3; named license alone stays R2 | N3/N4 still nominate |

## 7. Operating rules for agents / contributors

- Prefer **docs + nominations** before encoding.
- Encode holdouts only from a **user-confirmed** list and fixed T0.
- Prefer SME / mid-tier / non-textbook carriers for T4 E3 probes.
- Use iphouse (`user-iphouse`) for bibliographic / legal-status checks; still require human-readable product↔claim mapping notes.
- Never invent gold labels, USD outcomes, or fake adjudications for RC.

## 8. Pointers

| Doc | Role |
|---|---|
| [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md) | T1 理论备忘（Construct / Two Clocks / RC⊥R） |
| [`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md) | T1 短备忘：DEMPE ⊥ claims-check / E3–E4 |
| [`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md) | T2 既有模型比较矩阵 v0 |
| [`t2-v07-to-ivs-oecd-practice-schools.md`](t2-v07-to-ivs-oecd-practice-schools.md) | T2 深化：V0.7↔IVS 210 / OECD / 美欧中学派 |
| [`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md) | T2 场景选用决策树（V0.7 vs IVS/TP/FRAND/判赔） |
| [`model-v0.7.md`](model-v0.7.md) | Formal method |
| [`model-v0.8-design-draft.md`](model-v0.8-design-draft.md) | Research shape (not adopted) |
| [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md) | T4 prereg + appendices |
| [`t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md) | T4 H-E3 双编码盲评协议（新人可操作性；未开跑） |
| [`e3-holdout-nominees-round2.md`](e3-holdout-nominees-round2.md) | E3-N Round 2（部分已编码 N1/N2/N5） |
| [`e3-holdout-nominees-round3.md`](e3-holdout-nominees-round3.md) | E3-P Round 3（P1/P3/P4 encoded R3） |
| [`e4-holdout-nominees-round1.md`](e4-holdout-nominees-round1.md) | E4 Round 1（N1/N2/N5 encoded） |
| [`t4-international-holdout-nominees-round1.md`](t4-international-holdout-nominees-round1.md) | T4 INT Round 1 US/EP（INT-1/3/5 encoded） |
| [`t4-international-holdout-nominees-round2.md`](t4-international-holdout-nominees-round2.md) | T4 INT Round 2 JP/KR（INT-7/9/11 encoded） |
| [`../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md`](../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md) | T4 跨法域合成（CN/US/JP/KR；30 件已编码） |
| [`../../analysis/non-award-validation/holdout-e4-n125-synthesis.md`](../../analysis/non-award-validation/holdout-e4-n125-synthesis.md) | E4-N1/N2/N5 synthesis（R5/R5/R2） |
| [`rights-control-optional-parallel-plan.md`](rights-control-optional-parallel-plan.md) | Optional RC parallel track |
| [`../roadmap.md`](../roadmap.md) · [`../cold-start-status.md`](../cold-start-status.md) | Track A status |
| [`../research-tracks.md`](../research-tracks.md) | Track A / B boundary |
