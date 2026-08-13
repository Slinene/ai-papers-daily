---
title: 'Deciding When to Rely on Visual Information: Gated Multimodal Fusion in Sequential
  Recommendation'
title_zh: 决定何时依赖视觉信息：序列推荐中的门控多模态融合
authors:
- Natalija Glisovic
- Danica Kragic
- Martin Tegner
affiliations:
- IKEA Retail (Ingka Group)
- KTH Royal Institute of Technology
arxiv_id: '2608.10700'
url: https://arxiv.org/abs/2608.10700
pdf_url: https://arxiv.org/pdf/2608.10700
published: '2026-08-11'
collected: '2026-08-13'
category: RecSys
direction: 多模态序列推荐 · 自适应门控融合
tags:
- Multimodal
- Sequential Recommendation
- Gated Fusion
- Visual Utility
- Contrastive Learning
- Collaborative Filtering
one_liner: 提出 VisGate，通过门控机制逐项自适应融合视觉与协同信号，并分析视觉功效的上下文变化
practical_value: '- 在电商商品推荐中引入 item 级视觉门控，替代统一视觉融合。对视觉敏感度低的商品（如标准件、耗材）自动降低视觉权重，减少噪声；对非标品/时尚类增大权重，提升效果。

  - 冷启动与稀疏交互场景：当协同信号弱时，利用门控增强视觉信号，可改善新商品或长尾商品的推荐，因为论文验证了交互稀疏下视觉效用增加。

  - 视觉表征训练：采用序列共现对比学习而非简单对齐，可保持视觉与协同信号互补，提升融合有效性。可复用到多模态商品 embedding 训练。

  - 将学习到的门值作为可解释性/分析工具，辅助理解商品视觉特征对转化的贡献，指导选品、内容优化或特征裁剪。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态序列推荐通常统一融合视觉和协同信号，忽略 item 和用户上下文差异。视觉信息并非对所有 item 都同等有用，视觉效用应是随 item 和交互历史变化的潜在变量。

**方法关键点**：提出 VisGate，在 item 级做自适应融合决策，融合门控基于 item embedding 和用户当前序列上下文。视觉表征通过序列共现模式上的对比学习目标学习，保持与协同 embedding 的互补性，而非对齐到共享空间。框架以门控机制动态决定是否/多大程度依赖视觉信息。

**关键结果**：在推荐性能上达到 competitive，并利用学习到的门控作为测量工具，发现视觉效用跨 item 变化明显；交互稀疏时视觉效用增强，弥补协同信号不足；视觉效用与视觉独特性存在语义上有意义的相关性。证明细粒度融合和模态互补的重要性，并表明 item 级视觉效用可被估计和解释。
