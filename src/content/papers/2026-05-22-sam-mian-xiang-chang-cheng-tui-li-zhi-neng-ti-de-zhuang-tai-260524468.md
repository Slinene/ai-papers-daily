---
title: 'SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent'
title_zh: 'SAM: 面向长程推理智能体的状态自适应记忆'
authors:
- Yuyang Hu
- Hongjin Qian
- Shuting Wang
- Jiongnan Liu
- Ziliang Zhao
- Jiejun Tan
- Zheng Liu
- Zhicheng Dou
affiliations:
- GSAI, Renmin University of China
- Beijing Academy of Artificial Intelligence
arxiv_id: '2605.24468'
url: https://arxiv.org/abs/2605.24468
pdf_url: https://arxiv.org/pdf/2605.24468
published: '2026-05-22'
collected: '2026-05-27'
category: Agent
direction: 长程推理 Agent 记忆管理 · 状态自适应记忆
tags:
- State-Adaptive Memory
- Long-Horizon Agent
- Context Management
- OAT-GRPO
- Episodic Recall
- Memory Augmentation
one_liner: 提出状态自适应记忆框架 SAM，通过记忆线索与意图驱动回忆让智能体从长历史中重建决策支撑信息，无需重训练骨干模型
practical_value: '- **独立的记忆模块与主干解耦**：记忆模型独立训练、跨主干复用，适合在已有电商对话/推荐 Agent 上植入长程记忆，避免改造主干模型。

  - **分页存储 + 轻量线索**：将冗长的交互历史分页并压缩为 compact cues，仅保留线索在上下文，释放 context window；可借鉴到多轮对话或搜索推荐场景的长序列管理中。

  - **意图驱动的按需回忆**：只有在需要时才根据当前状态选择线索召回原始页面并重建所需信息，比一把摘要或窗口截断更精准，适合电商场景中先分散探索、后期需综合早前信息的任务。

  - **OAT-GRPO 训练范式**：将记忆调用建模为树结构，用专家委员会评估可恢复性并奖励下游任务成功，为训练独立的记忆模块提供了一种闭环方案，可迁移到需要优化长期决策质量的
  Agent 训练中。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：长程智能体推理（如深度搜索、多步浏览）面临交互历史不断增长、信息分散在不同时间步的挑战。现有方法或截断历史、或全局摘要、或简单检索，但均未根据智能体当前决策状态自适应地提供所需信息。作者将长程上下文管理重新定义为 **状态自适应记忆** 问题：智能体在任意时刻需要的是当前决策状态相关的支持信息，而非完整历史。

**方法关键点**：
- **分页存储与记忆线索（cues）**：将轨迹按 token 预算切分为页面，对每个页面生成一个 compact cue 作为轻量指针，并保留原始页面在外部存储。Cues 留在上下文作为持久的历史索引，避免重复传递完整页面。
- **意图驱动的回忆**：当需要访问过去信息时，智能体根据当前意图选择相关 cues，记忆模型从对应页面重建最相关的决策支撑内容并注入上下文，实现按需、状态条件化的信息访问。
- **独立记忆模块优化**：记忆模型与 Agent 主干解耦，训练分两阶段：
  1. **专家监督微调**：利用前沿模型（Claude-4.5-Opus、GPT-5.4）在正确轨迹上生成线索和回忆结果作为标记，对记忆模型进行 SFT。
  2. ** OAT-GRPO 强化学习**：设计树状记忆调用展开，在每次回忆处分支采样，并引入由专家委员会评估的可恢复性奖励和最终任务奖励，按动作级优势更新记忆模型。

**关键结果**：在 BrowseComp、BrowseComp-ZH、WideSearch、HLE 四个长程基准上，SAM 在两个 Agent 主干（GLM-4.7、Qwen3.5-35B-A3B）上均全面超越无记忆基线及其他上下文管理策略（最近k步、摘要、丢弃工具输出）。以 GLM-4.7 为例，BrowseComp 上 SAM 达到 56.5，比无管理（43.5）提升 13 个百分点，比最佳启发式 summary（53.5）仍有显著优势。消融表明 SFT 与 OAT-GRPO 互补，意图驱动的回忆是关键增益来源，而非简单的页面压缩；方法对页面大小（32K–96K）鲁棒，且在长轨迹（>80 轮）上优势更明显。
