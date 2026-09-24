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
- Patent Value Ledger（专利价值账本）Schema

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
- `schema/`：开放数据与 Patent Value Ledger Schema（筹备中）

## 品牌

《详见》英文统一为 **xiangsee**。

---

本项目仍处于研究阶段。当前模型和字段可能随着反证测试与样本外验证继续修订；重要变更将记录在 CHANGELOG 中。
