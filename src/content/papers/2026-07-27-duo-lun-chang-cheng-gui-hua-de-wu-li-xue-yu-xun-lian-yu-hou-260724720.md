---
title: 'The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training
  via Single- and Multi-Teacher On-Policy Agentic Distillation'
title_zh: 多轮长程规划的物理学：预训练与后训练阶段的智能体蒸馏研究
authors:
- Tianyi Men
- Zhuoran Jin
- Kang Liu
- Jun Zhao
affiliations:
- 中国科学院自动化研究所复杂系统认知与决策智能重点实验室
- 中国科学院大学人工智能学院
arxiv_id: '2607.24720'
url: https://arxiv.org/abs/2607.24720
pdf_url: https://arxiv.org/pdf/2607.24720
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: Agent 多轮长程规划能力分析
tags:
- Agentic Planning
- On-Policy Distillation
- GRPO
- World Model
- Multi-Turn
- Compositional Generalization
one_liner: 构建可控环境系统分析LLM智能体多轮长程规划的获取、塑造与集成机制
practical_value: '- **预训练数据构造**：构建多轮交互推荐/搜索Agent时，预训练阶段加入显式世界模型（如状态转移链式推理）数据，并混合少量长程轨迹，仅靠原子技能无法组合泛化。

  - **后训练算法选择**：若预训练数据质量不高或任务轮次长，优先使用在线策略蒸馏（OPD）而非GRPO，OPD更新方向更一致，有效区域更广。

  - **错误累积控制**：长程任务中次优轨迹的误差放大效应显著，在推荐Agent流程中可植入早期信号校验或中断机制，防止错误级联。

  - **多教师知识集成**：引入不同领域知识时，避免直接蒸馏冲突的规划模式，可通过寻找共享模式实现跨环境泛化，部分共享模式支持持续学习。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：基础模型智能体的多轮长程规划能力如何获得难以捉摸，现有模型在不可控的互联网数据上训练，无法厘清规划能力的获取、塑造与集成过程。

**方法关键点**：
- 构建统一可控的多轮环境，支持精确控制任务长度、数据质量、规划知识与模式。
- 将长程规划研究分解为三个阶段：预训练（能力获取）、单教师后训练（能力塑造）、多教师后训练（能力集成）。
- 预训练阶段分析数据格式、分布与质量的影响；后训练阶段基于互信息区分通用规划模式与任务特定知识，并对比GRPO与在线策略蒸馏（OPD）的适用区域；多教师在线策略蒸馏（MOPD）探究模式共享与冲突对能力集成的影响。

**关键结果**：
- 预训练中，通过思维链状态转移建模显式构建世界模型，长程泛化能力显著优于直接动作预测。纯原子技能训练无法实现组合泛化，增加少量长程数据即大幅提升。次优轨迹使错误随轮次放大，严重损害性能。
- 后训练中，OPD在低质量预训练数据或长轮次下有效区域宽于GRPO，能提供更一致的更新方向；但从不同知识背景的教师蒸馏未见程序可能损害学生已有世界模型。
- 多教师集成时，共享规划模式支持跨环境泛化，部分共享利于持续学习，完全冲突则造成严重干扰。
