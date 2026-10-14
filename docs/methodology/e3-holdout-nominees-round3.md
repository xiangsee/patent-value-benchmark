# E3 Holdout Nominees — Round 3（PASS-oriented；drugs / formulation）

> Status: **nominate only**（2026-10-14 Asia/Shanghai）  
> **Not encoded.** Formal: V0.7 / schema 1.0 unchanged. **No** V0.8 adopt/freeze.  
> Verified grant **B** via iphouse `search_patents` / `get_patent_detail`.  
> Excludes: H1–H9, E3-A/B/C, E3-N1–N6 (+ NX/NY), all `data/ledgers/*`（含 contrib / non-award / example）。

## Purpose

After Round 2 encode（E3-N1/N2/N5 → **3/3 R0 claims-fail**），T4 needs nominees where **public materials are more likely to allow claims-check PASS** — not more brand/process narratives.

Filter lesson from N1/N2/N5 is below; this round prefers **NHSA 申报/PPT or PI that cite an explicit ZL** plus **dose / 规格 / 处方药味 set / 剂型** that can map to claim elements.

Suggested T0 if later confirmed: **2026-10-13**（same as prior holdouts）unless user sets another.

## Why prior N1 / N2 / N5 failed

| ID | Domain | What looked “checkable” | Why claims-check **FAIL** |
|---|---|---|---|
| **E3-N1** | Cosmetics formula | Brand「三重蛋白」≈ patent title | No public **wt% / 比例 / 添加量** matching claim composition ranges |
| **E3-N2** | Ingredient process | Brand page names HA process patent | Process **parameters** and finished-SKU map not public |
| **E3-N5** | Machine vision | Product has hand-eye calibration feature | Claim needs **iterative weighted** algorithm; feature ≠ claim elements |

Synthesis: [`../../analysis/non-award-validation/holdout-e3-n125-synthesis.md`](../../analysis/non-award-validation/holdout-e3-n125-synthesis.md).  
Rule reinforced: **叙事 / 功能类点名 = E2 at best；E3 needs element-level public map.**

## Selection filter for Round 3（and next）

Prefer a candidate **only if most of the following hold**:

1. **Explicit public ZL** (or unique patent title + expiry that uniquely IDs the grant) in NHSA 申报材料 / PPT / 说明书 / company disclosure — not press alone.  
2. **Claim-matching public facts** of at least one type:  
   - **formulation / dose**: wt%、mg 规格、配比（e.g. 240 mg / 5 mg → 48:1）；或  
   - **TCM composition**: 公开处方药味集合 ⊆ claim 药味集合（定量份量仍可能 Unknown）；或  
   - **device datasheet**: parameters that instantiate claim elements；或  
   - **drug PI / 说明书**: indication / dose that maps use-claim elements.  
3. **Mid-tier carrier**（上市药企 / 中成药创新药 MAH），avoid Huawei / Mindray / BYD textbook stars and avoid re-using H/E3/N/ledger ZLs.  
4. **Grant B** confirmed in iphouse.  
5. Prefer **same-MAH or documented license chain**; note assignee≠MAH as residual risk (do not auto-fail nomination).

**Deprioritize**: cosmetics brand stories, process-only ingredient patents without public params, B2B software features, crystal-form / XRD claims（PI rarely discloses peaks）.

## Nominee table（E3-P1–P6）

| ID | ZL (app) | Grant pub | Owner (assignee) | Product / MAH | Domain | Why PASS-plausible | Main residual risks | Star level |
|---|---|---|---|---|---|---|---|---|
| **E3-P1** | ZL202111620840.4 | CN114224859B（2023-05-26） | 深圳信立泰药业股份有限公司 | 阿利沙坦酯氨氯地平片（复立坦®）/ 信立泰 | 化药复方制剂 | NHSA 2024 PPT **显式 ZL**；规格 **240 mg / 5 mg**；包芯片叙事 ↔ 双层/包芯权利要求；配比 48:1 落在从属权利要求常见比值带 | 辅料/增溶剂 **wt%** 未必上说明书；需 encoder 对 claim 1 辅料要素逐项核对 | Mid-large 上市药企；非教科书 IP 案 |
| **E3-P2** | ZL201110085430.4 | CN102145061B（2012-06-27） | 天津东方华康医药科技发展有限公司 | 益气通窍丸 / 扬子江四川海蓉 | 中药 1.1 组方 | NHSA PPT 点名「芪丹鼻敏药物及其制备方法」发明专利（与授权题/摘要一致）；公开处方 14 味 ⊆ claim 药味范围 | 公开多为**药味集合**而非份量；**assignee≠MAH**（需许可/转移链） | Mid TCM 创新药 |
| **E3-P3** | ZL200810100459.3 | CN101607032B（2011-08-31） | 青岛海川创新生物天然药物研究中心 | 小儿紫贝宣肺糖浆 / 健民药业集团 | 中药 1.1 组方 | NHSA 2024 申报表 **核心专利号 ZL200810100459.3**；处方 10 味与 claim 原料集合对齐 | 份量未公开；assignee≠MAH | Mid TCM；儿童专科 |
| **E3-P4** | ZL202110966782.4 | CN115708859B（2024-03-08） | 石家庄以岭药业股份有限公司（申请/A 为北京以岭） | 芪防鼻通片 / 以岭 | 中药 1.1 组方 | NHSA 2025 PPT **显式 ZL 202110966782.4**；组方 11 味公开；权利人与申报企业同集团 | 份量未知；集团主体名称需核对 | Mid-large TCM（以岭） |
| **E3-P5** | ZL200910048132.X | CN101502617B（2013-07-31） | 上海玉芝华医药科技有限公司 | 九味止咳口服液 / 卓和药业集团 | 中药 1.1 组方 | NHSA 申报表核心专利题名与授权摘要一致（矮地茶…炙甘草）；处方 9 味对齐 claim 份量范围之药味集；届满 2029-03 一致 | 表内未印 ZL 数字（题名+届满可唯一定位）；assignee≠MAH | Mid TCM 创新药 |
| **E3-P6** | ZL202111334633.X | CN113876766B（2024-08-27） | 深圳信立泰药业股份有限公司 | 阿利沙坦酯吲达帕胺缓释片 / 信立泰 | 化药 **用途** 权利要求 | 授权权利要求指向「ARB 单药控制不佳的高血压」；NHSA 2025 PPT 适应症与之对齐；规格 240/1.5 + 包芯片公开 | **用途权**≠制剂权；PPT「组合物专利至 2038」另件未在本表绑定；与 P1 同权利人（多样性弱） | Mid-large；与 P1 同企 |

## Evidence anchors（public）

| ID | Public anchor（非穷尽） |
|---|---|
| P1 | NHSA `YPSW202400278` PPT：脚注「一种复方降压药物组合物及其制备方法. ZL 2021 1 1620840.4」；规格 240 mg / 5 mg；包芯片说明 |
| P2 | NHSA `YPSW202400428` PPT：反复引用「芪丹鼻敏药物及其制备方法发明专利」；处方药味表 |
| P3 | NHSA `YPSW202400231` 申报表：核心专利 **ZL200810100459.3**；处方组成 |
| P4 | NHSA `YPSW202500297` PPT：发明专利证书 **ZL 202110966782.4**；组方表 |
| P5 | NHSA `YPSW202400100` 申报表：核心专利题名 + 届满 2029-03；处方 9 味 |
| P6 | NHSA `YPSW202500489` PPT：适应症「阿利沙坦酯单药治疗后血压控制不佳」；规格 240/1.5；包芯片 |

## Alternates（not in primary 6）

| ID | Note |
|---|---|
| **E3-PX** | 枳实总黄酮片 / 青峰 — 提取工艺权为主；公开难对 claim 工艺参数 → **N2-like FAIL 风险高**，默认不进主名单 |
| **E3-PY** | 淫羊藿素软胶囊 — NHSA 列「晶型」核心专利；PI 无 XRD 峰 → **晶型 claims 易 FAIL** |
| **E3-PZ** | 器械 datasheet 中坚案 — 本轮未找到足够强的公开参数↔claim 对，留待下轮专门筛 |

## Encoding gate（if user confirms）

1. Confirm ID subset（建议优先 **P1 + P3 + P4**，再选 1–2 个 TCM）。  
2. Fix T0.  
3. Encode formal ledger/evidence under V0.7；**claims check required** for any E3≠unknown.  
4. Synthesis note；**no** V0.8 adopt；**no** encode in this PR.

## Related

- Round 2 nominees / encode：[`e3-holdout-nominees-round2.md`](e3-holdout-nominees-round2.md) · N125 synthesis  
- Prior：E3-A/B/C · H1–H9 · [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md)  
- Program：[`world-class-roadmap.md`](world-class-roadmap.md) Track **T4**
