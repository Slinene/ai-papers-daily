---
title: 'FedHUR: Learning Hierarchical Utility-Guided Client Relations for Personalized
  Federated Recommendation'
title_zh: FedHUR：学习层次化效用引导的客户端关系用于个性化联邦推荐
authors:
- Mingzhe Han
- Jiahao Liu
- Dongsheng Li
- Jiankui Zhou
- Hansu Gu
- Peng Zhang
- Ning Gu
- Tun Lu
affiliations:
- Fudan University
- Microsoft Research Asia
- Independent
arxiv_id: '2609.11632'
url: https://arxiv.org/abs/2609.11632
pdf_url: https://arxiv.org/pdf/2609.11632
published: '2026-09-10'
collected: '2026-09-11'
category: RecSys
direction: 联邦推荐 · 个性化聚合
tags:
- Federated Learning
- Personalized Aggregation
- Hierarchical Clustering
- Utility Signals
- Collaborative Filtering
one_liner: 提出层次化效用引导的客户端关系学习框架，以 item-item filters 为聚合对象，提升联邦推荐个性化聚合效果
practical_value: '- 在电商推荐场景中联邦学习保护用户隐私，但跨客户端聚合时不应依赖单一全局相似度；可借鉴 FedHUR 思路，按类目/品牌/价格带等构建层次化用户关系，在不同粒度上分别聚合，缓解数据稀疏和兴趣差异问题。

  - 效用信号机制值得直接移植：让每个客户端先评估其他客户端信息对自己预测的增益，只聚合“有用”的客户端，避免引入噪声；这类似推荐系统中的增益筛选，可显著提升本地模型在长尾用户上的表现。

  - 以 item-item filters（如物品共现矩阵或物品向量）作为交换和聚合对象，比直接交换模型参数更轻量、可解释，适合部署在边缘设备或对通信开销敏感的场景；电商中可用商品
  embedding 的 item-item 关系替代原始梯度。

  - 全局层次聚类信息可以作为先验知识下发到客户端，再在客户端上进行个性化检索和聚合，这种“全局先验+本地效用”的架构可直接应用于大规模推荐模型的分布式微调或联邦增量训练。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：联邦推荐的核心挑战是如何跨客户端聚合有用信息实现个性化。现有方法通常基于预先定义的参数相似度或互补性构建单一的客户端关系，再据此确定聚合权重。这类方法存在两个缺陷：一是单一全局关系无法刻画推荐中用户关系的层次多粒度特性；二是预先定义的关系无法直接反映聚合后是否真正提升预测性能。

**方法关键点**：论文提出 FedHUR 框架，以 item-item filters 作为关系构建和聚合的对象。具体流程为：服务器首先聚合各客户端本地信息并进行聚类，得到全局层次化信息；每个客户端基于本地信息和全局层次信息计算层次化效用信号，指示哪些协作信息对提升自身预测有用；服务器利用这些效用信号检索对该客户端有用的其他客户端，进行个性化聚合。该方法不依赖固定的参数相似度假设，而是直接从预测增益角度学习客户端间的关系。

**关键结果**：在五个真实世界数据集上的实验表明，FedHUR 一致优于现有联邦推荐基线，验证了层次化效用引导的客户端关系学习在个性化联邦推荐中的有效性。
