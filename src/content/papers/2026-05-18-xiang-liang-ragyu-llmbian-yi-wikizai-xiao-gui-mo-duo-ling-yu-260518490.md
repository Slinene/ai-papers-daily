---
title: 'Vector RAG vs LLM-Compiled Wiki: A Preregistered Comparison on a Small Multi-Domain
  Research'
title_zh: 向量RAG与LLM编译Wiki在小规模多领域研究语料上的预注册对比
authors:
- Theodore O. Cochran
affiliations:
- AI for Altruism (A4A)
arxiv_id: '2605.18490'
url: https://arxiv.org/abs/2605.18490
pdf_url: https://arxiv.org/pdf/2605.18490
published: '2026-05-18'
collected: '2026-05-23'
category: RAG
direction: RAG架构对比与知识合成优化
tags:
- RAG
- LLM Wiki
- Knowledge Synthesis
- Citation
- Cost Comparison
- Multi-document QA
one_liner: 首次定量对比发现Wiki在跨论文合成与引用支持上优于RAG，但成本高；分解式RAG可低成本恢复部分优势
practical_value: '- 在电商知识库问答中，若需跨商品/多源信息合成（如对比评测），可借鉴Wiki预编译思路构建内部知识图，但需权衡高昂的查询token成本与构建开销。

  - 对成本敏感的业务，优先考虑分解式RAG（将问题拆解为子问题分别检索），既能提升跨文档合成效果又保持较低LLM调用成本，适合部署在实时客服或推荐解释生成中。

  - 引用的精确性评价不可只看整体有据性，需引入逐项引用检查机制，确保每一条声明都精准对应来源，这对电商合规回答至关重要。

  - 架构选择无银弹，应针对业务侧重点（证据组织、引用支撑、查询成本）做有针对性地选型，可设计混合式系统动态路由。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：比较两种帮助LLM在小规模研究语料上回答问题的架构——单轮向量RAG与LLM编译后的markdown Wiki。分析两者在证据组织、引用支持与成本上的权衡，为知识密集型问答系统设计提供依据。

**方法**：预注册研究，固定24篇论文、13个问题，使用相同答案生成模型，盲审评分。Wiki在检索阶段由模型从预编译的知识页面中获取内容，RAG直接从原文块检索。还探索了分解式RAG变体（将问题拆解为子问题分别检索并合成答案）。

**关键结果**：
- Wiki在“连接跨论文发现”上显著优于RAG，但“答案组织”优势在法官调整后不显著；RAG达到预设的单事实查找标准。
- 查询成本：Wiki每次查询使用的token数远超RAG，无法收回预付构建成本，与预期相反。
- 逐项引用检查：Wiki被引页面更常精确支持其陈述，即使整体有据性评分RAG更高。
- 分解式RAG恢复了大部分跨论文合成优势，且LLM成本更低，但未恢复Wiki的逐引用支撑优势。

**结论**：有依据的研究合成不是单一能力，证据组织、引用精准度和运行成本三者间存在权衡，没有一种架构在所有维度上最优。
