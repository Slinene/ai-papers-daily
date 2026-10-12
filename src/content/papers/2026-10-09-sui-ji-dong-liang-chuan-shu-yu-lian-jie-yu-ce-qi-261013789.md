---
title: Randomized Momentum Transport with Cheap Predictors
title_zh: 随机动量传输与廉价预测器
authors:
- El Mahdi Chayti
- Martin Jaggi
affiliations:
- Machine Learning and Optimization Laboratory (MLO), EPFL
arxiv_id: '2610.13789'
url: https://arxiv.org/abs/2610.13789
pdf_url: https://arxiv.org/pdf/2610.13789
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: 训练优化 · 随机动量传输
tags:
- optimization
- momentum
- variance reduction
- randomized transport
- training efficiency
- STORM
one_liner: 提出随机化动量传输，以概率 q 评估梯度修正并用廉价预测替代，在保持 O(T^-1/3) 收敛下显著降低 oracle 调用成本
practical_value: '- 在大模型/推荐模型训练中，二阶动量或梯度修正（如 HVP）计算昂贵，可借鉴随机化加权估计：以概率 q 触发精确修正，其余步用廉价预测（如在线对角预测器），用重要性权重保持条件均值。

  - 若采用 STORM 类优化器，当梯度差噪声模大于光滑常数时，设置 q<1 反而降低收敛首项系数（最多约 10%），可提供调节 q 的理论依据，降低训练成本同时性能不降。

  - 实验表明同等 oracle 预算下，q=1/4 的随机修正降低训练 loss 18-43%，提升 CIFAR-10 HVP 精度 1.5 点；在电商大模型训练中可先在小任务上验证并调整
  q，减少 GPU/TPU 前向与通信开销。

  - 在线对角预测器有 regret-to-convergence 保证，适合线上实时训练推荐模型的连续更新场景。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：动量方法如 STORM 和二阶动量需要每步额外 oracle call 计算梯度修正，训练成本高。  
**方法关键点**：引入随机动量传输估计式 \(\hat C_t = B_t + (J_t/q)(C_t - B_t)\)，\(J_t \sim \mathrm{Bernoulli}(q)\)，以概率 q 评估真实修正 \(C_t\)，否则使用廉价预测 \(B_t\)；估计量保持条件均值，方差增加 \((q^{-1}-1)E\|C_t - B_t\|^2\)，预测损失直接决定方差代价。在 transport-bias、second-moment、residual-control 假设下，对 LMO 更新包括 normalized、sign、Muon 方向，证明每个固定 \(q>0\) 均保持 \(O(T^{-1/3})\) 稳定界，且仅需 single-gradient 初始化。对 unnormalized STORM，当梯度差噪声模超过光滑常数时，部分 \(q<1\) 降低充分梯度预算首项系数最多约 10%。在线对角预测器具备 regret-to-convergence 保证。  
**关键结果数字**：在 MNIST1D 上，同等 oracle 成本下查询四分之一修正使最终训练 loss 降低 18%-43%；CIFAR-10 上 Hessian-vector transport 的测试精度提高 1.5 个百分点。
