---
title: Verifiable Retrieval for Legal Reasoning through Structure-driven Knowledge
  Graph
title_zh: 面向法律推理的可验证检索：结构驱动知识图谱
authors:
- Ibrahim Siddig
- Sviatoslav Tugeev
- Munir Georges
affiliations:
- Technische Hochschule Ingolstadt
arxiv_id: '2610.13695'
url: https://arxiv.org/abs/2610.13695
pdf_url: https://arxiv.org/pdf/2610.13695
published: '2026-10-09'
collected: '2026-10-13'
category: RAG
direction: RAG · 知识图谱结构化检索
tags:
- RAG
- Knowledge Graph
- Legal Reasoning
- Chunking
- Retrieval
- Verifiability
one_liner: 用结构驱动解析构建法律知识图谱，比较多种 KG 感知分块与检索策略以提升引文检索准确性
practical_value: '- 可将结构驱动解析迁移到电商/广告领域：基于商品类目树、属性 Schema、活动规则等层级结构构建 KG，替代固定长度分块，提升召回语义完整性。

  - 在客服导购 Agent 或规则问答系统中，要求输出附带来源证据（如具体条款、商品属性路径），实现可验证引用，降低幻觉风险。

  - 混合检索策略可借鉴：先经 KG 导航缩小候选范围，再做向量相似度匹配，平衡精确性与召回率，适合规则密集、文档规模大的场景。

  - 对生成式推荐中的可解释性有参考意义：生成 item/文案时绑定结构化来源，便于后续审计与用户信任建立。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：法律、医疗等可靠性敏感场景要求 AI 输出透明、可验证，但 LLM 黑箱特性难以满足。RAG 通过引入可解释文档降低幻觉风险，然而当源文档数量与规模增大时，朴素检索容易遗漏关键上下文，损害引用准确性。

**方法关键点**：以德国法典为对象，利用结构驱动解析将法律条文构建为知识图谱，用于文档导航与检索。论文比较了多种 KG-informed 的分块与检索策略（如基于条款/章节边界分块、图遍历与向量检索结合），以提升引用检索准确率为目标。

**结果**：论文未在摘要中给出具体数值，核心结论是结构化 KG 方法相对朴素检索能更完整地保留关键上下文，从而改善法律引文检索的可验证性。
