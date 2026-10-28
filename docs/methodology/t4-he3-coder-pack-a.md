# H-E3 盲评 · Coder A 包（patent Bot）

日期：2026-10-28 Asia/Shanghai  
收件人：**Coder A = patent Bot**  
Facilitator：code Bot · Adjudicator：xiang pu（交卷前不介入）  
正式基线：**V0.7 + schema 1.0** · **不要**写 V0.8 / RC 强制 / 美元总分

> 本包是你的**全部试验说明**。按下方展示顺序独立编码。  
> **本包不含**目标 R、claims-check 金标、另一 Coder 卷、案表 §F 密封键。

---

## 1. 必读（可见文档）

| 文档 | 用途 |
|---|---|
| [`../getting-started.md`](../getting-started.md) | 冷启动入口 |
| [`../cold-start-quick-reference.md`](../cold-start-quick-reference.md) | 速查 |
| [`../cold-start-trap-checklist.md`](../cold-start-trap-checklist.md) | 陷阱自检 |
| [`t4-inter-rater-blind-protocol-h-e3.md`](t4-inter-rater-blind-protocol-h-e3.md) | 盲评协议（指标与交付物） |
| [`t4-he3-visible-doc-pack.md`](t4-he3-visible-doc-pack.md) | 允许打开的固定路径总表 |
| 本包 §3 案表 + §4 展示顺序 | 你的案件与顺序 |

自行检索：**公开**专利文本、公开产品/监管页。可用 `validate_data` / CI。

---

## 2. 禁链清单（试验期间禁止打开）

打开下列任一路径即视为**破盲**（即使「只是好奇」）：

1. **`t4-inter-rater-blind-case-table-h-e3.md` 全文**（含 §F 密封键）——**只读本 coder-pack，不要打开案表文件**  
2. 任意 `analysis/non-award-validation/holdout-*-synthesis.md`（含 extrapolation / e3-abc / e3-n125 / e3-p134 等）  
3. 任意 `analysis/non-award-validation/holdout/` 下与下表专利对应的笔记  
4. 任意 `reports/generated/DIAG-LEDGER-HOLDOUT-*`（或同义诊断报告）中与下表专利对应的文件  
5. 已合并 `data/ledgers/holdout-*` 中与下表 **专利号** 对应的 Ledger（含金标 R）  
6. 另一 Coder（Leo）的草稿、频道或 PR  
7. Facilitator / Adjudicator 关于「该抬 / 不该抬」的口头或私信提示

允许：公开 CNIPA / 谷歌专利等文本；公司官网与监管公开页；仓库**通识**文档（Getting Started、schema、陷阱表、本协议、本包）。

---

## 3. 案表（层标签不是答案）

- `baseline` — 普通冷启动  
- `trap` — 易假抬表面；按陷阱表自处  
- `e3_candidate` — 须做 claims-check；结论可为 PASS / FAIL / unknown

| Blind ID | 专利号 | 发明名称（短） | 权利人（提示） | 层标签 | T0 |
|---|---|---|---|---|---|
| HE3-01 | ZL202111562464.8 | 基于大数据的中小企业信息化服务平台 | 深圳空间数字科技 | baseline | 2026-10-13 |
| HE3-02 | ZL202110686604.6 | 结合 RPA 和 AI 的许可证生成方法及装置 | 北京来也网络科技 | trap | 2026-10-13 |
| HE3-03 | ZL202010875322.6 | 负载敏感充液阀、液压系统和装载机 | 广西柳工机械 | trap | 2026-10-13 |
| HE3-04 | ZL201910958076.8 | 建立废钢等级划分神经网络模型方法 | 北京同创信通科技 | trap | 2026-10-13 |
| HE3-05 | ZL201710337622.7 | 助产用凝胶及其制备方法 | 成都英诺新科技 | e3_candidate | 2026-10-13 |
| HE3-06 | ZL201310419886.9 | 监护设备及其生理参数处理方法及系统 | 深圳迈瑞生物医疗 | e3_candidate | 2026-10-13 |
| HE3-07 | ZL202310277767.8 | 具有美白、抗衰功效的护肤组合物及其应用 | 江苏仅三生物科技 | e3_candidate | 2026-10-13 |
| HE3-08 | ZL202210708835.7 | 舒缓修护三重蛋白组合物及其应用 | 绽妍生物科技 | e3_candidate | 2026-10-13 |
| HE3-09 | ZL201810828154.8 | 机器人手眼标定系统及其工作流程 | 广东奥普特科技 | e3_candidate | 2026-10-13 |
| HE3-10 | ZL202111620840.4 | 复方降压药物组合物及其制备方法 | 深圳信立泰药业 | e3_candidate | 2026-10-13 |

---

## 4. 你的展示顺序（必须按此序）

种子：`HE3-A-2026-10-13`（无需理解算法；只按下列顺序做）

1. HE3-05  
2. HE3-01  
3. HE3-08  
4. HE3-03  
5. HE3-10  
6. HE3-02  
7. HE3-07  
8. HE3-04  
9. HE3-09  
10. HE3-06  

---

## 5. 每案交付物

对每一 Blind ID 交出（协议 §4）：

1. Ledger **schema 1.0** 草稿（或等价结构化草稿）  
2. Realization stage **R**（R0–R5）  
3. E3：**yes / no / unknown**  
4. claims-check：**PASS / FAIL / not_attempted**（`e3_candidate` 案必须尝试）  
5. 检索摘要（公开源 URL / 名称 + 一两句）  
6. 墙钟耗时（分钟）

**不要：** 强制 RC；美元 FMV；V0.8 字段；把本案草稿直接 merge 进主 holdout（交卷给 Facilitator 即可）。

---

## 6. 时限

- 每案墙钟 **90–180 分钟**  
- 整层 A（10 案）建议 **5 个工作日** 内交卷  
- 超时仍交 → 记 `operability=timeout_completed`；交不出可校验草稿 → `operability=fail`

---

## 7. 交卷

交卷给 **Facilitator = code Bot**。在 Adjudicator 宣布裁断阶段前，**不要**与 Coder B（Leo）讨论本案 R/E3。

---

## 8. 变更记录

| 日期 | 变更 |
|---|---|
| 2026-10-28 | 初版 Coder A 包；无 §F；顺序按冻结案表 |
