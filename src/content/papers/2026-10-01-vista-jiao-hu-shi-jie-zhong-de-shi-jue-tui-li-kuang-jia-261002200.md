---
title: 'VISTA: A Visual Harness for Reasoning in an Interactive World'
title_zh: VISTA：交互世界中的视觉推理框架
authors:
- Qiushi Han
- Keya Hu
- Linlu Qiu
- Cathy Wu
- Kaiming He
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2610.02200'
url: https://arxiv.org/abs/2610.02200
pdf_url: https://arxiv.org/pdf/2610.02200
published: '2026-10-01'
collected: '2026-10-04'
category: Agent
direction: 视觉增强多模态 Agent 长程推理
tags:
- Visual Agent
- Multimodal Model
- Visual Memory
- Interactive Environments
- Harness
one_liner: 多模态模型通过无损视觉记忆和主动视觉检索，在交互环境中大幅提升推理与行动效率
practical_value: '- **无损视觉记忆可复用**：在电商多模态 Agent 中，保留商品图、详情页截图等原始视觉信息，避免早量压缩，提升长程浏览与比较任务的表现。

  - **主动视觉检索机制**：让模型自行决定何时回看历史视觉观察（如之前看过的商品、对比图），减少人工设计的状态管理，适用于购物助手、视觉搜索等交互场景。

  - **迭代视觉工具调用**：将视觉输入拆解为可重组的片段（裁剪、放大、并排比较），在推理时动态调用，比一次性全图编码更灵活，适合复杂商品页面的多区域分析。

  - **低适配成本**：VISTA 的设计便于迁移到不同视觉环境，从业者可尝试将类似 harness 嵌入已有 VLM Agent，快速提升在视觉决策任务中的表现。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有语言 Agent 依赖文本观察，多模态 Agent 虽能接收图像，但视觉编码通常是有损压缩，丢失细节且历史观察难以完整保留，限制了模型在交互环境中的长程推理能力。

**方法关键点**：VISTA 是一个视觉 harness，让通用多模态模型直接通过视觉观察感知环境，并维护**无损视觉记忆**，以原始形式存储过去的每一帧观察。模型可以**主动检索**这些历史视觉观察，并在推理过程中**重新组织视觉输入**（例如并排比较、放大细节），而不受固定上下文窗口或文本摘要的限制。整个 harness 设计简洁，仅需少量修改即可适配不同视觉环境。

**关键结果**：在 ARC-AGI-3 上，VISTA 将 Claude Opus 5.0 的 Relative Human Action Efficiency 从 40.68 提升到满分 100.00，完成全部 25 个公开游戏，且动作次数比首次人类参与者少 57.4%。在另外三个覆盖多种视觉游戏和谜题的基准上，VISTA 也大幅超越相同底层模型配合最小 harness 的 baseline，验证了该方法的通用性。
