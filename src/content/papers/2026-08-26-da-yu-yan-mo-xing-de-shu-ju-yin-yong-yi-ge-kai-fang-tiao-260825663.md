---
title: 'Data Citation for Large Language Models: A Challenge'
title_zh: 大语言模型的数据引用：一个开放挑战
authors:
- Gianmaria Silvello
affiliations:
- University of Padua
arxiv_id: '2608.25663'
url: https://arxiv.org/abs/2608.25663
pdf_url: https://arxiv.org/pdf/2608.25663
published: '2026-08-26'
collected: '2026-08-30'
category: Other
direction: 数据引用与溯源 · LLM
tags:
- data citation
- provenance
- LLM
- RAG
- knowledge graphs
- training data attribution
one_liner: 提出 LLM 数据引用三方向：训练数据归因、推理时数据引用、知识图谱事实引用，与文档级引用 grounding 区分
practical_value: '- 在 RAG 或 Agent 工作流中，引用源不能只给文档块/URL，应设计数据引用层：对商品表、用户行为聚合、知识图谱三元组等结构化/半结构化数据，记录
  dataset+subset+query+version+timestamp 等固定性信息，避免引用粒度太粗导致无法复现。

  - 训练数据归因（如 influence functions、TRAK）可转化为数据贡献报表，用于合规审计、数据合作方结算；电商推荐模型若用外部数据或用户数据，可借此评估哪些训练集对模型行为影响大，平衡数据收益与版权风险。

  - 引用 KG 事实时，要把三元组（s,p,o）作为可引用单元，并沿 provenance 传播 credit：例如商品知识图谱中一个属性值来自某供应商，生成推荐解释时应溯源到具体三元组及其上游来源，增强可解释性和信任。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 正成为信息访问入口，输出来源复杂，涵盖训练语料、RAG 检索文档、知识图谱、工具/Agent 查询。现有引用研究主要把引用当作验证机制，且只针对文本，忽略了学术引用的信用与溯源功能，也忽视了数据引用。

**方法关键点**：论文区分“数据引用”与“文档级引用 grounding”，提出三个研究方向：
1. 训练数据归因：将影响估计转化为对模型参数中吸收语料的引用；
2. 推理时数据引用：在适当粒度和固定性上识别数据集、子集、查询结果；
3. 引用知识图谱事实：定义单个三元组引用的指称及信用沿溯源传播。

强调需数据库、信息检索、知识表示与 AI 社区联合推进。

**结果**：无实验数字，属于挑战/路线图论文，明确概念和未来研究路径。
