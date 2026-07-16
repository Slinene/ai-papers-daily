---
title: 'SPyCE: Skill-Policy Co-evolution for Multimodal Agents'
title_zh: SPyCE：多模态智能体的技能-策略协同进化框架
authors:
- Ru Zhang
- Weijie Qiu
affiliations:
- Zhejiang University
- Beijing University of Posts and Telecommunications
arxiv_id: '2607.13854'
url: https://arxiv.org/abs/2607.13854
pdf_url: https://arxiv.org/pdf/2607.13854
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: 多模态Agent · 技能-策略协同进化
tags:
- Multimodal Agent
- Skill Library
- Reinforcement Learning
- Hierarchical Skills
- Co-evolution
- Tool Use
one_liner: 将多模态推理轨迹蒸馏为层级技能库，与策略在强化学习中协同进化，形成自我改进闭环
practical_value: '- 构建层次化技能库：执行技能（局部视觉操作）和工作流技能（高层工具编排），可直接复用于电商多模态Agent设计，将商品图片分析、多步工具调用沉淀为可复用模块。

  - 技能与策略闭环进化：在线RL中，用策略生成的高分轨迹持续更新技能库，再用检索到的技能引导策略探索，可实现Agent自我改进，适合需要长期运行的搜索推荐辅助Agent。

  - 检索增强的策略条件：将历史成功技能作为先验注入策略模型，可大幅提高样本效率，尤其适用于多步交互场景（如智能客服、视觉比货），避免从零开始探索工具使用模式。

  - 视觉操作封装：把图像裁剪、对比、OCR等原子操作抽象为执行技能，可构建可组合的视觉推理流水线，降低MLLM直接操作像素的复杂度。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有多模态Agent要么仅靠强化奖励从零摸索可复用的工具使用模式，要么依靠静态记忆做测试时检索，缺乏将经验内化到策略的机制。论文洞察到，多模态推理轨迹应被蒸馏为可重用技能，并在训练中与策略协同进化。

**方法**：提出SPyCE框架，包含三层结构：执行技能捕获局部视觉操作（如图像裁剪、放大），工作流技能编码高层工具调用先验（如先搜索再比较），以及策略模型自身。训练时，策略以检索到的相关技能为条件进行rollout，生成轨迹后根据奖励筛选高质量样本，将其蒸馏进技能库；同时，技能库的更新又可以提供更强的先验引导策略探索，形成闭环进化。

**关键结果**：在8个多模态推理与工具使用基准上，SPyCE全面超越RL基线（如RLHF、PPO）和记忆基线（如RAG）。消融实验证实层次化技能设计和协同进化机制对性能提升至关重要：移除工作流技能或停止技能库更新均导致显著下降。该框架为构建自改进的多模态Agent提供了新范式。
