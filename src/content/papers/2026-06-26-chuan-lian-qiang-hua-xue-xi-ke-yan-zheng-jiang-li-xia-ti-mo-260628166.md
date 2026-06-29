---
title: Tandem Reinforcement Learning with Verifiable Rewards
title_zh: 串联强化学习：可验证奖励下提升模型协作与可读性
authors:
- Difan Jiao
- Raghav Singhal
- Robert West
- Ashton Anderson
affiliations:
- University of Toronto
- EPFL
arxiv_id: '2606.28166'
url: https://arxiv.org/abs/2606.28166
pdf_url: https://arxiv.org/pdf/2606.28166
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: RLVR 串联训练提升可读性
tags:
- RLVR
- Tandem Training
- Reasoning
- GRPO
- Compatibility
- Multi-model Communication
one_liner: TRL 让强模型在 RLVR 中与冻结弱模型交替推理，在保持自身能力同时显著提升可读性和交接鲁棒性
practical_value: '- **多模型协作代理**：在电商搜索/推荐的多 Agent 系统（如 Planner-Executor）中，可借鉴串联训练思路，让强模型与弱模型交替生成，迫使强模型输出弱模型能理解的推理，从而降低通信错误，提升整体鲁棒性。

  - **减少模型升级后的分布漂移**：当线上推理模型（如 LLM Ranker）升级到更强版本时，旧模型作为弱模型参与串联微调，能缓解新模型生成的推理与下游模块（如旧版特征解析器）的不兼容，避免线上表现骤降。

  - **提升 Chain-of-Thought 在推荐中的可解释性**：直接对推理链进行 RLVR 训练容易产生人类难以阅读的符号或语言混合，TRL 框架可约束推理链对弱模型（或人类）更友好，从而让推荐解释更自然。

  - **训练数据与线上推理的闭环**：可利用弱模型模拟真实用户或下游模块，在离线训练中通过滚动生成的方式收集奖励，无需频繁的在线实验即可评估新模型与现有系统的兼容性。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：RLVR 通过结果验证奖励极大提升了 LLM 的推理能力，但会导致推理过程偏离人类或弱代理可理解的模式（如可读性差、语言混杂），影响多模型协作和人类跟进。现有 tandem 训练只在概念验证中用于短链推理，能否扩展到长链 RLVR 未知。

**方法**：提出 TRL（Tandem RL），将串联训练引入 RLVR 管道。训练时，强模型（senior）与冻结的弱模型（junior）随机交替生成每个 token，整个 rollout 结束后根据最终答案奖励，仅对 senior 施加 GRPO 损失。该结构迫使 senior 学习弱模型能继续推理并达到正确终点的生成方式。

**关键结果**：在 Qwen3-4B-Instruct 上使用数学竞赛数据训练，TRL 在 solo 推理能力上与普通 GRPO 持平，同时从同一 rollout 结构中涌现三个特性：与 junior 的交接鲁棒性更强、相对于 junior 的分布漂移更小、思维链对 junior 的可读性更高。这表明 RLVR 可以在不牺牲个体性能的前提下，显著提升模型间的协作兼容性和人类可读性。
