---
title: 'ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both'
title_zh: ATLAS：一个词同时实现Agentic与潜在视觉推理
authors:
- Ziyu Guo
- Rain Liu
- Xinyan Chen
- Pheng-Ann Heng
arxiv_id: '2605.15198'
url: https://arxiv.org/abs/2605.15198
pdf_url: https://arxiv.org/pdf/2605.15198
published: '2026-05-13'
collected: '2026-05-17'
category: Reasoning
direction: 视觉推理 · 功能token
tags:
- Visual Reasoning
- Functional Token
- Agentic Reasoning
- Latent Reasoning
- Next-Token Prediction
- LA-GRPO
one_liner: 用单一离散功能token统一agentic操作与潜在视觉推理，无需视觉监督，兼容标准训练
practical_value: '- 功能token设计思路：在多模态对话或视觉Agent中，可将复杂视觉操作封装为离散token，避免生成中间图像，大幅降低计算开销。

  - LA-GRPO训练技巧：当行为token稀疏时，用静态加权的辅助目标锚定功能token，可稳定强化学习训练，适合电商Agent中稀疏动作（如工具调用）的场景。

  - 兼容性优势：功能token保持标准词表内，无需修改模型架构或训练流程，可直接融入现有LLM SFT和RL管线，工程移植成本低。

  - 可解释性增强：功能token为内部操作提供明确语义锚点，便于业务中审计Agent决策路径，提升系统透明度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视觉推理通常需要中间视觉状态，直接生成图像成本高，而agentic方法（通过代码/工具调用）引入外部执行延迟，latent方法（隐藏嵌入）难以任务泛化和并行训练。

**方法**：提出ATLAS框架，核心是用一个离散的功能token同时实现agentic操作和latent视觉推理。每个功能token对应一个内部化的视觉操作，但无需视觉监督，且保留在标准词表中，可通过next-token prediction生成。这避免了冗长的中间图像生成，同时完全兼容标准SFT和RL训练，无需架构改动。针对RL中功能token稀疏导致的训练不稳定，引入Latent-Anchored GRPO (LA-GRPO)，以一个静态加权的辅助目标锚定功能token，提供更强的梯度更新。

**结果**：在多个挑战性视觉推理基准上，ATLAS取得优越性能，同时保持了清晰的解释性，证实了单一token设计的有效性和训练稳定性。
