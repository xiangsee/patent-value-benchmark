# Claim Version Gate v0.3 · 授权权项版本闸门（研究协议）

**2026-10-29 · Research only · 适用层：Applied assessment / Rights Control 提前校验**

上游：`applied-evaluation-valuation-protocol-v0.1.md`、`applied-gates-v02-blind-pilot-preregistration.md`。不改变正式 V0.7、Ledger/Diagnostic Schema 1.0，也不自动采用 V0.8。

## 0. 这轮为什么必须增加版本闸门

AI模拟双视角复议之后，研究者对六件公开授权案例逐件核对了申请公开版本（A）与授权版本（B）。六个案例中五个权利要求总数发生变化，另一个虽然总项数未变，独立权利要求仍增加了具体限定。部分变化包括参数区间、菌种/配比、共焦位置关系、机械接触联锁、算法更新细节。

**可复核事实**：A、B文本的保护要素存在可观察差异。
**不得据此推导**：授权权项数量减少等于专利质量下降；从A转到B就一定无效；有授权B文本就一定稳定有效、已在产品上使用、或者已经具有现金价值。

这些案例对应的精确身份和评委模拟评分仍在本地协调底册；公共方法库这里只记录去标识化经验，以免影响未来真实人工盲评。使用**合成fixtures**执行工程校验。

## 1. 五道审查闸门（CV0—CV4）

| Gate | 通过的最低事实/证据 | 拒绝的错误推断 |
|---|---|---|
| CV0—身份与时间 | 唯一申请标识、公告号、辖区、优先日、估值/评审T0和B授权公告日 | 不同同族或不同辖区文件相互冒名；T0在授权前却使用未来B |
| CV1—授权原文 | A申请公开与**B授权公告**来源独立记录；指定用于研究的授权独立权项 | 仅有A文本或摘要，就讨论当前法律控制 |
| CV2—逐要素与修订 | 独立权项的技术要素列明；A→B**实质要素变化**复核；不同权项客体分别映射 | 仅比较“权项个数”或只把A文本的宽表述照抄进B |
| CV3—对比技术 | 至少明确比较任务、候选文献、公开日与被比较权项要素；记录检索边界 | 把Google Patents“Citations”当作最接近现有技术或自动宣布创造性/无效 |
| CV4—产品/金额 | E3须 exact patent/claims → value carrier；E4须patent-level可归因金额；金额还须通过 G0–G4 | 技术潜力、权项验证、企业收入、集团产品、许可传闻自动抬R3或给价 |

- `CV0~CV3` 通过最多表示**可以做基于授权文本的研究性技术/范围诊断**，不表示具备正式法律意见资格。
- `official_grant_current_status_verified` 与审查档案、年费、程序终局性信息属于正式法律状态核验；Google Patents等第三方状态字段**不能**替代。
- `CV4` 不接收 CV0~CV3 的“通过”自动升级；不得给出 `monetary_value`。
- **证据不完整应明确Unknown，不得记零**。

## 2. 时间与版本不可混用

真实历史T0在授权日之前：B授权版本可作为后验观察，但不得用于该时点的权利状态/评分。

对当前时点的授权专利：
1. 首先锁定B权项，尤其独立权利要求；
2. 再比较A与B，建立 `added/removed/modified elements` 的项目级改动清单；
3. 区分**方法、装置、组合物、产品**不同保护客体，不把某个B权1的使用范围扩展成所有产品；
4. 如发现分案/同族，单独建立不同claim-set记录，不得默认互相继承；
5. 在未做E3精准映射前，Realization最多保留当前直接可见的R阶段，不能凭权项差异直接推导市场成功。

## 3. 示例（合成，不是六件真实专利的再编码）

`data/experimental/claim-version/synthetic-fixtures.jsonl`包含：
- A-only：直接Blocked；
- B存在但无逐要素差异：Preliminary；
- B权项与A逐要素核过，候选现有技术来源可追溯：Claim-scoped research；
- 曾用未来授权版本回填历史T0：Blocked；
- 把T0后发表文献当优先权前的先例：Blocked；
- B已核但没有E3/E4：仍不得报货币估值。

运行：`python tools/validate_claim_version_gate.py`。
自动化只验证“可否进入下一段研究”，**绝不自动判定创新性、侵权、有效性、金额或奖项分数**。

## 4. 将来的真实双人评审不能被替代

先前只有**一套AI分别模拟两个评审视角**；本轮进行了公开授权文本证据复议，这也不等于两位独立真人评审。原 [Issue #91](https://github.com/xiangsee/patent-value-benchmark/issues/91) 继续保持开放，标注 `Not Run`。不能用AI分歧数写Cohen's κ或真实性能。

## 5. 对评估产品的具体改变

每件专利的可交付报告须包含一行“**授权权项版本与修改核验**”：

`CN/US/... · grant publication · independent claim ID(s) · source version · A→B material changes · date/T0 · prior-art search limits · claim-to-carrier mapping status`

在这些信息未明时，允许输出技术问题与研究线索，暂停法律控制与货币归因结论。

## 6. 限制与反证

- A/B权项项数相同，但独权可明显变化，因此“项数比对”不能充当全文比对。
- B权项更具体不自动等于“创新性高/低”或“市场价值低”。
- 检索到先例不等于足够证明创造性问题；必须清楚要素和技术动机、技术效果。
- 没找到实施资料不等于没有实施；必须记录搜索范围和“未知”。
- 真实货币估值仍须单独的可归因经济流、合同对象、权益范围与G0–G4准入。

**治理决定：**只增设研究方法与合成验证工具；不修改正式Ledger/Diagnostic、CI原有V0.7规则和任何客户历史评分。