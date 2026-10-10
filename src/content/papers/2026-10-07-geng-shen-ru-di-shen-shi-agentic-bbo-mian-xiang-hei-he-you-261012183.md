---
title: 'A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization'
title_zh: 更深入地审视 Agentic BBO：面向黑盒优化的 LLM Agent 基准测试
authors:
- Ming Chen
- Rong-Xi Tan
- Ke Xue
- Yu-Jie Zhou
- Taiye Lu
- Zhi-Xuan Gao
- Peng Xie
- Zijun Shen
- Chen Lu
- Haopu Shang
affiliations:
- State Key Laboratory of Novel Software Technology, Nanjing University
- School of Artificial Intelligence, Nanjing University
arxiv_id: '2610.12183'
url: https://arxiv.org/abs/2610.12183
pdf_url: https://arxiv.org/pdf/2610.12183
published: '2026-10-07'
collected: '2026-10-10'
category: Eval
direction: LLM Agent · 黑盒优化基准测试
tags:
- Agentic BBO
- LLM Agent
- Black-Box Optimization
- Benchmark
- Hyperparameter Optimization
- Finite-Budget
one_liner: 构建跨领域基准 AgenticBBO-Bench，统一评估 LLM Agent 在黑盒优化中的表现并分析关键设计因素
practical_value: '- 在推荐系统超参数优化（学习率、正则系数、embedding 维度等）或 AutoML 流程中，可让 LLM agent 结合任务语义与历史
  trial 结果生成候选配置，再由数值优化器精调，减少早期随机搜索浪费。

  - 当黑盒目标包含语义信息（如商品类目、广告文案风格、用户意图）时，将语义先验注入 agent 提示词能稳定提升搜索效率；但避免使用过于具体的先验知识，论文显示具体先验不稳定。

  - 线上 A/B 测试或流量有限的调参场景可借鉴 finite-budget 协议：在固定评估次数内对比不同策略，结合 LLM 推理成本选择 Pareto 前沿模型（如
  DeepSeek-V4.1-Flash），兼顾性能与成本。

  - 设计 agent 系统时不必堆砌额外数值工具，应优先利用任务语义和 agent 生成的优化轨迹；数值优化器可以有效吸收 agent 探索得到的轨迹，二者协同优于单独使用。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：黑盒优化广泛存在于科学和工程问题，评估成本高且次数有限。LLM agent 通过结合任务语义、计算工具和反馈决策带来新可能，但现有研究任务域与系统配置不一，难以公平比较和隔离设计因素。

方法：构建跨领域基准 AgenticBBO-Bench，覆盖合成函数、超参数优化、数据库调优、芯片设计、分子设计五类任务，统一 finite-budget 评估协议。比较 agentic BBO 与直接 LLM 方法及数值优化器，并系统研究三个关键因素：优化工具、任务信息与先验知识、LLM 在搜索中的角色。另设 five-task frontier challenge，评估七个 LLM 在 Codex agent harness 下的表现。

关键结果：agentic BBO 在全部五个领域的 family-averaged scores 均高于直接 LLM 方法，并在四个领域超过最佳数值优化器。实验显示：额外数值工具并不总能提升性能；任务语义广泛有用，但更具体的先验知识可靠性较低；数值优化器能有效吸收 agent 建立的搜索轨迹带来的增益。在 frontier challenge 中，GPT-6 Astra 与 DeepSeek-V4.1-Flash 处于性能与成本的 Pareto 前沿。
