---
title: When Does Momentum Help in Reinforcement Learning with Verifiable Rewards?
title_zh: 可验证奖励强化学习中动量何时有效
authors:
- Kaifei Wang
- Zikang Shan
- Liwei Wang
- Yinyu Ye
- Han Zhong
affiliations:
- Peking University
- Shanghai Jiao Tong University
- SIMIS
- Stanford University
arxiv_id: '2610.20413'
url: https://arxiv.org/abs/2610.20413
pdf_url: https://arxiv.org/pdf/2610.20413
published: '2026-10-14'
collected: '2026-10-15'
category: Training
direction: LLM 强化学习优化器动量策略
tags:
- RLVR
- momentum
- EMA
- AdamW
- GRPO
- optimization
one_liner: 证明 RLVR 中固定动量增益会被采样噪声淹没，需随学习率放大 β 才能稳定获益
practical_value: '- 在 RLVR/GRPO 类 LLM post-training 里，AdamW 的 β1 别只留默认 0.9；可以尝试 β1=1-1e-6
  甚至 1-1e-9，同时观察 reward/准确率是否稳定提升。

  - 如果想降学习率换取更稳训练，应同步放大 β，使 η/(1-β) 维持在安全区间，避免固定 β 导致动量增益被采样噪声淹没。

  - 做带采样奖励的在线策略优化（如 Agent 任务、推荐/广告的 policy gradient）时，若发现 momentum 无效，先别否定动量，检查 lr
  与 β 的比值是否过小；用少数 seed 很难区分固定 β 和 no-EMA，建议多 seed 或看 SNR。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
RLVR 中 Adam/AdamW 普遍沿用 β1=0.9，但近期工作发现动量收益不稳定甚至有害。论文通过 KL 正则 bandit + NPG 框架，解释动量何时有效以及 β 如何选。

**方法关键点**  
- 模型：softmax 参数化的 KL 正则 response-level bandit，优化 J(θ)=E[r]-γKL(πθ∥πref)，用 bias-corrected EMA NPG。  
- 核心量：ρ=η/(1-β)，代表 EMA 有效记忆窗口内的参数位移尺度。  
- exact gradients：0<ηγ<1 且 β≤((1-ηγ)/(1+ηγ))² 时，增大 β 严格加速且不 overshoot。  
- stochastic gradients：固定 β 下期望增益 O(ηβ/(1-β))，波动 std O(√(η/B))，η→0 时噪声主导，胜率趋于 1/2；若 β=1-η/ρ 且 ρ≤1/(4γ)，期望增益非退化，胜率→1。  
- 用较大 β + 更小 η，可在相同 update/sample 预算下匹配参数且降低跨 run 方差。

**关键实验**  
- 10-arm bandit：固定 β=0.9 在 η=1/4096 的 SNR≈0.04，scaled β 的 SNR≈3.4-3.8。  
- Qwen3-4B-Base + GRPO/DAPO-17k：SGD EMA 与 AdamW 上，更大 β 均提升验证准确率；小 lr+大 β 更稳且不损性能。  
- Qwen2.5-32B + AdamW：仅把 β1 从 0.9 提到 1-1e-9，step 150 平均准确率 44.3%→46.1%，提升近 2 个百分点。

**最值得记住的一句话**  
在低学习率 RLVR 中，固定 β=0.9 是次优的；应随 η 放大 β，使 η/(1-β) 进入安全常数区间。
