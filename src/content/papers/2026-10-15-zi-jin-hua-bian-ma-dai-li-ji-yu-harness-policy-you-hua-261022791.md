---
title: Self-Evolving Coding Agents via Harness-Policy Optimization
title_zh: 自进化编码代理：基于 Harness-Policy 优化
authors:
- Zhepei Wei
- Wenlin Yao
- Baolin Peng
- Danqing Wang
- Qianhui Wu
- Hao Cheng
- Yu Meng
- Jianfeng Gao
affiliations:
- Microsoft Research
- University of Virginia
- Carnegie Mellon University
arxiv_id: '2610.22791'
url: https://arxiv.org/abs/2610.22791
pdf_url: https://arxiv.org/pdf/2610.22791
published: '2026-10-15'
collected: '2026-10-20'
category: Agent
direction: Agent 自进化与强化学习
tags:
- LLM Agent
- Coding Agent
- Harness-Policy Optimization
- Self-Improvement
- Reinforcement Learning
one_liner: 提出 Self-HPO 框架，交替优化编码代理的 harness 与 policy，实现递归自改进，显著提升编码任务解决率
practical_value: '- 在电商推荐/搜索的 Agent 系统中，不要只微调策略模型或只调整工具/流程（harness），两者应联合迭代优化：让当前策略基于自身失败模式提出新的工具或交互脚手架候选，再用
  RL 更新策略，形成闭环。

  - 利用策略自身作为 harness proposer 的思路可以迁移到推荐 Agent：当 agent 在特定任务（如 query 改写、商品筛选）上频繁失败时，让其反思失败原因并生成新的工具描述、API
  调用模板或搜索流程，然后用这些新 harness 重新训练策略。

  - 从训练中收集困难样本（hard tasks）用于下一轮 harness 搜索，可以保证优化方向始终针对策略的当前薄弱点，避免盲目扩展工具集；对推荐系统来说，可借鉴此机制动态聚焦长尾
  query 或复杂会话场景。

  - 实验显示联合优化 harness 和 policy 的增益超过各自单独优化之和（joint gain > sum of individual gains），这提示在实际业务中，同时调整“模型能力”与“工具/流程”可能带来乘数效应，而非简单叠加。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 编码 Agent 的性能由策略模型（policy）和外部交互脚手架（harness）共同决定。但两者通常被独立优化：为某个 checkpoint 调整的 harness 可能不再适配更新后的策略，固定 harness 又会限制策略学习的轨迹空间。作者认为 harness 和 policy 应协同进化。

**方法关键点**：提出 Self-HPO，一个递归自改进框架，交替执行 H-step 和 P-step。在 H-step，当前策略分析自身在训练集上的失败案例，提出新的 harness 候选（如新的工具描述、交互规则）；通过评估选出最优 harness。在 P-step，使用选定的 harness 通过强化学习更新策略模型。训练中识别出的困难任务被收集起来，作为下一轮 H-step 的搜索集，确保 harness 优化始终针对策略的最新失败模式。整个过程无需人工设计 harness，策略自身充当 harness proposer。

**关键结果**：在三个编码基准上，Self-HPO 持续超过仅优化 harness 或仅优化 policy 的基线，将 Qwen3.5-35B-A3B 的平均解决率从 57.8% 提升到 64.8%，且提升泛化到分布外设置。进一步分析表明，两个优化组件即使与基础对应物配对也保持增益，而联合增益超过各自单独增益之和；同时改善 Pass@1 可靠性和 Pass@k 能力前沿。使用更强外部模型（Opus 4.8）作为 harness proposer 可带来额外提升。
