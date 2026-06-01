---
title: 'DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient
  Multi-Turn Optimization'
title_zh: 解耦轨迹生成与重要性加权微调的高效多轮优化
authors:
- Jian Mu
- Tianyi Lin
- Chengwei Qin
- Zhongxiang Dai
- Yao Shu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2605.31455'
url: https://arxiv.org/abs/2605.31455
pdf_url: https://arxiv.org/pdf/2605.31455
published: '2026-05-29'
collected: '2026-06-01'
category: Agent
direction: 多轮交互优化 · 加权监督微调
tags:
- Multi-turn optimization
- Weighted SFT
- KL-regularized RL
- Offline RL
- Self-correction
- Importance sampling
one_liner: 通过将KL正则化RL目标等价为重要性加权SFT，以监督效率实现多轮推理的强化学习性能
practical_value: '- **离线轨迹 + 重要性权重替代在线RL**：在对话式推荐、智能客服等需多轮交互的场景，可离线采样参考策略的轨迹，按指数回报加权后做SFT，避免每次模型更新都重跑多轮对话，显著降低训练成本。

  - **奖励塑形设计**：用折扣因子鼓励尽早成功，并加入重复惩罚防止模型原地打转，这种回报定义可直接复用于需要逐步修正输出的Agent任务（如多轮搜索、工具调用）。

  - **仅监督最后一轮**：在“正确即停”的交互协议下，只对轨迹的最终响应施加权重，跳过已被验证器否定的中间尝试，简单有效地改善了偏差-方差权衡，适用于类似纠错场景的轨迹数据利用。

  - **Prompt 级权重归一化**：对同一prompt下的多条轨迹独立计算分区函数进行归一化，保证权重只在局部比较相对好坏，稳定训练，这一技巧可推广至其他基于rollout重要性采样的微调方法。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM在多轮交互中需要自纠正能力，但现有方法要么采用在线RL（效果强但每步更新都需生成完整轨迹，成本极高），要么用离线SFT（高效但会遭遇分布偏移和行为崩溃）。DRIFT旨在留住RL的训练信号，同时保有SFT的训练效率。

**方法关键点**：
- **理论等价**：推导出KL正则化RL的目标与重要性加权SFT等价，将最优轨迹分布表示为参考分布的指数倾斜。
- **完全解耦**：分两阶段实现——①离线轨迹生成：用固定参考策略采样多条多轮交互轨迹，按设计的回报（折扣奖励+重复惩罚）计算指数权重，仅保留最后一轮及其权重。②加权SFT：在预收集的数据集上做token级加权交叉熵训练，权重由轨迹回报决定。
- **终端步保留**：因交互在首次正确时终止，仅对最终回答施加权重，避免给中间错误步骤分配正向信号。
- **稳定技巧**：采用prompt级分区函数归一化，缓解低β时权重方差过大问题。

**关键实验**：在MetaMathQA的MATH子集上训练，评估数学（MATH, MATH500, TheoremQA）和通用推理（MMLU-Redux, MMLU-Pro, GPQA）基准。Qwen2.5-3B和Llama3.1-8B下，DRIFT-5turn的multi@5准确率平均达到60.5%和55.6%，分别比UFO-5turn高0.5%和略低0.5%，但训练GPU时间节省数十小时。首轮和第2轮校正率明显高于其他方法。超参分析表明β=0.1、γ较小（如0.3）时效果最佳。

**最值得记住的一句话**：KL正则化RL下的最优策略可以通过对参考策略的轨迹做指数回报加权并执行SFT来逼近，从而把昂贵的在线多轮rollout彻底从训练循环中剥离。
