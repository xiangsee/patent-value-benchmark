# Patent Value Diagnostic 1.0 Draft

Patent Value Diagnostic 是 Patent Value Ledger 的标准输出端。

它不是独立分析，也不重新判断证据；它只把Ledger已经确认的状态转换成可读、可执行的诊断结果。

## 输出五部分

### 1. Current State
- 当前 R0–R5 阶段
- 当前最高 Evidence Level
- exact patent → value carrier 是否已经建立
- patent-level attributable value 是否已经建立
- Observability 状态

### 2. Confirmed Chain
列出已经不是 Unknown 的 Value Carrier 和连接。

### 3. Observed Metrics
保留原Ledger里的数值，同时保留 scope：
- enterprise
- product_project
- exact_patent

Diagnostic不得把 product_project metric 改写成 exact_patent metric。

### 4. Unresolved Gaps
逐项保留Ledger里的Evidence Gap / Attribution Gap。

### 5. Next Evidence Tasks
根据gap_type确定下一步补证目标，例如：
- exact_patent_mapping → E3
- patent_value_attribution → E4
- independent_verification → E5

## 明确不输出

- Gold概率
- 未经E4支持的专利估值金额
- 自动排名
- 把Unknown当0的总分

## 自动生成

```bash
python tools/generate_diagnostics.py
python tools/generate_diagnostics.py --check
```

生成文件：`data/diagnostics/generated.jsonl`

生成器是确定性的：同一Ledger必须生成同一Diagnostic。
