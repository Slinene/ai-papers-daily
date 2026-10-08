---
title: On KL-Regularized Policy Optimization
title_zh: KL正则化策略优化：面向异步LLM Agent的单Rollout免Critic更新
authors:
- Yifan Zhang
affiliations:
- Princeton University
arxiv_id: '2610.08963'
url: https://arxiv.org/abs/2610.08963
pdf_url: https://arxiv.org/pdf/2610.08963
published: '2026-10-05'
collected: '2026-10-08'
category: Training
direction: LLM agent 强化学习策略优化
tags:
- RLHF
- KL regularization
- policy optimization
- LLM agents
- critic-free
- importance sampling
one_liner: KLPO将KL正则锚定在采样器，实现每prompt单rollout、无critic的LLM agent策略优化
practical_value: '- 在异步在线 RL（如导购 Agent、客服 Agent、广告文案优化）中，当采样器与训练器策略不一致时，避免 importance
  ratio clipping，改用 KLPO 的 sampler 锚定 + 最小二乘拟合，可减少 off-policy 偏差与实现复杂度。

  - 每 prompt 单 rollout 且 critic-free，只依赖 terminal return，适合长轨迹/工具调用场景，省去 GRPO 成组采样成本，也省去
  value 网络与 learned normalizer。

  - 若业务已有 SPPO/GPO/REBEL/BPO 类策略优化，可参照 KLPO 统一视角进行替换或校准；top-K / binary KL 近似的精确 gap
  公式可用于低成本估计 KL 项时的偏差权衡。

  - 需注意论文为理论分析，未在具体推荐/电商数据上验证，实际落地前应先在小规模 agent 任务上验证稳定性与收益。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：异步 RL 训练 LLM agent 时，rollout 来自旧 checkpoint，且推理引擎概率与训练器在相同参数下也不一致；常用 importance ratio clipping 有偏，GRPO 需要每个 prompt 一组响应，长 episode 成本高。

**方法关键点**：KLPO 将 KL 正则项锚定在 sampler 策略；正则化改进步有闭式 Gibbs 解，通过最小二乘在 sampler 自身轨迹上拟合 log-ratio 最优性条件，完全避免 importance weights。对回归截距做 profile 后，log-partition 被替换为信号的 sampler 均值加 sampler-to-trainer KL。对 token 级策略 mirror descent 目标，梯度可由 terminal return 无 critic 计算，支持 sampler-centered scores 或单一轨迹残差，且工具输出随机时仍成立。证明独立 MC 估计 KL 项梯度无偏；推导 top-K / binary 近似的精确 KL gap；SPPO、GPO、REBEL、BPO 是其特例。

**关键结果数字**：论文为理论分析，摘要未报告实验指标；核心结果是每 prompt 仅需 1 条 rollout、无需 critic、无需 learned normalizer 或 group responses，即可获得无偏更新。
