---
title: 'Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task
  Selection'
title_zh: Task-CoEvolve：自适应验证任务选择的高效 Harness 优化
authors:
- Atsuyuki Miyai
- Kiyoharu Aizawa
- Toshihiko Yamasaki
affiliations:
- The University of Tokyo
arxiv_id: '2608.20169'
url: https://arxiv.org/abs/2608.20169
pdf_url: https://arxiv.org/pdf/2608.20169
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: LLM Agent 自适应验证任务选择
tags:
- LLM Agents
- Harness Optimization
- Adaptive Evaluation
- Variance-Weighted Sampling
- Evaluation Efficiency
one_liner: 通过方差加权采样聚焦高分歧任务并估计全量分数，在保持性能的同时将 harness 优化评估成本降 80%
practical_value: '- 在电商对话导购、自动化选品等 Agent 工作流中，harness/prompt 迭代需要跑大量案例，可借鉴 Task-CoEvolve：每轮只评估候选方案分歧最大的样本（能力边界附近），而不是固定全集，能大幅节省
  LLM 推理成本。

  - 用概率加权（Horvitz-Thompson / IPS）从部分采样样本估计全量指标，保证迭代间对比一致；推荐从业者熟悉 IPS，在评估 LLM 生成质量或
  Agent 决策时可直接迁移。

  - 工程实现简单：记录每个候选 harness 在各任务上的成功/失败结果，计算任务间方差作为采样权重，评估指标时用 1/采样概率 加权；无需额外模型，可快速接入现有优化循环。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM agent harness（脚手架/工具调用代码）优化通过不更新模型权重、迭代改写 harness 来提升性能，但现有方法每轮需要完整评估固定验证集，成本高，且很多任务随 harness 进化区分度下降。

**方法关键点**：Task-CoEvolve 让验证任务与 harness 共同进化。核心观察：候选 harness 分歧大的任务比稳定解决/失败的任务更有利于区分。采用基于历史结果的方差加权采样，将评估集中在 agent 能力边界附近的任务，采样分布随 harness 更新自适应调整；通过采样概率加权估计全量分数，保证不同迭代、不同评估子集之间可比。

**结果**：在 online text classification 和 Terminal-Bench 2.1 上，Task-CoEvolve 一致优于固定子集基线，最终性能与全量搜索相当，同时减少 80% 评估次数。
