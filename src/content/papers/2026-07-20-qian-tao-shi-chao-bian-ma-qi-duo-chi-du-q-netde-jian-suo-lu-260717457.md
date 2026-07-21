---
title: The Matryoshka Hypencoder
title_zh: 嵌套式超编码器：多尺度Q-Net的检索效率优化
authors:
- Majd Alkawaas
- Sean MacAvaney
affiliations:
- University of Glasgow
arxiv_id: '2607.17457'
url: https://arxiv.org/abs/2607.17457
pdf_url: https://arxiv.org/pdf/2607.17457
published: '2026-07-20'
collected: '2026-07-21'
category: Other
direction: 检索效率优化 · 嵌套式表示学习
tags:
- Hypencoder
- Matryoshka Embeddings
- Retrieval Efficiency
- Q-Net
- HyperNetwork
- Trade-off
one_liner: 提出支持多种Q-Net大小的Matryoshka Hypencoder，域内参数减少7倍，吞吐提升1.6-3.4倍。
practical_value: '- **动态Q-Net大小切换**：在推荐系统的召回或粗排阶段，借鉴嵌套式Q-Net思想，根据服务时延要求或流量压力，在线灵活裁剪Q-Net的隐藏层维度，在不改变模型结构的前提下实现效果-效率的动态折衷。

  - **预计算物品嵌入 + 轻量查询网络**：将Hypencoder架构迁移到召回：离线预计算所有物品的向量表示，在线仅用HyperNetwork为当前用户/查询生成一个小型评分网络，替代固定相似度函数，提升表达能力的同时保持低在线计算开销。

  - **多尺度联合训练**：在训练时同时优化多个嵌套大小的Q-Net，可让一个模型支持多种精度档位，避免为不同性能目标维护多个模型，简化部署和AB实验。

  - **适用于Agent调用的检索组件**：当LLM Agent需实时检索知识库或商品库时，可采用此种高吞吐且可调节精度的检索器，通过调整Q-Net大小匹配Agent对延迟和精度的即时需求。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Hypencoder利用超网络为每个查询生成一个轻量的浅层神经网络（Q-Net），对预计算的文档嵌入进行相关性打分，比传统内积或余弦相似度具有更强的表达力，但较大的Q-Net会带来较高的计算开销。受Matryoshka表示学习启发，希望在同一框架内支持多种大小的Q-Net，以在不同部署场景下灵活平衡效果与效率。

**方法关键点**：提出Matryoshka Hypencoder，在训练时同时对多个嵌套的Q-Net大小（例如隐藏层维度为512、256、128等）进行优化，通过对较大Q-Net施加排序损失，使较小Q-Net也能继承其排序能力；推理时可直接通过截取部分参数切换到更小的Q-Net，无需重新训练或额外适配。

**关键结果**：在域内retrieval任务上，使用约1/7的活跃参数即可达到与完整Q-Net近似的效果；域外任务仅需一半参数即保持同等效果。评分吞吐量相应提升1.6–3.4倍，显著改善了Hypencoder的实用部署可行性。
