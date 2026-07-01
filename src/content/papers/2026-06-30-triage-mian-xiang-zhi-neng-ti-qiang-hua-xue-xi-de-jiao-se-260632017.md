---
title: 'TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning'
title_zh: TRIAGE：面向智能体强化学习的角色类型化信用分配
authors:
- Yuanda Xu
- Zhengze Zhou
- Hejian Sang
- Xiaomin Li
- Jiaxin Zhang
- Xinchen Du
- Zhipeng Wang
- Alborz Geramifard
affiliations:
- LinkedIn Corporation
- Harvard University
- Johns Hopkins University
arxiv_id: '2606.32017'
url: https://arxiv.org/abs/2606.32017
pdf_url: https://arxiv.org/pdf/2606.32017
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent 角色条件信用分配
tags:
- GRPO
- Credit Assignment
- Agentic RL
- Process Reward
- Role-Typing
- Exploration
one_liner: 用角色标签（进展/探索/倒退）修正结果奖励，降低策略梯度方差，提升成功率与效率
practical_value: '- 在对话推荐、搜索导航等智能体训练中，用结构化判断器对轨迹片段打角色标签（决定性进展、有用探索、无进展基础动作、倒退），通过固定奖励映射（如探索给+0.2，倒退给-0.5）注入片段级过程奖励，直接纠正
  GRPO 的结果监督偏差，无需训练价值模型。

  - 即使任务失败，也可对探索行为给予小额正奖励，防止 GRPO 因统一惩罚而抑制智能体尝试新动作，从而在复杂交互环境（如商品搜索、多步决策）中维持探索。

  - 重点检测成功轨迹内的倒退动作（如重复点击、无效页面回退），并施加惩罚，能使策略学会更短路径完成任务，在实验中成功轨迹轮次额外减少约 10-15%，可直接用于优化电商智能体效率。

  - 该方法不需要学习奖励模型，只需一个可靠的角色分类器（可用 LLM 实现），工程成本低，适合快速集成到现有 GRPO 训练流程中。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：标准 GRPO 仅用最终结果作为统一优势信号，导致失败轨迹中惩罚有用探索，成功轨迹中奖励冗余或倒退动作，信用分配有盲点。

**方法关键点**：
- 提出 TRIAGE，在结果信用之上叠加语义角色轴：用结构化判断器将每个轨迹片段分为**决定性进展、有用探索、无进展基础动作、倒退**四类。
- 通过**固定角色条件规则**（如进展+1.0，探索+0.2，基础0，倒退-0.5）映射为有界片段级过程奖励，保持结果信号为优化方向，同时修正其偏差。
- 理论证明该角色条件信用是仅从角色标签可表达的最优片段级优势残差校正，能降低优势估计误差，得到更低方差的策略梯度。

**关键结果**：
- 在 ALFWorld、Search-QA、WebShop 上，相比 GRPO，TRIAGE 显著提升两种策略模型的成功率，并优于标量过程奖励及共享主干价值基线。
- 消融显示增益来自角色类型而非简单增密奖励：成功轨迹中检测倒退是主因，探索信用提供稳定辅助提升。
- 在已完成轨迹上，TRIAGE 相对 GRPO 额外减少环境交互轮次**10.4%** 和 **14.8%**。
