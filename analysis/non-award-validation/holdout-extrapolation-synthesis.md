# Holdout Extrapolation Synthesis (H1–H9)

日期：2026-10-13  
预注册：[`docs/methodology/external-extrapolation-preregistration.md`](../../docs/methodology/external-extrapolation-preregistration.md)（附录 A）  
正式基线：V0.7 + schema 1.0 · **未** adopt V0.8 · **未** 发明 gold/美元

> 交叉案笔记：小 N=9 普通/非教科书 holdout，统一 T0=2026-10-13。本文件按预注册 §4 勾选，**禁止只报喜**。

---

## 1. Per-case formal R

| ID | Layer | ZL | Formal R | E | Mapping | Trap / note |
|---|---|---|---|---|---|---|
| H1 | L1 | ZL202111562464.8 | **R0** | — | unknown | 普通软件 SME；无产品 E2 抬升 |
| H2 | L1 | ZL201910471967.0 | **R0** | — | unknown | 软件授权 SME |
| H3 | L1 | ZL202011067792.6 | **R0** | — | unknown | 区域液压 SME |
| H4 | L1 | ZL202011166628.0 | **R0** | — | unknown | 化工机械 SME |
| H5 | L1 | ZL202110513769.3 | **R0** | — | unknown | 陶瓷材料 SME |
| H6 | L2 | ZL202110686604.6 | **R0** | E2 | unknown | 来也 RPA 产品线 → **产品≠专利**；停 R0 |
| H7 | L2 | ZL202110448799.0 | **R0** | E2 | unknown | 刀具产品叙事；SKU↔grant 未确认 |
| H8 | L2 | ZL202010875322.6 | **R0** | E2 | unknown | 柳工装载机整机语境易假抬；停 R0 |
| H9 | L3 | ZL201910958076.8 | **R0** | E2 | unknown | 无效维持≠侵权胜诉；**RC 可选**；formal 仍 R0 |

**汇总：** 9/9 = R0；0 件 R3+；全部 `exact_patent_value_carrier_link = unknown`。

---

## 2. §4.1 主成功勾选

| 标准 | 结果 | 说明 |
|---|---|---|
| Holdout 完成率 ≥80% | **通过** | 9/9 通过 `validate_data.py` + Diagnostic/report；RC `validate_rights_control.py` 绿；unittest 42 OK |
| H-E1 无 E3 → 0 件 R3+ | **通过** | 9/9 无 E3；0 件 R3+ |
| H-E2 unknown mapping | **通过** | 全部 unknown；gaps 写明 exact mapping / attribution |
| H-E4 陷阱触发且正确处理 | **通过（弱–中）** | L2 H6/H7/H8 显式产品 E2 且拒抬 R；H9 权利叙事拒抬 R；未见「假抬成功混入通过」 |
| 综合笔记含失败模式 | **本文件** | 见 §3 |

**主成功（过程纪律 / 可操作性）：支持。** 不宣称预测准确率、不宣称美元、不默认 V0.8。

---

## 3. Failure modes & limits（诚实）

1. **全员 R0 的天花板：** 本轮公开材料下没有 exact-patent E3，故无法检验「有 E3 时能否正确升到 R3+」——外推支持的是**停住**，不是**抬升精度**。  
2. **选样仍偏「可写完」：** L1 多为中小权利人当前态；陷阱以「产品/整机叙事」为主，**未**强触发同族误映射 / 300+ 不继承 / pre-filing E2 soft-warn（本批无该类源）。若要强化 H-E4，需另开预注册补 1–2 件高陷阱案，**不得**静默扩容改标准。  
3. **H-E3 冷启动可用性：** 由代理按 Getting Started 编码一次 PR 绿，**不是**外部新人计时试验 → H-E3 标 **弱支持 / 未独立复测**。  
4. **H-E5 RC：** 仅 H9 一件有裁决叙事；RC 写出且不改 formal R；样本量不足 → H-E5 **inconclusive**（预注册允许，不影响主成功）。  
5. **证据深度：** 多案 E2 依赖公开产品/无效评述二级源；未做权利要求比对或许可合同核验——Observability 对 mapping/value 保持 unknown，符合 Unknown≠0。  
6. **Ledger ID 前缀：** 为避免「普通 LEDGER-ZL* 不得有 RC」测试被 L3 可选 RC 误伤，holdout 使用 `LEDGER-HOLDOUT-H*`。这是测试诚实性修补，**不是** schema 变更。  
7. **不假装：** 无 Gold 预测、无许可金、无「外推准确率 %」。失败模式未伪装成训练成功。

---

## 4. Hypotheses（预注册）对照

| 假设 | 判定 |
|---|---|
| H-E1 无继承 / 无假 R3+ | **支持** |
| H-E2 Unknown≠0 | **支持** |
| H-E3 冷启动可操作性 | **弱支持**（代理完成；缺外部新人复测） |
| H-E4 陷阱表面 | **支持（局限样本）** |
| H-E5 可选 RC 无摩擦 | **inconclusive**（n=1） |

---

## 5. Allowed next steps（§4.4）

| 允许 | 不允许 |
|---|---|
| 宣称「V0.7 在本小 N 普通 holdout 上外推纪律成立（停住/不混淆）」 | 自动 adopt V0.8 / freeze |
| 讨论文档/脚手架硬化（Getting Started、陷阱例） | 把 RC 塞进 1.0 必填 |
| 另开预注册补高陷阱案或外部新人计时 | 事后用 post-T0 成功回填 T0 R |

---

## 6. Pointers

- Case notes: `analysis/non-award-validation/holdout/`  
- Ledgers / evidence / sources: `data/*/holdout-ZL*.jsonl`  
- H9 RC: `data/experimental/rights-control/holdout-H9-ZL201910958076.8.jsonl`  
- Diagnostics/reports regenerated for 36 ledgers (27 prior + 9 holdout)
