---
title: 'The Magnitude Mirage: Rethinking Confidence for Reasoning-Intensive Retrieval'
title_zh: 量级幻象：重新思考推理密集型检索中的置信度
authors:
- Jamie Holdcroft
- Abdelrahman Abdallah
- Adam Jatowt
affiliations:
- UNSW Sydney
- University of Innsbruck
arxiv_id: '2609.15578'
url: https://arxiv.org/abs/2609.15578
pdf_url: https://arxiv.org/pdf/2609.15578
published: '2026-09-14'
collected: '2026-09-16'
category: RAG
direction: RAG 检索置信度与拒答优化
tags:
- RAG
- Retrieval Abstention
- Confidence Estimation
- Query Performance Prediction
- Score Distribution
- Magnitude Mirage
one_liner: 发现相似度分数大小在逻辑/时间推理查询中失效，提出零成本的分数分布信号可显著提升检索拒答 AUROC
practical_value: '- 在电商/客服/广告的 RAG 场景中，不要用原始相似度分数阈值做检索拒答；直接计算 top-1 与 top-k 的 Score
  Gap（s1 - sk）或 LSMV（局部分数均值与方差），零成本替换 magnitude thresholding。

  - 对于需要逻辑/时间约束的查询（如“价格低于500且评分4.5以上的红色连衣裙”），语义相似度分数会误导置信度判断，必须引入分数分布信号，否则拒答策略接近随机。

  - 工程实现上，只需在召回后保留 top-k 的分数向量，在线计算 gap / variance，无需额外推理或模型加载；可先离线在 reasoning-intensive
  查询集上验证 AUROC，再决定是否上线。

  - 评估检索器或 RAG 流水线时，除了 recall/NDCG，建议加入基于分布信号的 abstention AUROC，尤其在逻辑、时间推理类查询上，能暴露
  magnitude 指标的盲区。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
生产级 RAG 系统通常用相似度分数的阈值来做检索拒答，暗含“分数大小≈置信度”。但在需要逻辑推理或时间推理的查询中，这种实践会系统性失效：神经检索器会给语义相关但违反约束的文档打高分，导致基于分数大小的拒答接近随机，称为 Magnitude Mirage。

**方法关键点**  
在 11 种检索架构、28 个数据集上，覆盖三类认知层级：语义匹配（BEIR）、逻辑推理（BRIGHT）、时间推理（TEMPO）。系统对比六种零成本 Query Performance Prediction（QPP）指标，核心是从“分数大小”转向“分数分布信号”。重点指标包括 Score Gap（s1 - sk）和 LSMV（局部分数均值与方差的实用适配）。

**关键结果数字**  
放弃 magnitude、改用 distribution 信号后，abstention AUROC 最高提升 0.16；该收益主要来自从大小到分布的切换，分布指标之间的差异仅为该收益的 1/5 到 1/10。这些方法不需要额外推理、重训练或增加延迟，可直接作为部署中 magnitude thresholding 的零成本替代。
