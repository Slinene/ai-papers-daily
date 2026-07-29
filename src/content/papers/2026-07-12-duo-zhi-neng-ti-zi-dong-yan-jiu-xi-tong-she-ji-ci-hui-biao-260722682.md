---
title: A Vocabulary for Multi-Agent Automated Research Systems
title_zh: 多智能体自动研究系统设计词汇表
authors:
- Bardiya Akhbari
affiliations:
- Amazon AGI
arxiv_id: '2607.22682'
url: https://arxiv.org/abs/2607.22682
pdf_url: https://arxiv.org/pdf/2607.22682
published: '2026-07-12'
collected: '2026-07-29'
category: MultiAgent
direction: 多智体系统设计方法论与品味解耦
tags:
- multi-agent
- vocabulary
- automated research
- design patterns
- evaluation
- generative taste
one_liner: 为多智能体自动化研究系统定义八个可独立变化的架构坐标，分离生成式与评估式品味
practical_value: '- 用该词汇表标准化描述多智能体推荐架构（如对话式推荐中的 supervisor-agent、critic-worker），让团队快速对齐系统设计差异。

  - 分离“生成式品味”和“评估式品味”，在离线评估中同时关注候选新颖度（生成式品味）和 proxy 指标与真实在线效果的 gap（评估式品味），避免仅优化表面指标。

  - 借鉴“shared state S_cross”设计跨请求记忆，在长期用户建模或跨会话推荐中累积信息，让 agent 具备跨 run 学习能力。

  - 引入 meta-control 操作（spawn/kill, grant/revoke）动态调配 agent 能力和权限，在任务分发或分层推荐中按需激活子
  agent，减少闲置开销。'
score: 7
source: huggingface-daily
depth: abstract
---

自动化研究系统（autoresearch）设计选择繁杂且缺乏统一描述，难以系统比较和积累知识。该工作为多智能体自动研究系统定义一个词汇表，将设计空间分解为八个可独立变化的坐标：**agents**（谁执行），**operations**（可用操作），**messages**（通信方式），**capabilities**（能力分配），**shared state**（跨 agent/run 的可见状态），**policy**（next action 决策，包括 route, stop, meta-control 和 exploration），**initialization**（如何启动），以及 **evaluator**（评分组件）。一次运行的完整记录称为轨迹（trajectory），随机性带来轨迹分布而非单一行为。

该词汇表将每个结构设计问题（如 agent 何时通信、获取/失去能力、跨 run 携带信息）映射到独立坐标，便于控制变量试验。特别地，把“品味”这一模糊抱怨拆解为两个可分别优化的故障：**generative taste**（系统在获得任何评分前提出新颖轨迹的速率）和 **evaluative taste**（代理评分与真实质量的差距）。用该词汇表覆盖了 existing autoresearch 系统，实例化出 population, islands, supervisor pair, dialogue, blackboard 等常见模式，证明其通用性和区分能力。

关键贡献不是实验结果，而是将多智能体设计从 ad hoc 选择提升为可测试、可复用的结构化框架。
