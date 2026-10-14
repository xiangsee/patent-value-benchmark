# T4 Cross-Jurisdiction Validation Synthesis（CN / US / JP / KR）

日期：2026-10-14 Asia/Shanghai  
T0（holdout 钟）：**2026-10-13**（除非另注）  
正式基线：**V0.7 + schema 1.0** · **未** adopt / freeze V0.8  
预注册：[`../../docs/methodology/external-extrapolation-preregistration.md`](../../docs/methodology/external-extrapolation-preregistration.md)  
程序入口：[`../../docs/methodology/world-class-roadmap.md`](../../docs/methodology/world-class-roadmap.md)

> 把 **已编码** T4 holdout（H / E3-A·B·C / E3-N / E3-P / E4 / INT Round 1+2）收成一份 **跨法域** 可引用笔记。  
> 不替代各波 synthesis；**不**新编码；**不**发明 gold / 美元内在价格 / 胜诉预测准确率。

---

## 1. 范围与计数

| 法域 | 已编码 ID | n | R 分布 |
|---|---|---|---|
| **CN** | H1–H9；E3-A/B/C；E3-N1/N2/N5；E3-P1/P3/P4；E4-N1/N2/N5 | **24** | R0×16 · R2×1 · R3×5 · R5×2 |
| **US** | INT-1 / INT-3 / INT-5 | **3** | R0×1 · R3×1 · R5×1 |
| **JP** | INT-7 / INT-11 | **2** | R0×1 · R5×1 |
| **KR** | INT-9 | **1** | R3×1 |
| **合计** | — | **30** | R0×18 · R2×1 · R3×7 · R5×4 |

仍 **仅提名、未编码**：INT-2/4/6（Round 1）；INT-8/10/12（Round 2）；E4-N3/N4。

分波笔记：[`holdout-t4-phase-synthesis.md`](holdout-t4-phase-synthesis.md)（CN 波合并）· [`holdout-int-135-synthesis.md`](holdout-int-135-synthesis.md) · [`holdout-int-7911-synthesis.md`](holdout-int-7911-synthesis.md)

---

## 2. 共享阶梯（四法域同一把尺子）

```text
产品 / 品牌 / 整机叙事          → 最多 E2；常停 R0
监管贴纸 / 奖项 / 组合宣传       → 不等于 E3（须对 claim 要素）
显式专利号 + claims-check PASS → 可达 E3 / R3（仍可 FAIL）
E3 成立                        ≠ E4（映射 ≠ 可归因价值）
单件裁判判赔 + E3 + exact_patent 指标 → 可 R5
具名许可 / 服务费捆包            → 常停 R2；E4=Unknown
判赔金额 / 许可费               ≠ 内在专利价格（争议·交易情境）
Unknown ≠ 0 · 不继承 · Screening ≠ Proof · 判赔 ≠ 自动 R5
```

**跨法域观察：** 同一阶梯在 CN / US / JP / KR 上 **可执行且同向**——拒假抬与条件满足时诚实抬，都不依赖法域标签，而依赖 **证据形态**（叙事 vs 监管显式号 vs 单件裁判）。

---

## 3. 机制等价表（CN ↔ INT）

| 机制槽 | CN 已编码例 | INT 已编码例 | 共享结局 |
|---|---|---|---|
| **拒假抬（叙事/产品环境）** | H6–H8；E3-N1/N2/N5；E3-C | INT-1 TearLab；INT-7 Style | **R0** |
| **诚实 E3（监管/官方显式 + claim）** | E3-A/B；E3-P1/P3/P4 | INT-3 Aubagio OB；INT-9 Kerendia Green List | **R3**（无 E4） |
| **诚实 E4→R5（单件裁判）** | E4-N1；E4-N2 | INT-5 PureWick；INT-11 ReFa Art.102 | **R5** |
| **许可/捆包残留** | E4-N5（服务费捆） | （本轮无对位 INT） | **R2**（CN） |
| **权利叙事 ⊥ R** | H9（无效维持≠侵权胜诉；RC 可选） | — | formal **R0** |

监管通道对照（非自动继承）：

| 通道 | 法域 | 作用 | 不是什么 |
|---|---|---|---|
| NHSA / 说明书显式 ZL | CN | 提高 E3 候选密度 | ≠ E4 |
| FDA Orange Book + PI | US | 同左 | ≠ E4 |
| MFDS Green List + label | KR | 同左 | ≠ E4 |
| 单件法院/知財高裁判赔 | CN / US / JP | 可提供 E4 + exact_patent 指标 | ≠ 自动 R5；≠ 内在价 |

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

### 4.2 US / JP / KR — INT

| ID | 法域 | 专利 | Claims / map | R | 一句话 |
|---|---|---|---|---|---|
| INT-1 | US | US11536707B2 | FAIL | **R0** | TearLab 市售≠本专利 LFA 整合 |
| INT-3 | US | US8802735B2 | PASS (strong) | **R3** | Aubagio OB+PI；无 E4 |
| INT-5 | US | US10376407B2 | confirmed (court) | **R5** | PureWick 单件 royalty |
| INT-7 | JP | JP6956213B2 | FAIL | **R0** | Style 品牌≠多区块垫 claim |
| INT-9 | KR | KR101614164B1 | PASS (strong) | **R3** | Kerendia Green List；无 E4 |
| INT-11 | JP | JP5847904B2 | confirmed (court) | **R5** | ReFa 大合議单件判赔 |

---

## 5. 法域对照结论（诚实）

| 问题 | 结论 |
|---|---|
| V0.7 阶梯能否跨 CN→US/JP/KR 复用？ | **能（小 N）**：同一拒抬/诚实抬模式复现 |
| 多法域是否已「证明世界级覆盖」？ | **否**：n_INT=6；EP 未编码；冷启动新人计时仍弱 |
| 监管通道是否可互换？ | **形态等价、不得自动继承**：OB ≈ Green List ≈ NHSA 显式号，仍须 claims-check |
| 判赔法域差异是否改 R 规则？ | **不改**：CN/US/JP 单件裁判均要求 E3 + exact_patent 指标才 R5 |
| 对 T1/T2/T3 的含义 | T1：DEMPE⊥E3–E4 已由跨域样本加压；T2：场景树「何时用 V0.7 vs 判赔/FRAND」有实证锚；T3：RC/Horizon/Network 仍 research-only，**不**借本文件 adopt V0.8 |

---

## 6. 明确不宣称

- 无美元内在价值引擎、无胜诉/上市/许可费率预测准确率  
- 无 V0.8 adopt / schema freeze / S1 升格  
- 无「全法域 R5」或「Orange Book / Green List 自动 R3/R5」  
- 无 EP/其他法域完成；INT-2/4/6/8/10/12 **未**编码  
- CN 24 件 ≠ 全球代表性样本

---

## 7. 下一跳（需用户确认才编码）

1. INT-2/4/6 或 INT-8/10/12 — 用户确认 ID + T0 后再 encode  
2. E4-N3/N4 或新 E4 波（避开已编码集）  
3. 可选：EP / 更多 KR·JP 对称槽（仍须预注册扩展）  
4. T3 探针继续；**禁止**用本跨域合成顺带 adopt V0.8  

---

## 8. 指针

| Doc | Role |
|---|---|
| [`holdout-t4-phase-synthesis.md`](holdout-t4-phase-synthesis.md) | CN 波 H→E4 合并 |
| [`holdout-extrapolation-synthesis.md`](holdout-extrapolation-synthesis.md) | H1–H9 |
| [`holdout-e3-abc-synthesis.md`](holdout-e3-abc-synthesis.md) · [`holdout-e3-n125-synthesis.md`](holdout-e3-n125-synthesis.md) · [`holdout-e3-p134-synthesis.md`](holdout-e3-p134-synthesis.md) | E3 三波 |
| [`holdout-e4-n125-synthesis.md`](holdout-e4-n125-synthesis.md) | E4-N1/N2/N5 |
| [`holdout-int-135-synthesis.md`](holdout-int-135-synthesis.md) · [`holdout-int-7911-synthesis.md`](holdout-int-7911-synthesis.md) | INT R1 / R2 |
| [`../../docs/methodology/t4-international-holdout-nominees-round1.md`](../../docs/methodology/t4-international-holdout-nominees-round1.md) · [`…-round2.md`](../../docs/methodology/t4-international-holdout-nominees-round2.md) | 提名（含未编码） |
