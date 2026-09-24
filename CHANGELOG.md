# Changelog

## Unreleased

### Added
- 初始化 Xiangsee Patent Value Benchmark 公共研究库。
- 冻结 Patent Value Benchmark V0.6，开始第 25 届样本外验证。
- 建立 E1–E5 证据等级。
- 建立 T0 截断与 Outcome Leakage 控制规范。
- 明确 Unknown ≠ 0。
- 明确 Public Screening / Internal Gold Readiness 双引擎结构。
- 建立 Patent Record / Evidence / Matched Pair / Source Registry 四类 JSON Schema。
- 第 25 届结构化预览数据已扩展至：20 条专利记录、14 条证据记录、10 组 Gold–Silver matched pairs。
- 增加数据完整性验证脚本 `tools/validate_data.py`。
- 增加 GitHub Actions 自动校验工作流；Round 1–3 数据提交均通过 CI 验证。
- 增加 `publicly_available_date`，严格区分事件发生日期与信息公开可得日期。

### Changed
- “专利年龄”不再以申请号前四位作为正式代理；后续统一优先使用真实申请日与最早优先权日，并记录分案 / PCT 来源。
- 对非 Unknown 的分析判断，要求至少引用一个 evidence record。

- Milestone A 达到 10 组 matched pairs，暂停第25届扩样，进入 Cross-pair Synthesis。
