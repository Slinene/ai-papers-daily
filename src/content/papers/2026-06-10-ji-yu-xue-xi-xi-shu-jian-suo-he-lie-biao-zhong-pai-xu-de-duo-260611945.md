---
title: 'uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse
  Retrieval and Listwise Reranking'
title_zh: 基于学习稀疏检索和列表重排序的多轮RAG系统
authors:
- Simon Lupart
- Kidist Amde Mekonnen
- Zahra Abbasiantaeb
- Mohammad Aliannejadi
affiliations:
- University of Amsterdam
arxiv_id: '2606.11945'
url: https://arxiv.org/abs/2606.11945
pdf_url: https://arxiv.org/pdf/2606.11945
published: '2026-06-10'
collected: '2026-06-11'
category: RAG
direction: 多轮对话RAG · 稀疏检索 · LLM重排序
tags:
- Multi-turn RAG
- Learned Sparse Retrieval
- Listwise Reranking
- Conversational Search
- Query Rewriting
- Unanswerable Queries
one_liner: 结合学习稀疏检索与LLM重排序的多轮RAG管道，利用完整对话历史提升跨域泛化与鲁棒性
practical_value: '- 多轮对话历史的全上下文利用：使用LLM基于完整对话历史进行查询重写、重排序和生成，可迁移至电商客服/购物助手的多轮对话状态跟踪，提升连贯性。

  - 学习型稀疏检索（LSR）的跨域泛化：在不同商品类目或业务场景下无需频繁微调，适合电商导购、售后等多种语域快速冷启动。

  - 无法回答查询的识别与处理：在客服场景中可借鉴其拒答/转人工机制，提升系统安全性与用户体验。

  - 列表式重排序增强候选质量管理：利用LLM长上下文进行listwise重排序，可在对话式推荐中对候选商品列表进行全局排序，提升推荐精度。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
多轮对话检索与问答面临历史信息累积、话题漂移和歧义等挑战，同时需识别无法回答的查询。SemEval-2026 Task 8评测涵盖金融、云文档、政府、维基等领域，要求系统在信息不足时恰当响应。  

**方法**  
提出多阶段RAG管道：(1) 对话查询重写：基于完整对话历史，用LLM将当前查询转为适合检索的表述；(2) 学习型稀疏检索（LSR）：作为主检索引擎，利用其跨域强泛化能力召回初始候选文档；(3) 两阶段LLM重排序：先进行pointwise评分，再对截断候选集进行listwise重排，充分利用LLM长上下文优势；(4) 最终响应生成：继续用LLM基于全历史及重排后的证据合成答案。所有步骤均显式嵌入对话历史，确保上下文一致性。  

**结果**  
在SemEval-2026 Task 8评测中表现稳健，尤其在需要跨域泛化和处理无法回答查询的场景下，该管道展现出较高的鲁棒性和端到端效果，验证了LSR与LLM重排序协同的有效性。
