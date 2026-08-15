---
title: Self-Evolving Embodied Agents via Skill-Harness Evolution
title_zh: 通过技能与上下文代码进化实现自进化具身智能体
authors:
- Peidong Wang
- Zhiming Ma
- Ying Chang
- Xufang Luo
- Xiaocui Yang
- Shi Feng
- Yuqing Yang
- Dongsheng Li
affiliations:
- Northeastern University
- Microsoft Research
arxiv_id: '2608.11350'
url: https://arxiv.org/abs/2608.11350
pdf_url: https://arxiv.org/pdf/2608.11350
published: '2026-08-10'
collected: '2026-08-15'
category: Agent
direction: Agent 自进化 · 技能与harness优化
tags:
- Embodied Agents
- Self-Evolving
- Skill Harness
- Train-free
- Foundation Models
- Test-time Adaptation
one_liner: 提出SHAPER框架，冻结模型参数，通过环境交互进化可复用技能与上下文代码harness，实现无需训练的具身Agent自进化
practical_value: '- 在电商/Agent系统中可借鉴将LLM同时用作planner和optimizer：冻结模型，将成功经验沉淀为可复用技能（类似结构化RAG），通过目标环境rollouts自我进化，避免频繁微调带来的数据和算力成本。

  - 将prompt模板、工具调用逻辑、上下文代码视为可优化的外部参数（harness），在线上交互中持续调整，这与推荐系统中优化召回策略、重排规则等非参数组件思路一致，可低风险快速迭代。

  - 在无法标注大量数据或训练成本过高时，优先尝试基于test-time scaling的train-free方案（如verifier-free selection、voting）作为基线，可能接近SFT效果，适合初创或快速验证场景。

  - 注意该工作针对具身智能体，业务落地时需抽象其核心：固定模型权重，进化外部技能库和任务编排，对电商Agent的多轮对话、工具调用、query理解等模块具备直接迁移价值。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：具身智能体系统依赖基础模型及模型外部的技能、上下文、动作接口等非参数组件。传统SFT/RL需要额外数据和训练，而代码中心方法依赖可编程机器人API，在固定接口环境不可用。需要一种无需训练、能通过环境交互自我改进的Agent框架。

**方法关键点**：提出SHAPER，冻结模型参数，将同一模型同时作为planner和optimizer。在目标环境执行rollouts，模型规划动作并执行，根据反馈优化外部组件：①可复用技能（将成功经验抽象为可调用的skill）；②上下文代码harness（封装上下文管理与动作接口适配的代码模板）。通过迭代进化技能库和harness实现性能提升，无需更新模型权重。

**关键结果**：在VLABench和ESI-Bench两个具身基准上，SHAPER优于纯执行基线，并在部分设置下接近或超过SFT和test-time scaling基线（如verifier-free selection、voting），表明当模型训练昂贵或不可行时，技能与harness优化是自进化Agent的实用路线。
