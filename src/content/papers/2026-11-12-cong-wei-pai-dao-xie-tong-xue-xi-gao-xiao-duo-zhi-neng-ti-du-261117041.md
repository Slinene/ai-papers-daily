---
title: 'From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research'
title_zh: 从委派到协同：学习高效多智能体深度研究
authors:
- Yuyang Wu
- Yang Liu
- Zequn Xie
- Junjie Wang
- Dan Yang
- Zehao Tan
- Ding-Chu Zhang
- Junming Yang
- Yue Shen
- Jian Wang
affiliations:
- Ant Group
- University of Electronic Science and Technology of China
- Zhejiang University
- Southeast University
arxiv_id: '2611.17041'
url: https://arxiv.org/abs/2611.17041
pdf_url: https://arxiv.org/pdf/2611.17041
published: '2026-11-12'
collected: '2026-11-13'
category: MultiAgent
direction: 多智能体深度研究·贡献感知信用分配
tags:
- Multi-Agent RL
- Credit Assignment
- Deep Research
- Delegation
- Context Management
- GSPO
one_liner: 提出LEAD-RL，通过子代理报告贡献门控联合训练主代理与子代理，仅以最终答案正确性为团队奖励，提升质量与效率
practical_value: '- 多智能体搜索/导购系统中，不要对每个子 Agent 广播相同的最终奖励：可训练一个 LLM rubric judge 对子
  Agent 返回的报告评 helpful/neutral/harmful，再按方向 gate 团队 advantage（helpful 只继承正 advantage，harmful
  只继承负 advantage，neutral 保留原始信号）。这能避免成功轮次强化误导性搜索、失败轮次惩罚有效证据，适合商品比价、多源信息核实等复杂 Agent
  工作流。

  - 主 Agent 与子 Agent 共享同一策略参数并联合更新，比固定子 Agent 或主/子分离训练更利于角色协同，也避免推理时共享 checkpoint
  的角色策略不匹配；在电商导购的“任务路由 + 详情页收集 + 对比总结”三层 Agent 架构中可直接采用。

  - delegation 作为一种 active context management：让子 Agent 在隔离上下文中执行长工具调用，只返回结构化报告（结论、引用、不确定性），主上下文只保留路由和综合信息。这能缓解搜索/推荐场景中多跳检索造成的
  KV cache 和上下文膨胀，值得在商品深度研究、广告落地页调研等长链条任务中工程化。

  - 效率指标可借鉴 critical-path cost 和 idealized speedup，但不把它们作为 reward；仅保留最终业务指标（如答案正确/转化）作为
  reward，能自发得到更好的质量-效率前沿，避免手调成本系数。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

动机：多智能体深度研究系统常用 delegation 并行化搜索、隔离长工具轨迹，但仅有隔离不能保证有效，主代理与子代理必须协调：主代理要发出有用子任务，子代理要返回可靠证据。现有训练要么只优化主代理，要么给所有代理广播同一团队优势，会奖励误导性子代理报告、惩罚有用报告。LEAD-RL 针对这一信用分配歧义，提出贡献感知的联合主/子代理训练。

方法关键点：
- 将 delegation 视为主动上下文管理；主代理动态路由直接工具调用或并行子代理调用，子代理在隔离上下文中执行并返回简短报告，本地/全局验证器过滤报告和答案。
- 共享策略参数，主代理与子代理用角色特定指令条件化，从完整 swarm rollout 中联合更新。
- 训练时 rubric judge 对每个子代理报告评 helpful/neutral/harmful，输入为问题、参考答案、委托 brief、报告及其工具证据，不包含主代理最终回答；低于 0.8 置信度或不确定归为 neutral。
- 信用门控：helpful 报告只继承正团队 advantage，harmful 只继承负，neutral 保留原始；主代理直接继承团队 advantage。最终答案正确性仍是唯一团队 reward，没有 token/step/speedup 奖励。归一化子代理 advantage 避免子代理多引起过大更新。
- 采用 GSPO 作为策略优化目标，K=4 rollouts。

关键实验：在 BrowseComp、BrowseComp-ZH、GAIA、HLE、DeepSearchQA 五个基准和两个模型族（Ling-3-Flash 124B、Qwen3.6-35B）上提升；BrowseComp 上 LEAD-RL 相比 shared team credit joint RL 准确率 +2.49pp，critical-path cost 下降 24.5%（323.30 -> 244.22）；相比 SFT 准确率 +0.99pp 且 critical-path cost 下降 39.5%；验证集准确率提高 6.78 点而 critical-path cost 近似恒定；LEAD-RL 的 124B 模型超过 DeepSeek V4 Flash 284B 且 token 和 critical steps 更少。

最值得记住的一句话：有效的多智能体 delegation 不只是并行化，而是把信用分配到每个子代理报告：只纠正错误的信用方向，不引入过程奖励，最终答案正确性已足以同时改善质量和效率。
