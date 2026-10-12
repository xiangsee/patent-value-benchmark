# Track A — Cold-start Status

> 快照日期：2026-10-12（Asia/Shanghai）  
> 正式方法：**V0.7**；正式 schema：**1.0**（[`v0.1.0`](https://github.com/xiangsee/patent-value-benchmark/releases/tag/v0.1.0) 已冻结）  
> **不**采纳 V0.8；**无** Counterfactual experimental schema。

本页汇总 Track A 上、面向外部复现 / 普通冷启动可用性的 **contrib 样本**（`data/ledgers/contrib-*.jsonl`），按领域分组。奖项示例、Package B/C 非奖项机制样本见 Round 2 综合，不在本表重复。

## 普通冷启动样本（按领域）

全部为 **当前状态研究**、诚实停在 **R0**（无 E3 → 不升 R3+）。部分 ledger 会触发 `validate_data.py` 的 **pre-filing E2 soft warning**（exit 0；见 [`getting-started.md`](getting-started.md) §6.1）。

### Software / 软件

| 申请号 | 权利人 | 载体 | Ledger | 备注 |
|---|---|---|---|---|
| ZL202010574036.6 | 远光软件 | `software_algorithm` | [`contrib-ZL202010574036.6`](../data/ledgers/contrib-ZL202010574036.6.jsonl) | 实施例网址 ≠ E3 |
| ZL202110873119.X | 天地和兴 | `software_algorithm` | [`contrib-ZL202110873119.X`](../data/ledgers/contrib-ZL202110873119.X.jsonl) | 他案点名 ≠ E3；PP01 ≠ R/RC |

### Mechanical / 机械

| 申请号 | 权利人 | 载体 | Ledger | 备注 |
|---|---|---|---|---|
| ZL201911041536.7 | 广东科达液压 | `equipment` | [`contrib-ZL201911041536.7`](../data/ledgers/contrib-ZL201911041536.7.jsonl) | 申请前他案叙事 → soft warn |

### Chemical / 化工（工艺）

| 申请号 | 权利人 | 载体 | Ledger | 备注 |
|---|---|---|---|---|
| ZL202011377891.4 | 河北威远 | `process` | [`contrib-ZL202011377891.4`](../data/ledgers/contrib-ZL202011377891.4.jsonl) | 申请前原药登记 → soft warn |

### Materials / 材料

| 申请号 | 权利人 | 载体 | Ledger | 备注 |
|---|---|---|---|---|
| ZL202010866038.2 | 内蒙古中晶 | `material` | [`contrib-ZL202010866038.2`](../data/ledgers/contrib-ZL202010866038.2.jsonl) | 申请前产能/产品新闻 → soft warn |

### 外部冷启动门禁样本（#2；非「普通中坚」但仍属 Track A contrib）

| 申请号 | 权利人 | 载体 | Ledger | 备注 |
|---|---|---|---|---|
| ZL201910544929.3 | 比亚迪 | `product_system` | [`contrib-ZL201910544929.3`](../data/ledgers/contrib-ZL201910544929.3.jsonl) | 同族误映射 / 300+ 组合；关 [#2](https://github.com/xiangsee/patent-value-benchmark/issues/2) |

## 导航

| 文档 | 用途 |
|---|---|
| [`docs/getting-started.md`](getting-started.md) | 30 分钟冷启动（含 §6.1 soft warning UX） |
| [`docs/cold-start-quick-reference.md`](cold-start-quick-reference.md) | 一页速查 |
| [`docs/cold-start-trap-checklist.md`](cold-start-trap-checklist.md) | 提交前陷阱勾选 |
| [`docs/methodology/rights-control-research-overview.md`](methodology/rights-control-research-overview.md) | Rights Control 研究导读（实验；不进 Ledger 1.0） |
| [`docs/methodology/realization-path-research-overview.md`](methodology/realization-path-research-overview.md) | Realization Path 研究导读（实验） |
| [`docs/methodology/counterfactual-control-research-overview.md`](methodology/counterfactual-control-research-overview.md) | Counterfactual 研究导读（**无** schema） |
| [`analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`](../analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md) | Round 2 综合（**不** adopt V0.8） |
| [`docs/release/v0.1.0-notes.md`](release/v0.1.0-notes.md) · [Release v0.1.0](https://github.com/xiangsee/patent-value-benchmark/releases/tag/v0.1.0) | 发版说明 |

## 维护平台期（Maintenance plateau）

截至 2026-10-12：**Track A 表面已稳定**，进入维护平台期。

- 架构：**V0.7 adopted**（正式）
- Schema：**1.0 frozen**（[`v0.1.0`](https://github.com/xiangsee/patent-value-benchmark/releases/tag/v0.1.0)）
- V0.8 / Rights Control / Realization Path / Counterfactual：**research-only**；**不**采纳 V0.8；**不**建 CF experimental schema
- 采纳 V0.8：**需显式决策**（见 Round 2 综合）
- **普通冷启动扩样：已暂停**（software ×2、mech、chem、materials + #2 门禁案已覆盖四域；不再新增 contrib ledger，除非显式重启）
- 允许的维护：文档对齐、校验/CI 修复、研究导读修订；**不开新 ledger**

