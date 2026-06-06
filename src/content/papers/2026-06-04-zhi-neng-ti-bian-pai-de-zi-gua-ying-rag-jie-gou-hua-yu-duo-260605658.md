---
title: 'Agent-Orchestrated Adaptive RAG: A Comparative Study on Structured and Multi-Hop
  Retrieval'
title_zh: 智能体编排的自适应 RAG：结构化与多跳检索对比研究
authors:
- Anuj Maharjan
- Devinder Kaur
- Richard Molyet
affiliations:
- University of Toledo
arxiv_id: '2606.05658'
url: https://arxiv.org/abs/2606.05658
pdf_url: https://arxiv.org/pdf/2606.05658
published: '2026-06-04'
collected: '2026-06-06'
category: RAG
direction: RAG 自适应编排与多跳检索对比
tags:
- RAG
- Agentic AI
- Query Decomposition
- Multi-Hop Reasoning
- Adaptive Orchestration
- LLMs
one_liner: 提出 Agent 编排的自适应 RAG 框架，发现动态分解与反思并非普适，需根据查询和领域选择性使用。
practical_value: '- **按查询类型自适应路由**：电商 RAG 系统中，简单事实查询避免过度分解，多跳推理查询才启动迭代检索，避免统一处理带来的精度损失。

  - **引用准确性增强可参考反思机制**：在答案生成后增加轻量级自检（如检查引用是否支持声明），能明显提升可信度，但需控制延迟，可只在高风险场景（如售后纠纷、合规问答）开启。

  - **结构化领域优先采用查询分解**：对于商品说明书、运维手册等结构清晰的语料，动态分解能提升检索覆盖率和排序精度（MRR +0.17），可直接复用。

  - **成本感知的编排框架设计**：根据延迟预算和查询复杂度动态调节 agent 行为，避免“最强即最好”的暴力策略，对工程落地很有价值。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统 RAG 使用静态、单步检索，难以应对需要多跳推理或深度解析的复杂查询，在 DevOps 等高风险领域易出错。

**方法**：提出 Agent 编排的自适应 RAG 框架，核心包含三个组件：动态查询分解（将复杂问题拆成子问题）、迭代检索（逐步收集证据）和有界反思回路（生成答案后自检，最多重试 3 次）。在结构化 DevOps 知识库和多跳推理基准 MuSiQue 上对比评估。

**关键结果**：在结构化领域，查询分解带来显著收益（DevOps 总分 +0.04，MRR +0.17），但反思机制几乎无额外帮助；在多跳基准，分解反而降低排序精度（MRR 下降），反思能提升引用准确性却引入严重延迟。总体表明，agentic 增强并非普适，需自适应、成本感知地选择性应用。
