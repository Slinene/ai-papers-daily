---
title: Unsupervised Data-Efficient Cross-Modal Retrieval with Global-Neighborhood
  Alignment Hashing
title_zh: 无监督数据高效跨模态检索：全局邻域对齐哈希
authors:
- Runhao Li
- Xiaoxu Ma
- Zhenyu Weng
- Yue Zhang
- Guibo Luo
- Huiping Zhuang
- Zhiping Lin
- Yap-Peng Tan
affiliations:
- Nanyang Technological University
- South China University of Technology
- Henan Normal University
- Peking University Shenzhen Graduate School
- VinUniversity
arxiv_id: '2606.31517'
url: https://arxiv.org/abs/2606.31517
pdf_url: https://arxiv.org/pdf/2606.31517
published: '2026-06-30'
collected: '2026-07-06'
category: Multimodal
direction: 跨模态哈希 · 数据高效对齐
tags:
- cross-modal hashing
- data-efficient
- unsupervised learning
- vision-language model
- prototype alignment
- stochastic neighborhood
one_liner: 仅用少量图文对，通过原型全局对齐与随机邻域对比学习，将视觉–语言大模型语义结构压缩为二进制哈希码
practical_value: '- 在电商商品多模态检索中，可利用少量商品图文对训练哈希映射，大幅降低向量存储和检索成本，适合移动端或边缘设备部署。

  - 原型锚定全局对齐思想可迁移到推荐系统的多模态特征融合，通过维护类别原型保持哈希空间全局语义结构，缓解小样本特征坍塌。

  - 对比随机邻域对齐建模随机邻域关系，可缓解正负样本稀疏问题，在推荐中用于增强用户–物品交互图的表征学习，提升冷启动物品的语义索引质量。

  - 从视觉–语言基础模型（如 CLIP）蒸馏哈希码的方法，可借鉴用于冷启动物品的快速二进制语义 ID 生成，加速召回并降低在线存储开销。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有无监督跨模态哈希方法依赖大规模图文对，数据采集成本高，限制了实际应用。本文提出 Global‑Neighborhood Alignment Hashing (GNAH)，在少量图文对条件下保留视觉–语言基础模型的语义结构，学习紧凑二进制哈希码。

**方法**：关键设计包括两个模块：① **原型锚定全局对齐**（Prototype‑Anchored Global Alignment）：从连续空间中提取类别原型，将其作为锚点传递全局语义结构到汉明空间，保证哈希码的整体判别性。② **对比随机邻域对齐**（Contrastive Stochastic Neighborhood Alignment）：在传统对比学习基础上，为每个样本随机采样邻域点建模分布关系，缓解对稀疏成对相关性的过拟合，使哈希码捕获更丰富的局部结构。

**结果**：在多个跨模态检索基准上，数据受限设置下 GNAH 一致超越现有无监督方法（如 Flickr30K、MS COCO 上的召回率显著提升），验证了其数据高效性和实际部署价值。
