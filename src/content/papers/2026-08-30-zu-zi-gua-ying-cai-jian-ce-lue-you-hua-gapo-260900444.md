---
title: Group Adaptive Clipping Policy Optimization
title_zh: 组自适应裁剪策略优化（GAPO）
authors:
- Sheng Jia
- Xiao Wang
- Shiva Prasad Kasiviswanathan
- Rein Houthooft
affiliations:
- University of Toronto
- Amazon
arxiv_id: '2609.00444'
url: https://arxiv.org/abs/2609.00444
pdf_url: https://arxiv.org/pdf/2609.00444
published: '2026-08-30'
collected: '2026-09-07'
category: Training
direction: RLVR 训练 · 自适应裁剪
tags:
- RLVR
- GRPO
- GSPO
- Adaptive Clipping
- LLM Reasoning
- PPO
one_liner: 将 RLVR 中固定裁剪上界改为按组内正确数 c 闭式缩放，保护稀有正确 rollouts 的探索信号
practical_value: '- 在电商/搜索/对话式推荐中用 GRPO/GSPO 做 LLM 微调时，可以直接把固定 clip 上界换成 GAPO 的闭式自适应上界：epsilon_hi(c)
  = epsilon_lo + (epsilon_max - epsilon_lo) * (k-c)/(k-1)，只需根据当前 prompt 的 group 内正确样本数
  c 调整 clip，几乎不增加超参数，且无需 reward shaping。

  - 注意 advantage 归一化：不要对 group 内 reward 做 std normalize，否则会放大全对/全错组的权重，稀释稀有正确样本的学习信号；保留原始
  advantage 更利于探索，这一结论可以直接迁移到 query 生成或商品文案生成的 RLVR 训练。

  - 当发现模型 pass@1 尚可但 pass@k 多样性下降、困难 query 覆盖变差时，优先检查 clip fraction 是否对低 c rollouts
  过高，尝试把固定上界改为按 c 线性插值，成本极低，能有效保留困难 query 上的正确生成模式。

  - 若条件允许，尽量使用 sequence-level IS 而非 token-level IS；论文中 sequence-level 变体在数学基准上 pass@1
  更高，且在相同 clip range 下比 token-level 更稳定，可作为架构选择参考。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

Group-relative RLVR（如 GRPO、GSPO）通常对全体 rollouts 使用固定 importance-sampling (IS) ratio 裁剪边界。但固定裁剪忽略了 group 内正确样本数的巨大差异：难题上稀缺的正确 rollout（c 小，advantage A=(k-c)/k 大）与简单题上大量冗余的正确 rollout（c 大，advantage 小）被以相近比例裁剪，前者承载更强探索信号却被过度压制。paper 从 reverse-KL trust region 视角出发，指出最优 IS ratio 应随 advantage 指数增长，因此裁剪上界也应随 advantage 缩放，而不是全局统一。

## 方法关键点

- 从单 prompt 的 reverse-KL trust region 优化推导出最优 IS ratio：ρ_i* ∝ exp(A_i/λ)，线性化后得到 clip 上界应正比于 advantage。
- 在 RLVR 中 advantage 只由 group 内正确数 c 决定，因此得到闭式自适应裁剪：`epsilon_hi(c) = epsilon_lo + (epsilon_max_hi - epsilon_lo) * (k-c)/(k-1)`。
- c=1（最稀缺正确 rollout）获得最大 clip 上界 epsilon_max_hi，c=k 获得最小 epsilon_lo，中间线性插值；incorrect rollouts 固定用 epsilon_lo。
- 保留标准 PPO/GSPO surrogate objective，只修改 clip 阈值，不涉及 reward shaping 或 advantage shaping，继续直接优化 pass@1。
- 不进行 advantage std normalization，避免引入问题难度偏置。
- 提供 sequence-level IS 和 token-level IS 两种变体，主实验采用 GSPO 的 sequence-level IS。

## 关键实验与结果

- 训练数据：DeepScaleR（数学，39,202 样本）、DeepCoder（代码，24,269 样本）；模型：Qwen2.5-Math-1.5B、Llama-3.2-3B-Instruct、DeepSeek-R1-Distill-Qwen-1.5B。
- 对比 baselines：GRPO、Dr.GRPO、symmetric/asymmetric GSPO、F-GRPO、F-GSPO。
- Qwen2.5-Math-1.5B 上，GAPO 平均 pass@1 37.9（vs GSPO asym 37.7），AIME24 pass@1 17.9（vs 16.2，p<0.001），同时保留 pass@256；但 AMC 上有轻微回退。
- DeepSeek-R1-Distill-Qwen-1.5B 上，AIME24 pass@1/pass@16 达到 44.0/76.7，比 GSPO 高 +2.7/+3.4；代码任务 LCB pass@1 24.8 vs 22.4，HumanEval+ 71.7 vs 68.2。
- 训练动态：固定裁剪后期，low-c rollouts 的 clip fraction 与 high-c 接近，IS-advantage correlation 崩溃；GAPO 维持 r>0.8，并保留更多 medium-difficulty 问题的 solve rate。
- Checkpoint intervention 实验（图7）从 step600 切换到自适应裁剪后相关性恢复，排除其他混淆因素。

## 最值得记住的一句话

裁剪上界应该按 group 内正确数 c 线性缩放，把 clip 预算从冗余正确样本转移到稀有正确样本，这样既保护探索信号，又不需要 reward shaping。
