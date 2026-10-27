# E4 Holdout Nominees — Round 1（realization / attribution；not just E3 map）

> Status: **N1–N5 all encoded**（T0=2026-10-13；N3/N4 encode 2026-10-27 Asia/Shanghai）  
> Formal: V0.7 / schema 1.0 unchanged. **No** V0.8 adopt/freeze.  
> Outcomes：[`../../analysis/non-award-validation/holdout-e4-n125-synthesis.md`](../../analysis/non-award-validation/holdout-e4-n125-synthesis.md) — **N1 R5 · N2 R5 · N3 R5 · N4 R5 · N5 R2**。  
> Verified grant **B/C** via iphouse `search_patents`; court facts via `search_cases` / `get_case_detail`.  
> Excludes: H1–H9, E3-A/B/C, E3-N*, E3-P*, and all prior `data/ledgers/*` outside this round.

## Purpose

Prior T4 waves stress-tested **mapping discipline** (claims-check → E3 / R3). E4 asks a harder question:

> Is there **public, patent-level attributable value** (license revenue / named-product sales tied to the patent / court damages citing the patent)—not merely “product implements patent”?

Suggested T0 if later confirmed: **2026-10-13**（same holdout clock） unless user sets another.

## What counts as E4-plausible here

| Subtype | Public signal sought | Typical residual |
|---|---|---|
| **E4-damages** | Judgment names ZL and awards ¥ tied to that right | Statutory/discretionary vs proven lost profits; multi-patent cases |
| **E4-sales-loss** | Court uses rightsholder’s **named product** sales/contracts as loss basis for **this** ZL | Product may embody portfolio beyond the asserted claim |
| **E4-license** | Disclosed license fee **naming ZL(s)** | Bundle of patents; fee labeled as tech-service; related-party |
| **E4-product-sales** | Issuer discloses product revenue **and** ties that SKU to the patent | Brand/SKU revenue ≠ patent attribution without explicit link |

**Not enough for this round:** NHSA ZL sticker alone (that is E3); brand narrative; portfolio license line with no ZL.

## Learnings that shaped this filter (H / E3 / N / P)

| Wave | Result | Lesson for E4 |
|---|---|---|
| H1–H9 | 9/9 **R0** | Ordinary / weak link stay Unknown—do not invent attribution |
| E3-A/B vs C | R3 / R3 / R0 | Explicit ZL + claims-check can pass **or** fail |
| E3-N1/N2/N5 | 3/3 **R0** | Brand/process/feature narrative ≠ claim elements |
| E3-P1/P3/P4 | 3/3 **R3** (plausible) | Regulated ZL + dose/处方 can clear E3; **still no E4** |
| **This round** | N1–N5 encoded | Damages can clear R5 **with** E3; pool license / service-fee bundle cannot invent E4 |

## Nominee table（E4-N1–N5）

| ID | ZL (app) | Grant pub | Owner | E4 subtype | Why E4-plausible | Main residuals | Star level |
|---|---|---|---|---|---|---|---|
| **E4-N1** | ZL201410204545.4 | CN104008319B（2017-11-24） | 深圳市汇顶科技股份有限公司 | **damages** (+ infringer product-line profit) | `(2018)粤03民初3258号`：法院点名本 ZL；判赔约 **¥40,069,871.66**（含维权开支）；说理引用思立微指纹芯片净利润占比等 | 侵权获利拆分依赖被告产品线占比假设；非权利人自身产品销售 E4 | Mid-large 指纹芯片上市（非教科书 SEP） |
| **E4-N2** | ZL200680012412.0 | CN101160432B（2011-04-20） | 维美德公司（Metso/Valmet 盘壳） | **damages**（法院采侵权获利） | `(2020)苏01民初1204号`：点名本 ZL；判赔 **¥40,000,000** | 整机 vs 盘壳贡献；提名「销售损失」标签被裁判否定 | Mid industrial OEM |
| **E4-N3** | ZL99117225.6 | CN1088218C（2002-07-24） | 朗科 | **damages**（软许可 demote） | `(2014)深中法知民初字第510号`：单件判赔 **¥7,663,438.43**；claim 1 鉴定+比对 | **许可收入=专利池** → 不作单件 E4；**2019-11-14 届满** → historical damages | Mid listed；USB 闪存史 |
| **E4-N4** | **ZL01139886.8**（**替换**；非 ZL201010284583.7） | CN1194888C（2005-03-30） | 攀钢集团 + 攀钢钒钛 | **damages**（industrial process） | `(2020)川01知民初505号`：案涉/判赔/禁令主专利本 ZL；判赔 **¥29,648,800.5**；claim 1 A–J 覆盖 | 贡献率/利润率酌定；**2021-12-04 届满**；ZL2010… 仅被告抗辩 | Mid-large 央企资源材料 |
| **E4-N5** | ZL202010875349.5（同公告另列 3 件） | CN111998776B（2022-02-22） | 中科院长春光机所 → 长春奥普光电 | **license**（named ZLs + fee） | 上市公司公告列明本 ZL 等 4 件；对价 **200 万元** / 1 年 | 200 万主要记「技术服务」；多专利捆；无 E3 产品映射 | Mid listed 光电设备 |

## Evidence anchors（iphouse / public）

| ID | Anchor |
|---|---|
| N1 | iphouse case id `1459266` · patent CN104008319B · 粤03民初3258 |
| N2 | iphouse case id `1491317` · patent CN101160432B · 苏01民初1204 |
| N3 | iphouse case id `602316` · patent CN1088218C · 深中法知民初510 |
| N4 | iphouse case id `1755758` · patent **CN1194888C** · 川01知民初505 |
| N5 | 奥普光电关联交易公告（2024-10）· patent CN111998776B |

## Encoding status

| ID | Encoded? | R | Note |
|---|---|---|---|
| **E4-N1** | yes | **R5** | 单件判赔 + 裁判 E3；金额=争议情境 |
| **E4-N2** | yes | **R5** | 单件判赔；法院用**侵权获利**（非原告销售损失） |
| **E4-N3** | yes | **R5** | 单件判赔 + claim1；软许可 demote；届满 → historical gaps |
| **E4-N4** | yes | **R5** | **替换主键** ZL01139886.8；单件判赔 + claim1；届满 → historical gaps |
| **E4-N5** | yes | **R2** | 具名许可但服务费捆 + 无 E3 产品映射 |

纪律已落实：有判赔≠自动 R5；N5 许可费≠自动 E4；N3 池许可≠单件 E4；N4 主键已替换。**no** V0.8。

## Related

- E3 Round 2/3：[`e3-holdout-nominees-round2.md`](e3-holdout-nominees-round2.md) · [`e3-holdout-nominees-round3.md`](e3-holdout-nominees-round3.md)  
- Syntheses：N125（现含 N3/N4）· P134 · H extrapolation · E3-ABC  
- Program：[`world-class-roadmap.md`](world-class-roadmap.md) Track **T4**
