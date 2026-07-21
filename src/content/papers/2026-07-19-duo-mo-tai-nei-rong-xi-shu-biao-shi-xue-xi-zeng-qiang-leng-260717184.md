---
title: Learning Sparse Representations of Multimodal Content for Enhanced Cold Item
  Recommendation
title_zh: 多模态内容稀疏表示学习增强冷启动物品推荐
authors:
- Gregor Meehan
- Johan Pauwels
affiliations:
- Queen Mary University of London
arxiv_id: '2607.17184'
url: https://arxiv.org/abs/2607.17184
pdf_url: https://arxiv.org/pdf/2607.17184
published: '2026-07-19'
collected: '2026-07-21'
category: RecSys
direction: 稀疏表示学习 · 内容冷启动
tags:
- cold-start
- sparse embeddings
- multimodal
- content-based recommendation
- linear attention
- embedding compression
one_liner: 用稀疏嵌入替代稠密向量，以更低存储成本显著提升内容冷启动推荐准确性
practical_value: '- 冷启动物品直接用多模态内容（图片、文本）生成稀疏嵌入，无需交互历史，可无缝用于电商 / 广告新品推荐。

  - 稀疏嵌入显著降低存储成本（大幅压缩向量维度），并支持高效近似近邻检索，适合大规模商品目录。

  - 借鉴预稀疏化激活技术（基于线性注意力），可以增强物品间相似度的尖锐性和去噪效果，让稀疏表示更具判别力。

  - 稀疏性天然利于可解释推荐：非零维度可对应具体内容语义，方便向广告主解释为何推荐该物品。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：大规模目录中物品冷启动是推荐系统的关键难题，利用图像、文本等辅助内容生成冷物品表示是主流方案，但传统稠密嵌入存储开销大、检索延迟高。

**方法**：将稀疏表示学习引入内容冷启动范式，基于线性注意力设计一种预稀疏化激活函数（pre-sparsification activation），在训练时对相似度施加稀疏性约束，同时保留内容语义。该激活诱导相似度矩阵更尖锐且具备去噪效果，最终产出可解释的稀疏物品嵌入。

**结果**：在四个多模态推荐数据集上，稀疏嵌入的冷启动推荐准确率（Recall@20/50、NDCG）显著超越稠密基线，存储成本降低最高达 80%；尤其对多兴趣用户提升明显。同时，稀疏维度可追踪至具体内容特征，提供天然可解释性，且在空间与精度权衡中更鲁棒。
