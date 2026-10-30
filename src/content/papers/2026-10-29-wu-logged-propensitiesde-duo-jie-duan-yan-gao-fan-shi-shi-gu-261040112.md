---
title: 'Beyond IPS: Reliable Counterfactual Evaluation in Multi-Stage Ad Systems without
  Logged Propensities'
title_zh: 无Logged Propensities的多阶段广告反事实评估：混合加权奖励模型
authors:
- Mohsen Malmir
- Mohamed A. Radwan
- Houssam Nassif
- Murat Ali Bayir
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2610.40112'
url: https://arxiv.org/abs/2610.40112
pdf_url: https://arxiv.org/pdf/2610.40112
published: '2026-10-29'
collected: '2026-10-30'
category: Eval
direction: 广告排序离线评估 · 密度比加权
tags:
- Off-Policy Evaluation
- Density Ratio Estimation
- Direct Method
- Counterfactual Replay
- Ad Ranking
- Mixture Weighting
one_liner: 用多分类域分类器估计密度比，训练混合加权奖励模型，在无倾向分下提升广告离线策略选择可靠性
practical_value: '- 在无 propensities 的多阶段推荐/广告系统中，做离线策略筛选优先用「共享 reward model + mixture-weighted
  density ratio」，不要逐候选训练 per-policy reward model；实验显示 per-policy 加权反而更差。

  - 用多分类 domain classifier 区分 logging 与候选策略产生的 impression，取 q(j|z)/q(0|z) 作为密度比；裁剪到
  c=10–100 并监控 ESS/n，ESS 过低说明重叠差、权重不可靠。

  - 把冷启动质量（q(0|z)<τ 的候选 impression 比例）作为离线评估天堑诊断：若过大，离线选出的 top candidate 也可能翻车，应直接送线上
  A/B。

  - DM 估计值 MAE 偏高，但用于 Top-1 候选选择有效；若要更准确估计各候选价值或回归预算，可加 DR 残差修正，用同一组密度比权重，低重叠时提升明显。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多阶段广告系统（召回、粗排、精排、拍卖、过滤、定向）的曝光日志没有可靠 logged propensities，且下游变换不可观测，IPS/SNIPS 无法识别策略价值。离线评估常作为线上 A/B 前的高通量筛子，但 DM 在候选策略与 logging 分布相差大时有偏，容易选错候选。

**方法关键点**
- 将每个候选策略 replay 到 logged context，构造「logging + candidate」多分类数据集，训练 domain classifier qθ(g|z)。
- 用密度比公式 \hatΩ_j(z)=qθ(j|z)/qθ(0|z) 估计候选 vs logging 密度比，混合权重 \hatΩ(z)=Σβ_j\hatΩ_j(z)，默认 uniform β_j=1/N。
- 训练单个共享 reward model：log loss 按 \tildeΩ(z)=min(\hatΩ(z), c) 重加权，裁剪 c=10–100，监控 ESS/n 作为重叠诊断。
- 值误差界分解为 overlap、cold-start mass、replay concentration 三项；cold-start mass µ_j(τ) 是离线评估不可消除的残留项，给出离线 vs A/B 的路由规则。
- DR 修正：在加权 DM 上加上残差项 \hatΩ_j(z)(r−\hat r(z))，用同一组权重。

**关键实验**
- 合成仿真：10k users / 1k ads，70k impressions，50 seeds；低 ESS (<0.4) 下 Weighted DM Top-1 acc 0.81 vs Unweighted DM 0.67，Weighted DR 0.90；Weighted DR 在低/中 ESS 全指标最优。
- 生产流量：1 logging + 5 candidates，Weighted DM Top-1 acc 0.40 vs Unweighted 0.36、Per-policy 0.24；Weighted DR Top-1 acc 0.44；DM 的 MAE 明显高于 DR，但 Top-1 选择可接受。

**最值得记住的一句话**
无 propensities 时，用域分类器密度比重加权共享 reward model，能显著改善低重叠下的 Top-1 策略选择；冷启动 mass 是决定离线筛选还是转线上 A/B 的关键信号。
