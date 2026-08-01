---
title: 'DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented
  Generation'
title_zh: DualG-MRAG：解耦宏观推理与微观匹配的多模态检索增强生成
authors:
- Jiacheng Tao
- Qingyun Sun
- Haonan Yuan
- Ziwei Zhang
- Jianxin Li
affiliations:
- SKLCCSE, School of Computer Science and Engineering, Beihang University
arxiv_id: '2607.28580'
url: https://arxiv.org/abs/2607.28580
pdf_url: https://arxiv.org/pdf/2607.28580
published: '2026-07-30'
collected: '2026-08-01'
category: Multimodal
direction: 多模态RAG · 宏观-微观图解耦
tags:
- Multimodal RAG
- Graph Neural Networks
- Macro-Micro Graph
- Multi-hop Reasoning
- Query-driven Retrieval
- Dynamic Programming Decoding
one_liner: 双层次图框架解耦宏观拓扑推理与微观证据匹配，抑制多模态RAG中的检索噪声
practical_value: '- **宏观-微观图解耦架构**：可迁移到电商多模态知识图谱构建，宏观层建模商品、品类间拓扑关系，微观层存储细粒度属性（如颜色、材质），分开处理避免全局推理时被局部噪声干扰，同时保留精确匹配能力。

  - **查询驱动的GNN消息传递检索**：作为意图感知的多模态召回模块，以用户查询为起点在图上游走传播相关性，替代单纯向量相似度匹配，更适合需要多跳证据链的复杂推荐场景（如“适合户外旅行的轻便双肩包且防水”）。

  - **动态规划解码显式推理路径**：不再给LLM灌输零散文档块，而是提取“图片A→属性B→场景C”的结构化路径，可提升生成式推荐或问答的可解释性，便于业务调试与用户信任。

  - **细粒度视觉特征的层级使用**：微观图保留局部视觉证据，宏观图仅用粗粒度表示，避免图规模爆炸；在商品搜索中可对详情图做类似分层，平衡效率与精度。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有多模态RAG方法在复杂多跳推理任务中，要么仅做实例级独立匹配，忽略跨模态、跨文档的显式关系；要么引入图结构建模，但若融入细粒度视觉特征则导致图急剧膨胀和检索噪声，若使用粗粒度表示又会丢失关键局部证据，形成两难。

**方法**：提出双层次解耦框架DualG-MRAG，构建**宏观图（Macro Graph）**进行全局拓扑路由，抑制检索噪声；**微观图（Micro Graph）**保留细粒度局部证据，实现精确验证。检索被建模为查询驱动的GNN消息传递过程，在图节点间动态传播相关性。此外，设计**动态规划解码机制**，直接从GNN前向传播中提取结构化的显式推理路径，将其作为生成模型的输入，取代传统的孤立文档块。

**结果**：在多模态多跳QA数据集上，DualG-MRAG在证据召回率和复杂问答准确率上均超越现有基线方法，验证了解耦架构能有效权衡全局推理与局部匹配。
