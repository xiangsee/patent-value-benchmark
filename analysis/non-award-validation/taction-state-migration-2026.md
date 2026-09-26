# Taction v. Apple — State Migration Case Note

日期：2026-09-26  
状态：Exploratory case for Patent Value State Model 1.0  
注意：不改变V0.8既有adoption threshold

## Research question

Taction案例不是用来证明：

> 专利价值是动态的。

这个理论命题已有长期研究基础。

这里测试的是：

> **是否能够把同一专利在诉讼程序中的状态迁移，编码成benchmark可追踪的数据对象，并且不把jury verdict误写成realized value。**

## Patents

- US10,659,885
- US10,820,117

## State migration

### 2023 — summary judgment of noninfringement

District-court path against Apple is blocked before trial.

Interpretation:
- patent rights do not become zero;
- technology/product state does not become zero;
- Apple-specific infringement path becomes adverse;
- Apple-specific realizable value falls sharply.

### 2025-08-13 — Federal Circuit vacatur/remand

Source:
https://www.cafc.uscourts.gov/08-13-2025-23-2349-taction-technology-inc-v-apple-inc-opinion-23-2349-opinion-8-13-2025_2558003/

Federal Circuit vacated and remanded the noninfringement summary-judgment result, identifying errors in claim construction and exclusion of Taction expert infringement opinions.

Interpretation:
- underlying actuator technology did not change;
- legal/procedural state changed;
- the infringement path reopened;
- realizable-value pathways expanded.

### 2026-08-11 — apportionment evidence exclusion

Source:
https://docs.justia.com/cases/federal/district-courts/california/casdce/3%3A2021cv00812/705779/545

The district court excluded portions of Taction's technical apportionment opinions and reasonable-royalty opinions relying on them.

Interpretation:
- infringement and damages are separate states;
- remedy evidence can weaken even when the patent/infringement case continues;
- product scale cannot substitute for apportionment.

### 2026-09-03 — limited supplementation

Source:
https://docs.justia.com/cases/federal/district-courts/california/casdce/3%3A2021cv00812/705779/599

The court allowed limited supplementation of the existing apportionment record but did not permit a wholesale new testing program close to trial.

Interpretation:
- Remedy State is path-dependent and evidence-dependent;
- expert admissibility is itself a valuation-relevant procedural state.

### 2026-09-25 — jury verdict

Source:
https://www.law360.com/appellate/articles/2529150/breaking-apple-hit-with-historic-5-7b-patent-verdict

A California federal jury found infringement of the two patents and returned an approximately USD 5.7bn patent damages verdict.

Interpretation:

```text
Infringement State:
  jury finding = infringement

Remedy State:
  jury damages verdict ≈ USD 5.7bn

Cash Realization State:
  unresolved
```

The verdict is not a market purchase price for the patents and is not yet equivalent to collected cash.

## Benchmark implication

Taction reveals three fields that existing V0.7 / Rights Control objects do not fully cover:

1. **Infringement State**
2. **Remedy State**
3. **Cash / Economic Realization State**

It also highlights a cross-cutting context:

4. **Enforcement Capacity**

The latter must never be inherited into patent quality.

## Core guardrails

- Summary judgment loss ≠ patent value zero.
- IPR institution denial ≠ final confirmation of validity.
- Jury verdict ≠ intrinsic patent price.
- Jury verdict ≠ realized cash.
- Litigation funding ≠ patent quality.
- Product revenue / Apple sales ≠ patent-attributable value without apportionment.
- State migration must always be timestamped.

## What would falsify / limit this model?

The Realization Path object should not be adopted merely because Taction fits it.

It needs replication in at least:
- one licensing/settlement path without a merits verdict;
- one injunction/exclusion-order path where money is not the main remedy;
- one case where a large verdict is later materially modified, vacated, settled or collected.

Until then, it remains an exploratory benchmark object.
