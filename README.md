# Xiangsee Patent Value Benchmark

**《详见》专利价值开放基准库**

> Status: Research Preview / Work in Progress

Xiangsee Patent Value Benchmark 是《详见》（**xiangsee**）发起的开放研究项目。

项目研究的对象不是某一种奖项，也不是一个固定“高价值专利”标签，而是：

> **如何用可复核的证据描述一件专利的技术质量、权利控制力、现实价值实现、未来选择权，以及这些价值究竟能够归因到哪里。**

中国专利奖是项目早期的重要真实世界样本来源之一，但**不构成通用专利价值的定义，也不再作为主项目的目标变量**。

项目希望帮助研究者、企业和专业服务机构回答：

- 一件专利为什么可能成为核心技术资产？
- 技术价值如何从企业级、产品级进一步追溯到具体专利？
- 如何区分政策统计意义上的“高价值”、技术质量、私人资产价值、现实经营价值与社会/战略价值？
- 权利范围、稳定性、剩余期限、地域覆盖、绕开成本和组合语境如何影响专利资产价值？
- 哪些公开信号适合用于筛选候选专利，哪些证据才足以支持价值归因？
- 如何避免结果泄漏、幸存者偏差以及把 Unknown 错误编码成 0？

## 两条研究线

### A. Patent Value Benchmark — 主干

通用专利价值研究。

当前核心包括：
- Value State
- Attribution / Evidence
- Observability
- Value Realization
- Value Construct
- Rights Control（研究中）
- Counterfactual Control（研究中）
- Option / Future Value（研究中）
- Portfolio Context（研究中）
- Screening Signals（与Value Proof分离）

### B. China Patent Award Research — 独立模块

中国专利金奖 / 银奖 / 优秀奖研究作为独立需求长期保留。

该模块研究：
- 历届获奖项目与制度变化
- Gold / Silver / Excellent 的可观察差异
- 评奖标准与实际结果之间的关系
- 获奖项目后续技术、产业与经济表现
- 奖项能否作为某些价值维度的外部验证信号

**边界规则：**
- 不把“是否获奖”作为通用价值模型的目标变量；
- 不把金奖评价逻辑直接等同于经济价值；
- 金奖模块中经跨样本验证具有普适性的变量，可以进入通用模型候选集；
- 两条线可以交叉验证，但不合并为同一个需求。

详见：`docs/research-tracks.md`。

## 当前研究阶段

当前正式研究架构：**V0.7 (adopted)**

V0.7更准确的定位是：

> **Patent Value Evidence & Realization Architecture**

它把以下四层分开：
- Value State
- Attribution / Evidence State
- Observability State
- Value Realization Stage

正在进行：
- V0.8 Value Construct & Rights Control 研究议程
- Patent Value Ledger 1.0 Draft
- Patent Value Diagnostic 1.0 Draft
- 通用样本与非奖项样本扩展
- 外部冷启动复现
- Schema freeze + v0.1.0 release

历史上，第25届和第24届中国专利奖 Gold–Silver 样本曾用于形成和压力测试 V0.6/V0.7。该研究链完整保留，作为**模型形成史和奖项专项研究证据**，但不意味着今后的通用模型仍以奖项为中心。

## 核心研究链

```text
Knowledge
  ↓
Technology
  ↓
Patent
  ↓
Product / Process / Platform / Project
  ↓
Regulatory / Standard / Market
  ↓
Revenue / Social Impact
```

每一条箭头都需要 Evidence，而不是依靠企业规模、产品销量、政策标签或获奖结果自动推定。

## 核心原则

1. **Patent-level attribution**：企业价值不能自动归因给具体专利。
2. **Value construct first**：先说明研究的是哪一种“价值”，再谈指标。
3. **T0 cutoff**：历史验证只使用截止日前已存在的信息，避免 Outcome Leakage。
4. **Unknown ≠ 0**：公开信息缺失不能被编码为“没有价值”。
5. **Screening ≠ Proof**：引用、家族、权利要求、维持年限等首先是筛选信号，不自动构成价值事实。
6. **Award ≠ Universal Value**：获奖结果可以作为特定研究样本或外部信号，但不是通用价值定义。
7. **Public / Private separation**：公开库只发布可以合法公开、可追溯的数据与方法；企业内部经营、合同、客户及受限数据不进入公共数据层。
8. **Reproducibility**：重要判断保留来源、日期、证据等级、推断状态和版本。

## 目录

- `docs/methodology/`：研究方法与模型版本
- `docs/research-tracks.md`：通用价值模型与专利奖专项模块的边界
- `analysis/theory/`：通用价值理论研究
- `analysis/china-patent-award/`：中国专利奖专项入口
- `analysis/24th-validation/`、`analysis/25th-validation/`：历史奖项样本验证记录
- `data/`：清洗后的开放基准数据
- `schema/`：开放数据与 Patent Value Ledger Schema
- `data/ledgers/`：可校验的专利价值账本
- `examples/patent-value-ledger/`：提交模板

## Patent Value Ledger

一张账本串联：

`Knowledge → Technology → Patent → Value Carrier → Real-world Validation → Attributable Value`

公开模板见 `examples/patent-value-ledger/template.json`。

当前验收示例覆盖 R0 / R2 / R4：
- `data/ledgers/example-r0-huawei.jsonl`
- `data/ledgers/example-r2-power-license.jsonl`
- `data/ledgers/example-aikening.jsonl`

CI 会阻止：
- R3/R4/R5 没有 exact-patent 映射；
- R5 没有专利级可归因价值；
- Ledger 引用不存在的 source/evidence；
- 历史 T0 使用未来来源。

## Patent Value Diagnostic

Ledger 的标准输出不是总分，而是 Diagnostic：

- 当前 R0–R5
- 当前已出现的 evidence levels（非单调、可并存）
- 已确认的 exact patent → value carrier 链
- 产品/项目/专利级指标及其 scope
- unresolved gaps
- next evidence tasks
- non-inheritance / T0 warnings

生成：

```bash
python tools/generate_diagnostics.py
```

CI 会执行 `--check`，保证 Diagnostic 与 Ledger 不发生版本漂移。

## Human-readable Reports

结构化 Diagnostic 还会确定性渲染为 Markdown：

```bash
python tools/render_reports.py
```

输出位于 `reports/generated/`。

## Quick Start

第一次使用请直接看：

- `docs/getting-started.md` — 30分钟冷启动
- `docs/cold-start-quick-reference.md` — 一页速查

一键生成贡献草稿：

```bash
python tools/scaffold_ledger.py \
  --application-number ZL202012345678.9 \
  --title "你的专利名称"
```

## v0.1.0 Pre-release

发布前状态见 `docs/release/v0.1.0-readiness.md`。

目前剩余核心事项：
1. 一次不依赖本对话上下文的外部冷启动复现；
2. Schema freeze + GitHub tag/release。

## License

This is a multi-licensed repository:

- **Code / CI / JSON Schemas:** Apache-2.0
- **Original documentation:** CC BY 4.0
- **Original structured data / curation:** CC BY 4.0
- **Third-party source materials:** not relicensed; rights remain with their owners

See `LICENSE`, `NOTICE.md`, and `LICENSES/` for the full scope.
