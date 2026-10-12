# Package C — Non-Life-Science Complex Product Portfolio Replication

## CN110165116B / 比亚迪刀片电池 CTP 专利簇（汽车动力电池产品系统）

日期：2026-10-12  
状态：Package C non-life-science complex product portfolio replication — experimental; V0.7 remains adopted; V0.8 remains research-only; **no schema 1.0 change**  
关联：Issue #11

## 一、为什么选这件（而不是再做一次 SEP / 也不是复用 Apple–Samsung）

Package C 要求在 CRISPR portfolio 与 SEP/pool 之外，再完成：

1. **1× non-life-science complex product portfolio** 外部复现；
2. 价值明显落在 **产品系统 / 多专利栈**，而不是单件专利；
3. V0.7 单件 R-stage **说不清** portfolio context；
4. 避免把 Apple–Samsung Rights Control pair 直接当成 portfolio 案；
5. 优先有公开披露的多专利产品栈。

**比亚迪刀片电池 CTP 族**满足这些约束：

- 同优先权（2019-01-09）/ 同日申请（2019-06-21）形成 **大规模 CTP + 长单体** 专利簇（Google Patents family tree 列出 40+ 相关中国申请/授权）；
- 官方披露刀片电池为 **CTP 产品平台**，并装车汉 / 唐 / Atto 3；
- 媒体与管理层叙事常称「300+ 项核心专利」——明确是组合叙事；
- 锚点 **CN110165116B** 与 Issue #2 冷启动的同日兄弟 **CN110165118B** 可分离，专门做 portfolio 压力测试，而不复用 Rights Control 手机诉讼对。

锚定专利：

| 字段 | 公开事实 |
|---|---|
| 专利 | [CN110165116B](https://patents.google.com/patent/CN110165116B/zh) |
| 申请号 | CN201910544020.8 / ZL201910544020.8 |
| 发明人 | 王传福、何龙、孙华军、王信月、朱燕 |
| 权利人 | 比亚迪股份有限公司 |
| 授权日 | 2019-12-20 |
| 簇内互补例 | CN110165115B（V1/V2≥55% 体积利用率）；CN110165118B（同日结构兄弟） |
| 产品平台 | 刀片电池 Blade Battery（CTP） |
| 装车载体 | 汉 EV / 唐 / Atto 3（公司产品披露） |

## 二、T0 = 2026-10-12（当前状态冷启动）

Ledger：`data/ledgers/non-award-byd-blade-cn110165116-portfolio.jsonl`

### V0.7 能诚实记录的

| 维度 | 状态 |
|---|---|
| Realization stage | **R0 — Rights Existence** |
| CTP 专利簇成员资格 | confirmed（bibliography / family tree + siblings） |
| Blade / Han 产品平台事实 | confirmed at **product** scope |
| Exact patent → Blade / Han | **unknown** |
| Patent-level attributable value | **unknown** |
| 「300+ 专利」叙事 | observed at **program/platform** scope only |

### 为什么是 R0，而不是 R3+

能确认：

1. CN110165116B 已授权，且处于刀片 CTP 同日/同优先权专利簇中；
2. 刀片电池作为 CTP 产品平台、汉等车型装车有官方披露；
3. 互补兄弟专利覆盖「结构/支撑」与「体积利用率」等不同 claim theme。

不能确认：

1. 官方文件是否点名 **CN110165116B**（而非 118 或其他兄弟）被某款汉/唐/Atto 3 电池包实施；
2. 「300+ 专利」中有多少（哪怕 1%）属于本专利；
3. 若去掉本专利、保留 115/118/电芯层专利，产品是否仍可商业化。

因此：

> **exact patent → product = Unknown**  
> **patent-level attributable value = Unknown**  
> **不得把刀片/汉的产品成功抬成 R3/R4/R5**

这与 CRISPR 单件 US8697359 故意不继承 CASGEVY 产品价值同构；本案机制从「多权利人许可网络」换成「同权利人复杂产品系统多专利栈」。因缺少可确认的 rights-transaction 路径（CRISPR 的 Editas in-license / AVC 的 pool membership），本案停在 **R0** 而非 R2——这是诚实结果，不是失败。

## 三、对 V0.7 的压力测试：复杂产品组合能说清什么、说不清什么

### V0.7 做对了什么

- 允许记录 **portfolio membership** 与 **product-platform E2**，而不强迫升 R；
- **Unknown ≠ 0**：刀片/汉再成功，也不把金额或装车量分给单件 CTP 专利；
- 拒绝把「二手源常引 CN110165116」读成「官方 exact mapping」；
- 与 Issue #2 对 CN110165118 的 R0 冷启动一致，并显式保留 **同日兄弟误映射风险**。

### V0.7 仍然说不清楚的（需要 Portfolio / Product-System Network 对象）

同一件 CTP 专利的决策相关信息，很大一块是：

```text
Patent / Claim Set
        ×
Complementary sibling claim sets (structure vs utilization vs cell)
        ×
Same-assignee CTP filing wave
        ×
Product platform (Blade Battery)
        ×
Multi-vehicle fitment graph
        ×
Portfolio-size narrative (≠ any one grant)
```

而不是单件 R-stage。

具体丢失的 material information：

1. **Complementary claim-set layering** — 115 的利用率阈值与 116 的结构/支撑起草共同描述 CTP 架构，单件 Ledger 只能看见其中一个；
2. **Sibling mis-mapping risk** — 116 vs 118 同题同优先权，二手源常混用；Rights Control / exact mapping 必须按申请号拆开；
3. **Platform → multi-vehicle edges** — 汉/唐/Atto 3 是平台装车边，不是专利实施边；
4. **与 CRISPR / AVC 对照** — CRISPR 是竞争/互补多权利人 + stacked licenses；AVC 是协作 pool；本案是 **同权利人产品系统多专利栈**。三者都需要 graph object，但边的类型不同。

### 与 CRISPR / AVC 的对照（Package C 复制意义）

| 维度 | CRISPR US8697359 | AVC US6825782 | Blade CN110165116B |
|---|---|---|---|
| 行业 | 生命科学 | 视频编码 SEP | **汽车动力电池 / CTP** |
| 网络形态 | 竞争 portfolio + stacked licenses | 协作 patent pool | **同权利人复杂产品系统栈** |
| 单件阶段 | R2 | R2 | **R0** |
| 金额/规模证据 | portfolio license + product revenue | pool rate card | 平台装车 +「300+ 专利」叙事 |
| 金额能否分给单件 | 否 | 否 | **否** |
| H3 | Supported | Replicated (SEP/pool) | **Replicated (complex product)** |

## 四、H3 对本案的含义

- **H3 Portfolio Dependency**：在非生命科学、复杂汽车产品系统场景下再次成立——单件 Ledger 会丢失互补 claim 层、兄弟误映射、平台多车边与组合规模叙事。
- 本案 **不** 再扩展 SEP/pool 机制（已由 AVC 覆盖）；它补的是 Package C 清单里「complex product portfolio」这一格。

## 五、刻意不做的事

- 不改 schema 1.0；
- 不把 V0.8 research fields 写进正式 Ledger；
- 不把「300+ 专利」或汉 EV 销量继承为单件专利价值；
- 不发明未在公开族谱出现的专利号；
- 不把 Issue #2 的 CN110165118 冷启动 ledger 改写成 portfolio 案（另立 116 锚点）；
- 不采用 V0.8。

## 六、Package C 进度

| # | Case | Stage | Status |
|---|---|---|---|
| 1 | CRISPR portfolio (US8697359) | R2 | complete |
| 2 | AVC/H.264 pool SEP (US6825782) | R2 | complete |
| 3 | Blade CTP complex product portfolio (CN110165116B) | R0 | **complete（本 PR）** |

## 七、工件

- Ledger：`data/ledgers/non-award-byd-blade-cn110165116-portfolio.jsonl`
- Evidence：`data/evidence/non-award-v0.8-packagec-blade-cn110165116.jsonl`
- Sources：`data/source-registry/non-award-v0.8-packagec-blade-cn110165116.jsonl`
- Network note object：`analysis/non-award-validation/byd-blade-ctp-portfolio-network.json`
- Diagnostic：`reports/generated/DIAG-LEDGER-NA-BYD-BLADE-CN110165116-T0-2026.md`（校验后生成）
