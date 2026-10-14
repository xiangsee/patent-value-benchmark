# E3 Holdout Nominees — Round 2 (non-star, checkable link)

> Status: **NOMINATION ONLY** (2026-10-14 Asia/Shanghai)  
> **Not encoded.** Encode only after explicit user confirm of a subset + T0.  
> Formal: V0.7 / schema 1.0 unchanged. **No** V0.8 adopt/freeze.  
> Verified basics via iphouse `get_patent_detail` / `search_patents` (grant B where noted).  
> Excludes: H1–H9, E3-A/B/C, all existing `data/ledgers/*`.

## Purpose

After E3-A/B (R3) and E3-C (R0 claims-fail), we need **non-mega-star** CN cases where a public product↔patent link *may* be checkable — to test whether V0.7 still:

- refuses sticker / brand inflation without claim map;
- allows honest R3 when map holds;
- stays at Unknown when chain is long (ingredient → SKU).

Suggested T0 if confirmed: **2026-10-13** (same as prior holdouts) unless user sets another.

## Nominee table

| ID | ZL (app) | Grant pub | Owner (assignee) | Domain | Why E3 plausible | Main risks | Star level |
|---|---|---|---|---|---|---|---|
| **E3-N1** | ZL202210708835.7 | CN114948788B (2023-11-24) | 绽妍生物科技有限公司 | Cosmetics / formula | Title = 三重蛋白组合物; brand has Novtripro® 三重蛋白 product line | Product page may omit ZL (sticker risk like E3-C); formula vs claim map | Mid brand, not Mindray/Huawei textbook |
| **E3-N2** | ZL202110767111.5 | CN113493776B (2022-06-14) | 山东焦点福瑞达生物股份有限公司 | Ingredient / process | KeyC / 福瑞达品牌页点名「超焕活小分子玻尿酸」核心专利 | Process→finished SKU long chain; group-affiliate naming (焦点 vs 福瑞达股份) | Mid HA supplier / brand |
| **E3-N3** | ZL201310317104.0 | CN103450368B (2014-05-07) | 山东福瑞达生物工程有限公司 | Ingredient / process | 硅烷化玻尿酸；品牌页列为核心专利 | Old process patent; ingredient≠SKU; carrier may be portfolio-level | Mid (Freda group) |
| **E3-N4** | ZL202310642873.1 | CN116836264B (2024-02-20) | 完美（广东）日用品有限公司等 | Ingredient → consumer SKU | 直销/新闻称玛丽艳紧致拉提系列用 rhFEB，并点名本专利号 | Ingredient-in-product; Perfect mid-large direct-sales (not SME tiny); need claim vs label map | Mid-large, non-textbook IP case |
| **E3-N5** | ZL201810828154.8 | CN109129465B (2021-12-14) | 广东奥普特科技股份有限公司 | Machine vision / B2B | Hand-eye calibration system; Opt is mid-tier listed vision vendor | Weak public SKU naming; feature≠product packaging; B2B docs may be gated | Mid industrial, not consumer star |
| **E3-N6** | ZL202410648906.8 | CN118361570B (2024-10-25) | 河南泉舜流体控制科技有限公司 | Industrial valve / SME | Company news: 防堵塞放料阀用于石化等流体控制产品 | News ≠ datasheet ZL cite; very recent grant; equipment claim map hard | True SME |

## Alternate / trap (optional; not in primary 6)

| ID | ZL | Note |
|---|---|---|
| **E3-NX** | ZL201910751657.4 / CN110564797B | 媒体把「贻贝粘蛋白制备」记到绽妍产品；iphouse 权利人为 **成都英普博集生物科技有限公司**。适合测「营销点名 ≠ 权属/映射」。默认不进主名单。 |
| **E3-NY** | ZL202111361901.X / CN113876598B | 中山中研 O/W 纳米乳；授权清楚，但公开产品页点名弱（代工厂）。备用。 |

## Verification notes (iphouse)

- All primary six returned authorized **B** publications (or B via search) with matching application numbers.
- E3-N2/N3/N4 are **composition/process/ingredient** families — expect higher Unknown rate unless encoder finds exact SKU↔claim evidence.
- E3-N5/N6 diversify away from cosmetics-only bias.

## Encoding gate (do not skip)

1. User confirms ID subset (e.g. N1+N4+N6).  
2. Fix T0.  
3. Encode formal ledger/evidence/source under V0.7; claims check required for any E3≠unknown.  
4. Synthesis note; **no** V0.8 adopt.

## Related

- Prior: E3-A/B/C synthesis · H1–H9 synthesis · [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md)  
- Program: [`world-class-roadmap.md`](world-class-roadmap.md) Track T4  
