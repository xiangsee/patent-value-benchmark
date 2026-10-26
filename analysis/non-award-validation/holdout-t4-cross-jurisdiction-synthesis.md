# T4 Cross-Jurisdiction Validation Synthesis（CN / US / JP / KR / EP·UK）

日期：2026-10-26 Asia/Shanghai  
T0（holdout 钟）：**2026-10-13**（除非另注）  
正式基线：**V0.7 + schema 1.0** · **未** adopt / freeze V0.8  
预注册：[`../../docs/methodology/external-extrapolation-preregistration.md`](../../docs/methodology/external-extrapolation-preregistration.md)  
程序入口：[`../../docs/methodology/world-class-roadmap.md`](../../docs/methodology/world-class-roadmap.md) · 执行记分卡：[`../../docs/methodology/t1-t4-executive-scorecard.md`](../../docs/methodology/t1-t4-executive-scorecard.md)

> 把 **已编码** T4 holdout（H / E3-A·B·C / E3-N / E3-P / E4 / INT Round 1+2+3（**含 R1/R2 余件**））收成一份 **跨法域** 可引用笔记。  
> 不替代各波 synthesis；**不**新编码；**不**发明 gold / 美元内在价格 / 胜诉预测准确率。

---

## 1. 范围与计数

| 法域 | 已编码 ID | n | R 分布 |
|---|---|---|---|
| **CN** | H1–H9；E3-A/B/C；E3-N1/N2/N5；E3-P1/P3/P4；E4-N1/N2/N5 | **24** | R0×16 · R2×1 · R3×5 · R5×2 |
| **US** | INT-1 / INT-2 / INT-3 / INT-5 | **4** | R0×2 · R3×1 · R5×1 |
| **JP** | INT-7 / INT-8 / INT-11 | **3** | R0×2 · R5×1 |
| **KR** | INT-9 / INT-10 / INT-12 | **3** | R3×2 · R5×1 |
| **EP/UK** | INT-4 / INT-6 / INT-13–18 | **8** | R0×4 · R3×2 · R5×2 |
| **合计** | — | **42** | R0×24 · R2×1 · R3×10 · R5×7 |

仍 **仅提名、未编码**：E4-N3/N4。Round 1–3 INT **全部**已编码。

分波笔记：[`holdout-t4-phase-synthesis.md`](holdout-t4-phase-synthesis.md)（CN 波合并）· [`holdout-int-135-synthesis.md`](holdout-int-135-synthesis.md) · [`holdout-int-246-synthesis.md`](holdout-int-246-synthesis.md) · [`holdout-int-81012-synthesis.md`](holdout-int-81012-synthesis.md) · [`holdout-int-246-synthesis.md`](holdout-int-246-synthesis.md) · [`holdout-int-7911-synthesis.md`](holdout-int-7911-synthesis.md) · [`holdout-int-81012-synthesis.md`](holdout-int-81012-synthesis.md) · [`holdout-int-131517-synthesis.md`](holdout-int-131517-synthesis.md) · [`holdout-int-141618-synthesis.md`](holdout-int-141618-synthesis.md)

---

## 2. 共享阶梯（五法域同一把尺子）

```text
产品 / 品牌 / 整机叙事          → 最多 E2；常停 R0
监管贴纸 / 奖项 / 组合宣传       → 不等于 E3（须对 claim 要素）
显式专利号 + claims-check PASS → 可达 E3 / R3（仍可 FAIL）
有药 / MA / 品牌               ≠ 自动 E3（须 SPC/OB/Green List 等显式 map + claim）
E3 成立                        ≠ E4（映射 ≠ 可归因价值）
单件裁判判赔/和解头 + E3 + exact_patent 指标 → 可 R5
诉请 / pleadings / 海外头       ≠ E4（territoriality）
具名许可 / 服务费捆包            → 常停 R2；E4=Unknown
判赔金额 / 许可费 / 和解额       ≠ 内在专利价格（争议·交易情境）
Unknown ≠ 0 · 不继承 · Screening ≠ Proof · 判赔 ≠ 自动 R5
```

**跨法域观察：** 同一阶梯在 CN / US / JP / KR / **EP·UK** 上 **可执行且同向**——拒假抬与条件满足时诚实抬，都不依赖法域标签，而依赖 **证据形态**（叙事 vs 监管显式号 vs 单件裁判 / 和解头）。

---

## 3. 机制等价表（CN ↔ INT）

| 机制槽 | CN 已编码例 | INT 已编码例 | 共享结局 |
|---|---|---|---|
| **拒假抬（叙事/产品环境）** | H6–H8；E3-N1/N2/N5；E3-C | INT-1 TearLab；INT-2 S&D；INT-7 Style；INT-8 SIXPAD；**INT-13 Dyson；INT-14 Numatic Henry** | **R0** |
| **诚实 E3（监管/官方显式 + claim）** | E3-A/B；E3-P1/P3/P4 | INT-3 Aubagio OB；INT-9 Kerendia；INT-10 Wainua Green List；**INT-15 Fostair UK SPC** | **R3**（无 E4） |
| **监管对偶：有药无有效 map → 诚实 FAIL** | （CN 贴纸 FAIL 类近） | **INT-16 Xadago SPC 拒绝**；**INT-4 Aubagio EP 无 listing/已撤销**（对偶 INT-3） | **R0** |
| **裁判 E3 但无终局 E4 → 停 R3** | — | **INT-6 BGH 发回**（OLG Anbieten E3；诉请≠E4） | **R3** |
| **诚实 E4→R5（单件裁判）** | E4-N1；E4-N2 | INT-5 PureWick；INT-11 ReFa；INT-12 Golfzon Art.128；**INT-17 Geofabrics；INT-18 Anan UK head** | **R5** |
| **许可/捆包残留** | E4-N5（服务费捆） | （本轮无对位 INT） | **R2**（CN） |
| **权利叙事 ⊥ R** | H9（无效维持≠侵权胜诉；RC 可选） | — | formal **R0** |

监管通道对照（非自动继承）：

| 通道 | 法域 | 作用 | 不是什么 |
|---|---|---|---|
| NHSA / 说明书显式 ZL | CN | 提高 E3 候选密度 | ≠ E4 |
| FDA Orange Book + PI | US | 同左 | ≠ E4 |
| MFDS Green List + label | KR | 同左 | ≠ E4 |
| **UK/EU SPC + SmPC**（basic patent 指名） | **EP/UK** | 同左（INT-15 PASS） | ≠ E4；**SPC 拒绝支持 FAIL 非 PASS**（INT-16） |
| 单件法院/知財高裁/특허법원判赔或和解头 | CN / US / JP / KR / **UK** / **DE** | 可提供 E4 + exact_patent 指标 | ≠ 自动 R5；≠ 内在价；**pleadings/发回/海外头 ≠ E4** |

---

## 4. 全量已编码总表

### 4.1 CN — H / E3 / E4

| ID | 专利 | Claims / map | R | 一句话 |
|---|---|---|---|---|
| H1–H5 | 见 extrapolation synthesis | unknown | **R0** | 普通 SME；无假抬材料 |
| H6–H8 | 来也 / 刀具 / 柳工等 | E2 · unknown | **R0** | 产品线叙事拒抬 |
| H9 | CN110660074B | E2 · unknown | **R0** | 无效维持≠胜诉；RC 可选 |
| E3-A | CN107412885B | PASS | **R3** | NHSA→诺欣顺；无 E4 |
| E3-B | ZL201310419886.9 | PASS | **R3** | 迈瑞 CrozFusion；金奖≠E4 |
| E3-C | CN116158988B | FAIL | **R0** | 贴纸≠收窄 claim |
| E3-N1/N2/N5 | 见 N synthesis | FAIL | **R0** | 品牌/工艺/功能≠要素 |
| E3-P1/P3/P4 | 见 P synthesis | PASS (plausible) | **R3** | 显式 ZL+规格/处方；仍无 E4 |
| E4-N1 | CN104008319B | E3+E4 confirmed | **R5** | 单件判赔；金额=争议情境 |
| E4-N2 | CN101160432B | E3+E4 confirmed | **R5** | 法院改按侵权获利 |
| E4-N5 | CN111998776B | unknown | **R2** | 具名许可但服务费捆 |

### 4.2 US / JP / KR / EP — INT Round 1–2（含余件）

| ID | 法域 | 专利 | Claims / map | R | 一句话 |
|---|---|---|---|---|---|
| INT-1 | US | US11536707B2 | FAIL | **R0** | TearLab 市售≠本专利 LFA 整合 |
| INT-2 | US | US11533930B2 | FAIL | **R0** | TODDY 冷萃 ≠ flash-brew+冷冻浓缩 claim |
| INT-3 | US | US8802735B2 | PASS (strong) | **R3** | Aubagio OB+PI；无 E4 |
| INT-4 | EP | EP2477611B1 | FAIL | **R0** | 无 EP listing；已撤销；不继承 INT-3 US OB |
| INT-5 | US | US10376407B2 | confirmed (court) | **R5** | PureWick 单件 royalty |
| INT-6 | EP/DE | EP1070223B1 | confirmed (court offering) | **R3** | OLG Anbieten E3；BGH 发回无终局 E4 |
| INT-7 | JP | JP6956213B2 | FAIL | **R0** | Style 品牌≠多区块垫 claim |
| INT-8 | JP | JP6937153B2 | FAIL | **R0** | SIXPAD ≠ 特許6937153 钉 SKU |
| INT-9 | KR | KR101614164B1 | PASS (strong) | **R3** | Kerendia Green List；无 E4 |
| INT-10 | KR | KR102212275B1 | PASS (strong) | **R3** | Wainua Green List 10-2212275；无 E4 |
| INT-11 | JP | JP5847904B2 | confirmed (court) | **R5** | ReFa 大合議单件判赔 |
| INT-12 | KR | KR101031432B1 | confirmed (court) | **R5** | Golfzon Art.128⑦ ₩1.313B |

### 4.3 EP / UK — INT Round 3

| ID | 专利 | Claims / map | R | 一句话 |
|---|---|---|---|---|
| INT-13 | EP3941306B1 Dyson | FAIL | **R0** | Airwrap/Airstrait 品牌叙事 ≠ 双臂 plenum+30–60° claim 钉 SKU |
| INT-14 | EP3934499B1 Numatic | FAIL | **R0** | Henry/Hetty 罐式+HepaFlo ≠ end-cap 滤芯圆筒腔 claim |
| INT-15 | EP1787639B1 Chiesi / Fostair | PASS (strong) | **R3** | UK SPC/GB11/051 basic patent + BDP/formoterol；无 E4 |
| INT-16 | EP1613296B1 Newron / Xadago | FAIL | **R0** | 组合 claim vs 单方 MA；SPC/GB15/046 Art 3(b) 拒绝 → 诚实 FAIL |
| INT-17 | EP2430238B1 Geofabrics | confirmed (court) | **R5** | 单件 EP(UK) 损害探究 ≈£13.4M + 裁判 E3 |
| INT-18 | EP1435338B1 Anan/Rhodia | confirmed (court) | **R5** | 裁判 E3 + **仅** UK Head1 £85k 和解；海外诉请头驳回 ≠ E4 |

**Round 3 强化课：**

- **SPC 对偶**：INT-15（有 SPC + claim PASS → R3）vs INT-16（SPC 拒绝 + claim FAIL → R0）— 有药≠自动 E3。  
- **品牌/产品≠claims**：INT-13/14 与 INT-1/7 同向拒抬。  
- **Territorial E4**：INT-17 大额损害探究 vs INT-18 仅英头小额和解；pleadings / 海外头 **不得**记 E4。  
- **E3≠E4；判赔/和解≠自动 R5/FMV**：INT-17/18 均在 E3 + exact_patent 指标齐备时才 R5。

---

## 5. 法域对照结论（诚实）

| 问题 | 结论 |
|---|---|
| V0.7 阶梯能否跨 CN→US/JP/KR/**EP·UK** 复用？ | **能（小 N）**：同一拒抬/诚实抬模式复现；EP/UK Round 3 再加压 |
| 多法域是否已「证明世界级覆盖」？ | **否**：n_INT=18；冷启动新人计时仍弱；E4-N3/N4 未编 |
| 监管通道是否可互换？ | **形态等价、不得自动继承**：OB ≈ Green List ≈ NHSA 显式号 ≈ **UK SPC**，仍须 claims-check；**SPC 拒绝 = FAIL 信号** |
| 判赔法域差异是否改 R 规则？ | **不改**：CN/US/JP/UK 单件裁判/和解头均要求 E3 + exact_patent 指标才 R5；UK 另教 territoriality |
| 对 T1/T2/T3 的含义 | T1：DEMPE⊥E3–E4 已由跨域样本加压；T2：场景树「何时用 V0.7 vs 判赔/FRAND」有实证锚；T3：RC/Horizon/Network 仍 research-only，**不**借本文件 adopt V0.8 |

---

## 6. 明确不宣称

- 无美元内在价值引擎、无胜诉/上市/许可费率预测准确率  
- 无 V0.8 adopt / schema freeze / S1 升格  
- 无「全法域 R5」或「Orange Book / Green List / SPC 自动 R3/R5」  
- INT-1–18 **已**编码；E4-N3/N4 **未**编码  
- CN 24 + INT 18 = **n=42** ≠ 全球代表性样本；EP/UK/DE 仍小 N

---

## 7. 下一跳（需用户确认才编码 / 开跑）

1. E4-N3/N4 或新 E4 波（避开已编码集）— 用户确认 ID + T0 后再 encode  
2. 可选：开 H-E3 盲评（协议已有；**本文件不授权**）  
3. T3 探针继续；**禁止**用本跨域合成顺带 adopt V0.8  

---

## 8. 指针

| Doc | Role |
|---|---|
| [`holdout-t4-phase-synthesis.md`](holdout-t4-phase-synthesis.md) | CN 波 H→E4 合并 |
| [`holdout-extrapolation-synthesis.md`](holdout-extrapolation-synthesis.md) | H1–H9 |
| [`holdout-e3-abc-synthesis.md`](holdout-e3-abc-synthesis.md) · [`holdout-e3-n125-synthesis.md`](holdout-e3-n125-synthesis.md) · [`holdout-e3-p134-synthesis.md`](holdout-e3-p134-synthesis.md) | E3 三波 |
| [`holdout-e4-n125-synthesis.md`](holdout-e4-n125-synthesis.md) | E4-N1/N2/N5 |
| [`holdout-int-135-synthesis.md`](holdout-int-135-synthesis.md) · [`holdout-int-246-synthesis.md`](holdout-int-246-synthesis.md) · [`holdout-int-81012-synthesis.md`](holdout-int-81012-synthesis.md) · [`holdout-int-7911-synthesis.md`](holdout-int-7911-synthesis.md) | INT R1 / R2 |
| [`holdout-int-131517-synthesis.md`](holdout-int-131517-synthesis.md) · [`holdout-int-141618-synthesis.md`](holdout-int-141618-synthesis.md) | INT R3（EP/UK） |
| [`../../docs/methodology/t4-international-holdout-nominees-round1.md`](../../docs/methodology/t4-international-holdout-nominees-round1.md) · [`…-round2.md`](../../docs/methodology/t4-international-holdout-nominees-round2.md) · [`…-round3.md`](../../docs/methodology/t4-international-holdout-nominees-round3.md) | 提名（含未编码） |
