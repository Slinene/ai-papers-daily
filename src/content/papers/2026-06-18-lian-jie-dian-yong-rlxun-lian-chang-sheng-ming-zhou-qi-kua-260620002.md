---
title: 'Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain
  Generalization Via Reinforcement Learning'
title_zh: “连接点”：用RL训练长生命周期Agent的跨域泛化
authors:
- Yanxi Chen
- Weijie Shi
- Yuexiang Xie
- Boyi Hu
- Yaliang Li
- Bolin Ding
- Jingren Zhou
affiliations:
- Alibaba Group
arxiv_id: '2606.20002'
url: https://arxiv.org/abs/2606.20002
pdf_url: https://arxiv.org/pdf/2606.20002
published: '2026-06-18'
collected: '2026-06-19'
category: Agent
direction: Agent 长生命周期元能力训练
tags:
- long-lifecycle agents
- meta-RL
- end-to-end RL
- GRPO
- context management
- generalization
one_liner: 提出 CoD 框架，用端到端 RL 训练 LLM 在长序列任务中自我更新上下文，实现跨域泛化
practical_value: '- **长周期交互的Agent训练范式**：推荐/广告场景中的对话式Agent需在多个会话中持续积累用户偏好，可借鉴 CoD 的「解决任务
  + 更新上下文」交错部署模式，训练模型主动维护并利用对用户或环境的记忆。

  - **信用分配技巧**：采用动态规划思想，将每集回报定义为当前及未来任务奖励的均值，并以同位置轨迹均值作为基线计算优势，可迁移到多步推荐优化中，缓解长序列信用稀疏问题。

  - **探索激励环境设计**：通过隐藏关键信息（如动作映射）制造信息瓶颈，迫使模型主动探索，可用于构造模拟用户意图欠明确场景的训练集，提升 Agent 的主动信息获取能力。

  - **合成环境到真实业务的迁移**：实验显示在简单游戏环境中训练的元能力能泛化到终端仿真任务，业务中可尝试在低成本合成环境训练长生命周期能力，再迁移到真实业务
  Agent。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM 驱动的 AI Agent 在长期部署中需要持续探索环境、积累经验并自我更新上下文，以提升未来任务解决效率。现有 RL 训练多为单任务从零开始，与长生命周期部署脱节。为此，论文提出 “Connect the Dots”（CoD）元能力：在环境内连续解决不同但相关的任务，并主动更新上下文。

**方法关键点**：
- 框架设计：CoD-Deploy 抽象长期部署的「解决任务—更新上下文」交错过程；CoD-Train 采用完全匹配的 rollout 模式进行端到端 RL 后训练。
- RL 算法：基于 GRPO，设计精细信用分配——每集的回报取当前及未来所有解决任务奖励的均值，同位置的多条轨迹构成一组计算基线优势。引入自适应重加权缓解训练不稳定。
- 训练环境：设计 FrozenLake-Obscure（隐藏动作映射）和 Alchemy-Random（随机配方），通过信息隐藏迫使 Agent 必须依赖上下文传递知识，天然激励 CoD 行为。
- 评估：用更长任务序列和更高难度环境验证泛化，并测试未训练的 TerminalSimulator。

**关键实验**：
- 设定 A：仅用 FrozenLake-Obscure 训练，Qwen3-8B-Instruct 模型。训练后，首个任务（从零开始）平均奖励从 0.18 提升至 0.45，第 4 个任务（已累积上下文）从 0.28 提升至 0.76。
- 跨域泛化：同一模型在 Alchemy-Random 和 TerminalSimulator（CoD-Deploy 及 Ralph-loop 模式）上均观察到奖励提升，证明元能力跨域迁移。
- 设定 B：混合 FrozenLake-Obscure 和 Alchemy-Random 训练，同样展示跨域泛化，但训练稳定性略低，提示多域训练仍需优化。

**核心结论**：端到端 RL 可有效激发 LLM 的 CoD 元能力，使 Agent 通过自我更新上下文显著提升长序列任务表现，且该能力具有跨环境泛化潜力。
