---
title: 'Entropy Across the Bridge: Conditional-Marginal Discretization for Flow and
  Schrödinger Samplers'
title_zh: 跨越桥梁的熵：流与薛定谔采样器的条件边际离散化
authors:
- Bruno Trentini
- Dejan Stancevic
- Michael M. Bronstein
- Alexander Tong
- Luca Ambrogioni
affiliations:
- NVIDIA Corporation
- University of Oxford
- Radboud University
- AITHYRA
arxiv_id: '2605.16126'
url: https://arxiv.org/abs/2605.16126
pdf_url: https://arxiv.org/pdf/2605.16126
published: '2026-05-15'
collected: '2026-05-18'
category: Other
direction: 流匹配与桥采样的推理步调度
tags:
- flow matching
- Schrödinger bridge
- entropy rate
- discretization
- low-NFE inference
- sampling
one_liner: 提出条件边际熵率调度，无训练地实现低步数流匹配与桥采样的边界重非均匀步分配，显著改善生成质量
practical_value: '- 在低 NFEs 的流匹配/扩散推荐模型（如 Semantic ID 生成）中，可尝试边界重的非均匀采样步长，取代均匀或启发式分步，几乎零成本提升生成质量。

  - 熵率调度训练无关，只需根据条件熵估计或桥的闭式解（如高斯假设）调整时间网格，易部署到现有模型。

  - 电商场景中的商品图生成或分子生成，类似低步数优化可直接复用，将步数优先分配在起始和结束阶段。

  - 方法将边际与条件解耦，为设计更高效的生成式推荐解码器（如去噪扩散推荐）提供理论借鉴。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：流匹配与薛定谔桥模型在低函数评估次数（NFE）下，采样质量高度依赖离散网格，而现有网格多为启发式，未考虑桥的动态。

**方法**：提出条件边际熵率目标，解耦端点条件桥几何与边际流演化，导出训练无关的熵推理时间调度器。对高斯布朗桥，熵率呈闭式U形，驱使非均匀网格将更多步放在边界附近。

**结果**：在2D桥/流模型上，10步ODE-Heun MMD相比线性提升18.1%，SDE-Heun提升22.7%；CIFAR-10 EDM五步FID达186.3（线性200.5，余弦238.0）；AlphaFlow蛋白质生成在低NFE下CAMEO22和ATLAS基准均获提升。
