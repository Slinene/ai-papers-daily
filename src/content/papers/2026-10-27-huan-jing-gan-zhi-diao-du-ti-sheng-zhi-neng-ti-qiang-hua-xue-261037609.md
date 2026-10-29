---
title: 'EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement
  Learning'
title_zh: 环境感知调度：提升智能体强化学习采样效率
authors:
- Sihan Yang
- Weichen Bai
- Ruichuan An
- Yiming Cheng
- Zhiyuan Feng
- Tianyi Jiang
- Renye Yan
- Ning Ding
- Yifan Zhang
- Renrui Zhang
affiliations:
- PKU
- XJTU
- THU
- Samsung Research
- CASIA
arxiv_id: '2610.37609'
url: https://arxiv.org/abs/2610.37609
pdf_url: https://arxiv.org/pdf/2610.37609
published: '2026-10-27'
collected: '2026-10-29'
category: Training
direction: Agent RL 环境感知调度与批采样优化
tags:
- Agent RL
- Scheduling
- Environment-Aware
- Batch Selection
- Sample Efficiency
- LLM
one_liner: 通过环境感知调度任务与环境的 rollout 批次，提升 Agent 强化学习样本效率
practical_value: '- 在电商 Agent（导购、客服）的 RL/偏好训练中，不同任务环境（交易流程、工具 API、校验逻辑）成本与难度差异大，可借鉴
  EnvSched 思路：用历史 rollout 的 reward 方差/不确定性做任务调度，优先采样能拉大策略差异的样本，节省昂贵交互。

  - 构建任务-环境图：企业内部可复用工具、状态定义和验证器关系，构建图并用节点相似度传播统计量，预测信息量，无需额外 pilot 采样即可冷启动调度。

  - 通过 environment quota + similarity penalty 控制 batch 多样性，避免重复观察相似任务，提升每步梯度信息密度；该机制可直接迁移到多场景推荐/对话策略联合训练。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：语言智能体可执行环境规模扩大，rollout 生成与验证成本高。在有限 rollout 预算下，能否在环境层面组织、评估并调度任务实例，提高 agent RL 效率？

**方法关键点**：
- EnvSched 从 rollout 历史在线学习，通过双关系图建模环境-任务对：环境内边捕捉任务语义与共享工具/状态/验证器结构，跨环境边捕捉抽象执行与奖励拓扑。
- 沿两类边传播历史 rollout 统计，预测任务内 reward variance。
- 调度兼顾 exploitation（选取预测 reward variance 高的任务，提供信息量差异）与 coverage（每批覆盖欠观察环境与交互模式）。
- 引入环境配额和相似性惩罚，限制集中与冗余，无需额外 pilot rollouts。

**结果**：在 Qwen3-8B 上训练 40 步，BFCL-v3、tau-Bench、ACEBench-Agent 平均得分 48.81，超过随机任务选择 120 步最高分；同训练预算下，不同模型规模下游性能均有提升。消融实验验证了任务内奖励差异与环境间覆盖的互补作用。
