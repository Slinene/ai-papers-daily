---
title: 'DexterSQL: Deep Schema Exploration and Rule-based Correction for Text-to-SQL
  Generation'
title_zh: DexterSQL：深度 Schema 探索与规则修正的 Text-to-SQL 生成
authors:
- Anik Pramanik
- Murat Kantarcioglu
- Vincent Oria
- Shantanu Sharma
affiliations:
- New Jersey Institute of Technology
- Virginia Tech
arxiv_id: '2608.11889'
url: https://arxiv.org/abs/2608.11889
pdf_url: https://arxiv.org/pdf/2608.11889
published: '2026-08-12'
collected: '2026-08-16'
category: Other
direction: Text-to-SQL · 深度Schema探索与规则修正
tags:
- Text-to-SQL
- Schema Exploration
- Rule-based Correction
- Multi-path SQL Generation
- LLM Prompting
one_liner: 用深度 schema 探索、数据库无关规则修正与多路径生成提升 Text-to-SQL 准确率
practical_value: '- **Schema 细粒度探查可迁移到指标/取数场景**：对电商数据仓库中易混淆列（如“下单金额”vs“支付金额”）做单列+联合分布分析，自动发现区分性特征，注入
  prompt 可降低 LLM 列选择歧义。

  - **用训练集错误挖掘数据库无关修正规则**：把线上 Text-to-SQL 或 NL 查询解析的 badcase 回流，提炼成与具体库无关的纠错规则（如“时间条件不可省略”），可跨库持续累积并降低重复错误。

  - **依赖树骨架分解对复杂分析查询有用**：在生成 SQL 前先依据问句句法结构构建 dependency tree，拆成 SQL skeleton，能有效缓解条件遗漏/错放问题；电商运营复杂报表查询可直接借鉴该中间表示。

  - **非微调方案接入成本低**：整体基于 prompting，不改变 LLM 参数，适合快速迭代并叠加在已有 LLM API 上，适合业务初期验证。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：基于 prompting 的非微调 Text-to-SQL 方法普遍依赖粗粒度 schema 信息，难以区分歧义列；不捕获重复 SQL 生成失败模式；处理复杂问题时易出现条件遗漏、幻觉或错放。

方法关键点：DexterSQL 提出三个组件。1) Deep schema explorator：识别歧义列，分析其单独与联合数据分布，揭示列间关系和各自角色。2) Database-agnostic rule creator：仅在训练库上挖掘生成 SQL 与 gold SQL 的差异，转化为数据库无关的纠错规则，捕捉 LLM 重复失败模式。3) Multi-path SQL generation：引入基于 dependency tree 的中间表示，利用问句句法结构指导分解为 SQL skeleton，再生成最终 SQL，缓解复杂问题条件错置。

关键结果：在 BIRD-Dev 上，开源权重模型 GPT-OSS-120B 准确率达 67.6%，比最优基线至少提升 2.7%；闭源模型 GPT-4o 和 GPT-5.2 分别达 71.6% 和 72.2%，至少提升 0.9%。
