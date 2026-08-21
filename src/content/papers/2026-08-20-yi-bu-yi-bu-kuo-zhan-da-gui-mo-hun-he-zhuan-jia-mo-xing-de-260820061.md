---
title: 'Let''s Scale Step by Step: Compute-Efficient Hyperparameter Transfer for Large-Scale
  Mixture-of-Experts'
title_zh: 一步一步扩展：大规模混合专家模型的计算高效超参数迁移
authors:
- Nayeon Kim
- Hojin Lee
- Yunju Bak
- Jaesun Park
- Boseop Kim
affiliations:
- Kakao Corp.
- Upstage AI
arxiv_id: '2608.20061'
url: https://arxiv.org/abs/2608.20061
pdf_url: https://arxiv.org/pdf/2608.20061
published: '2026-08-20'
collected: '2026-08-21'
category: Training
direction: 大规模MoE训练超参数迁移
tags:
- MoE
- Hyperparameter Transfer
- muP
- Scaling Laws
- Muon Optimizer
- Learning Rate
one_liner: 提出计算高效的两步超参数迁移框架，通过宽度缩放迁移与token外推预测大规模MoE最优学习率
practical_value: '- 在训练大规模 MoE 推荐/广告模型时，可采用 μP 参数化 + 宽度缩放代理模型快速确定学习率，避免对完整尺寸模型做昂贵的超参扫描。对于需要频繁调整专家数量或模型宽度的业务，μP
  让最优 LR 在不同宽度间稳定迁移，显著降低调参成本。

  - 利用小代理模型在有限 token 预算下的 LR 扫描结果，通过线性回归外推到生产模型的超长训练 horizon（如 10T tokens），R²=0.95
  表明该迁移对 MoE 架构高度可靠。训练 infra 团队可据此搭建低成本 proxy 流程，预测大模型最优配置。

  - 若业务落地 DeepSeek-V3 类 MoE 架构（含 Multi-head Latent Attention 和 Muon optimizer），需同步引入对应的
  μP 适配，否则学习率等配置无法跨模型尺寸复用。工程上应把参数化与优化器选择固化进训练代码，保证迁移性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：MoE 架构能以较低计算量扩展模型容量，但在 extreme scale（模型尺寸与 token 预算同时巨大）下，通过 sweeping 优化学习率等超参数成本过高，需要低成本预测方法。

**方法关键点**：
- 提出两步超参数迁移框架：第一步，针对使用 Multi-head Latent Attention (MLA) 和 Muon optimizer 的 MoE 架构，专门适配 Maximal Update Parameterization (μP)，使最优学习率在宽度缩放模型中一致迁移；
- 第二步，沿 token 维度建立预测性缩放律：用小型 proxy 模型在有限预算下得到的最优 LR，通过线性回归外推到大规模训练 horizon（如 10T tokens）；
- 将该方法应用于自有基础模型（155B total, 17B active parameters）的从头预训练，验证配置预测准确性。

**关键结果**：外推最优学习率到万亿 token 训练规模时达到 R²=0.95 的高保真度；在此基础上，完整目标模型的训练稳定、评估有效，且只需极低消融成本即可确定最优配置。
