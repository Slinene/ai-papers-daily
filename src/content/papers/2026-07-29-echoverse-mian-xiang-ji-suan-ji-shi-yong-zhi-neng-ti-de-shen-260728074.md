---
title: 'Echoverse: Deep, Evolving Environments for Training Computer-Use Agents at
  Scale'
title_zh: Echoverse：面向计算机使用智能体的深度演化训练环境
authors:
- Yash Pandya
- Sahil Gupta
- Sarthak Harne
- Archana Yadav
- Kavyansh Chourasia
- Hussein Mozannar
- Vibhav Vineet
- Sara Abdali
- Corby Rosset
- Yash Lara
affiliations:
- Microsoft Research
arxiv_id: '2607.28074'
url: https://arxiv.org/abs/2607.28074
pdf_url: https://arxiv.org/pdf/2607.28074
published: '2026-07-29'
collected: '2026-07-31'
category: Training
direction: 合成环境生成与协同演化训练 Agent
tags:
- Computer-Use Agents
- Training Environments
- Co-evolution
- Synthetic Data
- Reinforcement Learning
- Stateful Applications
one_liner: 通过协同演化循环构建有深度、可自适应修复的合成环境，显著提升计算机使用智能体的性能与迁移能力
practical_value: '- 可借鉴协同演化循环，为电商搜索推荐 Agent 构建有深度的模拟环境（如带状态变化的用户会话），通过 rollout 反馈动态修复任务和验证逻辑，增强
  Agent 对复杂交互的适应力。

  - 利用数据库确认验证器（grounded verifier）设计推荐系统的离线评估环境，确保奖励与系统状态强一致，减少奖励黑客问题。

  - 在用户模拟器迭代中引入环境修复机制，根据真实失败案例自动生成针对性训练任务，提升模拟器的覆盖率和真实性。

  - 强化学习训练时，采用稀疏任务完成奖励与密集步骤奖励结合的混合 reward 设计，加速策略收敛并提高最终效果。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：训练计算机使用智能体需要能交互、可重置的有状态应用，但真实环境多为登录限制的封闭系统，合成环境成为关键替代。现有批量生成方法解决了数量问题，但缺乏行为深度与演化能力，训练效果受限。

**方法**：提出 Echoverse，将规范编译为有状态应用，任务完成通过与应用的数据库比对进行确认验证。核心是一个协同演化循环：在每次 rollout 评分后，一方面修复环境 Bug、调整任务难度、改进验证器；另一方面将成功/失败交互作为训练信号微调模型。这种双向反馈使环境与模型共同提升。

**关键结果**：在12个演化环境中训练后，9B 模型在14个评测集上准确率从36.5%提升至67.1%，仅比教师大模型低14个百分点。消融显示：深层环境将在线准确率从80.0%提升到85.0%（浅层环境反降至75.0%）；对单一界面控制进行多样化渲染训练后，知识可迁移到未见过的控件族和开放网页；修复单个环境使模型在该环境上从16.2%升至38.5%。用作强化学习空间时，结合确认验证器与密集步级裁判，保留集分数从58.8%提升至68.0%。
