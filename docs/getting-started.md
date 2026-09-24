# Getting Started — 30-minute Cold Start

目标：**完全不看项目历史聊天，只靠仓库，把一件新专利走完 Source → Evidence → Ledger → Diagnostic → Report。**

如果你第一次使用这个项目，请只按本页操作。遇到不确定时，优先填 `unknown`，不要猜。

## 0. 先理解三句话

1. **企业/产品价值不能自动变成专利价值。**
2. **Unknown ≠ 0。**
3. **R阶段必须停在证据允许的位置。**

如果只记住这三句话，就已经避免了大多数误用。

## 1. 准备环境

需要：
- Git
- Python 3.12（3.10+通常也可）
- 一个你愿意公开研究的中国发明专利

克隆：

```bash
git clone https://github.com/xiangsee/patent-value-benchmark.git
cd patent-value-benchmark
python -m pip install -r requirements-dev.txt
```

先确认基线：

```bash
python tools/validate_data.py
python tools/generate_diagnostics.py --check
python tools/render_reports.py --check
```

应该全部通过。

## 2. 生成一件专利的草稿

当前状态研究：

```bash
python tools/scaffold_ledger.py \
  --application-number ZL202012345678.9 \
  --title "你的专利名称" \
  --assignee "权利人名称"
```

历史T0研究：

```bash
python tools/scaffold_ledger.py \
  --application-number ZL202012345678.9 \
  --title "你的专利名称" \
  --assignee "权利人名称" \
  --t0 2024-02-05
```

它会生成：

```text
data/source-registry/contrib-ZL....jsonl
data/evidence/contrib-ZL....jsonl
data/ledgers/contrib-ZL....jsonl
```

Ledger默认停在 **R0**。这是正确行为，不是“没分析完”。

## 3. 先找Source，不要先打阶段

推荐顺序：

1. 专利原文 / 法律状态
2. 监管、标准、法定披露
3. 招股书 / 年报
4. 官方工程/项目材料
5. 企业正式披露
6. 学术论文
7. 可信媒体

每条Source至少记录：
- source_id
- title
- publisher
- URL
- source_date
- publicly_available_date
- T0是否可用

看 `schema/source-record.schema.json`。

### T0规则

如果你在做历史研究：

> 来源即使今天能搜到，只要当时T0之前还没公开，就不能进入T0证据。

## 4. 把事实拆成Evidence

不要写一条“大而全”的证据。

坏例子：

> “该公司很强，这个产品销量大，所以专利价值高。”

好例子拆开：

- E1：公司2023年营收XX
- E2：具体产品销量XX
- E3：招股书明确ZLxxxx对应产品A
- E5：许可备案/监管批准

每条Evidence只说它真正能证明的事情。

看 `schema/evidence.schema.json` 和 `docs/data-dictionary.md`。

## 5. 更新Ledger

重点按这条链填：

```text
Knowledge
  → Technology
  → Patent
  → Value Carrier
  → Real-world Validation
  → Attributable Value
```

### 你最容易犯的错误

**产品卖得很好，不等于这件专利就是R4。**

只有存在足够的 exact patent → value carrier 连接，才能把产品层的真实世界验证谨慎关联到专利。

### R阶段快速判断

- **R0**：只有专利权/技术事实
- **R1**：挂牌/报价/寻求许可
- **R2**：许可/转让/质押已经发生
- **R3**：exact patent已经进入具体价值载体
- **R4**：该连接下已经规模化真实世界验证
- **R5**：有E4，能把具体价值归到exact patent

**如果犹豫，停在较低阶段并写Gap。**

## 6. 运行完整闭环

先校验：

```bash
python tools/validate_data.py
```

再生成：

```bash
python tools/generate_diagnostics.py
python tools/render_reports.py
```

最后检查：

```bash
python tools/validate_data.py
python tools/generate_diagnostics.py --check
python tools/render_reports.py --check
```

你的Diagnostic会进入：
- `data/diagnostics/generated.jsonl`

人类可读报告会进入：
- `reports/generated/`

## 7. 看报告，不要看“分数”

报告应该回答：

- 当前停在R几？
- 已经确认什么？
- 哪些数字只是产品级？
- exact patent mapping有没有建立？
- R5为什么还没成立？
- 下一步该补什么证据？

如果你在找“87分”或“金奖概率”，说明你正在误用这个项目。

## 8. 提交PR

PR必须说明：

- Test patent
- Total time spent
- Why you stopped at the selected R stage
- 3 most confusing fields
- 3 hardest evidence types to find
- Whether you were tempted to turn Unknown into 0 / score
- Suggested improvements

请使用仓库PR模板。

## 9. 10分钟自查

提交前问自己：

- [ ] 我有没有把企业收入写成专利收入？
- [ ] 我有没有把产品销售自动继承给exact patent？
- [ ] 我有没有用T0后的材料回填过去？
- [ ] 我有没有把“没找到”写成“没有”？
- [ ] R1–R5有没有stage evidence？
- [ ] R3+有没有exact patent → value carrier连接？
- [ ] R5有没有E4 + exact_patent metric？
- [ ] Source、Evidence、Ledger能互相追溯？
- [ ] 三个check命令都通过？

如果全部是Yes，你已经完成一次合格的冷启动。
