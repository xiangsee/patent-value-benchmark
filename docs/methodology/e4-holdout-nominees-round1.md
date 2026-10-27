# E4 Holdout Nominees — Round 1（realization / attribution；not just E3 map）

> Status: **N1/N2/N5 encoded**（T0=2026-10-13；2026-10-14 Asia/Shanghai）· N3/N4 仍提名
> Audit 2026-10-27：N3 damages 锚点核实；N4 **主键应改为 ZL01139886.8**（见下表脚注）；两件均已期满（相对 T0=2026-10-13）  
> Formal: V0.7 / schema 1.0 unchanged. **No** V0.8 adopt/freeze.  
> Outcomes：[`../../analysis/non-award-validation/holdout-e4-n125-synthesis.md`](../../analysis/non-award-validation/holdout-e4-n125-synthesis.md) — **N1 R5 · N2 R5 · N5 R2**。  
> Verified grant **B/C** via iphouse `search_patents`; court facts via `search_cases` / `get_case_detail`.  
> Excludes: H1–H9, E3-A/B/C, E3-N*, E3-P*, and all `data/ledgers/*`（含 non-award / contrib / example）。

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
| **This round** | Nominate only | Need damages / named sales / named-ZL license—not another E3 map |

## Nominee table（E4-N1–N5）

| ID | ZL (app) | Grant pub | Owner | E4 subtype | Why E4-plausible | Main residuals | Star level |
|---|---|---|---|---|---|---|---|
| **E4-N1** | ZL201410204545.4 | CN104008319B（2017-11-24） | 深圳市汇顶科技股份有限公司 | **damages** (+ infringer product-line profit) | `(2018)粤03民初3258号`：法院点名本 ZL；判赔约 **¥40,069,871.66**（含维权开支）；说理引用思立微指纹芯片净利润占比等 | 侵权获利拆分依赖被告产品线占比假设；非权利人自身产品销售 E4 | Mid-large 指纹芯片上市（非教科书 SEP） |
| **E4-N2** | ZL200680012412.0 | CN101160432B（2011-04-20） | 维美德公司（Metso/Valmet 盘壳） | **damages** + **sales-loss** | `(2020)苏01民初1204号`：点名本 ZL；判赔 **¥40,000,000**；原告以自有 **热磨机系统** 销售合同单价（约 1404–1675 万元/台）论证损失 | 销售合同为系统整机，可能含非本件专利贡献；外国权利人 vs 国内制造 | Mid industrial OEM（非消费电子明星） |
| **E4-N3** | ZL99117225.6 | CN1088218C（2002-07-24） | 朗科（发明人邓/成无偿转让→公司；多案权利人） | **damages**（主）+ **license revenue (soft, demote)** | 单件判赔核实：`(2014)深中法知民初字第510号` 判决书 2017-04-07 · iphouse `602316` · **¥7,663,438.43**（仅本 ZL）；另有多件同 ZL 小额判赔。年报许可收入为**专利池/业务线**（2021≈1129 万 / 2022≈1756 万 / 2023≈616 万）—**不可单件归因** | **专利权已于 2019-11-14 期满**（相对 T0 已死）；许可 soft 勿抬 R5；USB 教材经典感 | Mid listed；技术史知名但非华为级 |
| **E4-N4** | **应改主键 ZL01139886.8**（原提名 ZL201010284583.7 **误**） | **CN1194888C**（2005-03-30）；原 CN101921941B 仅为被告抗辩提及 | **攀钢集团有限公司 + 攀钢集团钒钛资源股份有限公司**（非个人发明主张） | **damages**（industrial process） | `(2020)川01知民初505号` · iphouse `1755758` · 判赔合计 **¥29,648,800.5**（渝鑫 ¥29M+开支；钒璟 ¥1万+开支等）；**案涉/禁令/判赔载体均为 ZL01139886.8**；ZL201010284583.7 系被告主张自用许可/抗辩，法院未采信 | **原主键归因失败**；案涉专利 **2021-12-04 期满**（相对 T0 已死）；贡献率酌减已在说理中 | Mid-large 央企资源材料 |
| **E4-N5** | ZL202010875349.5（同公告另列 3 件） | CN111998776B（2022-02-22） | 中科院长春光机所 → 长春奥普光电 | **license**（named ZLs + fee） | 上市公司公告：《技术转让（专利实施许可）合同》列明 **ZL202010875349.5** 等 4 件；披露许可相关对价 **200 万元** / 1 年 | 公告将 200 万主要记为「技术服务和指导费」、技术秘密 0——**专利费 vs 服务费拆分**是 E4 核心风险；关联交易；多专利捆 | Mid listed 光电设备 |

## Evidence anchors（iphouse / public）

| ID | Anchor |
|---|---|
| N1 | iphouse case id `1459266` · patent CN104008319B · 粤03民初3258 |
| N2 | iphouse case id `1491317` · patent CN101160432B · 苏01民初1204 |
| N3 | iphouse judgment `602316` · `(2014)深中法知民初字第510号` · patent CN1088218C / ZL99117225.6 · 朗科年报「99专利」期满公告 + 专利池许可收入行 |
| N4 | iphouse `1755758` · `(2020)川01知民初505号` · **案涉 patent CN1194888C / ZL01139886.8**（原提名 CN101921941B 仅抗辩提及） |
| N5 | 奥普光电关联交易公告（2024-10）· patent CN111998776B · 同合同姐妹 ZL 仅作背景，编码时以用户确认的主键为准 |

## Encoding status

| ID | Encoded? | R | Note |
|---|---|---|---|
| **E4-N1** | yes | **R5** | 单件判赔 + 裁判 E3；金额=争议情境 |
| **E4-N2** | yes | **R5** | 单件判赔；法院用**侵权获利**（非原告销售损失） |
| E4-N3 | no | — | 仍提名；**KEEP**（damages 单件核实；期满+许可 soft 需编码纪律） |
| E4-N4 | no | — | 仍提名；**REPLACE 主键→ZL01139886.8** 后再编（原 ZL2010… 非判赔载体） |
| **E4-N5** | yes | **R2** | 具名许可但服务费捆 + 无 E3 产品映射 |

纪律已落实：有判赔≠自动 R5；N5 许可费≠自动 E4。**no** V0.8。

## Related

- E3 Round 2/3：[`e3-holdout-nominees-round2.md`](e3-holdout-nominees-round2.md) · [`e3-holdout-nominees-round3.md`](e3-holdout-nominees-round3.md)  
- Syntheses：N125 · P134 · H extrapolation · E3-ABC  
- Program：[`world-class-roadmap.md`](world-class-roadmap.md) Track **T4**
