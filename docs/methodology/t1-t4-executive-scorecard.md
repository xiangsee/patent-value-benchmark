# T1–T4 执行记分卡（Executive Scorecard）

> 日期：**2026-10-14** Asia/Shanghai · 中文主述  
> Formal：**V0.7 + schema 1.0** · **未** adopt / freeze V0.8  
> 程序总览：[`world-class-roadmap.md`](world-class-roadmap.md)  
> Holdout 计数口径：[#74 跨法域合成](https://github.com/xiangsee/patent-value-benchmark/pull/74) → [`../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md`](../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md)

**一句话：** 四轨并行推进世界级专利价值评估研究；本页只回答「各轨做完什么 / 还缺什么 / 下一刀砍哪」——**不**授权 adopt、编码或扩样。

---

## 总览

| 轨 | 状态灯 | 已完成（摘要） | 缺口 | 下一刀 |
|---|---|---|---|---|
| **T1 理论** | 🟢 文档成套 | Construct + DEMPE⊥E3–E4 + FRAND/判赔≠R5/FMV | 建构×场景选用总表未写 | 一张「建构×T2 树」对照表 |
| **T2 比较** | 🟢 导航可用 | 矩阵 + IVS/OECD 深化 + 场景决策树 | 缺少量已编码案的选用worked example | 可选：用 INT/E4 各 1 例走树 |
| **T3 探针** | 🟡 研究-only | P1–P8；RC 可选+#49 无裁决夹具 | Gate 0；未升格；无 S1 | **保持 Gate 0**；禁借 T4 成功 adopt |
| **T4 外推** | 🟢 小 N 成波 | **30** 件已编码（CN24+US3+JP2+KR1） | 未编码提名；H-E3 盲评未开跑 | 用户确认后再 encode；或开 H-E3 跑 |

**Holdout 计数（#74）：** 合计 **n=30** · R0×18 · R2×1 · R3×7 · R5×4 · 仍仅提名：INT-2/4/6、INT-8/10/12、E4-N3/N4。

---

## T1 理论

| | |
|---|---|
| **Done** | [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md)（Construct / Two Clocks / RC⊥R）；[`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md)；[`t1-frand-damages-vs-r5-fmv.md`](t1-frand-damages-vs-r5-fmv.md) |
| **Gaps** | 「价值建构 × 场景选用」一张总表仍缺；与金额学派字段级对照未收成 cheat-sheet |
| **Next knife** | 写短表：每建构对应 T2 树哪一枝 + 禁止偷换句（docs only） |

## T2 既有模型比较

| | |
|---|---|
| **Done** | [`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md)；[`t2-v07-to-ivs-oecd-practice-schools.md`](t2-v07-to-ivs-oecd-practice-schools.md)；[`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md) |
| **Gaps** | 决策树尚少「带已编码 holdout ID」的走查例；不阻碍日常选用 |
| **Next knife** | 可选附录：INT-5（判赔枝）+ INT-9（监管 E3 停 R3）各走一棵树 |

## T3 自有创新探针

| | |
|---|---|
| **Done** | P1–P8（含 P7 Horizon、P8 Network vocab）；RC optional 计划 + [#49](https://github.com/xiangsee/patent-value-benchmark/pull/49) 规则；无裁决夹具 `data/experimental/rights-control/fixture-no-ruling-ordinary-r0.jsonl` |
| **Gaps** | 全部 research / experimental；**无** S1–S3；CF 无 schema |
| **Next knife** | **停在 Gate 0**——只改探针文档或夹具，不借 T4 n=30 推动 V0.8 |

## T4 真实外推

| | |
|---|---|
| **Done** | 预注册；H→E3→E4 CN 波；INT R1/R2 部分编码；跨法域合成 **#74（n=30）**；H-E3 盲评协议稿 [`t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md) |
| **Gaps** | INT/E4 提名未编码；H-E3 **未开跑**；冷启动新人一致率未证；EP 等法域空 |
| **Next knife** | （A）用户确认 ID+T0 后 encode 下一枚；或（B）批准案表后开 H-E3 双人盲评——二者都需另批，本卡不授权 |

### T4 计数速查（摘自 #74）

| 法域 | n | R 分布 |
|---|---|---|
| CN | 24 | R0×16 · R2×1 · R3×5 · R5×2 |
| US | 3 | R0 / R3 / R5 各 1 |
| JP | 2 | R0 / R5 |
| KR | 1 | R3 |
| **Σ** | **30** | R0×18 · R2×1 · R3×7 · R5×4 |

---

## 硬停（本卡不解除）

- 不 adopt / freeze V0.8；不改正式 schema 1.0  
- 不自动 R5；不把 FRAND/判赔当 FMV  
- 不发明 gold / 美元预测准确率  
- 不扩普通 contrib 洪水；encode 须用户确认名单 + T0  

## 指针

| 文档 | 用途 |
|---|---|
| [`world-class-roadmap.md`](world-class-roadmap.md) | 四轨总览与进度板 |
| [`../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md`](../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md) | #74 跨法域计数与共享阶梯 |
| [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md) | T4 预注册 |
| [`t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md) | H-E3 协议（未开跑） |
