# Licensing Strategy — Decision Required

状态：**尚未选择许可证。**

在 v0.1.0 正式发布前，建议分别处理代码、原创文档和结构化数据，而不是用一个 LICENSE 覆盖所有内容。

## 1. Code

范围示例：
- `tools/*.py`
- GitHub Actions
- JSON Schema中具有软件/规范性质的部分

候选：

### Option A — MIT
优点：
- 简单、宽松、行业接受度高；
- 有利于企业、代理机构、研究者直接集成。

注意：
- 专利/商标等权利声明相对Apache-2.0更简洁。

### Option B — Apache-2.0
优点：
- 宽松；
- 对专利授权条款更明确；
- 大型企业/基础设施项目较常见。

建议倾向：**Apache-2.0 或 MIT 二选一。**

## 2. Original Documentation

范围：
- 方法论
- Data Dictionary
- README
- 原创分析文档

候选：
- **CC BY 4.0**：允许复制、改编和商业使用，要求署名。
- **CC BY-SA 4.0**：衍生内容需同许可分享，更强的开放回流要求。

若目标是成为行业通用标准，通常更倾向 **CC BY 4.0**。

## 3. Structured Dataset

范围：
- 本项目原创整理的结构化字段
- source registry中的链接、日期、状态
- 自己形成的 evidence/ledger/diagnostic 编码

候选：
- **CC BY 4.0**：要求署名；
- **CC0 1.0**：最大限度降低数据复用摩擦。

需要特别区分：

> 对第三方事实做结构化整理，不意味着本项目拥有第三方原始文档的版权或数据库权利。

仓库不应把受限数据库或第三方PDF全文重新授权出去。

## 4. Recommended package for decision

一个较平衡的组合：

- Code: **Apache-2.0**
- Original docs: **CC BY 4.0**
- Original structured data: **CC BY 4.0**
- Third-party source documents: **not redistributed / original rights reserved by their owners**

更开放的数据方案可把 structured data 改为 CC0。

## 5. Before adding LICENSE files

需要用户明确决定：
1. Code：MIT 还是 Apache-2.0？
2. Docs：CC BY 4.0 还是 CC BY-SA 4.0？
3. Data：CC BY 4.0 还是 CC0 1.0？

在明确决定前，本仓库不添加会造成误解的总LICENSE。
