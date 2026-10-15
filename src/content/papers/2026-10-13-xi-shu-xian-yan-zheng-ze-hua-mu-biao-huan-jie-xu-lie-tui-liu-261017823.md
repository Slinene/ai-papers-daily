---
title: Mitigating Popularity Bias in Sequential Recommendations with Sparse Prior-Regularized
  Objective
title_zh: 稀疏先验正则化目标缓解序列推荐流行度偏差
authors:
- Anton Pembek
- Anton Klenitskiy
- Alexander Savchenko
- Alexey Vasilev
affiliations:
- Sber AI Lab
- Lomonosov Moscow State University (MSU)
- HSE University
arxiv_id: '2610.17823'
url: https://arxiv.org/abs/2610.17823
pdf_url: https://arxiv.org/pdf/2610.17823
published: '2026-10-13'
collected: '2026-10-15'
category: RecSys
direction: 流行度偏差缓解 · 稀疏概率训练目标
tags:
- Popularity Bias
- Entmax
- Sequential Recommendation
- Logit Adjustment
- Fenchel-Young Loss
- Debiasing
one_liner: 把流行度先验注入 entmax 变分目标，让稀疏支持集由上下文与流行度共同决定，仅改 loss 即可去偏
practical_value: '- 可直接作为训练目标替换：在 SASRec/GRU4Rec 等序列召回中，把 softmax CE 换成 PR-entmax，只需在
  logits 上加 γ log q 后过 entmax，损失用 Fenchel-Young；线上推理仍用原始 logits，避免改变线上打分分布。q 可用训练集
  item frequency 估计，属于离线固定先验。

  - 超参搜索经验：α 在 1.2–1.6 且 1.5 附近 robust；γ 控制 debias 强度。电商可先固定 α=1.5，单独扫 γ，用 NDCG-Coverage/Novelty
  Pareto 前沿选点，而不是只看单点；同时用 Lorenz-style 曝光曲线观察头部集中度。

  - 大 catalog 落地注意：entmax 需要迭代求阈值 τ，训练比 CE 慢约 20%，但无额外显存；若 item 量极大，可先在 sampled softmax
  基础上做稀疏化或在小流量验证。该方法无架构改动，适合作为现有 pipeline 的轻量去偏插件。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：
序列推荐主流训练目标 softmax cross-entropy 诱导 dense 全局竞争，导致头部曝光过重、长尾覆盖不足；现有 logit adjustment 等去偏方法在 dense softmax 中全局调整 logits，常以牺牲 relevance 换取 debiasing。

方法关键点：
- **PR-entmax** 把流行度先验直接加入 entmax 的变分目标：argmax_{p∈Δ} <p,z> + θ H_α(p) - γ H(p,q)，其中 H_α 是 Tsallis 熵，H(p,q) 是相对物品先验的交叉熵。
- 闭式解为 p*_i = [(α-1)((z_i + γ log q_i)/θ - τ)]_+^{1/(α-1)}；先验以 additive logit correction γ log q_i 进入，且阈 τ 决定 active support：只有 z_i + γ log q_i > θτ 的负样本参与梯度。
- 稀疏支持集由上下文相关性与流行度共同决定，形成 popularity-aware 负样本选择；无关热门项被置零，相关热项保留。
- 推理时移除先验项，ranking 仅用 raw logits z_i。
- 特例：γ=0 退化为 entmax；α→1, γ=0 为 softmax CE；α→1, γ>0, θ=1 为 logit adjustment。

关键结果：
在 ML-1M、Tmall、Yambda-50M、Yoochoose、Zvuk 五个数据集上，用 SASRec 和 GRU4Rec 验证。PR-entmax 相比 CE 在多数 setting 同时提升 NDCG 与 Novelty/Coverage：SASRec ML-1M NDCG@10 +18%、Novelty@10 +17%、Coverage@10 +23%；GRU4Rec Tmall NDCG@10 0.216→0.291。 Pareto 前沿和曝光曲线显示其同时降低头部曝光集中度。消融表明单独 entmax 主要提 relevance 但 debias 不稳，单独 logit adjustment 主要提 debias 但伤 relevance，PR-entmax 兼得。α=1.5 在 [1.2,1.6] 区间稳定。

最值得记住：流行度先验加入稀疏映射后，debias 不再全局作用于所有负样本，而是通过 active support 选择机制，让去偏发生在上下文相关的竞争集合上。
