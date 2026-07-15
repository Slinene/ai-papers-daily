---
title: 'Enhancing LLMs through human feedback: a journey towards self-improvement'
title_zh: 通过人类反馈增强LLM：迈向自我改进之路
authors:
- Tatiana Pelc
- Gila Kamhi
- Asaf Avrahamy
- Adi Fledel-Alon
affiliations:
- Intel Corporation
arxiv_id: '2607.11267'
url: https://arxiv.org/abs/2607.11267
pdf_url: https://arxiv.org/pdf/2607.11267
published: '2026-07-13'
collected: '2026-07-15'
category: RAG
direction: 人类反馈驱动的RAG自我改进
tags:
- RAG
- human feedback
- self-improvement
- LLM-as-a-Judge
- RLHF
one_liner: 用辅助RAG系统收集并整合详细人工反馈，驱动主RAG回答的自我优化
practical_value: '- 在推荐或问答系统中，收集用户明确纠正的文本反馈（如“我要的不是XX，而是YY”），比隐式二元信号更能精准定位检索和生成缺陷

  - 可构建一个轻量的辅助RAG模块，专门处理用户反馈，动态修正知识库的检索权重或生成策略，而无需频繁重训大模型

  - 引入人类在环的持续反馈循环，将新反馈逐步纳入实时推理，适合线上快速迭代的电商搜索或客服场景

  - 利用LLM-as-a-Judge自动化评估反馈对系统改进的效果，降低人工评估成本，适合快速实验和上线'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统RAG系统难以捕捉用户偏好、适应变化的信息需求，且常见RLHF依赖简单的二元反馈，限制了学习深度。本文旨在利用人类提供的详细文本反馈（如纠正性建议）来持续改进RAG的准确性与相关性。

**方法**：提出双RAG架构：主RAG负责回答问题，辅助反馈RAG专门处理用户反馈。实现人类在环流程，持续收集、分类用户反馈，将其转化为对主RAG检索或生成环节的修正信号，集成到推理工作流中，使系统迭代自优化。评估采用LLM-as-a-Judge策略，在三个基准（含通用和定制领域）上测试。

**结果**：通过反馈驱动的增强，系统在准确性、相关性和整体回答质量上均得到显著提升，验证了该方法在自适应信息检索领域的有效性，为自主优化和用户参与驱动的改进树立了范例。
