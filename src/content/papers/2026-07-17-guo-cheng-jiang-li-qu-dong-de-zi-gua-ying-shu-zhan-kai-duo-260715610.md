---
title: Process Reward Informed Tree Rollout for Effective Multi-Turn RL
title_zh: 过程奖励驱动的自适应树展开多轮智能体强化学
authors:
- Xintong Li
- Sha Li
- Yuwei Zhang
- Changlong Yu
- Rongmei Lin
- Hongye Jin
- Shuyi Guan
- Xin Liu
- Linwei Li
- Qingyu Yin
affiliations:
- UC San Diego
- Amazon
arxiv_id: '2607.15610'
url: https://arxiv.org/abs/2607.15610
pdf_url: https://arxiv.org/pdf/2607.15610
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 多轮Agent RL · 树展开探索
tags:
- Tree Rollout
- Process Reward
- Multi-turn RL
- Agent Training
- GRPO
- SWE-Bench
one_liner: 基于中间过程评分引导树展开，使多轮Agent RL训练更高效，SWE-Bench提升5.0点
practical_value: '- 在多轮对话推荐/搜索中，可将完整对话轨迹组织为树，利用用户中间信号（如点击、停留）或任务子指标做过程评分，及早剪枝无效分支，节省推理成本。

  - 对于电商购物助手等多步Agent，把任务分解成子步骤并训练轻量过程评分器，在RL训练时动态分配采样预算，避免在死胡同路径上浪费rollout。

  - 借鉴共享前缀复用机制：不同分支共享前半段合理交互，避免重复生成相同历史，显著提升训练吞吐。

  - PATR与GRPO/PPO等标准策略优化兼容，可直接嵌入现有LLM Agent训练管线，只需额外训练一个过程奖励模型（可利用业务已有反馈信号），工程落地容易。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：多轮Agent RL训练（如GRPO）依赖独立采样完整轨迹，长程任务中均匀分配预算会大量浪费在无望路径，而有潜力的中间状态探索不足，影响样本效率。

方法：提出PATR框架，将多轮交互轨迹自然组织为树，每一轮作为分支决策点。核心是利用任务适配的过程反馈（如代码执行结果、环境得分）对部分轨迹进行实时评分，据此决定在哪些节点继续分支、哪些节点提前终止。通过从高潜力节点生成更多子轨迹、复用共享前缀、保守剪枝退化路径，在相同总采样预算下实现更高效的探索。该树展开组与传统策略优化方法（GRPO/PPO等）兼容，可直接用于策略更新。

结果：在FrozenLake和极具挑战的SWE-Bench上评估，其中SWE-Bench是之前树展开Agent RL方法几乎未涉足的任务。PATR将SWE-Bench性能提升最高+5.0点，FrozenLake提升+9.3点，且在不同任务设定下均稳定优于均匀采样基线。消融实验进一步证实过程评分引导的剪枝和分支策略是增益关键。
