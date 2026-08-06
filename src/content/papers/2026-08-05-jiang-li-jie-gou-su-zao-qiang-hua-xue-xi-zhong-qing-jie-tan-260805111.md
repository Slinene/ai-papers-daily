---
title: Reward Structure Shapes the Interaction Between Episodic Exploration and Neural
  Memory in Reinforcement Learning
title_zh: 奖励结构塑造强化学习中情节探索与神经记忆的交互
authors:
- Jai Malegaonkar
- Rohan Patil
- Henrik I. Christensen
affiliations:
- UC San Diego
arxiv_id: '2608.05111'
url: https://arxiv.org/abs/2608.05111
pdf_url: https://arxiv.org/pdf/2608.05111
published: '2026-08-05'
collected: '2026-08-06'
category: Other
direction: 探索-记忆交互的奖励结构依赖性分析
tags:
- Exploration Bonuses
- Neural Memory
- Reward Structure
- Partial Observability
- RL
one_liner: 揭示探索奖励与记忆架构的互补关系取决于奖励结构而非密度
practical_value: '- 该工作为 RL 基础研究，业务可借鉴点有限，但其关于探索与记忆互补性的结论可启发电商搜索 Agent 中长序列决策：探索奖励应当与记忆容量协同设计，而非简单叠加。

  - 奖励信号的结构（监督何种记忆内容）会放大或抹平不同网络架构差异，类似推荐系统中，辅助目标的设计会改变序列模型对用户行为的记忆重点。

  - 提出的“结构稀疏”与“潜在稀疏”概念可迁移至长程用户兴趣探索场景：若短期行为奖励无法有效指引长期兴趣发现，需要专门的探索机制来弥补记忆负担。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：部分可观测 RL 中，探索与记忆常被独立研究，且稀疏奖励的定义混淆了信号密度与监督内容。需要厘清探索奖励与记忆架构的交互关系如何受奖励结构影响。

**方法关键点**：
- 设计三种环境，控制记忆内容的获取方式（需主动发现并保留、奖励直接监督的单一线索、纯定时观测流）。
- 交叉情节探索奖励（episodic bonus）与多种神经记忆架构（如 RNN、Transformer 等）。
- 操控奖励结构（而非密度），验证交互模式变化；提出观测锚定奖励机（observation-anchored reward machines），区分结构稀疏性（无需历史即可重现回报）和潜在稀疏性（单步奖励对探索行为定价错误）。

**关键结果**：
- 相同奖励信号在不同记忆内容场景下产生三种交互模式：① 放大架构差异（需无监督保留时）；② 统一至共同上限（存在单一奖励监督线索时）；③ 无影响（单纯定时观测）。
- 稠密奖励仅当直接监督所需记忆时才消除加成效应；微小探索惩罚（不改变最优策略）即可引向次优稳态，奖励能纠正。
- 揭示探索与记忆并非替代关系：奖励诱导暴露，记忆将暴露转化为回报。
