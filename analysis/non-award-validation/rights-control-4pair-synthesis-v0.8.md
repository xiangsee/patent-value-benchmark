# Claim-set Rights Control — 4-Pair Cross-case Synthesis

日期：2026-09-26  
状态：Package A preregistered replication threshold complete  
正式架构：V0.7 remains adopted  
V0.8：research-only

## 一、结论

四组对照完成后，可以做一个比“Rights Control有用”更明确的判断：

> **Claim-set Rights Control 已达到进入 V0.8 候选 Schema 设计阶段的证据门槛。**

这里说的是：

**candidate schema design**

不是：

**V0.8 adoption**。

## 二、四组样本

| Pair | Realization contrast | Rights-control contrast | 新增信息 |
|---|---|---|---|
| i4i × Amgen | R5 vs R4 | injunction/enforcement vs genus claims invalid | realization ≠ legal control |
| Apple ’381 c19 × ’915 c8 | R4 vs R5 | reexam-confirmed vs adverse reexam posture | higher realization ≠ stronger rights |
| SynQor ’702 c56 × ’021 c30 | **R4 vs R4** | patentability sustained vs obviousness rejection affirmed | equal R-stage ≠ equal rights |
| Wirtgen ’309 c29 × Caterpillar ’693 c19 | **R4 vs R4** | IPR survives vs unpatentable FWD + live LEO | rights = adjudication + finality + operative remedy |

随着样本推进，控制条件不断收紧。

第四组已经把问题推进到：

> “valid / invalid”本身都不够。

## 三、稳定重复出现的最小字段

四组真正重复出现、而不是只在单个故事里出现的字段是：

### Identity

- patent_id
- claim_set_id
- jurisdiction
- as_of_date / T0

### Scope

- scope_type
- value_carrier_mapping

### Adjudication

- proceeding_type
- forum
- challenged_claims
- outcome
- decision_date

### Finality

- appeal_status
- rehearing_status
- cancellation_certificate / formal effect
- finality_state

### Operative Control

- enforceability_state
- operative_injunction / exclusion / remedy
- current ability to assert/exclude

这些已经获得跨样本支持。

## 四、哪些字段还不能因为“合理”就冻结

第一轮理论议程还提出：

- design_around_cost
- design_around_time
- blocking_power
- FTO dependency
- performance_loss_if_removed

这些概念很重要。

但四组Rights Control复制并没有系统验证这些字段。

所以它们只能继续作为：

> Counterfactual Control research candidates

不能因为概念好听就一并塞进Claim-set Rights Control Schema。

## 五、建议的最小实验对象

下一步可以设计：

```text
claim_set_rights_control {
  rights_control_id
  patent_id
  claim_set_id
  jurisdiction
  as_of_date

  scope_type
  value_carrier_mapping

  adjudication_events[] {
    proceeding_type
    forum
    decision_date
    claims_at_issue
    outcome
    status
  }

  finality_state {
    appeal_status
    rehearing_status
    formal_cancellation_or_confirmation
  }

  operative_control {
    enforceability_state
    injunction_or_exclusion_order
    remedy_status
  }

  evidence_ids[]
}
```

注意：

> **不提供Rights Control总分。**

原因是最后一组已经证明，状态可能互相张力：
- PTAB不利；
- cancellation尚未发生；
- ITC remedy仍然有效。

把这些压成一个0–100分，会再次损失最重要的信息。

## 六、与V0.7如何连接

最合理的结构不是把Rights Control塞回R0–R5。

而是并列：

```text
Patent / Claim Set
│
├─ V0.7 Realization State
│    R0 → R5
│
├─ Attribution / Evidence
│
├─ Observability
│
└─ Claim-set Rights Control
     ├─ adjudication
     ├─ finality
     └─ operative control
```

于是可以出现合法组合：

- R5 + strong rights
- R5 + weak/adverse rights
- R4 + strong rights
- R4 + adverse-but-still-operative rights

这正是四组样本实际观察到的世界。

## 七、Package A verdict

预注册要求：

> 4组Same-realization / Different-rights-control对照。

结果：

# 4 / 4 complete

因此：

> **H1 replication threshold met。**

但整个V0.8 adoption threshold仍未达到：

- Rights Control pairs：**4 / 4**
- clean early-stage option retrospectives：**0 / 4**
- portfolio case：**1 / 1**
- Two Clocks case：**1 / 1**
- SEP / patent-pool / cross-license replication：**0 / 1**

## 八、治理决定

Package A 到这里停止扩样。

下一步不是Pair #5。

下一步是两件事：

1. **实验性 Claim-set Rights Control Schema**
2. 转入 Package B / C 的未完成验证

除非未来新样本反证，否则不再机械增加Rights Control案例。

