# 盲评结果回流与一致性计算

必须由两位**不同真人评审**完成独立打分，并提交各自的文件。协调人最后才可接触两份结果。

从A/B工作簿各自的`独立评分`工作表导出CSV（保留“编码、评委内部编码、权项/对比核验、产业实施核验、四维分数、综合分”标题）：

```bash
python tools/compare_applied_reviewers.py --a ReviewerA.csv --b ReviewerB.csv
```

不提供参数时，工具必须输出：

```text
{"status":"Not Run","reason":"two independent reviewer CSVs not yet supplied"}
```

它只计算：
- 成对数据覆盖率；
- 审核状态一致率；
- 两位评委的 Cohen κ（类别不变、期望一致率为1时为`null`，不能写成“完美一致”）；
- 在两份评分都有合法数值时的平均绝对分差。

六件只是试运行，不能外推总体、宣称有预测能力；缺分不按零分。提交前不得将评委姓名、专利映射、内部收入或历史底分上传到GitHub。
