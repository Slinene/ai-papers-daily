---
title: 'More Correct Mass, Worse Answers: Why Power Sampling Can Fail and How to Fix
  It'
title_zh: 更多正确质量，更差答案：Power Sampling 为何失败及修复
authors:
- Haohui Yang
- Jiaxing Sun
- Xiujun Ma
affiliations:
- State Key Laboratory of General Artificial Intelligence, Peking University
arxiv_id: '2608.14420'
url: https://arxiv.org/abs/2608.14420
pdf_url: https://arxiv.org/pdf/2608.14420
published: '2026-08-14'
collected: '2026-08-17'
category: Reasoning
direction: Power Sampling 推理时采样修正
tags:
- Power Sampling
- Self-Consistency
- Importance Weighting
- Test-time Scaling
- LLM Reasoning
- Distribution Sharpening
one_liner: 揭示 Power Sampling 提升正确轨迹概率却伤害自洽性聚合，提出 Relative-Rank SoftSat 与重要性加权修复
practical_value: '- 在 LLM 多路生成投票、Agent 决策聚合或生成式推荐候选排序中，避免直接用模型全局概率/置信度做幂次加权（类似 p^α
  或降低温度）。它可能放大单一高概率错误路径，压制多个中等概率正确路径的集体支持；改用 prompt 内相对排名（percentile）并对 top 项做饱和增益，可保留投票所需的中尾部多样性。

  - 对不同 prompt/上下文做候选打分时，不要直接比较绝对 log-likelihood，否则同一阈值在不同问题上效果差异很大（dose mismatch）。先做
  per-prompt 分位标准化再做 reweighting，能更稳定地控制分布变形强度。

  - 固定推理预算下，可把从 sharpened 目标分布重复采样 N 次替换为从 Base 分布采样 N 条后用重要性权重聚合，文中在 MoreHopQA 上选择一致率达
  99.55%，延迟降低 7.42 倍；适合线上 LLM 候选生成/投票，无需额外模型调用。

  - 评估多候选推理或生成式推荐结果时，不要只看 pass@k 或 top-1 正确率，要监控 answer-level margin 和正确答案的覆盖结构；全局
  sharpening 可能提升正确轨迹总质量但降低 gold-answer margin，导致最终聚合变差。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
Power Sampling 在全轨迹分布上做 p^α，被视为无需 verifier 的推理时增强前端，常用于 self-consistency 等多采样聚合。但论文发现一个悖论：即使正确轨迹的总概率质量上升，下游投票准确率反而下降。在 9 个模型-基准设定里，Power 在 7 个中退化，最大降幅 18.5 个百分点。原因是两类 mismatch：coverage mismatch 指全局 sharpening 把质量集中在少数占优路径，压制多个中等概率正确路径的集合支持，即使 pass@k 较高；dose mismatch 指固定 α 在不同问题上的分布变形强度差异巨大，因为 problem-specific 的 likelihood 方差不同。

## 方法关键点
- **Relative-Rank SoftSat**：用 prompt 内相对排名 u_p(τ) = Pr[ℓ(X) ≤ ℓ(τ)] 替代绝对 log-likelihood，统一变形剂量；增益函数 SoftSat_m(u) = 1 - (1 - min(u/m, 1))^2，对中等 rank 提升、对 top 饱和，保留覆盖。
- **重要性加权实现**：不重复运行 Power-SMC N 次，而是对共享 Base 候选池做 importance-weighted aggregation，权重 r = exp(β·SoftSat_m(rank)) 或 Power 下 r = exp((α-1)ℓ(τ))，配合 weighted self-consistency / ModeX，同预算无额外模型调用；理论证明渐进等价并给出 O(N^{-1/2}) 收敛率。
- 实际使用 m=0.75, β=1，clip 到 [0.75,17] 后做均值归一化。

## 关键实验
在 BigCodeBench、LiveAoPSBench、PHYSICS 三个基准，Nemotron-4B、Qwen3.5-9B、Ministral-8B 三个模型上，以 N=8、temperature=1、top-k=50 的 Base pool 比较 Uniform、Power α=4、SoftSat。Power 在 6 个 LiveAoPS/PHYSICS 设定全降，LiveAoPS Nemotron 降 18.47 个百分点；SoftSat 相对 Uniform 在 5/9 设定提升，最大回归仅 1.004 个百分点，移除了 Power 的大幅退化。在 MoreHopQA Case-5 上，重复 Power-SMC 与重要性加权实现最终答案一致率 99.55%，准确率差 0.089 个百分点，延迟降低 7.42 倍。

最值得记住的一句话：**判断一个 sharpened 分布不能只看单轨迹质量或 pass@k，而要看它是否为下游聚合保留了足够的支持结构；用相对排名 + 饱和增益替代全局幂次，并用重要性加权实现同预算目标采样。**
