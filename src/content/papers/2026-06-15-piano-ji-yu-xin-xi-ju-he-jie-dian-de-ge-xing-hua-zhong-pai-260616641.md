---
title: 'PIANO: Personalized Reranking via Information Aggregation Node for Music Search
  Optimization'
title_zh: PIANO：基于信息聚合节点的个性化重排序优化音乐搜索
authors:
- Weisheng Li
- Chuqiao Huang
- Pengcheng Li
- Zhengchao Peng
- Qiang Xiao
- Zhongqian Xie
- Qiang Huang
- Chuanjiang Luo
affiliations:
- NetEase Cloud Music
arxiv_id: '2606.16641'
url: https://arxiv.org/abs/2606.16641
pdf_url: https://arxiv.org/pdf/2606.16641
published: '2026-06-15'
collected: '2026-06-16'
category: RecSys
direction: 个性化重排序 · 列表级多目标优化
tags:
- personalized reranking
- listwise reranking
- multi-objective optimization
- cross-attention
- information aggregation node
- music search
one_liner: 引入历史查询交叉注意力与列表级聚合Token，实现列表级多目标重排序，显著提升CTR/CVR
practical_value: '- **历史查询兴趣精炼**：电商搜索中，用户历史搜索 query 包含丰富意图，可借鉴 QDIR 的交叉注意力机制，将当前 query
  与历史 query 序列显式对齐，过滤无关偏好，提升重排序的相关性。

  - **列表级多目标预估**：用可学习的 [CLS]-style token（IAN）聚合候选列表特征，直接预测整列表的 CTR/CVR 联合分布，而非逐物品
  trade-off，适合需要在列表层面平衡点击和转化的推荐场景。

  - **端到端重排序架构**：PIANO 将精炼的兴趣向量和物品特征一起送入 IAN，输出列表级分数，可作为排序模型的后置模块集成到现有管线，改动成本低。

  - **多目标优化在搜索广告的迁移**：在广告系统中，同时优化 CTR 和 CVR 时，可以尝试引入列表级聚合预测，让模型学习列表级的最优展示组合，避免局部物品级平衡导致整体效率下降。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：音乐搜索需同时对齐用户当前查询意图和长期偏好，并联合优化 CTR 与 CVR。现有序列模型依赖物品交互历史，无法利用历史搜索 query 校准意图；且多目标优化仅在物品级进行，忽略列表整体的 trade-off。

**方法关键点**：提出 PIANO 个性化列表级重排序框架，包含两个核心组件：
- **Query-Driven Interest Refiner (QDIR)**：利用交叉注意力，让当前 query 匹配历史查询序列，精炼出与当前意图对齐的用户长期偏好。
- **Information Aggregation Node (IAN)**：一个可学习的 [CLS] 风格 token，在序列输入前插入，经过多层交互后聚合候选列表的全部信息，直接输出列表级 CTR 和 CVR 预测，实现列表级多目标优化。

**关键结果**：在公开数据集和网易云音乐工业环境验证，在线 A/B 测试取得 CTR +0.62%、CVR +4.45% 的显著提升，证实了历史查询利用和列表级多目标预估的有效性。
