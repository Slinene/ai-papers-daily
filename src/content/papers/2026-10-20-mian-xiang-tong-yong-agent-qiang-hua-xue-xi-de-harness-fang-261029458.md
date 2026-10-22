---
title: Harness Scaling for Generalizable Agentic Reinforcement Learning
title_zh: 面向通用 Agent 强化学习的 Harness Scaling 方法
authors:
- Fei Bai
- Huatong Song
- Chuan Hao
- Ran Tao
- Jian Yang
- Bryan Dai
- Wayne Xin Zhao
- Ji-Rong Wen
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- IQuest Research
- Beihang University
arxiv_id: '2610.29458'
url: https://arxiv.org/abs/2610.29458
pdf_url: https://arxiv.org/pdf/2610.29458
published: '2026-10-20'
collected: '2026-10-22'
category: Agent
direction: Agentic RL · Harness 缩放训练
tags:
- Harness Scaling
- Agentic RL
- Generalization
- Orthogonal Design
- Cross-Harness Transfer
- RLHF
one_liner: 将 agent 执行 harness 因子化并正交选择 18 个训练配置，跨 harness RL 显著提升未见配置与外部黑盒泛化
practical_value: '- 在训练搜索/推荐/电商 Agent 时，不要只用单一 harness；可对同一任务构造多个执行配置变体（system prompt、工具
  schema、观察格式、上下文压缩策略、workflow 约束），提升策略对生产环境变化的鲁棒性。

  - 如果 harness 组合空间过大，可用 strength-2 正交设计从组合爆炸中选训练子集，保证各组件 realization 及两两组合均衡覆盖；在固定训练预算下，这比随机采样或全量穷举更好。例如推荐
  Agent 的 prompt 模板、召回通道、排序特征视图、记忆压缩等维度都可以做正交选择。

  - 采用 locality-aware assignment：每个训练任务采样一个 anchor harness，再配 1-2 个 Hamming 距离最近的
  harness，既保留同任务局部变化，又全局覆盖多个配置；实验表明 K=2 效果最佳，且优于随机 assignment。

  - 关键结论可直接迁移：在白盒多 harness 配置上训练，迁移到未见外部黑盒 harness（如 Claude Code）的效果，优于直接在该黑盒 harness
  上做 SFT 或 RL。适合冷启动、跨平台迁移、多租户 Agent 系统。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有 Agentic RL 通常只在单一固定 harness 下优化策略，容易导致策略对特定执行配置过拟合，跨 harness 泛化差。Agent harness 是模型与工具、上下文、工作流之间的执行层，其多样性尚未被作为 scaling 维度系统研究。

### 方法关键点
- 将 harness 因子化为 5 个组件：system prompt、tool interface、observation、context management、workflow；每个组件 3 个 realization，构成 3^5=243 的组合空间。
- 用 strength-2 正交设计从 243 个配置中选出 18 个训练配置，满足 pairwise balance：每个 realization 出现 6 次，每对组件 realization 组合出现 2 次，Rao bound 约束下最小可用规模。
- 跨 harness 训练：每个 task 随机采样一个 anchor harness，再选其 Hamming 距离最近的 K-1 个配置（K=2），同一任务在相近配置下产生多条轨迹，全局覆盖与局部控制变化结合。
- 优化沿用标准 PPO/GRPO clipped objective，但 rollout 来自多 harness task-harness 分布；同时验证 GRPO 与 PPO。

### 关键实验
在 ClawGym-Task 上训练 Qwen3-4B-Instruct 与 Qwen3-30B-A3B-Instruct，评估 ClawGym-Bench、JobBench-Easy、PinchBench。
- In-space 泛化：18 个 held-out 未见配置上，Harness Scaling 相比 Single-Harness RL，4B GRPO 平均从 29.81 提升到 39.04，PPO 从 33.91 到 36.93；30B GRPO 从 37.29 到 42.78，PPO 从 36.31 到 41.89。
- 外部黑盒迁移：在 Claude Code 上，Harness Scaling 平均 37.22（4B）/41.20（30B），超过 Black-Box SFT（35.08/38.08）和 Black-Box RL（33.38/36.28）。
- 消融：结构化 18-harness 优于随机 18 和全 243 配置；K=2 每任务 harness 数最佳；locality-aware assignment 优于随机 assignment。

### 最值得记住的一句话
> 在固定 RL 训练预算下，通过结构化选择的多种白盒 harness 配置进行跨配置训练，比单一复杂黑盒 harness 直接训练更能提升 agent 对未见执行环境的泛化能力。
