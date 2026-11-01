# CV3 Source Publication Timing & Technical Mapping — v0.3 Addendum

> 2026-11-01 · Applied research / **research-only** · V0.7 adopted and formal Schema 1.0 unchanged
> Preceded by: [Claim Version Gate v0.3](claim-version-gate-v0.3.md)
> Privacy: no previously supplied award data, company accounts, or the six blind-case publication-number crosswalk is put into this public repo.

## Finding

Six external ordinary patents were revisited using the **granted independent-claim text** rather than merely subject matter or A application claims. One earlier research comparison cited the **grant B of a different application that became public after the subject's claimed priority**, whereas the earlier **A publication of that same reference application was publicly available before the subject's claimed priority**.

Thus two dates and two exact publication documents must be distinguished:

1. **Identity/version**: one application may be published first as A, then in different claim scope as B.
2. **Availability**: a citation to B does not establish what exact content was available to the public on its eventual grant date, or earlier.
3. **Technical relevance**: even a temporally eligible A disclosure requires **specific mapping to each granted-claim element**; shared IPC, generic field or same applicant cannot substitute.
4. **Legal relevance**: claimed effective priority, exceptions and the relevant legal rule require legal review; a simple date comparator is **screening**, not a novelty/inventive-step ruling.

No ex post product/portfolio revenue is a substitute for E3 exact-claim-to-carrier evidence. A patent's A/B or cross-document citation is not a verified R3 or monetary event.

## Procedure

| Gate | Question | Outcome permitted |
|---|---|---|
| CV3a Traceability | Is the comparator identified by a **specific publication** number, publication date and source URL? | Missing => `UNTRACED` |
| CV3b Temporal availability | Was **that publication** publicly available on or before the chosen conservative screening cutoff? | After => `POST_CUTOFF`, may prompt earlier A lookup; no automatic substitution |
| CV3c Technical overlap | Is there a reviewer-supplied per-element mapping to the exact granted independent claim? | Missing => `TIME_ELIGIBLE_UNMAPPED` |
| CV3d Review handoff | Evidence mapping, reviewer, claim number and differences are recorded? | `ELEMENT_MAPPED_REVIEW` means further specialist analysis only |

**Do not treat these labels as novelty decisions, legal admissibility of a prior-art document, patent quality ranks, or patent values.** A document can be chronologically eligible and technically remote.

## Research-only automated checks

`tools/validate_prior_publication_gate.py` and `tests/test_prior_publication_gate.py` protect synthetic cases:

- B version after subject cutoff is blocked even if reference A was earlier; reviewer must inspect the actual A content;
- A version before subject cutoff may pass temporal screening, but not element mapping automatically;
- shared family root or same applicant does not inherit disclosed elements;
- adding an unsupported `technical_overlap=verified` string does not bypass claim-element records;
- element-level review with source anchors can hand off to human technical assessment while **all E3, E4, R-stage increases and monetary values remain undefined**.

## Bounded six-case audit (method summary only)

- Six granted B claims and at least one potential earlier public technical reference per case were checked at the publication-date level.
- One reference needed **B→A publication-version correction** in a chronology check.
- The identified references range from fairly close technical purpose to generic shared techniques. **None received a final prior-art validity determination**; no exhaustive prior-art search is claimed.
- No independently verified exact-claim→commercial-carrier E3 or exact-patent economic E4 evidence surfaced in this bounded source search. `Unknown ≠ zero`; absence of corroboration is **not** proof of nonimplementation.
- This is a researcher source review following one-model/two-persona role simulation. **Actual independent human reviewer comparison: Not Run** (Issue #91 remains open).

## Acceptance criteria before model promotion

Require multiple reviewers to be able to reproduce:
- which **specific** A/B publication was available at the relevant date;
- a claim-by-claim technical mapping with cited text passages and a reasoned alternative account;
- independent sources for product or process implementation when asserting E3;
- an explicit abstention from currency valuation when G0–G4 attribution is missing.

No V0.8 adoption, no formal Ledger/Diagnostic schema changes, and no ratings of the original user's 17 cases are part of this addendum.
