---
title: 'From Repositories to Training Environments: Scaling Long-Horizon Coding Agents
  with Environment Evolution Loop'
title_zh: 从仓库到训练环境：用环境进化循环扩展长时程编程 Agent
authors:
- Yang Tian
- Tianyu Zheng
- Xiyuan Yang
- Yaxin Du
- Chengran Yang
- Bo Zhao
- Jian Yang
- Bryan Dai
affiliations:
- Beihang University
- School of AI, Shanghai Jiao Tong University
- IQuest Research
arxiv_id: '2611.21152'
url: https://arxiv.org/abs/2611.21152
pdf_url: https://arxiv.org/pdf/2611.21152
published: '2026-11-16'
collected: '2026-11-18'
category: Training
direction: 训练环境合成 · 长时程 Agent
tags:
- Environment Synthesis
- Coding Agents
- RL Training
- Proxy Feedback
- Long-Horizon
- Environment Evolution
one_liner: RepoFactory 将真实仓库转化为可验证环境，通过 Environment Evolution Loop 提升训练价值，训练出的模型在长时程编程基准上显著增益
practical_value: '- 可借鉴环境合成思路：在构建推荐/Agent 训练环境时，用可验证的 proxy 信号（如任务可完成性、状态耦合度、覆盖范围）自动筛选和演化环境，替代昂贵的人工标注或完整
  rollout 评估。

  - Environment Evolution Loop 的乘法目标设计（validity × structural coupling × implementation
  scope）能放大多个质量维度的短板，避免单一指标过拟合；在电商 Agent 模拟器或多轮对话任务环境筛选中可参考。

  - 从真实仓库/业务日志到可交互训练环境的转化 pipeline 值得迁移：将静态日志转化为 agent 可逐步执行并接收反馈的环境，更适合训练长时程策略（如购物助手、营销策略
  Agent）。

  - 用廉价 proxy feedback 快速迭代环境，减少真实评估次数，降低训练成本；在推荐系统的用户模拟器或广告投放策略训练中可尝试类似分层反馈机制。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长时程 coding agent 训练依赖可验证反馈的环境，但现有 pipeline 多为线性过程，只到 validation 为止，无法指导训练环境的价值提升；递归自改进（RSI）又因 rollout 和训练成本高、反馈慢而受限。需要及时可靠的 proxy 信号来提升训练环境质量并规模化合成。

**方法关键点**：提出 RepoFactory，一条自动化 pipeline，把真实仓库转化为可验证环境，让 agent 根据语言规格从零构建完整项目。核心是 Environment Evolution Loop：用 proxy feedback 优化 multiplicative objective，同时考虑 validity（环境可验证）、structural coupling（结构耦合度）和 implementation scope（实现范围）。该 loop 在不依赖完整模型训练和下游评估的情况下，持续演进环境，提高训练价值。

**结果**：RepoFactory 生成 10,159 个环境，覆盖 17 个软件领域。基于这些环境训练 Qwen3.5-35B-A3B 得到 RepoHorizen-35B-A3B，在 NL2Repo-Bench 上提升 22.6 个百分点，在五个长时程编程和 agentic 任务基准上平均提升 8.5 分；未使用环境演化时分别仅提升 17.5 和 6.4 分，证明 Environment Evolution Loop 带来额外收益。
