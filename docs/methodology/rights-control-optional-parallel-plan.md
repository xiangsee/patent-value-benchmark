# Rights Control — Optional Parallel-Track Implementation Plan（细则）

日期：2026-10-13  
状态：**Research / design spec only — NOT frozen, NOT adopted**  
正式方法基线：**V0.7 (adopted)**  
正式数据表面：**Ledger / Diagnostic `schema_version: "1.0"`（[`v0.1.0`](https://github.com/xiangsee/patent-value-benchmark/releases/tag/v0.1.0) 已冻结）**  
实验对象：`schema/experimental/claim-set-rights-control.schema.json`（`experimental-0.1`）  
前置：[`model-v0.8-design-draft.md`](model-v0.8-design-draft.md) §3.2B / §5 S1 · [`rights-control-research-overview.md`](rights-control-research-overview.md) · P1 [`v0.8-probes/p1-rc-field-promotion-diff.md`](v0.8-probes/p1-rc-field-promotion-diff.md) · P2 [`v0.8-probes/p2-rc-negative-ordinary-r0.md`](v0.8-probes/p2-rc-negative-ordinary-r0.md) · PR [#49](https://github.com/xiangsee/patent-value-benchmark/pull/49)

> **硬边界**  
> 本文是 **可选并行轨** 的实施细则与迁移草图，供评审。  
> - **不** freeze 任何 schema；**不** bump 正式 `1.0`；**不**采纳 V0.8；  
> - **不**把 RC 写进正式 Ledger 行；**不**开放普通冷启动扩样；  
> - 冷启动 / 外部复现默认 **只碰 V0.7 + schema 1.0**；RC **永远可选**。

---

## 1. Purpose & non-goals

### 1.1 Purpose

把「若将来把 RC 升为 **optional 并行对象**」需要遵守的规则写成可执行细则，固定三件已拍板事实：

1. **RC 对普通专利永远可选**（默认不填、不出现也不失败）。  
2. **允许无裁决 RC 记录**（`adjudication_events: []` + finality `not_applicable`）。  
3. **`value_carrier_mapping` 不属 RC 核心**（可选；E3 真相在 V0.7）。

并回答：何时填、何时留空、如何与 Ledger 1.0 并存、升格前仍缺哪些决策门。

### 1.2 Non-goals

| 不做 | 原因 |
|---|---|
| 本文件触发 schema freeze / V0.8 adopt | 需用户另行显式批准（Gate 1–4） |
| 修改 formal Ledger / Diagnostic / validate_data 合同 | 正式表面已冻结 |
| 要求冷启动 PR 附带 RC | 与 #49 / P2 冲突；破坏可用性 |
| 发明 `rights_control_score` | Round 2 / experimental 明确禁止 |
| 把 CF / RP / Network 并进本对象 | 边界分离；禁止一次塞全 |
| 普通样本洪水 / 新 contrib ledger | 维护平台期扩样暂停 |
| 在同一 PR 做「升格 + 大改字段 + 发版」 | 设计草案禁止捆绑 |

---

## 2. When to fill RC vs leave empty

### 2.1 默认：留空

下列情形 **不要** 创建 RC 记录：

1. Getting Started / Issue #2 类 **普通冷启动**（四域 contrib、无裁决叙事）。  
2. 仅有 PP01 / 质押 / 法律状态旗标（陷阱：**PP01 ≠ R / RC**）。  
3. 只有产品/平台 E2、无 claim-set 裁判或行政程序。  
4. 作者不确定司法辖区切片或 T0 对齐——宁可 Unknown 在 Ledger notes，也不编造裁决。

> **无 RC 文件 = 合法完整贡献。** Formal CI（`validate_data.py` 等）不得因缺少 RC 失败。

### 2.2 适合填写（仍可选）

在 **已有** V0.7 Ledger 的前提下，且至少一项成立：

| 信号 | 例（仓库内） |
|---|---|
| 同 R、不同法律控制 的对照研究 | Package A 四对照 |
| claim-set 级 IPR / 再审 / 上诉 / ITC | Wirtgen × Caterpillar |
| 需要分开记「不利裁决」与「仍 operative 的救济」 | PTAB FWD + ITC LEO |
| 显式研究 H1 Rights Control | Round 1/2 非奖项机制样本 |

填写位置：**仅** `data/experimental/rights-control/`（或未来并行目录，见 §5）；**禁止**写入 `schema_version: "1.0"` 的 ledger JSON 字段。

### 2.3 决策树（贡献者）

```text
有 V0.7 Ledger？
  └─ 否 → 先做 Ledger；不要先写 RC
  └─ 是 → 存在 claim-set × 辖区 × T0 的裁决/行政程序叙事？
            └─ 否 → 默认不写 RC
                      └─（可选）若研究需要显式「查过、无裁决」
                         → 允许写 no-ruling 记录（§3）
            └─ 是 → 可选写 RC（有事件）；不要发明 score
```

---

## 3. No-ruling + `not_applicable` rules（已实现于 experimental-0.1 / #49）

### 3.1 规则表

| 规则 | 要求 |
|---|---|
| R1 Optionality | 普通专利 **永远不要求** RC |
| R2 Empty events | `adjudication_events` **可以为 `[]`** |
| R3 No-ruling finality | 若事件为空：`finality_state.status` **与** `formal_effect` **必须** = `not_applicable`；finality `evidence_ids` 可空 |
| R4 Events vs N/A | 若事件非空：`finality_state.status` **禁止** `not_applicable`；finality 需证据 |
| R5 Scope for unasserted | 未诉专利可用 `scope_type: all_granted_claims` |
| R6 Mapping optional | `value_carrier_mapping` **可省略**；若写且 status≠unknown，需证据；**不得**反写正式 R/E3 |
| R7 T0 discipline | 事件 `decision_date` 与引用 evidence 的 `observed_date` 均 ≤ `as_of_date` |
| R8 No score | 拒绝任何 score / 概率字段 |
| R9 Ledger bridge | `source_ledger_ids` 指向已存在的 formal ledger；一对多允许 |

校验入口：`tools/validate_rights_control.py`（与 `validate_data.py` **分离**）。

### 3.2 最小有事件核 vs 无裁决核

**有事件（Package A 形态）建议核：**  
`rights_control_id`, `schema_version`, `source_ledger_ids`, `patent_id`, `claim_set_id`, `claims_at_issue`, `jurisdiction`, `as_of_date`, `scope_type`, `adjudication_events` (≥1), `finality_state`, `operative_control`, `evidence_ids`

**无裁决形态：**  
同上，但 `adjudication_events: []`，finality = `not_applicable` / `not_applicable`，`operative_control` 可诚实为 `unknown` / `none`；`evidence_ids` 可引用「法律状态检索、未发现裁决」类语境证据（**不得**把 PP01 写成 operative control）。

### 3.3 与 P1 清单的关系

| P1 建议 | #49 状态 |
|---|---|
| minItems 1→0 | **已做** |
| finality `not_applicable` | **已做** |
| `all_granted_claims` | **已做** |
| `value_carrier_mapping` 移出 required | **已做** |
| `as_of_date` → `t0_date` 重命名 | **未做**（破坏性；留待升格 PR 显式迁移） |

---

## 4. Parallel coexistence with V0.7 Ledgers

### 4.1 双轨合同（现行）

| | Formal（贡献默认） | RC experimental（可选并行） |
|---|---|---|
| 问题 | Value / Evidence / Observability / R0–R5 | claim-set 法律控制 |
| Schema | `schema/*.schema.json`，`1.0` | `schema/experimental/…`，`experimental-0.1` |
| 数据 | `data/ledgers/` 等 | `data/experimental/rights-control/` |
| 校验 | `validate_data.py` + diagnostic/report | **仅** `validate_rights_control.py` |
| CI 含义 | 通过 = 正式表面一致 | 通过 = 实验对象可测；**≠** 升格 |

合法世界（不得互相推导）：

- R5 + 强 RC / R5 + 弱 RC / R4 + 强 RC / R4 + 不利裁决但仍 operative  
- **R0 + 无 RC**（普通冷启动常态）  
- **R0 + no-ruling RC**（显式「无裁决」研究注记，罕见）

### 4.2 链接方向

- RC → Ledger：经 `source_ledger_ids`（必填于 RC 侧）。  
- Ledger → RC：**无** formal 字段；文档/导读可交叉链接。  
- Diagnostic 1.0：**不**渲染 RC，除非未来 Gate 批准「只读注解」且仍 optional。

### 4.3 贡献者可见文案（建议固定句）

> Rights Control 是可选实验对象。普通冷启动 **不要** 填。无裁决也可以创建 RC，但通常没必要。正式验收只看 V0.7 Ledger / schema 1.0。

---

## 5. Migration sketch — later optional-parallel（仅草图；本 PR 不实施）

> 触发条件：用户显式批准「S1 — Optional RC parallel」（设计草案 §5），**不是**本文件合并。

### 5.1 建议最小升格包

1. 将 experimental-0.1 的 **稳定子集** 复制或别名为并行 formal-optional schema（版本字符串待 Gate 1 / Q-M1）。  
2. 数据可继续住在 `data/experimental/rights-control/` **或** 迁到 `data/rights-control/`（需迁移说明）；**禁止**塞进 ledger 行内。  
3. CI：formal job 仍只跑 1.0；RC job 保持独立；README / Getting Started 增加「可选」横幅。  
4. CONTRIBUTING：明确「缺 RC ≠ 不完整」。  
5. **单独立 release notes**；禁止与 Horizon/Network/CF/RP 捆绑。

### 5.2 兼容

- 全部现有 `schema_version: "1.0"` 行继续合法。  
- 现有 9 条 Package A RC 记录应无改或仅机械迁移。  
- no-ruling 规则与 optionality **原样带入**（不得在升格时改回 minItems≥1 或必填 mapping）。

### 5.3 回滚

- 删除/停用并行目录与独立 workflow 步骤即可；1.0 表面不受损。  
- git tag `v0.1.0` 为安全锚。

### 5.4 明确不在 S1 做的事

- 改默认方法名为 V0.8  
- Diagnostic 强制展示 RC  
- CF schema、RP 升格、Network freeze  
- `as_of_date` 重命名（除非同 PR 提供机械迁移 + 测试）

---

## 6. Decision gates before any freeze / adopt

沿用设计草案 §6；与 RC 并行轨直接相关的勾选：

### Gate 0（事实 — 已满足）

- [x] Package A 4/4 + Round 2 synthesis  
- [x] experimental RC 与 formal 隔离  
- [x] #49：可选 + 无裁决 + mapping 可选  

### Gate 1 — 治理（用户）

- [ ] 是否批准进入 **S1 optional parallel**（方法仍可称 V0.7）？  
- [ ] 对外版本叙事（Q-M1）？  
- [ ] 谁批准 / 回滚标准？  

### Gate 2 — 范围（用户）

- [ ] S1 **仅** RC，不含 Horizon/Network/CF/RP？  
- [ ] 冷启动文案确认「永远可选」写入 Getting Started / CONTRIBUTING？  

### Gate 3 — 风险（未关闭不升格）

- [x] 普通专利不增摩擦（可选前提下；见 P2）  
- [ ] Getting Started 实操句审查（双轨不混淆）  
- [ ] 无 score / 无池费率继承护栏在文档+CI 命名上仍清晰  

### Gate 4 — Freeze / release（独立）

- [ ] 冻结文件列表与 `schema_version` 字符串  
- [ ] 迁移说明 + 示例 + 外部复现清单  
- [ ] 单独 release；用户显式「批准 freeze」文本  

**本文件合并 ≠ 勾选任何 Gate 1–4。**

---

## 7. Pointers（权威来源）

| 主题 | 指针 |
|---|---|
| 对外导读 / 库存 | [`rights-control-research-overview.md`](rights-control-research-overview.md) |
| 实验设计说明 | [`claim-set-rights-control-experimental-0.1.md`](claim-set-rights-control-experimental-0.1.md)（含 No-ruling §） |
| 数据字典 | [`claim-set-rights-control-data-dictionary.md`](claim-set-rights-control-data-dictionary.md) |
| 字段升格 diff | P1 [`v0.8-probes/p1-rc-field-promotion-diff.md`](v0.8-probes/p1-rc-field-promotion-diff.md) |
| 普通 R0 负例 | P2 [`v0.8-probes/p2-rc-negative-ordinary-r0.md`](v0.8-probes/p2-rc-negative-ordinary-r0.md) |
| 用户决定落地 | PR [#49](https://github.com/xiangsee/patent-value-benchmark/pull/49) |
| V0.8 形状 / S1 | [`model-v0.8-design-draft.md`](model-v0.8-design-draft.md) |
| Schema 横幅 | [`schema/experimental/README.md`](../../schema/experimental/README.md) |

---

## 8. Document control

| 项 | 值 |
|---|---|
| 类型 | Optional parallel-track **plan / 细则** |
| 实施状态 | **未**启动 S1；experimental-0.1 规则已含 #49 |
| Schema | **not frozen**；formal 仍 `1.0` |
| 下一步工程 | 仅当用户勾选 Gate 1–2 后另开升格 PR |

