---
title: 'What is Missing from AI Post-Training AI: An Empirical Analysis'
title_zh: AI 后训练中缺失什么：实证分析
authors:
- Joy Jia Yin Lim
- Xin Huang
- Hao Peng
- Yaxi Lu
- Xin Cong
- Zhong Zhang
- Maosong Sun
- Yankai Lin
affiliations:
- Tsinghua University
- Renmin University of China
- University of Electronic Science and Technology of China
arxiv_id: '2608.19072'
url: https://arxiv.org/abs/2608.19072
pdf_url: https://arxiv.org/pdf/2608.19072
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: LLM Agent 后训练能力实证分析
tags:
- LLM Agent
- Post-training
- Strategy-level capability
- Execution-level capability
- AI-for-AI
- Empirical Analysis
one_liner: 发现 LLM Agent 后训练时策略锁定在初始阶段，仅做局部调整，经验、人类指导与推理算力均无法激发策略级自省
practical_value: '- 若用 LLM Agent 做搜索/推荐模型自动调参或训练流水线，不要只给历史经验或 prompt 提示：需在框架中设置强制策略审查点，要求
  agent 根据验证集波动、性能 plateau 等证据重写全局训练策略，避免陷入局部搜索。

  - 经验驱动 scaffold 能提升执行效率，但不会改变策略方向；因此对需要探索不同召回/排序结构或生成式推荐 Semantic ID 空间的场景，仅靠积累经验不够，应引入多样性注入或不同策略并行。

  - 人类指导只能修正初始策略，开始训练后 agent 会退回局部调整；工程上可在训练循环中加入自动化干预触发器（如验证指标停滞 N 步），强制 agent 重新评估目标与超参数。

  - 增加推理算力对简单任务有效，难任务几乎无增益；在复杂商品理解或长链路推荐优化中，不要把算力花在更多推理 token 上，而应投资于更好的策略搜索算法或全局探索机制。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM Agent 已能端到端后训练 LLM（写代码、启动训练、评估 checkpoint），但常把执行级能力与策略级能力混为一谈。需要实证检验 agent 在持续实验过程中是否会根据证据修订高层训练策略。

方法关键点：分析大量公开后训练轨迹；将能力分为执行级（在既定策略内迭代）和策略级（随实验证据更新全局判断）。设计三类递进干预：经验驱动 scaffold、人类指导、增加推理算力。在 GSM8K、HumanEval 等任务上评估。

关键结果：轨迹分析显示 agent 在初始阶段锁定训练策略，后续预算几乎都用于局部调整。经验驱动 scaffold 显著提升执行效果（GSM8K +12.6，HumanEval +40.8），但策略保持静态；人类指导能纠正初始策略，但训练开始后仍退回局部调整循环；额外推理算力只在简单任务有效，最难任务几乎无增益。结论：agent 缺乏的不是经验、指导或推理算力，而是执行过程中自发重估策略的机制。
