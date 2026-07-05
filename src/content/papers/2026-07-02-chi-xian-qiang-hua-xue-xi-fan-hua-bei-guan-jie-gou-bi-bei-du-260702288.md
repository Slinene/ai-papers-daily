---
title: 'Generalization in offline RL: The structure is more important than the amount
  of pessimism'
title_zh: 离线强化学习泛化：悲观结构比悲观程度更重要
authors:
- Max Weltevrede
- Matthijs T. J. Spaan
- Wendelin Böhmer
affiliations:
- Delft University of Technology
arxiv_id: '2607.02288'
url: https://arxiv.org/abs/2607.02288
pdf_url: https://arxiv.org/pdf/2607.02288
published: '2026-07-02'
collected: '2026-07-05'
category: Agent
direction: 离线RL泛化 · 悲观结构对称性
tags:
- offline RL
- generalization
- pessimism
- symmetry
- data augmentation
- consistency loss
one_liner: 在上下文MDP中，悲观结构的对称性而非悲观程度，决定了离线RL最优泛化；建议用策略提取一致性增强。
practical_value: '- 设计离线策略学习时，优先考虑数据覆盖的结构对称性，而不是盲目调节保守系数。

  - 数据增强不应仅用于扩充训练集，更应通过**策略提取阶段的一致性损失**注入对称归纳偏好，尤其适用于已知旋转、平移等对称性的推荐/Agent环境。

  - 若业务场景存在对称性（如用户偏好对商品类别旋转不变），可显式约束价值函数对称，以提升泛化。

  - 离线训练Agent时，避免在增强数据上直接做价值迭代，改用先离线训练再策略提取时加入一致性正则，能更稳定地利用增强。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：离线RL中的悲观程度常被认为与泛化存在权衡，过度保守会阻碍分布外泛化。本文在上下文MDP（CMDP）框架下揭示，**泛化好坏的关键不是悲观程度，而是悲观结构是否尊重底层对称性**。即使悲观程度很高，若价值函数保持对称，也能达到最优泛化；反之，轻微悲观但不对称的价值函数可能泛化失败。

**方法要点**：
- 理论上证明，在具有对称性的CMDP中，最优价值函数必须对称；数据覆盖结构决定了学到的悲观结构。
- 为了使悲观价值函数对称，可能需要数据增强（DA），但常见做法（在增强数据集上直接离线训练）会破坏悲观度的校准。
- 提出应在**策略提取阶段**引入一致性损失，让策略在面对对称变换时输出一致的动作，从而间接保持价值函数的对称性，而不干扰离线价值训练。

**实验结果**：在旋转对称的reacher环境中，使用IQL和CQL算法，策略提取阶段加入DA一致性损失，相比直接在增强数据上训练，能获得更高回报，验证了理论。
