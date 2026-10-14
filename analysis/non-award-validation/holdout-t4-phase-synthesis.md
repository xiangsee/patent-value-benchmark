# T4 Phase Synthesis — H / E3 / N / P / E4（合并）

日期：2026-10-14 Asia/Shanghai  
T0（holdout 钟）：**2026-10-13**（除非另注）  
正式基线：**V0.7 + schema 1.0** · **未** adopt / freeze V0.8  
预注册：[`docs/methodology/external-extrapolation-preregistration.md`](../../docs/methodology/external-extrapolation-preregistration.md)

> 把 T4 **CN 波**外推学习收成一份可引用笔记。不替代各波 synthesis；不发明 gold / 美元预测准确率。
> 含 INT 的跨法域总表见 [`holdout-t4-cross-jurisdiction-synthesis.md`](holdout-t4-cross-jurisdiction-synthesis.md)。

---

## 1. 波次总表

| 波 | 样本 | Formal R | 测到什么 | 测不到什么 |
|---|---|---|---|---|
| **H1–H9** | 普通/半明星 holdout | **R0 ×9** | 拒假抬升；产品 E2 ≠ R3；RC 可选不改 R | 「有真 E3 时能否正确抬」 |
| **E3-A/B/C** | 显式映射探针 | **R3 / R3 / R0** | claims-check **双向**：可过可不过 | R4/R5、可归因 ¥ |
| **E3-N1/N2/N5** | 叙事偏中间案 | **R0 ×3** | 品牌/工艺/功能叙事 ≠ claim 要素 | 中段 E3 密度上限 |
| **E3-P1/P3/P4** | 医保显式 ZL + 规格/处方 | **R3 ×3**（plausible） | 监管材料点名 ZL + 可对主骨架 → 诚实 R3 | **仍无 E4** |
| **E4-N1/N2** | 单件法院判赔 | **R5 ×2** | 单件 + 裁判 E3 + exact_patent 指标 → 可 R5 | 内在专利定价；销售损失自动成立 |
| **E4-N5** | 具名许可公告 | **R2** | 许可披露 = E5/R2；服务费捆 ≠ E4 | 自动 R3/R5 |

分波笔记：[`holdout-extrapolation-synthesis.md`](holdout-extrapolation-synthesis.md) · [`holdout-e3-abc-synthesis.md`](holdout-e3-abc-synthesis.md) · [`holdout-e3-n125-synthesis.md`](holdout-e3-n125-synthesis.md) · [`holdout-e3-p134-synthesis.md`](holdout-e3-p134-synthesis.md) · [`holdout-e4-n125-synthesis.md`](holdout-e4-n125-synthesis.md)

---

## 2. 阶梯纪律（可背诵）

```text
产品/品牌叙事     → 最多 E2，常停 R0
显式 ZL + claims  → 可达 E3 / R3（仍可 FAIL）
映射成立          ≠ 可归因价值（E3 ≠ E4）
法院单件判赔      → 可 E4；升 R5 仍需 E3 + exact_patent 指标
具名许可费        → 若捆包/服务费科目 → 常停 R2，E4=Unknown
判赔 / 许可金额   ≠ 内在专利价格（争议/交易情境）
Unknown ≠ 0；不继承；Screening ≠ Proof
```

---

## 3. 过滤器演进（提名质量）

| 轮 | 过滤器 | 结果 |
|---|---|---|
| H | 普通/半明星 + 陷阱层 | 9/9 停住 |
| E3-ABC | 显式映射候选 | 2 PASS / 1 FAIL |
| N | 「看起来有产品」但无要素级公开 | 3/3 FAIL（叙事陷阱） |
| P | **显式 ZL** + 可对 claim 的规格/处方 | 3/3 R3 plausible |
| E4 | 判赔点名 ZL / 具名销售损失 / 具名 ZL 许可 | 2×R5（判赔）+ 1×R2（许可残留） |

含义：T4 外推成功 = **过程可操作 + 拒假抬 + 条件满足时诚实抬**，不是预测胜诉或定价。

---

## 4. E4 专项（相对 E3）

1. **有判赔 ≠ 自动 R5**（E4-N1/N2）：必须同时有裁判确认的 exact-patent↔carrier 与 `scope_level=exact_patent` 指标；金额写入 gaps 为争议情境。  
2. **销售损失软标签会撒谎**（E4-N2）：法院说理改用侵权获利——编码以裁判为准，不保留提名话术。  
3. **具名许可 ≠ E4**（E4-N5）：四件捆 +「技术服务和指导费」+ 关联交易 → attributable_value 保持 Unknown → **R2**。  
4. **E3-P 的 R3 不预支 E4**：医保贴纸与处方对齐停在 R3。

---

## 5. 对世界级模型的含义（T4 → T1/T2/T3）

| 含义 | 指向 |
|---|---|
| V0.7 R/E/Obs 在未见专利上可执行 | 正式面继续正确 |
| 「抬升精度」需 E3/E4 密度，不只靠拒抬 | 继续提名/编码需用户确认 |
| 货币证据必须带 scope/actor/legal context | 设计草案 §3.2E Monetary rule 已由 E4 波实证 |
| 许可/组合/服务费是 Horizon/Network 边界问题 | **不**塞回 R；T3 旁路对象仍 research-only |
| 冷启动 H-E3（新人计时）仍弱 | 不宣称世界级可用性已证明 |

---

## 6. 明确不宣称

- 无美元内在价值引擎、无胜诉/上市预测准确率  
- 无 V0.8 adopt / schema freeze  
- 无「全员 R5」或「许可自动 R5」  
- CN holdout ≠ 多法域外推完成  

---

## 7. 下一跳（仍需用户确认才编码）

- E4-N3/N4 仍提名；或新 E4 波（需避开已编码集）  
- 国际/非 CN 外推预注册扩展（可选）  
- T3：Horizon / Network / optional RC 探针继续，**不**借 T4 成功顺带 adopt  

跨法域合并（含 INT）：[`holdout-t4-cross-jurisdiction-synthesis.md`](holdout-t4-cross-jurisdiction-synthesis.md)

程序入口：[`docs/methodology/world-class-roadmap.md`](../../docs/methodology/world-class-roadmap.md)
