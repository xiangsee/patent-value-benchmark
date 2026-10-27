# Holdout E4 Round 1 synthesis（N1–N5）

日期：2026-10-27 · T0=**2026-10-13** · iphouse `get_case_detail` + 上市许可公告 · **未** adopt V0.8

| ID | ZL | E3 | E4 | R | 要点 |
|---|---|---|---|---|---|
| E4-N1 | ZL201410204545.4 | confirmed（裁判） | confirmed（判赔 ¥40.07M） | **R5** | 单件；思立微指纹芯片侵权；酌定侵权获利 |
| E4-N2 | ZL200680012412.0 | confirmed（claim1 比对） | confirmed（判赔 ¥40M） | **R5** | 单件盘壳；法院**未**采信原告销售损失，改按被告获利 |
| E4-N3 | ZL99117225.6 | confirmed（claim1 鉴定+比对） | confirmed（判赔 ¥7.663M） | **R5** | 单件 USB 闪存；软许可=池 **demote**；相对 T0 **已届满**（2019-11-14）→ historical damages |
| E4-N4 | **ZL01139886.8**（替换主专利） | confirmed（claim1 A–J） | confirmed（判赔 ¥29.65M） | **R5** | 攀钢氮化钒工艺；**非** ZL201010284583.7；贡献率酌减；相对 T0 **已届满**（2021-12-04） |
| E4-N5 | ZL202010875349.5 | unknown | unknown | **R2** | 具名许可但四件捆 + 服务费科目；无产品映射 |

## 纪律（相对提名与「判赔≠自动 R5」）
1. **N1/N2/N3/N4**：判赔可支撑 R5 **仅当**同时具备 exact-patent E3 映射 + `scope_level=exact_patent` 指标；金额=争议情境，写入 gaps，不作内在定价。
2. **N2 纠正**：提名中的「销售损失」软标签在裁判说理中被否定——编码以法院采用的**侵权获利**为准。
3. **N3**：软「专利授权许可收入」= 专利池 → **不作**单件 E4；仅法院单件判赔升 R5。届满 → historical damages gaps。
4. **N4**：提名原稿主键错误——**替换**为案涉/判赔/禁令主专利 ZL01139886.8；被告 ZL2010… 仅抗辩。届满 → historical damages gaps。
5. **N5**：具名 ZL 许可 = E5/R2；**不能**把 200 万服务费抬成 E4/R5。
6. E3 ≠ E4；E4 ≠ 内在专利价格；Formal = V0.7 + schema 1.0。
