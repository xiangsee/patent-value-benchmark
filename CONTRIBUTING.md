# Contributing

感谢参与 Xiangsee Patent Value Benchmark。

这个项目欢迎的不是“给某件专利打一个分”，而是**补一条可以复核的证据链**。

## 可以贡献什么

- 新的公开 source record
- 新的 evidence record
- Patent Value Ledger
- 对现有证据等级的异议
- T0 时间纠错
- patent → product / process / project 的新映射证据
- 反例：能够推翻当前判断的资料
- Schema / validator 改进

## 提交一件专利前

请先检查：

1. 事实属于企业、产品还是 exact patent？
2. 来源在目标 T0 时是否已经公开？
3. 是事实、Strong Evidence、Inference 还是 Unknown？
4. 产品收入是否被错误写成专利收入？
5. 是否存在 post-T0 outcome leakage？
6. 是否有版权或数据库许可限制？

## 推荐流程

1. 在 `data/source-registry/` 注册来源。
2. 在 `data/evidence/` 拆分事实证据。
3. 建立 `data/ledgers/` Ledger。
4. 运行：

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_data.py
```

5. 提交 Pull Request。

## 证据优先级

一般优先：
- 官方专利文献
- 监管 / 标准 / 法定披露
- 招股书 / 年报
- 官方项目 / 工程材料
- 企业正式披露
- 学术论文
- 可信媒体

同一事实尽量使用最接近原始事实的一手来源。

## 不接受

- 只有宣传口号、无法定位来源的结论
- 用获奖后宣传解释获奖前状态
- 把企业收入直接当专利价值
- 将“没有搜到”写成“没有”
- 未授权公开的企业内部材料
- 受限数据库全文的批量复制

## 争议处理

如果两个贡献者对同一判断不同，优先：
- 保留原始证据；
- 分离事实与推断；
- 降低判断状态，而不是强行统一；
- 必要时标记为 Unknown / disputed。

这个库允许“暂时不知道”。
