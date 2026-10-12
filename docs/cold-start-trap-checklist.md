# Cold-start Trap Checklist

> 用途：冷启动 / 外部复现提交前的**陷阱自查**。  
> 正式方法：**V0.7**；正式 schema：**1.0**（冻结）。  
> **不**采纳 V0.8；`schema/experimental/*` 不是 Ledger 字段。

关联：
- Issue [#2](https://github.com/xiangsee/patent-value-benchmark/issues/2) / PR [#22](https://github.com/xiangsee/patent-value-benchmark/pull/22)（外部冷启动）
- PR [#40](https://github.com/xiangsee/patent-value-benchmark/pull/40)（他案点名 ≠ 本案 E3；PP01 ≠ R/RC）
- Round 2 综合：[`analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md`](../analysis/non-award-validation/round2-adoption-readiness-synthesis-v0.8.md)
- 操作指南：[`docs/getting-started.md`](getting-started.md) · [`docs/cold-start-quick-reference.md`](cold-start-quick-reference.md) · [`docs/cold-start-status.md`](cold-start-status.md)

---

## A. 同族 / 兄弟专利误映射（sibling-family false mapping）

- [ ] 升 R3+ 前，来源是否**点名本专利号**（申请号 / 公开号 / 授权号）？
- [ ] 是否排除了同日 / 同优先权 / 同族兄弟专利被二手源混写的可能？
- [ ] `family_note` 是否记录了易混淆的同族件（若存在）？
- [ ] 规则自检：**同族热度 ≠ exact patent → value carrier**
- [ ] 说明书/实施例里出现的产品网址或工具名，是否被误当成 **E3 官方映射**？（实施例叙述 ≠ 监管/官方专利→产品披露）

## B. R0 + E2 不抬高 R

- [ ] R0 是否只在证据允许时收录产品 / 项目层 E2？
- [ ] 没有 E3 映射时，是否**仍停在 R0–R2**？
- [ ] 一句话是否成立：**R0 + E2 is allowed; R0 + E2 ≠ R3**
- [ ] `exact_patent_value_carrier_link` 在 R0 是否保持 `unknown`？
- [ ] `evidence_levels_present` 是否**只**含 status≠unknown 支撑的层级？
- [ ] 若有 `status=unknown` 的 E3「寻而未得」行：是否**未**把 `"E3"` 写入 `evidence_levels_present`？（unknown-E3 ≠ present）

## C. 「300+ 专利组合」不可继承

- [ ] 来源是否只是「专利组合 / 技术体系 / N+ 件专利支撑产品」笼统叙事？
- [ ] 是否把产品收入、企业收入或池费率自动摊到单件专利？
- [ ] 升 R3+ / R5 前是否具备本专利号级 E3（以及 R5 的 E4）？
- [ ] 规则自检：**portfolio / program scope ≠ single-patent attributable value**

## D. 他案点名 ≠ 本案 E3

- [ ] 公司 IP / 项目新闻点名的是不是**别的**专利号（或只有「发明 N 项 / 实用新型 M 项」计数）？
- [ ] 是否误把「他案已嵌入产品」叙事写成**本案** E3？
- [ ] 升 R3+ 前，来源是否点名**本**申请号 / 公开号 / 授权号？
- [ ] 规则自检：**他案点名 ≠ 本案 E3**

## E. PP01 / 法律状态旗标 ≠ R / RC

- [ ] 是否把 PP01（专利权保全）、质押、许可意向等法律状态旗标当成 R 升级依据？
- [ ] 是否因 PP01 自动填写 / 发明 Rights Control（RC）正式或实验字段？
- [ ] 法律状态是否只放在 `family_note` / notes / 语境证据，而**不**抬 R？
- [ ] 规则自检：**PP01 ≠ R / RC**（RC 研究另走 experimental 导读）

## F. Round 2 额外风险（研究层，勿写进正式 1.0 字段）

- [ ] 有没有把 Rights Control / Realization Path / Counterfactual Control / Portfolio Network 研究或实验对象当成正式 Ledger？（导读：[`rights-control-research-overview.md`](methodology/rights-control-research-overview.md)、[`realization-path-research-overview.md`](methodology/realization-path-research-overview.md)、[`counterfactual-control-research-overview.md`](methodology/counterfactual-control-research-overview.md)）
- [ ] 有没有把 option signals 写成伪定量分数？
- [ ] 有没有把一司法辖区权利状态复制到其他国家？
- [ ] 历史 T0 研究有没有用 post-T0 材料回填？


## H. 申请日前的项目 / 产品新闻 ≈ 他案

- [ ] 项目新闻、产品上市、原药登记、环评产能等日期是否**早于本案申请日**？
- [ ] 若早于本案申请日：是否几乎必然在讲**更早工艺 / 他案 / 产品层事实**，而不是本案授权实现？
- [ ] 是否误把「申请前已存在的产品线」当成本案 E3？
- [ ] 规则自检：**申请日前的项目/产品新闻 ≈ 几乎总是他案（或与本案无关的产品层事实）**
- [ ] `validate_data.py` 若打印 soft warning（`pre-filing … not E3`）：是否已核对、**未**据此升 R3+？（警告**不**失败 CI；**exit 0 = 通过**；UX 见 [`getting-started.md`](getting-started.md) §6.1）
- [ ] 是否避免「为消警告而发明 E3 / 改 mapping / 抬 R」？
- [ ] `scaffold_ledger.py` notes / 终端是否已提醒「validate_data 会对申请日前 E2/产品类日期 soft-warn」？

## G. 提交前命令

若使用虚拟环境（见 Getting Started）：

```bash
source .venv/bin/activate   # 或直接用 .venv/bin/python ...
python tools/validate_data.py
python tools/generate_diagnostics.py --check
python tools/render_reports.py --check
python -m unittest discover -s tests -p "test_coldstart_levers.py"
```

实验对象（可选，**不**改变正式验收）：

```bash
python tools/validate_rights_control.py
python tools/validate_realization_paths.py
```
