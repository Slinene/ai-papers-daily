---
title: Toward Calibrated Mixture-of-Experts Under Distribution Shift
title_zh: 分布偏移下校准混合专家模型
authors:
- Gina Wong
- Drew Prinster
- Suchi Saria
- Rama Chellappa
- Anqi Liu
affiliations:
- Johns Hopkins University
arxiv_id: '2606.20544'
url: https://arxiv.org/abs/2606.20544
pdf_url: https://arxiv.org/pdf/2606.20544
published: '2026-06-18'
collected: '2026-06-19'
category: Training
direction: 分布偏移下 MoE 校准
tags:
- Mixture-of-Experts
- Calibration
- Distribution Shift
- Adversarial Reweighting
- Soft Routing
- Hard Routing
one_liner: 证明硬路由 MoE 的专家级校准在分布偏移下仍能保证全局校准，而软路由不成立，并提出对抗重加权提升校准-准确率权衡
practical_value: '- 推荐/广告系统常面临分布偏移（促销、季节、新用户群），使用 MoE 结构时可直接借鉴本文结论：硬路由下只需校准各专家即可保证整体概率可靠性，工程实现更轻量。

  - 若业务需软路由以获取更平滑的专家组合，可用提出的对抗重加权损失（惩罚偏移下的路由聚合校准误差）微调模型，尤其适合高价值子集（高消费用户、长尾物品）上的概率估计优化。

  - 广告出价、CTR 预估对概率校准极其敏感，该方法在不牺牲精度的前提下提升 ECE，可直接集成到训练 pipeline 中，作为辅助损失项。

  - 在 Agent 多智体或任务路由场景，不同专家处理不同意图/域，分布偏移常见，本文的理论分析和训练技巧可指导路由策略选择与校准保障。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：MoE 在大规模系统中广泛使用，但其在分布偏移下的校准行为尚不明确。个体专家校准能否保证整体模型校准？软/硬路由有何差异？

**方法关键点**：理论分析表明，对于硬路由（top-1 指派），只要每个专家在各自负责的输入区域上校准，就足以保证整体模型在任意分布偏移下校准；而软路由（概率加权组合）下，专家校准不能自动保证全局校准，因为路由权重本身可能引入校准偏差。基于此，提出**对抗重加权**方法：在训练中引入一个对抗分布的样本权重，该权重放大当前模型在路由聚合后校准误差最大的区域，从而驱动模型在分布偏移下仍保持良好校准。损失函数在原任务损失上增加该项惩罚，可以端到端训练。

**关键结果**：在图像分类、文本分类等任务及多种分布偏移（逐类偏移、协变量偏移）下，对抗重加权方法在保持精度的同时显著降低期望校准误差（ECE），尤其在困难子集上改善明显，且对 MLP、ResNet、Transformer 等多种模型结构均有效。
