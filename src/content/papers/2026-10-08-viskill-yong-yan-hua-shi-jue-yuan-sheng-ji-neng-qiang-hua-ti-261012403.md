---
title: 'ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills'
title_zh: ViSkill：用演化视觉原生技能强化 VLM 智能体
authors:
- Hongxing Li
- Dingming Li
- Yixin Li
- Yong Du
- Wenqi Zhang
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Yongliang Shen
affiliations:
- Zhejiang University
arxiv_id: '2610.12403'
url: https://arxiv.org/abs/2610.12403
pdf_url: https://arxiv.org/pdf/2610.12403
published: '2026-10-08'
collected: '2026-10-11'
category: Agent
direction: Agent 强化学习 · 视觉技能库
tags:
- VLM Agents
- Reinforcement Learning
- Skill Library
- Visual-Native
- PPO
- Sample Efficiency
one_liner: 提出 ViSkill，将成功轨迹编码为视觉原生技能卡，检索引导推理与奖励塑造，形成技能库与策略优化闭环
practical_value: '- 视觉原生技能表示：在电商导购/UI 自动化 Agent 中，截图、布局标注等视觉信息不要全部文本化；把成功交互的关键帧保存为“视觉技能卡”，检索后直接作为多模态上下文，减少空间关系丢失，提高策略泛化。

  - 技能库与策略优化闭环：将成功轨迹蒸馏回技能库，并让检索技能同时用于推理和奖励塑形，使技能积累与策略改进互相强化；业务 Agent 可用类似机制积累成功会话片段，提升样本效率。

  - 冷启动机制：用少量高质量演示初始化技能库，加速早期 RL 训练；新业务或新场景上线时，可从历史专家轨迹构建种子技能库，减少冷启动成本。

  - 奖励塑形技巧：引入检索技能相似度作为辅助奖励，有助于稳定训练，但需监控技能库陈旧度避免误导策略。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有技能增强型智能体多为文本中心，将空间布局和动作-状态对应线性化为语言，丢失关键几何结构；近期工作开始引入视觉证据，但技能构建与策略优化分离，未能实现相互增益。

**方法关键点**：ViSkill 是一个视觉原生技能学习框架，把成功交互轨迹编码为复合视觉技能卡，直接供 VLM 智能体访问。检索到的技能同时用于指导推理和奖励塑形；成功轨迹被蒸馏回技能库，形成技能积累与策略改进的闭环。可选冷启动机制用少量演示初始化技能库，加速早期学习。

**关键结果**：在 Sokoban、FrozenLake、PrimitiveSkill 三个环境上，ViSkill 总体成功率达 0.89，冷启动初始化为 0.91，超过所有专有和开源基线，且收敛速度快于标准 PPO。
