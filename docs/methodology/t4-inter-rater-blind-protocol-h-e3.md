# T4 Inter-Rater / Dual-Coder Blind Protocol（H-E3 新人可操作性）

日期：2026-10-14 Asia/Shanghai（案表冻结 / 授权开跑：2026-10-28）  
状态：**研究协议** — 案表已冻结并**授权开跑**；**仍不**授权把盲评草稿合并进 holdout；案表 → [`t4-inter-rater-blind-case-table-h-e3.md`](t4-inter-rater-blind-case-table-h-e3.md)；Coder 包 → [`t4-he3-coder-pack-a.md`](t4-he3-coder-pack-a.md) · [`t4-he3-coder-pack-b.md`](t4-he3-coder-pack-b.md)  
正式基线：**V0.7 + schema 1.0** · **未** adopt / freeze V0.8  
锚定假设：预注册 [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md) **H-E3**（Cold-start operability）及可选加门 §6.3  
程序入口：[`world-class-roadmap.md`](world-class-roadmap.md)

> 目的：把「新人 / 第二编码者能否按 Getting Started 独立得到可复现的 R 与 E3 判断」写成可执行盲评协议。  
> 当前 H1–H9 合成将 H-E3 标为 **弱支持**（代理完成；缺外部新人复测）——本文件是补测设计，**不是**已完成试验报告。

---

## 1. 目的与非目标

### 1.1 目的

1. 量化 **双编码者** 在固定案集上对 **Realization stage（R）** 与 **E3 / claims-check 结论** 的一致性。  
2. 分离「工具/文档不可用」与「证据本身 Ambiguous」两类失败。  
3. 为 roadmap「Not proven inter-rater reliability」提供 **可开跑** 的试验规格。

### 1.2 非目标（硬）

| 不做 | 原因 |
|---|---|
| 用一致率当「准确率 / 金标准命中」 | 一致 ≠ 正确；本轮无美元 / 总分 gold |
| 本 PR 启动编码或改已发表 holdout R | 协议冻结 ≠ 开跑；开跑需用户另批案表 + T0 |
| adopt V0.8 / freeze schema / S1 | 与 H-E3 正交 |
| 强制普通案填写 RC | RC 永远可选（#49） |
| 比较两个编码者谁「更资深正确」 | 裁断协议服务可操作性，不人物评级 |

---

## 2. 样本设计

### 2.1 规模（预注册默认）

| 层 | n（案） | 用途 |
|---|---|---|
| **核心层 A** | **8–12** | 主报告：新人可操作性 + R/E3 一致率 |
| 其中陷阱子集 | ≥3 | 产品叙事强 / 贴纸 / 同族拥挤等（压拒假抬） |
| 其中 E3 候选子集 | ≥2 | 有显式专利号或监管点名候选（压诚实抬与 FAIL） |
| **可选层 B** | +4–6 | 仅当层 A 一次跑完且用户批准扩样；可含 1–2 非 CN |

**合计默认上限：** 不开层 B 时 **≤12**；开层 B 时 **≤18**。  
小于 8 案 → 只允许描述性笔记，**不得**宣称「H-E3 已独立复测通过」。

### 2.2 纳入 / 排除

**纳入：** 公开可得、非 Round 1/2 教科书机制 in-sample；优先普通 / 半明星 CN 发明；每案可锁定 T0。  
**排除：** 已作本试验「标准答案展示」的培训案；编码者本人曾私写过该案正式 Ledger；缺公开源导致无法冷启动的案。

### 2.3 案表冻结

开跑前单独冻结一页 **案 ID 表**（专利号、T0、层标签 A/B、是否陷阱/E3 候选）。  
改表必须修订本协议日期行，并在结果笔记标明「案表修订后」。

**已冻结并授权开跑（2026-10-28）：** [`t4-inter-rater-blind-case-table-h-e3.md`](t4-inter-rater-blind-case-table-h-e3.md)  
层 A **n=10**（陷阱 3 · E3 候选 6 · 基线 1）；T0=**2026-10-13**；角色：Coder A=patent Bot · Coder B=Leo · Adjudicator=xiang pu · Facilitator=code Bot。  
Coder 包（**无** §F）：[`t4-he3-coder-pack-a.md`](t4-he3-coder-pack-a.md) · [`t4-he3-coder-pack-b.md`](t4-he3-coder-pack-b.md)。**开跑 ≠ encode 合并。**

---

## 3. 人员与盲法

### 3.1 角色

| 角色 | 人数 | 要求 |
|---|---|---|
| **Coder A / Coder B** | 2 | 至少一人为 **仓库新人**（未参与该案原 encode；未读该案已合并 synthesis 结论表） |
| **Adjudicator** | 1 | 第三人；开跑前不读两份草稿；只在分歧裁断阶段介入 |
| **Facilitator**（可兼任 Adjudicator 以外的维护者） | 0–1 | 发案、收卷、计时；**不**提示 R/E3 答案 |

允许：两名均为新人；或一名新人 + 一名熟悉工具但不熟悉本案表的编码者。  
禁止：用「已知道该案合并 R」的原作者当 Coder，除非明确标为 **非盲校准席**（不计入主一致率）。

### 3.2 盲什么

| 对 Coders 隐藏 | 对 Coders 可见 |
|---|---|
| 他案 / 本试验的目标 R、已发表 synthesis 结论行 | Getting Started、V0.7、schema 1.0、陷阱表、本协议 |
| 另一 Coder 的草稿与分数 | 公开专利文本、公开产品/监管页（自行检索） |
| Adjudicator 倾向 | 案表上的专利号与 T0 |
| 「这题应该抬 / 不该抬」的口头暗示 | validate_data / CI 用法 |

### 3.3 时限（可操作性度量）

每案墙钟建议：**90–180 分钟**（含检索）；整层 A 建议在 **5 个工作日** 内双人交卷。  
超时仍交卷 → 记 `operability=timeout_completed`；交不出可校验 Ledger → `operability=fail`（计 H-E3 失败信号）。

---

## 4. 双编码流程

```text
1. Facilitator 发案表 + 固定 T0 + 文档包（不含任何目标 R）
2. Coder A、B **独立** 按 Getting Started 写 Ledger 1.0（可诊断草稿）
3. 每人提交前自跑 validate_data；允许文档级修正，禁止互看
4. 密封交卷 → Facilitator 登记提交时间与 CI 结果
5. 仅当两份都交卷后，打开一致性比较（§5）
6. 分歧 → Adjudicator 按 §6 裁断；裁断理由写入笔记
7. 结果笔记只报协议指标；不把一致率写成准确率
```

**交付物（每 Coder × 每案）：**

1. Ledger JSONL（schema 1.0）或等价结构化草稿  
2. 显式字段备忘：`realization_stage`（R）、`exact_patent_value_carrier_link` / claims-check 结论（PASS / FAIL / unknown）、E3 是否成立（yes / no / unknown）  
3. 检索日志摘要（URL / 文书名即可；勿贴全文版权材料）  
4. 自报耗时（分钟）

不要求：RC 实验对象、美元指标、V0.8 字段。

---

## 5. 指标（主：R 与 E3 一致）

### 5.1 主指标

| 指标 | 定义 | 报告方式 |
|---|---|---|
| **R 一致率** | 两 Coder 的 `realization_stage` 完全相同的案数 / 有效案数 | 比例 + 分子分母；附分歧列联 |
| **E3 一致率** | 两 Coder 对「E3 是否成立」三分类（yes / no / unknown）相同的案数 / 有效案数 | 同上 |
| **Claims-check 一致率**（附） | PASS / FAIL / not_attempted 一致 | 与 E3 分列，避免把「未做核验」算成 FAIL 一致 |
| **一次 CI 绿率**（H-E3 操作） | 首次 PR/校验即绿，或仅文档级修正后绿 | 按 Coder 与按案各报一次 |
| **可完成率** | 时限内交出可校验 Ledger 的案比例 | 低于预注册预期 → H-E3 崩溃信号 |

### 5.2 建议补充（不替代主指标）

- **粗 κ（Cohen’s κ）** 在 R 与 E3 上各算一版；n&lt;12 时只作描述，不作「显著」宣称。  
- **加权一致（可选）：** R 相邻一级（如 R0 vs R2）与跨三级（R0 vs R5）分列，防止把「差一级」与「假抬成功」混谈。  
- **陷阱命中：** 陷阱子集上，是否两人都拒假抬（R3+ = 0）。

### 5.3 预注册通过线（建议；开跑前可微调但须写明）

| 门 | 建议阈值 |
|---|---|
| H-E3 操作未崩溃 | 可完成率 ≥ **80%**；一次 CI 绿率 ≥ **70%**（按案、两 Coder 平均） |
| 一致性「可讨论」 | R 一致率 ≥ **0.70** 且 E3 一致率 ≥ **0.70** |
| 一致性「强支持」 | 上两者均 ≥ **0.80**，且陷阱子集无双人假抬 R3+ |
| 主失败 | 可完成率 &lt;50%，或陷阱子集出现 **双人** 假抬 R3+，或 E3 一致率 &lt;0.50 |

未达「强支持」仍可报「弱支持 / 需改 Getting Started」——与当前 extrapolation synthesis 语气一致。

---

## 6. 分歧裁断

### 6.1 何时裁断

仅当某案 **R 不一致** 或 **E3 三分类不一致**（或一人 FAIL、一人 PASS 且影响 R）时进入裁断。  
CI 格式分歧（字段名、日期格式）由 Facilitator 文档级修正，**不**算实质分歧。

### 6.2 裁断顺序

1. Adjudicator 先只看：**专利公开文本 + 两份检索日志中的同源公开材料 + T0**（仍不看已发表 synthesis 目标行）。  
2. 对照 V0.7 硬规则：Unknown≠0、不继承、Screening≠Proof、E3≠E4、判赔≠自动 R5。  
3. 给出 **裁断 R** 与 **裁断 E3**，并勾选原因码（下表）。  
4. 若证据在 T0 下确实不足 → 裁断为 **unknown / R0（或证据允许的最低 R）**，不得用 post-T0 结果抬升。

### 6.3 原因码（写入笔记）

| 码 | 含义 |
|---|---|
| `DOC_GAP` | Getting Started / 陷阱文档不足导致误用 |
| `EVIDENCE_AMBIG` | 公开源本身 Ambiguous（合理人可分歧） |
| `RULE_MISREAD` | 误读 V0.7 规则（如贴纸当 E3） |
| `LEAKAGE_RISK` | 疑似用了 post-T0 或内部知识 |
| `SCOPE_MIX` | 搞混 claim-set / 同族 / 产品线范围 |

报告时：**DOC_GAP + RULE_MISREAD** 计为工具/文档问题；**EVIDENCE_AMBIG** 计为任务难度，不单独判 H-E3 崩溃。

### 6.4 裁断后怎么用

- 主一致率仍基于 **裁断前** 双人原始标签（协议诚实）。  
- 另附一行「裁断后参照标签」供后续文档修订，**不**回写已合并 holdout，除非用户另批 encode PR。

---

## 7. 明确不宣称

本协议跑完后，**即使**达到「强支持」门，也 **不得** 自动宣称：

1. 模型「准确」或可替代人类估值 / 律师意见  
2. 跨法域 / 全球新人普遍可操作（样本默认偏 CN）  
3. V0.8 应被 adopt，或 schema 应 freeze  
4. 一致率 = 外推预测效度（那是 H-E1/E2/E4 主轨，不是本协议单独能证明的）  
5. 美元、胜诉、许可费率可被一致编码出来  
6. 未参与试验的持有人/审查员会得到同一 R

允许宣称的上限语气：

> 「在 n=…、双人盲评下，R/E3 一致率分别为 …；新人可完成率为 …；H-E3 从弱支持更新为 …（仍受样本与法域限制）。」

---

## 8. 与既有 T4 材料的关系

| 材料 | 关系 |
|---|---|
| [`external-extrapolation-preregistration.md`](external-extrapolation-preregistration.md) | 本协议落实 H-E3 + §6.3 可选人类 gold 门 |
| [`../analysis/non-award-validation/holdout-extrapolation-synthesis.md`](../../analysis/non-award-validation/holdout-extrapolation-synthesis.md) | 现状：H-E3 弱支持；本协议是补测设计 |
| [`../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md`](../../analysis/non-award-validation/holdout-t4-cross-jurisdiction-synthesis.md) | 跨法域已编码合成；**不**本试验案表 |
| Getting Started / traps | 试验「可见文档包」；分歧原因码可反哺修订 |
| [`t4-inter-rater-blind-case-table-h-e3.md`](t4-inter-rater-blind-case-table-h-e3.md) | 层 A 案表（2026-10-28 **冻结**；已授权开跑；仍不 encode 合并） |
| [`t4-he3-coder-pack-a.md`](t4-he3-coder-pack-a.md) · [`t4-he3-coder-pack-b.md`](t4-he3-coder-pack-b.md) | Coder A/B 盲包（**无** §F 密封键） |
| [`t4-he3-visible-doc-pack.md`](t4-he3-visible-doc-pack.md) | 可见文档固定路径；禁读全文案表 |

---

## 9. 开跑检查清单

- [x] 案表冻结（ID / T0 / 层）— [`t4-inter-rater-blind-case-table-h-e3.md`](t4-inter-rater-blind-case-table-h-e3.md)（2026-10-28）  
- [x] 两名 Coder + Adjudicator + Facilitator 确认：patent Bot / Leo / xiang pu / code Bot  
- [x] 盲包就绪（[`t4-he3-coder-pack-a.md`](t4-he3-coder-pack-a.md) · [`t4-he3-coder-pack-b.md`](t4-he3-coder-pack-b.md)；§F 未发 Coder）  
- [x] 本协议通过线确认（§5.3 未改）  
- [x] 明确：**开跑 ≠ encode 合并**；合并仍需另 PR + 用户确认  

---

## 10. 变更记录

| 日期 | 变更 |
|---|---|
| 2026-10-14 | 初稿：样本、盲法、分歧裁断、R/E3 指标、不宣称；docs only |
| 2026-10-27 | 指针 → 案表草案 `t4-inter-rater-blind-case-table-h-e3.md`（层 A=10；**未**冻结、**未**开跑）；docs only |
| 2026-10-28 | 案表冻结并授权开跑；角色填入；Coder 包 A/B + visible-doc-pack；§9 勾选；Coder 禁读全文案表；**仍不** encode 合并 |
