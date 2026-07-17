---
title: Mutable Low-Rank Sketches for Retrain-Free Recommendation
title_zh: 可变低秩草图：免重训的实时推荐
authors:
- Hector J. Garcia
- Nick Clayton
affiliations:
- University of Michigan
- Criteo
arxiv_id: '2607.15242'
url: https://arxiv.org/abs/2607.15242
pdf_url: https://arxiv.org/pdf/2607.15242
published: '2026-07-16'
collected: '2026-07-17'
category: RecSys
direction: 实时推荐 · 嵌入鲜活性
tags:
- Mutable Sketches
- KP-tree
- Low-rank Projection
- Embedding Freshness
- Collaborative Filtering
one_liner: 用KP-tree存储用户偏好，固定低秩投影，新评分到达时动态更新嵌入，无需重训
practical_value: '- 将用户特征更新与模型重训解耦：固定低秩投影，只在线更新KP-tree中的用户偏好向量，实现实时推荐，避免频繁重训大模型

  - KP-tree支持对数时间点更新和内部求和传播，适合电商场景中用户行为实时流入时的低延迟嵌入计算（<1ms）

  - 稀疏数据场景下采用范数比例采样替代均匀采样，可显著提升物品覆盖率（40–130%），改善冷启动和新颖度

  - 整体框架简单：一次离线学习低秩基矩阵，在线部分只需维护带有聚合统计的树结构，工程实现复杂度低，便于集成到现有特征平台'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：两阶段推荐中用户嵌入在重训前保持固定，导致“陈旧性”。即使增量方法（eALS、FunkSVD）也直接修改分解，耦合数据鲜活性与模型重算。

**方法**：提出可变草图。每个用户的偏好向量存储在**KP-tree**（稀疏段树，支持求和聚合）中，拟合一个**低秩投影**并固定。当新评分到达时，在对数时间内插入树中更新偏好向量，再通过固定低秩基矩阵即时重新计算用户嵌入，无需梯度计算、不触碰模型参数。插入时传播内部求和，保持采样分布一致，支持随时基于当前状态重建草图。

**理论**：证明每个新观测单调收紧预测误差包络（定理1），这是FunkSVD和eALS等缺乏的保证。

**结果**：在KuaiRec上，可变草图仅读取1.8%数据即达到RMSE 0.810，优于ALS的0.822（读取100%数据），批次更新速度快8倍。新用户首次评分后<1ms即可获得个性化推荐。稀疏数据（密度<1%）下，KP-tree的范数比例采样比均匀采样提高40–130%的物品覆盖率。
