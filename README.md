# Xiangsee Patent Value Benchmark

**《详见》高价值专利开放基准库**

> Status: Research Preview / Work in Progress

Xiangsee Patent Value Benchmark 是《详见》（**xiangsee**）发起的开放研究项目。项目以中国专利奖等经过现实世界验证的高价值专利样本为起点，研究一项知识如何从技术形成、专利保护，进入产品 / 工艺 / 平台 / 工程，并最终形成可验证的经济与社会价值。

本项目的目标不是“预测谁一定会获得中国专利金奖”，而是建立一个可复核、可反驳、可持续更新的 **Gold Readiness / Patent Value Benchmark**，帮助研究者、企业和专业服务机构回答：

- 一件专利为什么可能成为核心技术资产？
- 技术价值如何从企业级、产品级进一步追溯到具体专利？
- 金奖、银奖与优秀奖样本之间有哪些可观察差异？
- 哪些证据能够支持“专利已经形成现实价值”的判断？
- 如何避免结果泄漏、幸存者偏差以及把 Unknown 错误编码成 0？

## 当前研究阶段

当前研究架构：**V0.7 (adopted)**

正在进行：
- 第 25 届中国专利奖：V0.6 10组配对已封存并完成Cross-pair Synthesis
- 第 24 届中国专利奖：完成V0.7跨届外部压力测试，四层架构已 adopted
- 历届 Gold / Silver / Excellent 结构化基准库设计
- Patent Value Ledger 1.0 Draft：Schema、公开模板、首个示例与CI验证已上线
- Patent Value Diagnostic 1.0 Draft：由Ledger确定性生成诊断、缺口和下一步补证任务

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

每一条箭头都需要 Evidence，而不是依靠企业规模、产品销量或获奖结果自动推定。

V0.7进一步把 **Value State / Attribution & Evidence / Observability / Value Realization Stage** 四层分开，防止把“价值低”和“公开看不见”混为一谈。

## 核心原则

1. **Patent-level attribution**：企业价值不能自动归因给具体专利。
2. **T0 cutoff**：历史验证只使用申报截止日前已存在的信息，避免 Outcome Leakage。
3. **Unknown ≠ 0**：公开信息缺失不能被编码为“没有价值”。
4. **Gold vs Silver matched pairs**：优先比较同届、同技术领域、申请时间与主体类型接近的样本。
5. **Public / Private separation**：公开库只发布可以合法公开、可追溯的数据与方法；企业内部经营、合同、客户及受限数据不进入公共数据层。
6. **Reproducibility**：重要判断保留来源、日期、证据等级、推断状态和版本。

## 目录

- `docs/methodology/`：研究方法与模型版本
- `data/`：清洗后的开放基准数据（逐步发布）
- `analysis/`：样本外验证与研究分析
- `schema/`：开放数据与 Patent Value Ledger Schema
- `data/ledgers/`：可校验的专利价值账本
- `examples/patent-value-ledger/`：提交模板

## 品牌

《详见》英文统一为 **xiangsee**。

---

本项目仍处于研究阶段。当前模型和字段可能随着反证测试与样本外验证继续修订；重要变更将记录在 CHANGELOG 中。


## Patent Value Ledger

V0.7 已经落成可填写的 **Patent Value Ledger 1.0 Draft**。

一张账本串联：

`Knowledge → Technology → Patent → Value Carrier → Real-world Validation → Attributable Value`

公开模板见 `examples/patent-value-ledger/template.json`。当前验收示例覆盖 R0 / R2 / R4：
- `data/ledgers/example-r0-huawei.jsonl`
- `data/ledgers/example-r2-power-license.jsonl`
- `data/ledgers/example-aikening.jsonl`。

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

CI 同时检查：
- Ledger → Diagnostic 是否同步；
- Diagnostic → Markdown report 是否同步。

## v0.1.0 Pre-release

发布前状态见 `docs/release/v0.1.0-readiness.md`。

目前剩余核心事项：
1. 许可证最终选择；
2. 一次不依赖本对话上下文的外部冷启动复现；
3. Schema freeze + GitHub tag/release。


## License

This is a multi-licensed repository:

- **Code / CI / JSON Schemas:** Apache-2.0
- **Original documentation:** CC BY 4.0
- **Original structured data / curation:** CC BY 4.0
- **Third-party source materials:** not relicensed; rights remain with their owners

See `LICENSE`, `NOTICE.md`, and `LICENSES/` for the full scope.
