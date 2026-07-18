---
title: 'Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov
  Jump Processes'
title_zh: 并发图像理解与生成：自校正耦合马尔可夫跳过程
authors:
- Minh-Quan Le
- Armand Comas
- Alexandros Lattas
- Stylianos Moschoglou
- Pedro Vélez
- Amit Raj
- Aaron Germuth
- Thabo Beeler
- Dimitris Samaras
- Di Qiu
affiliations:
- Google
- Google DeepMind
- Stony Brook University
arxiv_id: '2607.13188'
url: https://arxiv.org/abs/2607.13188
pdf_url: https://arxiv.org/pdf/2607.13188
published: '2026-07-13'
collected: '2026-07-18'
category: Multimodal
direction: 多模态耦合生成 · 自校正采样
tags:
- multimodal generation
- masked diffusion
- cross-modal coupling
- self-correction
- joint understanding
one_liner: 提出自校正耦合马尔可夫跳过程(SC-CMJP)与训练自由采样器CO₂Jump，实现多模态生成中跨模态实时纠错
practical_value: '- 多模态对话系统（如虚拟试穿、商品咨询）可借鉴 SC-CMJP 的跨模态置信度加权机制，确保生成的图文实时对齐，减少矛盾输出，提升用户体验。

  - CO₂Jump 无需额外训练，可在现有掩码扩散模型上即插即用，适合电商场景中快速迭代多模态生成能力（如产品图与描述同步生成）。

  - 自校正 remasking 可用于内容审核或智能设计：当生成图像与文本描述不一致时自动触发修正，保证多模态素材的合规性和一致性。

  - 去噪步数与性能单调正相关的结论，提示在 Agent 链式推理中加强跨模态交互的累积效应，为多步决策任务（如搜索→推荐→解释）提供架构参照。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有掩码扩散模型(MDM)在联合生成文本和图像时，要么交错解码，要么并行独立更新，仅共享上一步历史，未能实时利用对方最新决策，且无法重新掩码纠错，导致跨模态矛盾累积。

**方法关键点**：
- 提出自校正耦合马尔可夫跳过程(SC-CMJP)：一种模态的转移率由另一模态的置信度分数通过跨模态注意力加权决定，使生成过程相互感知。
- 引入 remasking 跳：当跨模态证据不支持已做出的决定时，主动撤回并修正，实现在线纠错。
- 基于 SC-CMJP 设计 CO₂Jump 采样器：训练自由、单趟完成，无需额外成本。
- 构建并开源三个大规模联合多模态生成数据集（JEdit-1M、JMaze-200K、JNono-200K）及分布内外基准。

**关键结果**：CO₂Jump 在图像编辑、理解和视觉推理（迷宫、数织）任务上达到最佳联合性能；采样器性能随去噪步数单调上升，验证了跨模态耦合的增益可沿生成长度累积。
