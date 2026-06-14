---
title: 'MLT-Dedup: Efficient Large-Scale Online Video Deduplication via Multi-Level
  Representations and Spatial-Temporal Matching'
title_zh: MLT-Dedup：基于多级表示与时空匹配的大规模在线视频去重
authors:
- David Yuchen Wang
- Haoying Li
- Hailun Xu
- Wei Chee Yew
- Zirui Zhu
- Sanjay Saha
- Hao Hei
- Kanchan Sarkar
- Kun Xu
affiliations:
- TikTok
- National University of Singapore
arxiv_id: '2606.12215'
url: https://arxiv.org/abs/2606.12215
pdf_url: https://arxiv.org/pdf/2606.12215
published: '2026-06-10'
collected: '2026-06-14'
category: Other
direction: 大规模视频去重 · 多级表示与时空匹配
tags:
- video deduplication
- multi-level embeddings
- spatial-temporal matching
- efficient retrieval
- near-duplicate detection
- large-scale
one_liner: 多级表示联合时空匹配，显著降低线上重复率并提升索引容量5倍
practical_value: '- **多级表示与分级匹配范式可迁移至推荐去重**：用轻量级稀疏 Embedding 快速召回候选重复商品/内容，再加载精细 Embedding
  做高精度比对，平衡效率与精度，适合大规模推荐流中实时去重。

  - **DiF-SiM 相似度模块可用于内容理解**：差异增强相似度能定位局部重复片段，可借鉴到视频/直播切分、片段检索或商品主图去背景后相似度判定，提高变体识别鲁棒性。

  - **稀疏检索设计提升索引容量**：用低维稀疏向量构建索引，容量翻倍，对于推荐系统里海量物品指纹索引（如向量召回库）有直接参考价值，可降低索引内存，扩大候选集覆盖。

  - **在线去重决策框架**：结合业务策略（容忍度、时间窗口）与相似度证据的脱耦设计，可直接移植到电商推荐中的内容质量治理、重复商品惩罚或去重策略配置。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：UGC 视频大规模出现近似重复内容，损害用户体验并增加存储带宽成本。现有去重方案受限于索引预算不足与效率-精度权衡，难以及时覆盖海量候选。

**方法**：提出 MLT-Dedup 框架，包含两个核心组件：1）多级视频编码器（ML-VE），同时提取细粒度帧级 Embedding 与稀疏片段级 Embedding；2）DiF-SiM 相似度模块，通过差异特征增强时空匹配，精准定位重复时间片段并提供可靠相似度证据。在线流程中，稀疏 Embedding 负责高效候选检索，仅召回少量候选后加载帧级 Embedding 精确匹配，大幅降低匹配开销；DiF-SiM 输出可配置的相似度边界支撑业务决策。

**结果**：在真实大规模平台的线上 A/B 实验中，MLT-Dedup 在 90% 精度下将重复率相对降低 91%，稀疏检索设计将索引容量提升 5 倍，有效支撑全量候选覆盖，实现业务落地。
