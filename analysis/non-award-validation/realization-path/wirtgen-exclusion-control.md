# Realization Path Replication — Wirtgen ITC Exclusion Path

日期：2026-09-26  
状态：Issue #16 replication path 3  
路径类型：infringement / exclusion / control realization

## 结论先行

Wirtgen的US7828309 claim 29说明：

> **专利价值实现不一定表现为收到钱。**

2019年，ITC认定相关Caterpillar道路铣刨机侵犯claim 29，并发布Limited Exclusion Order。

截至2026-09-26，USITC的Outstanding Section 337 Exclusion Orders列表仍然列出：

> 337-TA-1067 — Road Milling Machines and Components Thereof

以及US7828309等相关专利。

因此这里实现的是：

# Control Realization

而不是Cash Realization。

## 1. Infringement / entitlement established

claim 29与Caterpillar PM620的产品映射已经通过ITC程序建立。

因此：

```text
Entitlement / Infringement State:
  established
```

## 2. Remedy became operative control

ITC不是给Wirtgen一个巨额damages verdict。

而是：

> 禁止符合条件的侵权道路铣刨机及相关部件未经许可进入美国。

因此：

```text
Realization Mechanism:
  Limited Exclusion Order

Economic effect:
  exclusion / market control
```

这是一种已经实现的专利经济价值。

它不能被写成：

`cash_received = 0 → value not realized`

## 3. 长期状态也可以持续

到2026年，337-TA-1067仍然出现在USITC outstanding orders列表。

说明Realization Path需要表达：

- remedy issued
- remedy stayed?
- remedy modified?
- remedy vacated?
- remedy outstanding?
- remedy expired?

也就是说，Remedy本身也是一个时间化资产状态。

## 4. 对原模型的修正

如果模型只设计：

`Cash Realization State`

那么Wirtgen会被错误编码成：

> nothing realized.

实际上它已经取得并维持了排除竞争产品进口的法律能力。

所以建议改成：

# Economic Realization State

并允许至少三类channel：

- cash realization
- control / exclusion realization
- contractual / future-cash realization

## 5. 与Rights Control的边界

这里要避免再次混淆。

Claim-set Rights Control记录：

> claim 29本身的权利控制状态。

Realization Path记录：

> Wirtgen如何把这项权利针对Caterpillar推进成一个实际生效的排除令。

两者有关，但不是一回事。

