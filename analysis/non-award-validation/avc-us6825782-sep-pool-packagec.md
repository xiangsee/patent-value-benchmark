# Package C — SEP / Patent-Pool External Replication

## US6825782B2 / NTT Docomo arithmetic coding & termination inside the AVC/H.264 Patent Portfolio License

日期：2026-10-12  
状态：Package C SEP/pool replication — experimental; V0.7 remains adopted; V0.8 remains research-only; **no schema 1.0 change**  
关联：Issue #11

## 一、为什么选这件（而不是诉讼-only「假 SEP」）

Package C 要求在 CRISPR portfolio 之外，再完成：

1. **1× SEP / patent-pool / cross-license** 外部复现；
2. 优先 **可公开核验** 的池或交叉许可（MPEG LA / Via LA、VIA Licensing、Avanci、或清晰 FRAND-SEP 披露）；
3. 避免 CRISPR；避免只有诉讼损害赔偿、没有许可结构的伪 SEP；
4. **不发明专利**——必须能在公开清单里指到具体专利号。

**AVC/H.264 Patent Portfolio License（Via LA，前 MPEG LA）** 满足这些约束：

- 公开 **Attachment 1 / Cross-Reference Chart** 列出具体专利与标准条款映射；
- 公开 **Licensor** 与大量 **Licensee** 名单；
- 公开 **费率表 / enterprise cap**，并明确费率 **不随专利件数增减**；
- 结构是真正的 **multi-licensor patent pool**，不是单边诉讼叙事。

锚定专利：

| 字段 | 公开事实 |
|---|---|
| 专利 | [US6825782B2](https://patents.google.com/patent/US6825782B2/en) |
| 发明人 | Frank Jan Bossen |
| 权利人 | NTT Docomo, Inc. |
| 授权日 | 2004-11-30 |
| 申请号 | 10/665,638（filed 2003-09-18） |
| 池映射 | Via LA 2026-02 Cross-Reference：claim **12** → H.264 **§9.3** CABAC 条款族 |
| 许可方 | Via LA 公开名单含 **NTT DOCOMO, INC.** |

Avanci 虽有公开车端费率，但 **不公开专利清单**，无法在公开源上把「某一件专利 ∈ 池」钉死；本案因此选择 Via LA AVC。

## 二、T0 = 2026-10-12（当前状态冷启动）

Ledger：`data/ledgers/non-award-avc-us6825782-sep-pool.jsonl`

### V0.7 能诚实记录的

| 维度 | 状态 |
|---|---|
| Realization stage | **R2 — Rights Transaction** |
| Pool membership / licensor path | confirmed（cross-ref + NTT Docomo licensor） |
| Standard essentiality map (pool chart) | confirmed（claim 12 → §9.3） |
| Exact patent → named product | **unknown** |
| Patent-level attributable value | **unknown** |
| Pool royalty card | observed at **program** scope only |

### 为什么是 R2，而不是 R3+

能确认：

1. 该专利出现在 AVC 专利组合许可的公开交叉表中；
2. 权利人是公开的 AVC licensor；
3. 因此存在 **pool-mediated rights transaction**（权利进入多许可人组合许可并可被再许可）。

不能确认：

1. 哪一个具体手机 / OS / 摄像头 / STB / 流媒体实现了 claim 12；
2. 公开费率表中有多少（哪怕 $0.01）属于本专利；
3. 若去掉本专利，被许可人是否仍须支付同一费率（FAQ 已暗示：费率不随专利件数变化）。

因此：

> **exact patent → product = Unknown**  
> **patent-level attributable value = Unknown**  
> **不得把池费率或被许可人生态抬成 R3/R4/R5**

这与 CRISPR 单件 US8697359 故意停在 R2 同构，只是机制从「生物医药组合许可网络」换成了「标准必要专利池」。

## 三、对 V0.7 的压力测试：池 / SEP 能说清什么、说不清什么

### V0.7 做对了什么

- 允许把 **pool membership + licensor 路径** 记成 R2（真实权利交易），而不强迫写成 R0；
- 允许记录 **标准映射证据**（`standardized_in`）而不自动继承产品实施；
- **Unknown ≠ 0**：公开池费率很大，也不把金额分给单件 SEP；
- 拒绝把「Apple / Google / Netflix 在被许可人名单」读成「他们的产品实施了 US6825782」。

### V0.7 仍然说不清楚的（需要 Portfolio & Jurisdiction Network 对象）

同一件 SEP 的决策相关信息，很大一块是：

```text
Patent / Claim Set
        ×
Patent Pool / FRAND program
        ×
Multi-licensor membership
        ×
Licensee graph
        ×
Standard / profile scope
        ×
Rate card (independent of patent count)
        ×
Essential-counterpart jurisdictions
```

而不是单件 R-stage。

具体丢失的 material information：

1. **Pool membership graph** — Attachment 1 是数百/上千件专利与多司法辖区同族，不是一件专利；
2. **Rate-card independence** — 公开 FAQ：费率不因 essential patent 增减而变；单件 R 阶段无法表达「边际专利对池价格贡献可为零」；
3. **Licensor–licensee–standard 三角** — 被许可人买的是组合自由实施权，不是单件专利的双边许可；
4. **与 CRISPR 对照** — CRISPR 是竞争/互补 portfolio + stacked licenses + 司法辖区分歧；AVC 是协作型 pool + 统一定价。二者都需要 graph object，但边的类型不同。

### 与 CRISPR 的对照（Package C 复制意义）

| 维度 | CRISPR US8697359 | AVC US6825782 |
|---|---|---|
| 行业 | 生命科学 / 基因编辑 | 消费电子 / 视频编码 SEP |
| 网络形态 | 竞争 portfolio + stacked licenses | 协作 patent pool |
| 单件阶段 | R2 | R2 |
| 金额证据 | portfolio license + product revenue | pool rate card + enterprise cap |
| 金额能否分给单件 | 否 | 否 |
| H3 | Supported | **Replicated outside life science** |

## 四、H3 / H4 对本案的含义

- **H3 Portfolio Dependency**：在非生命科学、公开专利池场景下再次成立——单件 Ledger 会丢失 pool graph、统一定价与被许可人网络。
- **H4 Monetary evidence is contextual**：池费率是 **program-scope** 证据，不是 intrinsic patent price；且公开规则写明与专利件数脱钩。

## 五、刻意不做的事

- 不改 schema 1.0；
- 不把 V0.8 research fields 写进正式 Ledger；
- 不把诉讼损害赔偿当 SEP 价值；
- 不发明未在 Via LA 清单出现的专利号；
- 不把 Avanci「无专利清单」案例硬做成 exact-patent 映射。

## 六、Package C 进度

| # | Case | Stage | Status |
|---|---|---|---|
| 1 | CRISPR portfolio (US8697359) | R2 | complete |
| 2 | AVC/H.264 pool SEP (US6825782) | R2 | **complete（本 PR）** |
| 3 | non-life-science complex product portfolio | — | remaining 0/1 |

## 七、工件

- Ledger：`data/ledgers/non-award-avc-us6825782-sep-pool.jsonl`
- Evidence：`data/evidence/non-award-v0.8-packagec-sep-avc-us6825782.jsonl`
- Sources：`data/source-registry/non-award-v0.8-packagec-sep-avc-us6825782.jsonl`
- Network note object：`analysis/non-award-validation/avc-sep-pool-network.json`
- Diagnostic：`reports/generated/DIAG-LEDGER-NA-AVC-US6825782-T0-2026.md`
