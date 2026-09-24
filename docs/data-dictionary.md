# Data Dictionary

版本：**v0.1.0 draft**

本文件定义 Xiangsee Patent Value Benchmark 的核心术语。目标是让不同研究者、企业和代理师对同一字段尽量得到一致理解。

## 1. 判断状态

| 值 | 含义 | 可以怎么写 | 不能怎么写 |
|---|---|---|---|
| `confirmed` | 来源直接、明确支持该事实/连接 | 招股书明确写某专利对应某产品 | 仅凭企业主营业务推断 |
| `strong_evidence` | 多项事实高度支持，但缺少直接明示 | 权利人、技术路线、产品描述高度一致 | 当成已确认事实 |
| `inference` | 合理推断，但替代解释仍存在 | 根据技术结构推断产品模块 | 用确定语气表述 |
| `unknown` | 当前证据不足或不可观察 | “未能从公开T0资料确认” | 写成“没有”“0” |

**硬规则：Unknown ≠ 0。**

## 2. Evidence Levels（非单调等级）

E1–E5 **不是一个从低到高的总分阶梯**，可以并存。

| Evidence | 定义 | 示例 |
|---|---|---|
| **E1 Enterprise** | 企业层事实 | 公司收入、研发投入、行业地位 |
| **E2 Product / Project** | 产品、工程、临床或项目层事实 | 产品销售额、医院覆盖、工程数量 |
| **E3 Exact Patent → Value Carrier** | 具体专利与具体价值载体的连接 | 招股书明确列出专利号与产品/核心技术 |
| **E4 Patent-level Attributable Value** | 能将性能、成本、收入等归因到具体专利 | 专利实施使良率提升X%、可归因增量利润Y |
| **E5 Independent Verification** | 独立核验属性 | 监管批准、许可备案、第三方测试、标准文件 |

### 为什么E5不“高于”E4

E5回答“有没有独立核验”，E4回答“价值能不能归到这件专利”。

一个许可备案可以是 **E5**，但并不意味着已经达到 **E4**。

因此Ledger使用：
- `evidence_levels_present: ["E2","E3"]`

而不是“最高等级E3”。

## 3. Value Realization Stage

| Stage | 名称 | 必要含义 |
|---|---|---|
| **R0** | Right Exists | 专利权/申请事实存在 |
| **R1** | Market / Transfer Intent | 挂牌、报价、寻求许可等 |
| **R2** | Rights Transaction | 许可、转让、质押等已经发生 |
| **R3** | Implemented in Value Carrier | exact patent 已进入具体产品/工艺/平台/工程 |
| **R4** | Scaled Real-world Validation | 已经规模化市场、工程、临床或用户验证 |
| **R5** | Patent-level Attributable Value | 性能、成本、收入或社会价值可归因到exact patent |

### Non-inheritance

以下推理禁止自动成立：

```text
企业R4 → 产品R4 → 专利R4
产品收入 → 专利价值
发生许可 → 已经实施
已经实施 → 已经规模化
已经规模化 → 已经完成专利级价值归因
```

### 机器规则

- R1–R5必须有 `realization_stage_evidence_ids`
- R3–R5必须有非Unknown的exact patent → value carrier连接
- R5必须包含E4，且至少有一个 `scope_level=exact_patent` 的可归因指标

## 4. Observability State

| 值 | 含义 |
|---|---|
| **public** | 普通外部研究者可公开取得 |
| **disclosed_regulated** | 年报、招股书、监管申报等正式披露 |
| **internal** | 企业内部可取得，公开层不可见 |
| **restricted** | 合同、客户、审计、许可等受限资料 |
| **unknown** | 不知道证据是否存在 |

Observability不等于Evidence Quality。

“公开看不见”不能推出“没有价值”。

## 5. Metric Scope

所有数字必须标记归属层级。

### enterprise
企业整体指标。

例：
- 企业营收100亿元
- 企业研发投入10亿元

### product_project
产品、工程、临床项目指标。

例：
- 产品销售30亿元
- 进入200家医院
- 100个工程部署

### exact_patent
能够归因到具体专利的指标。

例：
- 实施本专利后能耗下降12%
- 本专利对应许可费300万元
- 经专项审计确认专利实施新增利润5000万元

**只有 exact_patent + 非Unknown attribution 才能支持R5。**

## 6. Value Carrier Types

| 类型 | 示例 |
|---|---|
| molecule | 化合物/分子 |
| material | 材料 |
| process | 制造/制备工艺 |
| component | 核心部件 |
| equipment | 整机/装备 |
| product_system | 产品系统 |
| software_algorithm | 软件/算法 |
| protocol_platform | 协议/平台能力 |
| drug_biologic | 药物/生物制品 |
| medical_device | 医疗器械 |
| engineering_infrastructure | 工程/基础设施 |
| standard | 标准 |
| other | 其他 |
| unknown | 尚未确认 |

## 7. Analysis Mode

### public
只使用可以合法公开、可以提供source_id的信息。

### internal
企业授权后可加入：
- 技术BOM
- 客户/订单
- 合同
- 专项审计
- 内部性能测试
- 成本/良率贡献
- 许可条款

Internal数据不得未经授权提交到公共仓库。

## 8. Time Policy

### current_state
研究当前状态。

### historical_t0_cutoff
历史复原模式。只能使用T0当日或之前已经公开可得的信息。

Post-T0信息只能做：
- outcome label
- later ground truth

不得倒灌提升T0状态。

## 9. 三个典型例子

### R0 — 华为无线通信示例
专利与技术问题明确，但公开T0资料未建立exact patent → 标准条款/设备连接。

正确：**R0 / Unknown**

错误：因为华为5G很强，就自动写成R4。

### R2 — 电网导线追踪许可示例
具体专利存在许可备案。

正确：**R2**

错误：许可发生就自动认定产品已经实施、规模部署。

### R4 — 艾可宁示例
招股书明确exact patent → 产品技术，产品已上市并有销量、收入、医院覆盖。

正确：**R4，E2+E3，R5 Unknown**

错误：把产品4050.29万元收入全部写成专利价值。
