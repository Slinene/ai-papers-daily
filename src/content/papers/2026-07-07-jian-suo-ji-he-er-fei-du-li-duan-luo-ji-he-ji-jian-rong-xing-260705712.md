---
title: 'Retrieving a Set, Not Independent Passages: Set-Level Compatibility Learning
  for Efficient Set Exploration'
title_zh: 检索集合而非独立段落：集合级兼容性学习实现高效集合探索
authors:
- Mooho Song
- Jay-Yoon Lee
affiliations:
- Seoul National University
arxiv_id: '2607.05712'
url: https://arxiv.org/abs/2607.05712
pdf_url: https://arxiv.org/pdf/2607.05712
published: '2026-07-07'
collected: '2026-07-08'
category: RAG
direction: 集合级检索 · 多跳推理
tags:
- multi-hop retrieval
- set-level compatibility
- late-interaction
- cross-encoder
- efficient set exploration
- RAG
one_liner: 将多跳检索建模为查询-集合兼容性评分，用轻量自注意力和交叉编码器联合学习集合兼容性
practical_value: '- **组合证据检索思路**：在需要多个协同信息源的任务（如电商问答、客服多轮、Agent 工具调用）中，不要独立对每个文档/物品打分，而应评估集合级别的兼容性，避免局部最优导致的冲突或冗余。可借鉴
  ParaSet 的轻量集合打分方式，在 bi-encoder 编码的向量上引入自注意力，高效评估候选集合的整体相干性。

  - **训练目标迁移**：将“完整兼容集合 > 残缺/噪音集合”的排序损失引入学习排序（LTR），可用于搭配推荐（如服装组合）、多创意组合评估等场景，让模型学会全局最优组合而非单物品最优。

  - **异构检索器互补**：ParaSet（快速探索）与 SetCE（精确重排）的组合效果优于单一检索器的更多召回，启发我们在多路召回融合中，有意识设计互补的检索器（如语义匹配
  vs. 协同过滤），通过合并输出而非简单增加单个检索器的数量来提升效果。

  - **工程实现参考**：ParaSet 在预计算好的段落向量上做自注意力，无需重新编码，非常适合对延迟敏感的在线集合探索；类似思路可用于实时推荐中，对召回的物品集合基于已缓存
  embedding 做兼容性快速打分。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：多跳问答和检索增强推理需要选择一组协同有用的证据段落，而现有检索器大多独立打分或局部序列决策，无法建模段落间的兼容性。LLM 可一次性选择整个集合但计算成本过高。

**方法**：将多跳检索形式化为查询-集合兼容性评分，提出训练目标让模型将完整兼容的证据集排在残缺或含噪音的集合之上，使集合评分对变长和部分噪音鲁棒。基于该框架设计了两个互补的集合打分器：
- **ParaSet**：轻量级 late-interaction 打分器，在预计算的 bi-encoder 嵌入上应用自注意力，快速评估候选集合的兼容性，适合大规模候选探索。
- **SetCE**：交叉编码器重排器，使用相同的集合级目标训练，更精确地建模跨段落交互。

**结果**：在多个多跳 QA 基准上，集合级兼容性学习显著提升检索和下游问答性能。集合级检索器不仅优于传统文档级检索器，且二者输出互补：合并 ParaSet 与 SetCE 的结果，性能强于简单地从文档级检索器获取更多段落。
