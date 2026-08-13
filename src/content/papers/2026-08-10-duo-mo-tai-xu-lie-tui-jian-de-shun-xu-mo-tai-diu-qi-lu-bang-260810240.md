---
title: Sequential Modality Dropout for Robust Multi-Modal Sequential Recommendation
title_zh: 多模态序列推荐的顺序模态丢弃鲁棒性方法
authors:
- Guanqun Yang
- Wenlong Zhang
affiliations:
- Stevens Institute of Technology
arxiv_id: '2608.10240'
url: https://arxiv.org/abs/2608.10240
pdf_url: https://arxiv.org/pdf/2608.10240
published: '2026-08-10'
collected: '2026-08-13'
category: RecSys
direction: 多模态序列推荐鲁棒性
tags:
- Multi-modal
- Sequential Recommendation
- Dropout
- Robustness
- Modality Missing
one_liner: 训练时整段历史独立擦除单模态，让多模态序列推荐在模态缺失时保持 HR@10 精度
practical_value: '- 电商多模态序列模型（如商品图+标题描述）常遇到无图/无文本；可直接将 SMD 作为训练时模态 dropout：对每个 batch，以概率
  p 对某模态在整条用户序列上置 0/掩码，让模型不依赖单一模态，实现仅需数行。

  - 线上部署前用 retention 指标评估模态缺失下 HR@10 的保留比例，而非只看全模态准确率；设定服务等级，例如文本缺失时至少保留 90% 才允许上线。

  - 若主模型为简单加和融合（additive backbone），可额外加 cross-modal reconstruction loss，把极端缺失下的 retention
  从 90% 提升到 98%；对于复杂交互融合模型也可尝试但需验证。

  - 生产数据中物品缺失比例高（如 Beauty 类文本缺失 48%），应模拟训练时高缺失率（p=0.9+）以贴近真实；SMD 在 95% per-item missing
  下仍保留 61% HR@10，而未做仅 22%。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

动机：多模态序列推荐通常假设所有物品具备完整图文，但电商真实目录中大量商品缺文本或图片；模型在完整数据上训练后，线上模态缺失时 HR@10 显著下降。

方法：提出 Sequential Modality Dropout（SMD），训练时对每条用户历史独立地以概率 p 抹除图像或文本整个模态流，使模型学会不依赖任一单模态；可选 cross-modal reconstruction loss 进一步增强。

结果：在 4 个 Amazon 域、4 个骨干上，SMD 将文本保留率提升 1.0–3.2×，且完整模态精度几乎不损失；95% 逐物品缺失下保留 61% HR@10（无 SMD 22%）；可选重建 loss 在简单加和骨干上把保留率从 90% 提到 98%。
