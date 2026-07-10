---
title: Improving Ad-hoc Search Effectiveness for Conversational Information Retrieval
  via Model Merging
title_zh: 通过模型合并提升对话检索中的即席搜索有效性
authors:
- Ahmed Rayane Kebir
- Jose G. Moreno
- Lynda Tamine
affiliations:
- University of Toulouse, IRIT
arxiv_id: '2607.08540'
url: https://arxiv.org/abs/2607.08540
pdf_url: https://arxiv.org/pdf/2607.08540
published: '2026-07-09'
collected: '2026-07-10'
category: RecSys
direction: 对话式检索 · 模型合并
tags:
- Model Merging
- Conversational IR
- Ad-hoc Search
- Zero-shot
- Catastrophic Forgetting
one_liner: 无需微调，通过参数合并融合即席与对话检索能力，零样本NDCG@3提升最高15%
practical_value: '- 当电商搜索需要同时支持多轮对话与常规即席查询时，可直接合并对话微调模型与基础检索模型，避免重新训练和灾难性遗忘，节省大量资源。

  - 使用线性（Model Soup）或球面插值（Slerp）两种合并策略，工程实现简单，可作为多任务模型部署的轻量级方案。

  - 在零样本场景下，合并模型对未见过的查询表现出更好泛化性，适合快速应对新领域或冷启动的检索需求。

  - 该方法提供了一种模型能力组合的思路，可借鉴用于融合不同业务场景（如推荐与搜索）下的微调模型，提升单一模型的综合表现。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：对话信息检索需综合考虑历史上下文，但主流方法基于对话数据微调检索器，会导致灾难性遗忘，模型丧失原本的即席搜索性能，且重训练成本高。

**方法**：提出训练无关的模型合并策略，将预训练的即席检索模型与在对话数据上微调的模型进行参数级融合，得到单一模型同时适用于两类场景。采用两种合并方式：线性平均（Model Soup）和球面线性插值（Slerp）。

**结果**：在标准即席搜索与对话检索数据集上，合并模型显著提升了对话检索器的即席搜索能力，零样本条件下NDCG@3最大提升15%，同时跨数据集泛化性增强，有效缓解了灾难性遗忘。
