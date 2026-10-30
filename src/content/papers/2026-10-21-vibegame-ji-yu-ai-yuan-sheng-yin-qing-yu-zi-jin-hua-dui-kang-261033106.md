---
title: 'VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving
  Adversarial Agent Team'
title_zh: VibeGame：基于 AI 原生引擎与自进化对抗智能体团队的提示词生成游戏
authors:
- Wenbo Hu
- Ken Li
- Jiazhe Wei
- Yukang Cao
- Weiyi Hong
- Jiayi Dai
- Chenjun Bai
- Jiajun Liang
- Yucheng Liao
- Ruichuan An
affiliations:
- PRLab, Nanjing University
- S-Lab, Nanyang Technological University
- Liblib.ai
arxiv_id: '2610.33106'
url: https://arxiv.org/abs/2610.33106
pdf_url: https://arxiv.org/pdf/2610.33106
published: '2026-10-21'
collected: '2026-10-30'
category: MultiAgent
direction: 多智能体对抗式游戏生成
tags:
- Multi-Agent
- LLM
- AI-Native Engine
- Self-Evolution
- Game Generation
- Schema-Validated State
one_liner: 用 AI 原生引擎与八个专用对抗智能体，从提示词端到端生成可玩 2D 游戏项目
practical_value: '- **可借鉴的结构化可执行状态**：把复杂系统状态定义为 schema-validated text，并提供 frame/time-step
  同步的 inspect/execute/verify 接口；可迁移到广告出价、query 改写等 Agent 场景，将候选 query、context、约束写成结构化状态，critic
  agent 分步读取、回滚和验证，避免直接依赖全量代码。

  - **实施者/审查者对抗解耦**：用多个 specialist agents 把生成与审查分离，多轮 loop 找问题；可复用到搜索广告文案、商品推荐理由生成
  pipeline，一个 agent 产出、一个 agent 基于规则或仿真反馈审查，降低线上事故风险。

  - **训练免费自进化机制**：将成功项目蒸馏为 skeletons、modules 和 collaboration contracts，作为未来任务的模板；业务中可把历史成交的
  prompt 工作流沉淀为可复用 SOP、模块库和 agent 间接口契约，减少每次从零生成并提升多 agent 协作稳定性。

  - **评估思路**：PA2G 与 P2G 区分“给定资产库”和“自主生成资产”，能更干净地评估 agent 的规划与集成能力；推荐实验也可区分“给定候选”与“生成候选”，定位系统瓶颈。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM agent 已能用自然语言辅助软件开发，但端到端游戏开发仍难：需要同时协调代码、场景、资产、动画、物理与配置，并要求开发者通过交互测试验证整体行为。

**方法关键点**：VibeGame 构建了一个 AI-native game engine，将项目状态表示为 schema-validated 结构化文本，并提供 frame-synchronous runtime control，使 agent 能按自身节奏 inspect game state、execute actions、verify behavior。在此接口上设计 Adversarial Agent Team，由八个专用 agent 将 implementation 与 review 分离，通过多轮 loop 发现问题并修复。对每个验收通过的项目，引入训练无关的 self-evolution 机制，将其蒸馏为可复用的 skeletons、modules 和 collaboration contracts，供后续开发使用。

**关键结果**：在 GameCraft-Bench 子集上评估 PA2G（给定资产库）和 P2G（自主生成美术）。VibeGame 在 P2G 设置下，相较同样底层模型的一系列 agent harnesses 持续更优，包括 GPT-6.1-Sol。
