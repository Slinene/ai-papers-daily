---
title: An Agentic Hybrid Top-Down and Bottom-Up Approach to Knowledge Graph Generation
title_zh: 代理式混合自顶向下与自底向上的知识图谱生成方法
authors:
- Emma Jouffroy
- Warren Jouanneau
- Marc Palyart
affiliations:
- Malt, Paris, France
arxiv_id: '2608.07023'
url: https://arxiv.org/abs/2608.07023
pdf_url: https://arxiv.org/pdf/2608.07023
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: Agent 知识图谱构建
tags:
- Knowledge Graph
- LLM
- Agentic Patterns
- Entity Reconciliation
- Multilingual
- Skill Taxonomy
one_liner: 提出结合 LLM 与 Wikidata 的代理式混合管道，实现多语言技能概念的自适应对齐与涌现
practical_value: '- 混合外部知识库（Wikidata）与 LLM 的思路可直接迁移到电商商品属性图谱构建：已有 SPU/属性对应 Wikidata
  或 Freebase 实体进行锚定，LLM 负责发现并结构化新属性或长尾品类。

  - 代理反思（agentic reflexion）模式用于未匹配概念的迭代恢复，可解决商品描述中不断出现的新词、新属性（如“可折叠”“氮化镓”）无法对齐的问题，工程上可设计类似的检查-再生成-去重闭环。

  - 多语言规范化及去重阶段对跨境电商标品属性对齐（如颜色、尺寸）有直接借鉴：先用 LLM 多语言标准化，再基于语义相似度去重，减少人工 mapping 成本。

  - 自愈（self-healing）框架与主动策展（active curation）思想可用于实时商品库的质量监控：自动检测失效或低置信度映射并重新调和，保障下游搜索推荐的特征质量。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：HR 平台面临数万条不标准、多语言自由文本技能声明，导致人才匹配困难。传统手工构建分类学不可扩展，纯 LLM 方案存在幻觉和缺乏可解释元数据。

**方法关键点**：
- 提出混合知识图谱生成管道，将 LLM 锚定在 Wikidata 多语言知识图谱上，结合自顶向下（已知实体映射）与自底向上（涌现新概念）策略。
- 采用代理反思模式（agentic reflexion），对未匹配概念迭代恢复：先尝试对齐，失败则动态创建新节点并生成关系元数据。
- 管道分五阶段：实体调和、多语言规范化、主动策展、去重、未匹配概念恢复。处理覆盖五种欧洲语言，自动适应技能噪声和漂移。

**关键结果**：
- 构建了一个可扩展、可解释、自愈的技能知识图谱，并衍生出结构化分类体系。系统能在无监督下持续整合新涌现技能，无需手动干预。
