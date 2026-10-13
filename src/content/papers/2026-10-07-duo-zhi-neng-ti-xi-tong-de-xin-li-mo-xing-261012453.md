---
title: Mental-Models for Multi-Agent Systems
title_zh: 多智能体系统的心理模型
authors:
- Hanan Gani
- Lulu Shao
- Manmohan Chandraker
affiliations:
- University of California, San Diego
arxiv_id: '2610.12453'
url: https://arxiv.org/abs/2610.12453
pdf_url: https://arxiv.org/pdf/2610.12453
published: '2026-10-07'
collected: '2026-10-13'
category: MultiAgent
direction: 多智能体心智建模与决策
tags:
- Mental Models
- Theory of Mind
- Multi-Agent
- Belief-Conditioned Reward
- Latent Representation
one_liner: 显式学习对手潜在心理状态作为决策变量，提升多智能体交互质量与心智推理能力
practical_value: '- 在电商谈判、客服对话、推荐 Agent 与用户交互等场景，可显式建模用户隐藏意图、预算或偏好，将推断出的 latent partner
  state 作为策略输入，而不是只依赖 prompt 或 memory。

  - 借鉴 belief-conditioned reward model：先推断用户/对手潜在状态，再对候选回复、推荐项或谈判动作打分，用这个信号训练策略，能提升多轮交互的适应性和个性化。

  - 一阶/二阶心智状态结构可用来预测用户对推荐结果的下一步反应，例如接受、拒绝或砍价，从而让 Agent 提前调整推荐策略或话术。

  - 训练完成后推理时不依赖在线访问对手模型，可独立部署，对实时在线服务友好；但在业务中用户意图分布广泛，建议先在小范围高价值场景试点。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
当前基于大模型的多智能体系统大多通过 prompt 设计、记忆或端到端行为塑造来工作，缺乏显式的对手状态表示，难以在部分可观测条件下推理对方的隐藏信念、意图和可能反应。

## 方法关键点
提出 mental-model-enabled agents 框架：
- 学习一个 amortized recursive Theory-of-Mind 表示，包含一阶和二阶心理状态结构，从观测历史中推断对手潜在状态。
- 联合学习 belief-conditioned reward model，以推断出的对手状态为条件评估候选动作。
- 在该 belief-aware 信号下训练策略，使 Agent 在推理时可独立行动，同时保留显式对手建模的好处。
- 同一框架在 language-only 和 multimodal 两种 benchmark 上评估。

## 关键结果
显式心理状态建模在语言和多模态设置下均一致提升交互质量与 Theory-of-Mind 性能，优于基础智能体系统，表明结构化对手建模是通用多智能体系统的一个有效归纳偏置。
