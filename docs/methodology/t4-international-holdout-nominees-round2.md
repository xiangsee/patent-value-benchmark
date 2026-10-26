# T4 International Holdout Nominees — Round 2（JP / KR）

> Status: **INT-7–12 all encoded**（T0=2026-10-13；2026-10-26 Asia/Shanghai）  
> Formal: V0.7 / schema 1.0 unchanged. **No** V0.8 adopt/freeze.  
> Verified bibliographic grants via iphouse `search_patents` / `get_patent_detail`（hyphenated pubs）；E3/E4 公开锚点经 MFDS 허가특허목록（Green List）/ 知財高裁要旨 / 특허법원 판결 / 新闻二次源。  
> **Excludes** 全部 CN holdout、Round 1 INT-1–INT-6 及仓库既有 US/EP ledger 集合。

Suggested encode T0 if later confirmed: **2026-10-13**（与 CN / INT Round 1 同钟）unless user sets another.

---

## Purpose

Round 1 把拒抬 / claims-check / 单件判赔纪律推到 **US / EP**。本轮把同一过滤器推到 **JP / KR**，并按三类混搭：

| 桶 | 目标 | 期望压力 |
|---|---|---|
| **(a) R0 discipline** | 有品牌/产品线叙事但无 exact-patent 公开映射 | 停 R0；拒假抬 |
| **(b) Checkable E3** | 监管级 patent↔drug 可核（KR Green List ≈ US Orange Book） | 诚实 R3（仍无 E4） |
| **(c) Possible E4** | 判决**点名单件专利**+金额 | 有 E3+exact_patent 指标才可谈 R5；判赔≠自动 R5 |

**法域注记：** 日本**无**美/韩式药品专利登记簿（JP「オレンジブック」是溶出质量资料，**不是**专利列表）。故本轮 E3 桶以 **KR MFDS 허가특허목록（Green List）** 为主；JP 侧用 R0 品牌叙事 + Art.102 大合議判赔填桶。

---

## Nominee table（INT-7–INT-12）

| ID | 桶 | Patent | Owner | 公开锚点 | Why nominated | Main residuals | Star |
|---|---|---|---|---|---|---|---|
| **INT-7** | **(a) R0** | **JP-6956213-B2** | 株式会社ＭＴＧ | iphouse grant 2021-11-02；发明名称「姿勢保持具」；Style BX 等姿势支撑产品线公开存在 | 中小消费健康器械；品牌叙事强、公开材料**未**把本专利号钉到具体 SKU → 易假抬 | Style 系列多 SKU / 多分案；无说明书级 claim 要素对照 | Mid JP consumer device |
| **INT-8** | **(a) R0** | **JP-6937153-B2** | 株式会社ＭＴＧ | iphouse grant 2021-09-22；「筋肉電気刺激装置」；SIXPAD EMS 产品线公开 | EMS 品牌叙事 ≠ 单件 EMS 专利 claim 实施证明；同族/邻接 EMS 专利众多 | Abs2 / Powersuit 等产品与本 B2 的要素级映射未公开 | Mid JP wellness EMS |
| **INT-9** | **(b) E3** | **KR-101614164-B1** | Bayer IP GmbH | iphouse grant 2016-04-20；化合物族 title；**케렌디아정（finerenone / Kerendia）** MFDS Green List 等재특허报道（10-1614164） | 监管显式 listing + 化合物 claim → 对齐 CN E3-P / INT-3 OB 过滤器 | 同品另有晶型/制法专利（如 10-2830206）；claims-check 仍需对照说明书；**无**公开单件 E4 | Mid specialty CKD drug（非 Keytruda 级） |
| **INT-10** | **(b) E3** | **KR-102212275-B1** | Ionis Pharmaceuticals | iphouse grant 2021-02-05；TTR/HBV 调节寡聚物；**Wainua（eplontersen）** 韩许可/Green List 候选锚点（10-2212275） | 第二件 KR 监管映射；罕见病反义药；检验 Green List 多药密度 | 编码前须在 nedrug / 허가특허목록 **再核**等재行；多专利可能同品挂载 | Mid rare-disease antisense |
| **INT-11** | **(c) E4** | **JP-5847904-B2** | 株式会社ＭＴＧ | iphouse grant 2016-01-27；「美容器」；知財高裁大合議 **平成31(ネ)10003**（令和2年2月28日）：**本件特許権２**侵害成立，损害赔偿 **¥440,060,000**（含律师费）；原告製品=ReFa 系实施品 | **单件** Art.102① 判赔口径清晰（本件特許１不构成侵害） | 争议情境金额；覆灭/销售不能事情已内嵌；非内在定价；需核对 claim↔原告产品 | Mid JP beauty device（教科书大合議，但非消费电子明星案） |
| **INT-12** | **(c) E4** | **KR-101031432-B1** | Golfzon Co., Ltd. | iphouse grant 2011-04-26；虚拟高尔夫模拟装置；특허법원 **2021나1510**（2023-04-12）：对本专利侵害成立，损害赔偿本金 **₩1,313,225,245**（Art.128⑦ 相当额；贡献率 7%） | KR 法域单件判赔 + 禁令/废弃；检验国际 E4 与 Art.128 | LBOX 红acted 专利号（新闻/二源确认 10-1031432）；贡献率争议情境；硬件+软件捆绑 | Mid KR screen-golf / sports tech |

---

## Bucket notes

### (a) R0
- 刻意选 **MTG** 消费健康线（Style / SIXPAD）：产品环境极强，但公开材料缺 exact-patent↔SKU。  
- 成功标准：编码后 **R0** + mapping unknown（与 H1–H9 / E3-N / INT-1 同纪律）。

### (b) E3
- **INT-9** 对齐 CN E3-P / INT-3：监管材料 **显式专利号** + 可对 claim。  
- **INT-10** 提供第二药；若编码时 Green List 行核验失败 → 诚实 FAIL / 降 R0，**不**用品牌叙事抬升。  
- JP 无 OB 等价物 → 本轮不硬凑 JP E3。

### (c) E4
- **INT-11** 优先于同案 JP5356625（特許１）：大合議认定 **仅特許２** 侵害并算定损害。  
- **INT-12** 提供 KR Art.128 轨道；本金 ₩1.313B（不含另案延迟损害新闻口径混淆）。  
- **有判赔≠自动 R5**（须 E3 + exact_patent 指标）。备选未入表：JP-4866978-B2（フジ医療器 / 令和2(ネ)10024，约 ¥391.5M）— 可作后续 Round。

---

## Evidence anchors

| ID | Anchor |
|---|---|
| INT-7 | iphouse `JP-6956213-B2` · Style BX 产品公开页（无专利号钉SKU） |
| INT-8 | iphouse `JP-6937153-B2` · SIXPAD 产品线公开页 |
| INT-9 | iphouse `KR-101614164-B1` · Hitnews / MFDS Green List 케렌디아 10-1614164 |
| INT-10 | iphouse `KR-102212275-B1` · Wainua/eplontersen 韩侧 listing（编码再核） |
| INT-11 | iphouse `JP-5847904-B2` · courts.go.jp 平成31(ネ)10003 要旨 PDF |
| INT-12 | iphouse `KR-101031432-B1` · 특허법원 2021나1510（LBOX）· Golfzon/YNA 新闻 |

---

## Encoding status

| ID | Encoded? | R | Note |
|---|---|---|---|
| **INT-7** | yes | **R0** | Style ≠ multi-block/protrusion claim；claims FAIL |
| **INT-8** | yes | **R0** | SIXPAD ≠ 特許6937153 钉 SKU；claims FAIL |
| **INT-9** | yes | **R3** | Green List + finerenone；无 E4 |
| **INT-10** | yes | **R3** | Green List 10-2212275 on Wainua（2026-10-12≤T0）；无 E4 |
| **INT-11** | yes | **R5** | 大合議特許２ ¥440.06M + 裁判 E3 |
| **INT-12** | yes | **R5** | 특허법원 Art.128⑦ ₩1.313B + 裁判 E3 |

纪律已落实：产品叙事≠E3；Green List≠自动 E4；判赔≠自动 R5（本案 INT-11 条件满足）。**no** V0.8。

## Related

- Encode synthesis：[`../../analysis/non-award-validation/holdout-int-7911-synthesis.md`](../../analysis/non-award-validation/holdout-int-7911-synthesis.md) · [`../../analysis/non-award-validation/holdout-int-81012-synthesis.md`](../../analysis/non-award-validation/holdout-int-81012-synthesis.md)  

- Round 1 US/EP：[`t4-international-holdout-nominees-round1.md`](t4-international-holdout-nominees-round1.md)  
- CN T4 phase：[`../../analysis/non-award-validation/holdout-t4-phase-synthesis.md`](../../analysis/non-award-validation/holdout-t4-phase-synthesis.md)  
- Program：[`world-class-roadmap.md`](world-class-roadmap.md) Track **T4 international**
