---
title: 'Experience Memory Graph: One-Shot Error Correction for Agents'
title_zh: 经验记忆图：智能体的一次性错误修正
authors:
- Wenjun Wang
- Yuchen Fang
- Fengrui Liu
- Zibo Liang
- Kai Zheng
affiliations:
- University of Electronic Science and Technology of China
- Yangtze Delta Region Institute (Quzhou), UESTC
- Shenzhen Institute for Advanced Study, UESTC
arxiv_id: '2607.13884'
url: https://arxiv.org/abs/2607.13884
pdf_url: https://arxiv.org/pdf/2607.13884
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: 图匹配驱动的Agent一次性错误纠正
tags:
- Error Correction
- Graph Matching
- Experience Memory
- LLM Agents
- One-Shot Learning
- Self-Correction
one_liner: 通过图匹配失败与成功轨迹，提取编辑操作实现零试错的Agent错误修复
practical_value: '- 对推荐/对话Agent的失败修复：可离线从成功与失败轨迹构建动作决策图，在线匹配快速纠正，避免反复试错带来的延迟和成本。

  - 跨任务泛化：利用跨任务边共享修正经验，例如电商搜索中不同品类下的意图误解或步骤遗漏问题，可复用修正模式。

  - 工程轻量：记忆图可预先构建，推理时仅需子图匹配与编辑操作检索，不依赖大模型多次推理，适合低延迟场景。

  - 扩展至生成式推荐：在生成式推荐流程中，若出现不合理item生成，可借鉴编辑路径思想（增、删、替换）快速调整上下文，提升生成质量。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent在长程任务中常因累积错误导致失败，现有反思机制依赖提示词迭代试错，成本高、难泛化。

**方法**：提出经验记忆图（EMG），将失败恢复建模为图匹配问题。训练阶段，将失败与成功轨迹转化为有向动作决策图，通过图匹配提取：1) 公共子图（成功工作流），2) 图编辑路径（指示如何增、删或重标记动作来纠正失败）。这些子图和编辑路径存入记忆图，包含任务内节点和跨任务边。测试时，EMG根据当前观察检索相关编辑路径，直接指导Agent一次性执行，无需试错。

**结果**：在ALFWorld和ScienceWorld上，EMG的成功率和平均奖励均超越Reflexion等最强基线，同时消除了测试时的反复试错，显著降低时间和API成本。
