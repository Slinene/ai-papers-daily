---
title: 'AutoMem: Automated Learning of Memory as a Cognitive Skill'
title_zh: AutoMem：将记忆管理作为可训练技能的自动化学习框架
authors:
- Shengguang Wu
- Hao Zhu
- Yuhui Zhang
- Xiaohan Wang
- Serena Yeung-Levy
affiliations:
- Stanford University
arxiv_id: '2607.01224'
url: https://arxiv.org/abs/2607.01224
pdf_url: https://arxiv.org/pdf/2607.01224
published: '2026-07-01'
collected: '2026-07-02'
category: Agent
direction: Agent 记忆管理自动化 · 长程任务优化
tags:
- memory management
- agent
- metamemory
- long-horizon tasks
- LLM fine-tuning
- automated optimization
one_liner: 通过双循环自动优化记忆结构与训练记忆熟练度，将记忆管理变为可学习技能，在长程游戏中实现2-4倍性能提升
practical_value: '- **可迁移的记忆架构**：将文件系统操作提升为一级记忆动作，与任务动作并列，让模型自行决定何时读写笔记。电商推荐Agent可借鉴此模式，维护用户长期偏好文件、会话上下文文件，实现跨会话记忆。

  - **自动优化记忆提示与模式**：手工设计记忆结构（提示、文件模式、动作词汇）在长程任务中不可行。可借鉴其外循环思路，用强LLM审查历史推荐交互的完整轨迹，自动迭代优化Agent的记忆结构，减少人工工作量。

  - **利用成功轨迹训练记忆决策**：内循环从大量episodes中提取好的记忆决策（何时记录偏好、何时检索历史），作为微调信号。在搜索/推荐Agent中，可挖掘用户满意会话，训练模型做出更好的记忆操作，提升长期用户体验。

  - **记忆与任务分离的优化范式**：仅优化记忆技能，不改动任务动作行为，就带来巨大提升。表明在复杂推荐系统中，可将记忆管理作为独立模块针对性优化，性价比高。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：长程任务中，LLM智能体的记忆管理至关重要，但手工设计记忆结构（提示、文件模式、动作词汇）极其困难，且记忆错误会在数千步后才暴露，难以通过人工审查全轨迹来优化。认知科学认为记忆是一种可学习的元技能（metamemory），受此启发，工作将记忆管理视为可独立训练的技能。

**方法**：提出AutoMem框架，包含双循环自动化优化。外层结构优化循环：用一个强LLM审查完整的agent轨迹，迭代修订记忆结构文档（包括内存文件布局、读写动作词汇、何时使用记忆的提示），让agent与记忆的交互方式更合理。内层熟练度训练循环：从大量episodes中自动识别agent自身做出的正确记忆决策（如恰当的存储/检索时刻），将这些决策作为训练信号，直接微调模型，提升其记忆执行力。整个过程无需人工干预，记忆优化与任务动作优化分离。

**结果**：在Crafter、MiniHack、NetHack三个程序生成的长程游戏上测试，仅优化记忆结构（未改动任务动作行为），基准agent性能提升约2-4倍。对Qwen2.5-32B-Instruct模型，在内层额外训练后，性能可匹敌Claude Opus 4.5、Gemini 3.1 Pro Thinking等前沿闭源系统。证明记忆管理是独立的高杠杆优化目标。
