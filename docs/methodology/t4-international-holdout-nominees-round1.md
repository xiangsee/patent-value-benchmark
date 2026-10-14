# T4 International Holdout Nominees — Round 1（US / EP）

> Status: **INT-1/3/5 encoded**（T0=2026-10-13；2026-10-14 Asia/Shanghai）· INT-2/4/6 仍提名  
> Formal: V0.7 / schema 1.0 unchanged. **No** V0.8 adopt/freeze.  
> Outcomes：[`../../analysis/non-award-validation/holdout-int-135-synthesis.md`](../../analysis/non-award-validation/holdout-int-135-synthesis.md) — **INT-1 R0 · INT-3 R3 · INT-5 R5**。  
> Verified bibliographic grants via iphouse `search_patents`；E3/E4 公开锚点经 FDA Orange Book / D.Del. judgment / BGH 意见等。  
> **Excludes** all existing `data/ledgers/*` US/EP（含 i4i、mRNA、CRISPR、AVC、GMR、LIB、OLED、PageRank、Amgen、Apple/Samsung、Synqor、road-milling 等）及全部 CN holdout。

Suggested encode T0 if later confirmed: **2026-10-13**（与 CN holdout 同钟）unless user sets another.

---

## Purpose

CN T4 波已验证拒抬 / claims-check / 单件判赔纪律。本轮把同一过滤器推到 **US / EP**，并按三类混搭：

| 桶 | 目标 | 期望压力 |
|---|---|---|
| **(a) R0 discipline** | 有产品/品牌叙事但无 exact-patent 公开映射 | 停 R0；拒假抬 |
| **(b) Checkable E3** | 监管/标签级 patent↔product 可核 | 诚实 R3（仍无 E4） |
| **(c) Possible E4** | 判决点名专利+金额，或具名许可费 | 有 E3+exact_patent 指标才可谈 R5；判赔≠自动 R5 |

---

## Nominee table（INT-1–INT-6）

| ID | 桶 | Patent | Owner | 公开锚点 | Why nominated | Main residuals | Star |
|---|---|---|---|---|---|---|---|
| **INT-1** | **(a) R0** | **US11536707B2** | TearLab Research, Inc. | iphouse grant 2022-12-27；公司泪液渗透压检测产品线公开存在 | 中小医械；产品叙事强、权利要求为微流控+侧流分析组合 → 易假抬，公开材料难做要素级 E3 | 产品说明书未必覆盖 claim 全部要素 | Mid SME device |
| **INT-2** | **(a) R0** | **US11533930B2** | S&D Coffee, Inc. | iphouse grant 2022-12-27；flash brew / 浓缩咖啡工艺叙事 | 食品工艺专利；品牌饮料叙事 ≠ 工艺 claim 实施证明 | 工厂工艺不公开 | Mid food OEM |
| **INT-3** | **(b) E3** | **US8802735B2** | Sanofi | FDA Orange Book：**Aubagio®** (teriflunomide) NDA202992 **Drug product** 旗标；7mg/14mg 片剂 | 监管显式 listing + 片剂稳定性制剂 claim → 可对标 CN E3-P 过滤器 | 同 NDA 另有 use patents；claims-check 仍需对照辅料/工艺；**无**公开单件 E4 | Mid specialty MS drug（非 Keytruda 级） |
| **INT-4** | **(b) E3** | **EP2477611B1** | Sanofi | 与 US8802735 **同族**（family 41510564）；Aubagio EU MA / 片剂产品公开 | EP 侧同制剂族；检验「无 Orange Book 时」E3 可操作性 | EU SmPC **通常不列**专利号 → E3 依赖同族+产品公开+claims；弱于 US OB | Mid EP pharma |
| **INT-5** | **(c) E4** | **US10376407B2** | Purewick Corp. | D.Del. *PureWick v. Sage* 终局：对本专利判 **reasonable royalty ≈ USD 1,799,193**（PrimoFit）；侵权成立 | **单件**判赔口径清晰（对比同案 ’376/’989 共享 lost profits） | 仍属争议情境金额；非内在定价；需核对 claim↔PrimoFit | Mid med-device（BD 体系，非消费电子明星案） |
| **INT-6** | **(c) E4** | **EP1070223B1** | ASJ Holding ApS | BGH X ZR 104/22（2024-05-07）涉本 EP（DE 效力）损害赔偿计算规则；过热蒸汽干燥装置 | EP/DE 法域判赔语境；检验国际 E4 可观测性与 territoriality | 公开意见重在损害计算法理，金额拆分需编码时再核；外国工业案 | Mid industrial EP |

---

## Bucket notes

### (a) R0
- 刻意选 **非教科书** US 中小权利人；有产品环境但无监管点名 ZL。  
- 成功标准：编码后 **R0** + mapping unknown（与 H1–H9 / E3-N 同纪律）。

### (b) E3
- **INT-3** 对齐 CN E3-P：监管材料 **显式专利号** + 剂型可对 claim。  
- **INT-4** 压力：EP 无 OB 等价物时，同族+MA 产品是否足够做 **plausible** E3——允许 FAIL 为诚实结果。

### (c) E4
- **INT-5** 优先于同案 US10226376：后者与 ’989 **共享** lost profits，单件归因更脏。  
- **INT-6** 提供 EP 判赔轨道；**有判赔≠自动 R5**（须 E3 + exact_patent 指标）。

---

## Evidence anchors

| ID | Anchor |
|---|---|
| INT-1 | iphouse `US-11536707-B2` |
| INT-2 | iphouse `US-11533930-B2` |
| INT-3 | iphouse `US-8802735-B2` · FDA Orange Book NDA202992 Drug product |
| INT-4 | iphouse `EP-2477611-B1` · family 41510564 with INT-3 |
| INT-5 | iphouse `US-10376407-B2` · D.Del. 1:19-cv-01508 final judgment ¶ royalty on ’407 |
| INT-6 | iphouse `EP-1070223-B1` · BGH X ZR 104/22 |

---

## Encoding status

| ID | Encoded? | R | Note |
|---|---|---|---|
| **INT-1** | yes | **R0** | TearLab Osmolarity ≠ LFA/analyte claim；claims FAIL |
| INT-2 | no | — | 仍提名 |
| **INT-3** | yes | **R3** | OB Drug product + PI 辅料对齐 claim 1/36/37；无 E4 |
| INT-4 | no | — | 仍提名（EP 同族） |
| **INT-5** | yes | **R5** | 单件 royalty ≈$1.80M + 裁判 E3；争议情境 |
| INT-6 | no | — | 仍提名（EP/DE） |

纪律已落实：产品叙事≠E3；OB≠自动 E4；判赔≠自动 R5（本案 INT-5 条件满足）。**no** V0.8。

## Related

- CN T4 phase：[`../../analysis/non-award-validation/holdout-t4-phase-synthesis.md`](../../analysis/non-award-validation/holdout-t4-phase-synthesis.md)  
- Program：[`world-class-roadmap.md`](world-class-roadmap.md) Track **T4 international**
