# P8 — Network relation vocabulary v0（约定稿）

> 状态：**V0.8 probe — research-only；NOT frozen / NOT adopted / NOT schema**。正式面仍为 **V0.7 + schema 1.0**。  
> 前置：[`p4-network-json-naming.md`](p4-network-json-naming.md) · 设计草案 [`../model-v0.8-design-draft.md`](../model-v0.8-design-draft.md) §3.2D / §5 **S3 预备**（本文件 ≠ 批准 S3）。  
> 适用对象：`analysis/non-award-validation/*-network.json` 研究制品。

---

## 1. Purpose & non-goals

### Purpose

把 P4 草图里的「共享 relation 候选」固化成一份 **可对照的受控词表 + 边键约定**，使后续 network JSON：

1. 优先使用 snake_case `relation`；  
2. 把「非继承」写成一等边 `not_apportioned_to`；  
3. 为 CRISPR 类自由文本边提供 **只读映射表**（不强制回写历史字符串）。

### Non-goals

| 不做 | 原因 |
|---|---|
| Schema freeze / validator | S3 未批准；仍 research JSON |
| 改写 CRISPR 既有 `relation` 自由文本 | 避免破坏已引用分析制品 |
| 生成 portfolio score / 池费率→单件价 | 设计草案硬禁 |
| V0.8 adopt | 用户未批准 |

---

## 2. Document header（三例共通核）

必有（已存在）：

| 键 | 含义 |
|---|---|
| `network_id` | 稳定 id |
| `status` | 须含 research / not schema-adopted 语义 |
| `t0_date` | 切片日 |
| `purpose` | 一句话研究目的 |
| `nodes[]` | `{id, label, type}` |
| `edges[]` | 至少 `{from, to, relation}` |

**本轮可选、非破坏元数据（已写入三例）：**

```json
"convention": {
  "doc": "docs/methodology/v0.8-probes/p8-network-relation-vocabulary-v0.md",
  "version": "0.1-research",
  "relation_surface": "legacy_preserved"
}
```

- `relation_surface=legacy_preserved`：历史 `edges[].relation` **保持原样**；规范化以本文件映射表为准。  
- 未来新边：优先直接写 §3 规范码（可将 `relation_surface` 标 `canonical_preferred`）。

---

## 3. Controlled `relation` vocabulary（snake_case）

### 3.1 Core（跨 CRISPR / AVC / Blade 共享意图）

| code | 方向语义（from → to） | 出现例 | 不得解读为 |
|---|---|---|---|
| `owns` | 主体拥有专利/claim_set | AVC | 自动 E3 |
| `contains_claim_set` | 专利/组合包含 claim_set | AVC | claim 有效 |
| `member_of` | 专利 ∈ portfolio / 池组合 | Blade；AVC 近义 `member_of_portfolio_license` | 单件价值=组合价值 |
| `licenses_to` | 许可方 → 被许可方/集合 | AVC | 许可费=E4 单件 |
| `essential_to` | claim_set / 专利 → 标准条款 | AVC（现 `essential_to_sections`） | SEP⇒高 R |
| `exact_implemented_in` | 专利 → 具名产品（E3 候选边） | Blade | 无证据也写 confirmed |
| `not_apportioned_to` | 组合经济/叙事 **不可**分摊到该专利 | AVC、Blade | 「无价值」；实为 **非继承** |
| `complements` | 同组合内互补主题 | Blade≈`complementary_claim_theme` | 自动抬 R |
| `blocks` | 阻断/对抗（诉讼或行政对抗） | CRISPR 类对抗边的规范目标码 | 胜诉金=专利价 |

### 3.2 Extended（允用；保持短码）

| code | 含义 | 来源对齐 |
|---|---|---|
| `administers` | 池管理方管理池 | AVC |
| `licensor_in` | 权利人作为池内许可方 | AVC |
| `prices_as` | 经济对象按某费率/价目计价 | AVC（**非**单件 intrinsic price） |
| `equipped_in` | 平台/系统装备了某产品 | Blade |
| `underpins_candidate` | 专利为平台叙事候选支撑（弱于 exact） | Blade |
| `sibling_mis_mapping_risk` | 同族/姊妹件误映射风险边（诊断用） | Blade |
| `develops_commercializes` | 主体开发/商业化产品 | CRISPR 自由文本规范化目标 |
| `in_force_in` | 权利/组合在某法域仍有效或未决 | CRISPR「estate remains」类 |
| `asserted_in` | 在某法域主张/诉讼 | CRISPR litigation 类 |
| `competes_with` | 干涉/抵触申请对抗 | CRISPR interference / Count 1 |
| `in_licensed` | 被许可方获得许可 | CRISPR |

### 3.3 Aliases（读时等价；写新边时用左列）

| 规范码 | 历史/近义字符串（保留可读） |
|---|---|
| `member_of` | `member_of_portfolio_license` |
| `essential_to` | `essential_to_sections` |
| `complements` | `complementary_claim_theme` |
| `develops_commercializes` | `develops/commercializes` |
| `competes_with` | `U.S. interference`；`PTAB Count 1 competing subject matter`；`Interference 106,115 and broader priority disputes` |
| `in_licensed` | `in-licensed` |
| `licenses_to` | `non-exclusive Cas9 license including CASGEVY field`（加 `detail`） |
| `asserted_in` | `asserted patent rights / litigation` |
| `in_force_in` | `large unaffected patent estate remains after Count 1 priority decision`；`non-U.S. estate remains`；`mixed revocation/amended-claim outcomes`（outcomes 亦可用 `detail`） |

> CRISPR 边 **不回写**：分析文继续引用原 `relation` 句子；本表供检索/未来边使用。

---

## 4. Edge key convention

| 键 | 要求 | 三例现状 |
|---|---|---|
| `from`, `to`, `relation` | **必有** | 全有 |
| `status` | 推荐：`confirmed` / `strong_evidence` / `inference` / `unknown` | CRISPR、Blade 有；AVC 缺 |
| `evidence_ids` | 推荐数组（可 `[]` 若仅结构示意） | CRISPR、Blade 有；**AVC 缺** |
| `detail` | 可选自由文本补充 | AVC、Blade 部分有 |

**新边清单（作者自检）：**

1. `relation` ∈ §3.1/§3.2（或先查 §3.3 alias 再选规范码）  
2. 尽量带 `status` + `evidence_ids`  
3. 组合费率/产品收入 → 单件：必须考虑是否应加 `not_apportioned_to`  
4. 禁止发明 `network_score` / 边权重

---

## 5. Node `type`（保留并微扩展）

已见表：`patent`, `claim_set`, `portfolio`, `product`, `jurisdiction`, `licensee`, …  
扩展保留：`patent_pool`, `standard`, `owner_licensor`, `pool_administrator`, `licensee_set`, `program_economics`, `product_platform`, `program_narrative`, `commercialization_stack`。

新类型可加，但须在 `purpose` 或边 `detail` 说明；**不要**用 type 偷运价值分数。

---

## 6. Hard rules（与 V0.7 对齐）

```text
Portfolio / pool value  ≠  Σ single-patent values
Jurisdiction A          ≠  Jurisdiction B
Pool royalty            ≠  patent price
Program「N+ patents」   ≠  E3
Edge exists             ≠  R-stage uplift
not_apportioned_to      =  非继承一等边（不是注释）
```

Network 对象 **不**写入 formal Ledger 行；不经 `validate_data.py`。

---

## 7. What changed in this PR（轻量元数据）

三份既有 JSON **仅**增加顶层 `convention` 对象（§2）；**未**改 `nodes` / `edges` / 既有 `relation` 字符串。

| 文件 | 变更 |
|---|---|
| `crispr-portfolio-network.json` | +`convention` |
| `avc-sep-pool-network.json` | +`convention` |
| `byd-blade-ctp-portfolio-network.json` | +`convention` |

---

## 8. Stop conditions

- 无 schema / CI 新强制  
- 无 V0.8 adopt / S3 启动  
- 无自由文本边被静默改写  
- 无分数字段
