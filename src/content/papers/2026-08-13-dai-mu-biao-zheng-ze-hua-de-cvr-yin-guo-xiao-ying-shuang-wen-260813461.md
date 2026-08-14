---
title: Doubly Robust Estimation of Causal Effect on CVR with Targeted Regularization
title_zh: 带目标正则化的 CVR 因果效应双稳健估计
authors:
- Jiayi Dan
- Bo Li
- Lu Deng
- Yong Wang
affiliations:
- Tsinghua University
- Tencent Inc.
arxiv_id: '2608.13461'
url: https://arxiv.org/abs/2608.13461
pdf_url: https://arxiv.org/pdf/2608.13461
published: '2026-08-13'
collected: '2026-08-14'
category: RecSys
direction: CVR 因果效应估计 · 双稳健 + 目标正则化
tags:
- Doubly Robust
- CVR
- Causal Inference
- Targeted Regularization
- Uplift Modeling
- Selection Bias
one_liner: 为链式点击-转化结果构造双稳健因果效应估计器，并用目标正则化提升稳定性
practical_value: '- 在 CVR 因果效应估计中，不要只在点击样本上应用标准因果估计器；可直接采用论文推导的影响函数校正项，构造 `P_n(μ2/μ1)
  + P_n(δ(A=a)/(π μ1^2)[(Y2-μ2)μ1 - (Y1-μ1)μ2])`，实现对点击选择偏差和 nuisance model 误差的双稳健。

  - 工程实现上优先用目标正则化替代 one-step DR 校正：在 loss 中加入 `R = mean((Y2-μ2)/μ1 - (Y1-μ1)μ2/μ1^2
  - ε(a)/π)^2`，用低维 spline 参数 ε(a) 学习校正项，能避免低点击率下分母放大导致的数值不稳定。

  - 多任务同时估计 CTR 和 CVR 因果效应，并显式建模 `μ2 = μ1 * tilde μ2`，可共享底层表征、利用 Y2≤Y1 的先验，提升样本效率；同时
  block 从目标正则化项传到 propensity 的梯度，保证 π 估计质量。

  - 对连续 treatment，采用 varying-coefficient 网络（spline 基函数控制网络权重）可防止 treatment 信号被高维协变量淹没，在广告/补贴策略评估中较易迁移。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
CVR 是电商和广告中衡量二阶段转化效率的关键指标，但直接对点击样本估计策略对 CVR 的因果效应会引入选择偏差；现有 ideal loss 类方法只能无偏估计全样本损失，无法保证最终估计量无偏。本文从半参数理论出发，直接对目标 estimand `ψ_a = E[P(Y2(a)=1|Y1(a)=1,X)]` 构造双稳健估计量，解决链式结果下的因果效应估计问题。

## 方法关键点
- 将 CVR 因果效应定义为全人群上的条件概率，利用 `Y2=1 ⇒ Y1=1` 的依赖，目标改写为 `E[E(Y2|X,A=a)/E(Y1|X,A=a)]`。
- 推导目标 estimand 的 influence function 与 von Mises 展开，构造 DR 估计量：`ψ̂_dr = P_n(μ̂2/μ̂1) + P_n(δ(A=a)/(π̂ μ̂1^2)[(Y2-μ̂2)μ̂1 - (Y1-μ̂1)μ̂2])`。
- 理论上证明该估计量在 nuisance 参数以 `o_P(n^{-1/4})` 收敛时达到 root-n 一致性，收敛快于任意 nuisance 模型，因此对神经网络等灵活估计器更鲁棒。
- 为提升实际稳定性，提出目标正则化：用可学习低维参数 ε(a)（spline 近似）替代 one-step 校正项，训练 loss 增加 `R(μ̂1,μ̂2,π̂,ε)`，最终估计为 `ψ̂_tr = mean(μ̂2/μ̂1 + ε(a)/π̂)`，不需要 cross-fitting。
- 多任务联合估计 CTR 与 CVR 因果效应，并构建 `μ̂2 = μ̂1 × μ̃2` 保证转化率不超过点击率；目标正则化梯度不反向传播到 propensity 网络。

## 关键实验
在合成数据、半合成 News 和 CRITEO-UPLIFTv2 上与 DragonNet、VCNet、DRNet、TARNet、Causal Forest、ECUP 等基线对比，AMSE 指标上 CVR 任务显著优于所有基线：合成数据 Ours 达到 0.00248，News 达到 0.00101；消融显示去掉目标正则化后性能大幅下降（如合成数据 0.00981）；与直接 loss debiasing 结合标准因果估计器的方法对比，本文方法仍明显更优。

最值得记住的一句话：无偏 loss 不等于无偏 estimator，必须直接对目标 estimand 构造双稳健校正项，配合目标正则化才能在 CVR 因果效应估计中同时获得稳定性与理论保证。
