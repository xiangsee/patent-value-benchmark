# Realization Path Replication — Editas → Vertex → DRI

日期：2026-09-26  
状态：Issue #16 replication path 2  
路径类型：license / recurring cash / secondary monetization

## 结论先行

这个案例直接反证了一个过于诉讼中心的假设：

> **专利价值实现不需要先经过侵权认定。**

2023年12月12日，Editas与Vertex签署非独占Cas9许可，覆盖SCD/TDT领域的BCL11A ex vivo gene editing，包括CASGEVY。

没有jury verdict。

没有infringement judgment。

没有damages award。

但经济价值真实实现了。

## 1. License execution

Vertex获得相关Cas9技术/专利权利的非独占许可。

合同约定：
- USD 50m upfront
- potential additional USD 50m contingent upfront
- annual license fees through 2034
- Broad/Harvard share for the underlying Cas9 technology

因此在Realization Path语言中：

```text
Infringement State:
  not required

Transaction State:
  license executed

Future cash rights:
  created
```

这说明：

> **Infringement State不能是所有Realization Path的必填前置步骤。**

## 2. Cash actually received

Editas 2023 Form 10-K确认：

> USD 50m upfront cash payment已经收到。

这和Taction的jury verdict形成非常重要的对照。

Taction：

```text
$5.7bn verdict
cash realization = unresolved
```

Editas：

```text
no infringement verdict
$50m upfront
cash realization = confirmed
```

所以：

> **Legal valuation event的金额可以巨大但未兑现；许可金额可以较小，却已经是真正实现的现金。**

## 3. Recurring realization

2024年第一季度，Editas又确认收到：

> USD 10m annual license fee.

因此license并不是一个一次性event。

它创建的是：

> **未来现金流权利。**

Realization Path必须能表示：
- upfront
- recurring fee
- contingent fee
- sales-based fee
- royalty-like future payments

但这些仍然都是合同scope内的价值证据，不是单件专利价格。

## 4. DRI让路径再次分叉

2024年10月3日，Editas把Vertex许可项下的一部分未来应收款转让给DRI，换取：

> USD 57m upfront cash.

这里发生的已经不是：

`Patent → License`

而是：

```text
Patent / Portfolio Rights
        ↓
Vertex License
        ↓
Future Receivables
        ↓
DRI Monetization
        ↓
Cash Today
```

这是非常重要的新发现。

> **Realization Path不是一条线，而可能继续生成新的可交易资产。**

未来许可费本身可以被金融化。

## 5. 模型修正

Taction最初让我们提出：

```text
Infringement State
→ Remedy State
→ Cash Realization State
```

Editas说明，这不是一般结构。

至少还必须存在：

```text
License / Transaction Branch
→ Contractual Payment Rights
→ Cash Received
→ Secondary Receivable Monetization
```

因此：

- `infringement_state`应当是optional；
- `remedy_state`过于诉讼中心；
- Realization Path必须有transaction mechanism；
- rights subject必须允许portfolio / field rights，而不只是exact patent。

## 6. 仍然坚持non-inheritance

这条路径实现了真实现金。

但不能写：

> 某一件Broad CRISPR专利值5000万美元、1000万美元或5700万美元。

原因是交易scope是：
- portfolio / Cas9 technology
- specific field
- contractual rights
- future receivables

因此所有金额保留原scope，不拆给单件专利。

