---
title: Retrieval Augmented Generation Compositionality
title_zh: 检索增强生成（RAG）的组合性评估
authors:
- Ido Levy
- Segev Shlomov
- Leshem Choshen
affiliations:
- IBM
- Weizmann Institute of Science
arxiv_id: '2610.29722'
url: https://arxiv.org/abs/2610.29722
pdf_url: https://arxiv.org/pdf/2610.29722
published: '2026-10-20'
collected: '2026-10-23'
category: RAG
direction: RAG 流水线组合评估
tags:
- RAG
- Compositionality
- Evaluation
- Retrieval
- Faithfulness
- LASAGNA
one_liner: 系统评估RAG各阶段技术组合，发现孤立增益不可叠加且最优组合随语料规模变化
practical_value: '- 在电商/Agent的RAG知识库或购物问答中，不要只按单模块离线指标选型：三种检索技术孤立预测+47%联合提升，组合后仅+17%，单点提分可能被其他阶段抵消。

  - 同时跟踪检索质量（如NDCG@10）和最终忠实度/业务指标；组件对两者增益方向可能相反，避免为召回率牺牲生成质量。

  - 语料规模从小规模实验到全量商品库/百万级文档时，必须重新验证最优组合；小语料最优配置不一定在大语料保持，应做分规模子集测试。

  - 借鉴LASAGNA思路搭建内部RAG实验框架，固定其他阶段做单变量替换，支持不同语料规模与多指标报告，沉淀可复现的pipeline配置。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现代RAG管线由embedding、chunking、检索、rerank、query augmentation、context compression、agentic验证等多阶段技术组成，但现有评估通常只做单阶段孤立实验，无法说明组合后的真实增益，也不清楚检索质量与答案忠实度是否偏好同一设计，以及小语料结论能否外推到大语料。

**方法关键点**：提出开源框架LASAGNA，用于可控RAG组合评估；预注册三个假设，在8个benchmark、5K–200K文档规模上测试450种配置，覆盖8个主要设计阶段。

**关键结果**：三种检索技术孤立预测+47%的联合提升，实际组合仅+17%；组件增益在检索指标（NDCG@10）和忠实度上堆叠方式不同，优化一个可能损害另一个；最佳组合随语料规模变化，小语料胜出的配置在大语料未必最优。结论：孤立增益不可靠，新的RAG技术必须纳入完整管线评估。
