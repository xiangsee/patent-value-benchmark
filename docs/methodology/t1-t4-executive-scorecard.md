# T1–T4 执行记分卡（Executive Scorecard）

> 日期：**2026-10-27** Asia/Shanghai · 中文主述  
> Formal：**V0.7 + schema 1.0** · **未** adopt / freeze V0.8  
> 程序总览：[`world-class-roadmap.md`](world-class-roadmap.md)  
> Holdout 计数口径：[`../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md`](../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md)（INT-1–18 全量刷新；历史 [#74](https://github.com/xiangsee/patent-value-benchmark/pull/74) / [#82](https://github.com/xiangsee/patent-value-benchmark/pull/82) / [#83](https://github.com/xiangsee/patent-value-benchmark/pull/83)）

**一句话：** 四轨并行推进世界级专利价值评估研究；本页只回答「各轨做完什么 / 还缺什么 / 下一刀砍哪」——**不**授权 adopt、编码或扩样。

---

## 总览

| 轨 | 状态灯 | 已完成（摘要） | 缺口 | 下一刀 |
|---|---|---|---|---|
| **T1 理论** | 🟢 文档成套 | Construct + DEMPE⊥E3–E4 + FRAND/判赔≠R5/FMV + **建构×场景表** | 金额学派字段 cheat-sheet 仍可加深 | 可选：与 IVS/OECD 字段级一行对照 |
| **T2 比较** | 🟢 导航可用 | 矩阵 + IVS/OECD + 决策树 + **INT-5/9 走查** | 仍可加更多法域例 | 可选：再补 E4-N5（许可捆包）走树 |
| **T3 探针** | 🟡 研究-only | P1–P8；RC 可选+#49 无裁决夹具 | Gate 0；未升格；无 S1 | **保持 Gate 0**；禁借 T4 成功 adopt |
| **T4 外推** | 🟢 小 N 成波 | **42** 件已编码；INT R1–R3 **全编码** | E4-N3/N4；H-E3 未开跑 | 开 H-E3 盲评或编 E4-N3/N4——本卡不授权 |

**Holdout 计数：** 合计 **n=42**（CN 24 + INT-1–18）· R0×24 · R2×1 · R3×10 · R5×7 · 仍仅提名：E4-N3/N4。跨法域合成已按 INT-1–18 全量刷新。

---

## T1 理论

| | |
|---|---|
| **Done** | [`t1-theory-memo-value-construct.md`](t1-theory-memo-value-construct.md)；[`t1-dempe-vs-claims-e3e4.md`](t1-dempe-vs-claims-e3e4.md)；[`t1-frand-damages-vs-r5-fmv.md`](t1-frand-damages-vs-r5-fmv.md)；[`t1-construct-scenario-matrix.md`](t1-construct-scenario-matrix.md) |
| **Gaps** | 与 IVS/OECD 字段级一行 cheat-sheet 仍可加深（非阻塞） |
| **Next knife** | 可选字段级对照；**不**借此 adopt V0.8 |

## T2 既有模型比较

| | |
|---|---|
| **Done** | [`existing-models-comparison-matrix.md`](existing-models-comparison-matrix.md)；[`t2-v07-to-ivs-oecd-practice-schools.md`](t2-v07-to-ivs-oecd-practice-schools.md)；[`t2-scenario-selection-decision-tree.md`](t2-scenario-selection-decision-tree.md)；[`t2-decision-tree-walkthrough-int5-int9.md`](t2-decision-tree-walkthrough-int5-int9.md) |
| **Gaps** | 许可捆包 / FRAND 组合走查仍可补（非阻塞） |
| **Next knife** | 可选 E4-N5 或 SEP 假想枝；**不**新编码 |

## T3 自有创新探针

| | |
|---|---|
| **Done** | P1–P8（含 P7 Horizon、P8 Network vocab）；RC optional 计划 + [#49](https://github.com/xiangsee/patent-value-benchmark/pull/49) 规则；无裁决夹具 `data/experimental/rights-control/fixture-no-ruling-ordinary-r0.jsonl` |
| **Gaps** | 全部 research / experimental；**无** S1–S3；CF 无 schema |
| **Next knife** | **停在 Gate 0**——只改探针文档或夹具，不借 T4 n=42 推动 V0.8 |

## T4 真实外推

| | |
|---|---|
| **Done** | 预注册；H→E3→E4 CN 波；INT R1–R3 **complete（INT-1–18）**；跨法域合成 **全量刷新** → **n=42**（CN/US/JP/KR/EP·UK·DE）[`../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md`](../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md)；H-E3 协议稿 |
| **Gaps** | E4-N3/N4；H-E3 **未开跑**；新人一致率未证 |
| **Next knife** | （A）用户确认后编 E4-N3/N4；或（B）开 H-E3 盲评——本卡不授权 |

### T4 计数速查（跨法域合成；INT-1–18 全量）

| 法域 | n | R 分布 |
|---|---|---|
| CN | 24 | R0×16 · R2×1 · R3×5 · R5×2 |
| US | 4 | R0×2（INT-1/2）· R3×1（INT-3）· R5×1（INT-5） |
| JP | 3 | R0×2（INT-7/8）· R5×1（INT-11） |
| KR | 3 | R3×2（INT-9/10）· R5×1（INT-12） |
| EP/UK·DE | 8 | R0×4（INT-4/13/14/16）· R3×2（INT-6/15）· R5×2（INT-17/18） |
| **Σ** | **42** | R0×24 · R2×1 · R3×10 · R5×7 |

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
| [`t1-construct-scenario-matrix.md`](t1-construct-scenario-matrix.md) | T1 建构×场景对照表 |
| [`t2-decision-tree-walkthrough-int5-int9.md`](t2-decision-tree-walkthrough-int5-int9.md) | T2 树走查 INT-5 / INT-9 |
| [`../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md`](../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md) | T4 跨法域合成（**INT-1–18 全量**；n=42；CN/US/JP/KR/EP·UK·DE） |
| [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md) | T4 预注册 |
| [`t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md) | H-E3 协议（未开跑） |
| [`t4-international-holdout-nominees-round1.md`](t4-international-holdout-nominees-round1.md) · [`round2`](t4-international-holdout-nominees-round2.md) · [`round3`](t4-international-holdout-nominees-round3.md) | T4 INT R1–R3（INT-1–18 **已编码**） |
