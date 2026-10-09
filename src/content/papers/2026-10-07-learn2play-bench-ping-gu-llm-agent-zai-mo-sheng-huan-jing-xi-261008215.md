---
title: 'Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar
  Environments?'
title_zh: Learn2Play Bench：评估 LLM Agent 在陌生环境从经验学习的能力
authors:
- Yibo Li
- Jinhang Qiu
- Zhi Zheng
- Qianyun Guo
- Jiaying Wu
- Shuo Ji
- Bryan Hooi
affiliations:
- National University of Singapore
arxiv_id: '2610.08215'
url: https://arxiv.org/abs/2610.08215
pdf_url: https://arxiv.org/pdf/2610.08215
published: '2026-10-07'
collected: '2026-10-09'
category: Eval
direction: LLM Agent 经验学习评估基准
tags:
- LLM Agents
- Experience Learning
- Benchmark
- Text Games
- Agent Harness
- Self-evolving
one_liner: 设计新文本游戏基准 Learn2Play Bench，揭示保留完整交互轨迹优于总结规则、改变 harness 可提升性能并降本
practical_value: '- 在电商客服、导购、自动谈判等 Agent 场景中，优先保留完整的动作-反馈交互轨迹作为后续决策上下文，而不是仅让 LLM 总结成规则或策略；原始轨迹能保留更多细节，有助于更有效的经验学习。

  - 固定 LLM 骨干模型后，优先优化 Agent harness（状态管理、观察剪枝、动作选择器、循环控制等）可能比微调模型更划算：论文显示更换 harness
  可同时提升性能并降低推理成本，对业务降本增效有直接借鉴意义。

  - 评估 Agent 上线前的学习/适应能力时，应设计规则新颖或反直觉的任务，避免模型利用预训练知识掩盖交互学习不足；同时通过变化游戏实例测试泛化，类似电商场景中的新品类、新活动规则快速适应测试。

  - 人类玩家策略多样性显著高于 Agent，且重复动作更少，提示在 Agent 探索机制中可引入多策略采样、多样性正则或 epsilon-greedy，避免过早陷入局部策略，对复杂对话和推荐交互尤其有用。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有基准难以区分 LLM Agent 的“交互学习”与“已有知识推理”，因为任务规则已写在指令中或预训练已熟悉。为此设计 Learn2Play Bench，包含规则新颖或反直觉的文本游戏，迫使 Agent 通过交互获取知识。

方法关键点：游戏提供可复现反馈和自动评分，支持同一游戏重复尝试以评估经验学习；同时变化游戏实例测试泛化。系统评估了骨干模型、自进化方法和 Agent harness 对学习能力的影响。

关键结果：保留完整的动作与反馈记录比将其总结成规则或策略更能支持有效学习；顶尖人类玩家的峰值分数高于所有评估的 Agent，人类策略更多样、重复动作更少；在固定骨干模型下，更换 Agent harness 能提升性能并降低估计推理成本。这些发现为改进 LLM Agent 的经验学习提供了方向。
