---
title: 'RL-Index: Reinforcement Learning for Retrieval Index Reasoning'
title_zh: RL-Index：用强化学习优化索引推理的检索增强框架
authors:
- Yongjia Lei
- Nedim Lipka
- Zhisheng Qi
- Utkarsh Sahu
- Koustava Goswami
- Franck Dernoncourt
- Ryan A. Rossi
- Yu Wang
affiliations:
- University of Oregon
- Adobe Research
arxiv_id: '2606.16316'
url: https://arxiv.org/abs/2606.16316
pdf_url: https://arxiv.org/pdf/2606.16316
published: '2026-06-15'
collected: '2026-06-16'
category: RAG
direction: 索引侧推理优化 · RAG 性能提升
tags:
- reinforcement learning
- index reasoning
- GRPO
- RAG
- retrieval augmentation
- LLM
one_liner: 将检索推理从查询时移到索引阶段，用 GRPO 优化文档的理由生成，提升检索效果并降低在线延迟
practical_value: '- **离线预计算理由，降低在线延迟**：在商品搜索或推荐系统的索引构建中，可预先为每个文档/商品生成推理性的文本描述（rationale），将复杂推理从查询时转移到离线阶段，显著减少线上推理耗时。

  - **利用 GRPO 优化索引策略**：借鉴 RL-Index 使用 Group Relative Policy Optimization 直接以检索相似度作为奖励信号的方式，对商品内容生成模型进行策略优化，无需人工标注，自动提升召回或排序效果。

  - **即插即用，跨检索器泛化**：该方法生成的文档增强理由适用于多种 dense/sparse 检索器及生成模型，可作为一套标准化索引流程引入现有搜索/推荐系统，无需大幅改造原有架构。

  - **可解决复杂意图匹配**：对于电商中需逻辑推导的查询（如“送长辈的保健礼品”），可通过预先生成涵盖场景、知识点的理由，增强文档的语义覆盖，提升长尾查询的检索精度。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有 RAG 系统多在查询时进行推理（如 query rewriting），导致在线延迟高，且未能充分利用离线索引阶段的推理潜力。对于需要复杂推理的匹配（如数学、编程问题），仅靠表面语义检索不足。

**方法**：提出 RL-Index，将推理移至索引阶段。为每个文档生成一个理由（rationale），显式编码其能回答的隐含查询模式。采用 GRPO（Group Relative Policy Optimization）优化理由生成策略，直接使用检索相似度作为可验证的奖励信号，通过强化学习提升索引质量。训练时，对同一文档采样多个理由，分组比较奖励，以此更新策略模型。

**关键结果**：在 BRIGHT 基准上，检索召回率（如 Recall@10）与下游问答准确率均有显著提升，同时在线推理延迟降低。学习到的理由增强可泛化至不同检索器（如 BM25、dense retriever）和生成器，展示出强即插即用性。
