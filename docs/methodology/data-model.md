# Open Data Model

本项目的数据结构以“可复核、可追溯、可版本化”为第一目标，而不是追求一次性评分。

## 四类核心对象

### 1. Patent Record
记录奖项、专利基本信息、T0、产业与价值载体分类，以及 V0.6 冻结维度的判断状态。

### 2. Evidence Record
每一项事实或判断必须尽量拆成独立 evidence record，并记录：
- 来源
- 来源日期
- 证据等级 E1–E5
- 是否在 T0 以前可用
- Confirmed / Strong Evidence / Inference / Unknown

### 3. Matched Pair
Gold 与 Silver / Excellent 的配对实验对象。
必须记录配对依据，并明确哪些维度能区分、哪些维度仍是 Unknown。

### 4. Source Registry
统一管理外部来源，避免相同来源重复录入，也方便后续检查链接、许可和时间截面。

## 关键设计原则

- 不把奖项等级写入分析变量。
- 不把 Unknown 编码为 0。
- 不因为获奖后宣传补强历史预测数据。
- 不将企业级证据自动继承给产品或具体专利。
- 不将产品销量自动归因给其中每件实施专利。
- 每条重要事实尽可能具有 source_id 和 evidence_id。

Schema 位于 `schema/`。
