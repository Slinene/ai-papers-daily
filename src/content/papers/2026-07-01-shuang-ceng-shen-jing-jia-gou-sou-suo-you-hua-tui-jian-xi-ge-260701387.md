---
title: 'Bi-NAS: Towards Effective and Personalized Explanation for Recommender Systems
  via Bi-Level Neural Architecture Search'
title_zh: 双层神经架构搜索优化推荐系统个性化解释
authors:
- Longfeng Wu
- Yao Zhou
- Tong Zeng
- Zhimin Peng
- Bhanu Pratap Singh Rawat
- Lecheng Zheng
- Giovanni Seni
- Dawei Zhou
affiliations:
- Virginia Tech
- Google
- Amazon
arxiv_id: '2607.01387'
url: https://arxiv.org/abs/2607.01387
pdf_url: https://arxiv.org/pdf/2607.01387
published: '2026-07-01'
collected: '2026-07-04'
category: RecSys
direction: 可解释推荐 · 神经架构搜索
tags:
- Explainable Recommendation
- Neural Architecture Search
- LLM
- Personalization
- Cross-Attention
one_liner: 通过双层NAS同时优化注意力与特征交互，并集成LLM生成个性化推荐解释，提升准确性与解释质量
practical_value: '- 将NAS用于搜索推荐解释模型的最优结构，自动设计特征交互与注意力机制，避免手工调参。

  - 利用LLM零样本提示生成解释，结合用户特征偏好与物品属性对齐，可快速实现个性化推荐理由。

  - 双层搜索空间（intra-layer和inter-layer）可迁移到电商推荐中优化多模态特征融合的解释头。

  - 该方法在提升推荐准确度的同时改善解释质量，适用于商品详情页的“为什么推荐”模块，提升点击率和信任度。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：推荐系统亟需有效且个性化的解释来增强用户信任与决策，但手工设计最优解释模型结构困难，且现有方法难以灵活适配多变场景。

**方法**：提出双层神经架构搜索框架 Bi-NAS，同时优化解释模块的**层内设计**（交叉注意力机制类型）和**层间设计**（特征交互函数连接方式），自动发现高效结构。在此基础上，集成大语言模型（LLM），通过零样本提示将**用户特征偏好**与**物品质量分数**对齐，生成个性化自然语言解释。

**结果**：在四个真实数据集上，Bi-NAS 不仅提升推荐准确率，还显著提高解释有效性（如解释相关性、用户满意度等），整体框架同时兼顾精度与可解释性。
