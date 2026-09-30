---
title: 'Learning What to Remember: Long-horizon Counterfactual Memory Optimization'
title_zh: 学习该记住什么：长时程反事实记忆优化
authors:
- Jiaming Tang
- Mingyan Liu
- Armin Sarabi
affiliations:
- University of Michigan
arxiv_id: '2609.37930'
url: https://arxiv.org/abs/2609.37930
pdf_url: https://arxiv.org/pdf/2609.37930
published: '2026-09-29'
collected: '2026-09-30'
category: Training
direction: 长时记忆优化 · 反事实信用分配
tags:
- Memory Optimization
- Counterfactual Credit Assignment
- PPO
- Long-context LLM
- Document-level IE
- Potential-based Reward Shaping
one_liner: 提出 MGPO 用反事实差分给每次记忆改写分配长时程增量效用，训练紧凑可迁移记忆策略
practical_value: '- 在会话式推荐或多轮 Agent 中，对用户画像/上下文的每次更新，用反事实差分评估该更新对后续推荐或决策的增量价值，而不是仅用最终转化或奖励信号，能更准确地学习何时保留、丢弃或改写记忆。

  - 工程上解耦记忆写入器与下游读取器（推荐模型/LLM），可以用小模型训练 compact 记忆生成策略，再服务于多个大模型，降低推理延迟和成本；论文中 8B
  writer + 14B reader 的组合可跨模型家族复用。

  - 采用 potential-based reward shaping 技巧：从回报中减去更新前状态的未来效用作为控制变量，保持策略梯度无偏同时降低方差，训练更稳定。

  - 对于长文档/长会话中延迟价值的信息，设计跨未来多个步骤的边际收益聚合，并用位置相关 EMA 归一化不同步长的回报，可借鉴到长时记忆策略的 RL 训练。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

动机：持久记忆允许 LLM 在长交互中携带信息，但有限容量要求选择性保留。学习记忆更新的困难在于信用分配：一次改写可能很久之后才有用，且最终效用可能主要继承自已有记忆。本文提出 MGPO 解决该问题。

方法关键点：
- 将记忆写入和读取解耦，可学习 writer 更新有界文本记忆，冻结 reader 评估效用。
- 对每次重写，比较前后记忆状态在同一目标上的效用差，跨未来所有目标聚合得到 Memory Gain。
- 证明 Memory Gain 是 potential-based reward shaping，不改变策略梯度但降低方差。
- 用 PPO 优化，position-wise EMA 校准回报，KL 正则。
- 在文档级 IE 上构造可加 F1 代理作为效用。

关键结果：
- SciREX 上实体聚类 F1 比 Direct Readout 提升 30.9%，关系 F1 提升 60.6%，同时平均记忆长度从 202 降至 43（-78.7%）。
- AIPAN-10K 跨域迁移超过其他 learned memory 方法，实体聚类 F1 39.2，关系 F1 22.9。
- 消融显示长时程反事实信用优于仅用 factual reward 等变体。

最值得记住的一句话：学习记忆的关键是给每次改写分配其独有的长时程边际效用，而非奖励整个记忆状态。
