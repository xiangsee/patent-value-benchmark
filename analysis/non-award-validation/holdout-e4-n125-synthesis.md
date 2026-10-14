# Holdout E4-N1/N2/N5 synthesis（Round 1 encode）

日期：2026-10-14 · T0=**2026-10-13** · iphouse `get_case_detail` + 上市许可公告 · **未** adopt V0.8

| ID | ZL | E3 | E4 | R | 要点 |
|---|---|---|---|---|---|
| E4-N1 | ZL201410204545.4 | confirmed（裁判） | confirmed（判赔 ¥40.07M） | **R5** | 单件；思立微指纹芯片侵权；酌定侵权获利 |
| E4-N2 | ZL200680012412.0 | confirmed（claim1 比对） | confirmed（判赔 ¥40M） | **R5** | 单件盘壳；法院**未**采信原告销售损失，改按被告获利 |
| E4-N5 | ZL202010875349.5 | unknown | unknown | **R2** | 具名许可但四件捆 + 服务费科目；无产品映射 |

## 纪律（相对提名与「判赔≠自动 R5」）
1. **N1/N2**：判赔可支撑 R5 **仅当**同时具备 exact-patent E3 映射 + `scope_level=exact_patent` 指标；金额=争议情境，写入 gaps，不作内在定价。
2. **N2 纠正**：提名中的「销售损失」软标签在裁判说理中被否定——编码以法院采用的**侵权获利**为准。
3. **N5**：具名 ZL 许可 = E5/R2；**不能**把 200 万服务费抬成 E4/R5。
4. E3 ≠ E4；E4 ≠ 内在专利价格；Formal = V0.7 + schema 1.0。
