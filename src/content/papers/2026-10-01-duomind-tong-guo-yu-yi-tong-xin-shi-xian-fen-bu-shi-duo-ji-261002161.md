---
title: 'DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication'
title_zh: DuoMind：通过语义通信实现分布式多机器人协调
authors:
- Hanchu Zhou
- Dechen Gao
- Hang Wang
- Brendan Lynch
- Boqi Zhao
- Qiyao Ma
- Raman Goyal
- Junshan Zhang
affiliations:
- University of California, Davis
- Microsoft Research
- Analog Devices
arxiv_id: '2610.02161'
url: https://arxiv.org/abs/2610.02161
pdf_url: https://arxiv.org/pdf/2610.02161
published: '2026-10-01'
collected: '2026-10-04'
category: MultiAgent
direction: 多智能体语义通信与分层协调
tags:
- Semantic Communication
- Multi-Robot Coordination
- VLM
- VLA
- Hierarchical Planning
- Distributed Systems
one_liner: 提出 DuoMind 分层框架，用 VLM 生成语义协调消息、VLA 执行底层动作，并构建 RoboPoly 基准验证多机器人长程协作
practical_value: '- 多智能体系统可借鉴分层架构：VLM 类大模型负责高层任务分解、状态理解与消息生成，下游 executor（VLA/工具调用/排序模型）负责底层精确执行；电商
  Agent 中可将 LLM planner 与推荐/搜索执行器解耦，减少长程任务中的误差累积。

  - 通信设计上不要传原始观测，而是传由 orchestrator 生成的简短、任务相关的语义消息；这能降低跨 Agent 通信带宽、隔离敏感特征，适合跨团队/跨域推荐与检索
  Agent 协作。

  - 每个 Agent 的规划步可同时输出“给自己的低层指令”和“给同伴的语义消息”，实现去中心化闭环协调；在业务 Agent 中可让节点在返回动作同时发布 state
  summary/intent，便于多 Agent 异步协同。

  - 评估上可借鉴 RoboPoly 强调长 horizon、闭环、分布式控制的做法，构建多 Agent 业务评测集，并通过消融实验区分“分层编排”与“语义通信”的收益，而不是只看最终业务指标。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：VLM/VLA 推动单机器人通用能力提升，但多机器人系统需要同时解决长时程协调与精细执行，现有方法和基准较少。

方法关键点：DuoMind 采用分布式分层框架，每个机器人包含 VLA-based action model 负责底层动作执行，VLM-based orchestrator 负责高层推理与机器人间协调；每个规划步，orchestrator 接收任务指令、本地观测和其他机器人消息，生成给 action model 的低层指令和给同伴的语义消息。该设计利用 VLM 的语义推理与 VLA 的精确动作生成互补优势。还提出 RoboPoly 基准，包含需要分布式闭环控制的长程操作任务。

结果：在 RoboPoly 和 RoboTwin 上 DuoMind 相比基线一致提升多机器人任务表现；消融实验验证分层编排与语义通信均有贡献。
