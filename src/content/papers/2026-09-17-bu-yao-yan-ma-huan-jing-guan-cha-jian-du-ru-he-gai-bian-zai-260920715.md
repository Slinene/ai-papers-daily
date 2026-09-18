---
title: 'Don''t Mask the Environment: Observation Supervision Changes How Agents Explore
  Under RL'
title_zh: 不要掩码环境：观察监督如何改变 Agent 在 RL 下的探索
authors:
- Juzheng Zhang
- Disha Makhija
- Manoj Ghuhan Arivazhagan
- Vinayshekhar Bannihatti Kumar
- Rashmi Gangadharaiah
affiliations:
- University of Maryland
- AWS AI Labs
arxiv_id: '2609.20715'
url: https://arxiv.org/abs/2609.20715
pdf_url: https://arxiv.org/pdf/2609.20715
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: Agent 轨迹 SFT 监督目标扩展
tags:
- Agent Training
- Observation Supervision
- GRPO
- SFT
- Exploration
one_liner: SFT 同时监督 observation token，无需额外数据即可提升后续 GRPO 的 pass@k 与探索多样性
practical_value: '- 在训练对话式推荐 / 搜索 Agent 时，SFT 阶段可以对环境返回的观察 token（如商品信息、搜索结果片段）也计算交叉熵损失，不增加数据、参数或序列长度，能显著提升后续
  RL 的采样质量（pass@k）。

  - 若 Agent 需要工具调用或多轮交互，联合监督 action 与 observation 可以防止模型过度特化于动作生成，保持对环境的预测能力，使 RL
  阶段策略更新幅度更小、更稳定。

  - 对于需要高多样性输出的场景（如广告文案生成、Query 推荐），可借鉴 ActObs 思路：在预训练或 SFT 时对“用户反馈”或“系统状态”也加监督，让
  RL 后模型保留更多熵，提升 pass@k 而非只追求 pass@1。

  - 工程实现上零额外成本：只需修改 loss mask，把原本作为上下文的 observation token 也纳入预测目标，即可复用现有 SFT 流水线。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：标准 SFT 只对 agent 自己产生的 action token 计算 loss，环境返回的 observation token 仅作为上下文。这种做法是否为下游 RL 提供了最优初始化？

**方法关键点**：
- 提出 ActObs：在 SFT 时同时监督轨迹中已经存在的 observation token，让模型学习预测动作后果。
- 部署时 agent 不生成 observation，但训练时预测 observation 不增加数据、参数、序列 token 或前向次数。
- 后续用 GRPO 做 RL，对比 action-only 初始化与 ActObs 初始化的差异。

**关键结果**：
- SFT 阶段两种方法性能相近，但经过 GRPO 后明显分化。
- Qwen3-4B 上，ActObs 初始化的 GRPO 在 Terminal-Bench 2.0 的所有采样预算下 pass@k 均高于 action-only。
- Qwen3-8B 上，牺牲少量 pass@1 换来更高 pass@k（pass@16 +3.4pp），并解决更多不同任务。
- 跨域代码编辑 aider-polyglot 上，4B 模型 pass@1 提升 4.2pp，任务在 SFT 和 RL 中均未见过。
- 分析显示：ActObs 在 RL 中保留更多熵，策略移动更少，最终策略更接近 SFT 初始化；原因是 SFT 中 action 与 observation 梯度迅速正交，action-only 遗留大量 observation 梯度残差并导致环境预测退化，联合监督避免了单边特化。
