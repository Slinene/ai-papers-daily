---
title: 'Agent-G^2: Gaussian Guidance for Agentic Reinforcement Learning'
title_zh: Agent-G^2：面向 Agentic RL 的高斯引导框架
authors:
- Zixuan Wang
- Yanrui Miao
- Zhengxi Lu
- Teng Pan
- Yiwen Qiu
- Hongxing Li
- Peng Qiu
- Ruiqing Zhang
- Yongliang Shen
affiliations:
- Zhejiang University
- Baidu Inc.
- Shandong University
arxiv_id: '2608.23318'
url: https://arxiv.org/abs/2608.23318
pdf_url: https://arxiv.org/pdf/2608.23318
published: '2026-08-23'
collected: '2026-08-27'
category: Agent
direction: Agent 强化学习训练 · 引导深度采样
tags:
- Agentic RL
- Hint-based RL
- Gaussian Guidance
- Rollout Efficiency
- ALFWorld
- WebShop
one_liner: 用在线估计的高斯分布动态采样每个任务的专家轨迹引导深度，替代固定或逐样本探测，显著降低 rollout 成本并提升 Agent RL 效果
practical_value: '- 在电商/搜索用 LLM Agent 做多步交互（如智能导购、商品筛选、客服对话）时，可保留专家轨迹前缀作为 warm start，但不必固定深度；借鉴高斯引导在线估计每个任务/query
  的引导深度，平衡探索与专家先验，缓解稀疏奖励。

  - 按任务难度聚类动态调整引导强度：将用户 query 或 session 按难度分簇，分别估计均值方差，避免“一刀切”的固定提示长度，适配长尾/复杂场景。

  - 无需额外 probe rollouts，直接从策略优化已产生的 rollouts 估计分布，节省采样成本，适合在线 RL 预算有限的业务，尤其在大规模推荐/搜索
  agent 调优时。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：长时程 agent 任务面临奖励稀疏，hint-based RL 通过保留专家轨迹前缀让策略从更接近成功的状态开始探索。引导深度是关键：太浅探索难，太深过拟合专家。现有方法中，调度式共享固定深度忽略任务异质性；逐样本探测有效但需要额外 rollout，成本高。

方法：发现有效引导深度形成近似高斯分布带，而非单点最优。Agent-G^2 从在线已收集的 rollout 估计每个任务引导深度的高斯分布，无需 probe rollouts 或学习深度预测器。分布中心由全局基线和按簇难度组合，方差跟踪簇内方差。每个任务从对应高斯中采样深度，实现低成本、自适应引导。

结果：在 ALFWorld 和 WebShop 上，使用 Qwen2.5-1.5B / 7B-Instruct，Agent-G^2 在 ALFWorld 上比最强 hint-based、hint-free、Aux-RL 基线分别高出 2.3 / 3.9 / 7.4 分，且 rollout 成本不到逐样本探测的三分之一。
