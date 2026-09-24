# External Reproduction Test Protocol

目的：验证一个**没有阅读本项目历史聊天记录**的外部使用者，能否仅依赖仓库内容完成一次 Patent Value Ledger → Diagnostic。

## Tester profile

建议至少一名：
- 专利代理师 / 专利律师；或
- 企业研发 / IP人员；或
- 技术投资 / 技术转移人员。

不要求参与过本项目研究。

## Start here

测试者只需要仓库，不应得到额外口头说明。

第一步打开：

- `docs/getting-started.md`
- `docs/cold-start-quick-reference.md`

然后按指南执行。

## Test task

请选择一件**不在现有示例中的中国发明专利**。

仅使用公开来源，完成：

1. Source Registry entries
2. Evidence Records
3. Patent Value Ledger
4. 本地运行CI相关脚本
5. 生成Diagnostic和Markdown report
6. 使用仓库PR模板提交

## Tester must not receive

- 本项目历史对话
- 作者针对该专利的预先判断
- “应该填到R几”的提示
- 奖项等级预测

## Success criteria

### Structural
- Schema validation通过
- Source/Evidence/Ledger引用完整
- Diagnostic自动生成
- Markdown report自动生成

### Method
测试者能够正确理解：
- Unknown ≠ 0
- E1–E5非单调
- Product value ≠ Patent value
- R2 ≠ R3
- R4 ≠ R5
- historical T0不能使用未来资料

### Usability
记录：
- 完成总耗时
- 最难理解的3个字段
- 最难寻找的3类证据
- 是否出现“想给一个分数”的冲动
- 哪些说明文档仍不足

## Pass rule

满足：
- 所有CI通过；
- 没有发生层级自动继承；
- 没有把Unknown当0；
- 测试者能够解释为什么自己的最终stage停在那里。

## Output

提交一个PR，并在PR描述中附：
- Test patent
- Time spent
- Ambiguities encountered
- Suggested schema/document changes

完成一次通过测试后，v0.1.0的“外部复现”阻塞项可勾选。
