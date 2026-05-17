---
title: 'To discretize continually: Mean shift interacting particle systems for Bayesian
  inference'
title_zh: 基于均值漂移交互粒子系统的贝叶斯推断离散化方法
authors:
- Ayoub Belhadji
- Daniel Sharp
- Youssef M. Marzouk
affiliations:
- Center for Computational Science and Engineering, Massachusetts Institute of Technology
- Laboratory for Information and Decision Systems, Massachusetts Institute of Technology
arxiv_id: '2605.14142'
url: https://arxiv.org/abs/2605.14142
pdf_url: https://arxiv.org/pdf/2605.14142
published: '2026-05-13'
collected: '2026-05-17'
category: Training
direction: 粒子系统贝叶斯采样 · MMD 最小化
tags:
- Mean Shift
- MMD
- Interacting Particle Systems
- Bayesian Inference
- Quadrature
- Gradient Flow
one_liner: 提出均值漂移交互粒子系统，通过 MMD 最小化逼近目标分布，实现免归一化常数的贝叶斯积分近似。
practical_value: '- 推荐系统中贝叶斯模型（如贝叶斯个性化排序）的后验推断常面临多模态挑战，该方法的交互粒子系统能有效捕捉多模态和 anisotropy，避免模式坍缩，从而提升参数估计的准确性。

  - 方法不依赖归一化常数，且支持无梯度实现，适用于优化非可微排序指标（如 NDCG）的场景，可直接用于粒子优化。

  - 粒子系统实现简单，易于并行化，可用于需要在线更新后验的实时推荐或动态定价场景。

  - 对于生成式推荐中的隐变量模型，可将此方法用于近似后验采样，替代传统的 MCMC 或变分推断，提高采样多样性和效率。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：贝叶斯推断中，针对复杂后验分布的高效积分是核心挑战。传统方法如MCMC可能混合缓慢，而基于梯度流的方法往往依赖归一化常数或全梯度信息，限制了应用场景。

**方法**：提出均值漂移交互粒子系统（MSIPS），通过最小化粒子集合与目标分布之间的最大平均差异（MMD）来构造加权求积规则。关键创新在于：1) 动力学对未知归一化常数保持不变，无需估计；2) 提供无梯度和梯度知情两种实现模式；3) 粒子通过交互式均值漂移收敛到目标分布的高密度区域，自然捕获多模态与 anisotropy，避免模式坍缩。系统扩展了经典均值漂移算法和最优量化方法至连续分布情形。

**结果**：在包括多模态混合、贝叶斯分层模型、PDE约束反问题等多种基准测试中，MSIPS 展现出快速收敛和高维可扩展性，能够准确近似复杂后验的期望值，验证了其在贝叶斯推断和科学计算中的有效性。
