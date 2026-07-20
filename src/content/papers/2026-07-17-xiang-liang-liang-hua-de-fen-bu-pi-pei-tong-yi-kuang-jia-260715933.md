---
title: 'Distributional Matching for Vector Quantization: A Unified Theoretical and
  Empirical Framework'
title_zh: 向量量化的分布匹配统一框架
authors:
- Xianghong Fang
- Litao Guo
- Hengchao Chen
- Yuxuan Zhang
- XiaofanXia
- Dingjie Song
- Yexin Liu
- Hao Wang
- Harry Yang
- Qiang Sun
affiliations:
- University of Toronto
- The Hong Kong University of Science and Technology
- Boston College
- Lehigh University
- Southern University of Science and Technology
arxiv_id: '2607.15933'
url: https://arxiv.org/abs/2607.15933
pdf_url: https://arxiv.org/pdf/2607.15933
published: '2026-07-17'
collected: '2026-07-20'
category: GenRec
direction: 生成式推荐 · 向量量化优化
tags:
- vector quantization
- codebook collapse
- distribution matching
- Wasserstein distance
- training stability
one_liner: 通过分布对齐统一解决向量量化中的训练不稳定和码本坍塌
practical_value: '- 可将提出的分布匹配正则化（Wasserstein 或 MMD 损失）直接加入向量量化训练，解决 Semantic ID 生成中常见的码本利用率低问题。

  - 闭式近似（高斯假设下的 Wasserstein 距离）计算高效，适合在线推荐模型的训练管道集成。

  - 框架提供诊断现有 VQ 方法失效的统一视角，可从分布对齐角度改进量化过程的稳定性和码本利用率。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：向量量化（VQ）广泛用于生成式推荐（如 RQ-VAE 生成 Semantic ID）和视觉 tokenization，但长期面临训练不稳定和码本崩溃问题。本文指出根源在于特征向量与码向量之间的分布不匹配，导致梯度估计偏差和码字利用不足。

**方法关键点**：提出分布匹配框架，通过最小化特征分布与码向量分布的距离来对齐两者。具体实例化两种目标：基于 Wasserstein 距离的闭式近似（假设高斯分布）和非参数的最大均值差异（MMD）。这些正则化项可与标准 VQ 损失联合优化，无需改变量化前向过程。

**关键结果**：在视觉 tokenization 任务（ImageNet）上，该方法显著提升码本利用率和训练稳定性，重建质量与基线相当或更优，且对超参数不敏感。消融实验验证了分布匹配优于传统坍塌预防方法。
