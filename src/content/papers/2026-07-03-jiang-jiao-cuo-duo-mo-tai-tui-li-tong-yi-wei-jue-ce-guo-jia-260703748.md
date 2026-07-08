---
title: Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process
title_zh: 将交错多模态推理统一为决策过程：BRAID框架
authors:
- Zican Hu
- Xuyang Hu
- Yiming Liu
- Zuwei Long
- Wei Liu
- Yunzhuo Hao
- Jiawei Gu
- Linjie Li
- Yu Cheng
- Zhenhong Sun
affiliations:
- Nanjing University
- Tencent Youtu Lab
- Shanghai AI Laboratory
- Tsinghua University
- University of Washington
arxiv_id: '2607.03748'
url: https://arxiv.org/abs/2607.03748
pdf_url: https://arxiv.org/pdf/2607.03748
published: '2026-07-03'
collected: '2026-07-08'
category: Multimodal
direction: 多模态推理 · 统一 MDP · 强化学习优化
tags:
- multi-modal reasoning
- reinforcement learning
- Markov decision process
- vision-thinking guidance
- unified model
one_liner: 提出 BRAID，把多轮文本-图像推理建模为统一 MDP，用 RL 联合优化文本与图像生成，并引入 VLM judge 提供稠密回合反馈
practical_value: '- **电商多模态 Agent 联合优化**：在商品文案配图、展示广告创意生成等多轮交互场景中，可将文本和图像生成纳入统一 MDP，用
  RL 同时优化文本 token 和图像扩散去噪路径，避免只微调文本而忽略图像质量的半优化问题。

  - **中间图像价值评估**：引入 VLM judge 对多轮推理中每一张中间图像打分，提供稠密回合级奖励。在搜索推荐 Agent 的多步调用中，可类似地用 judge
  评估每一步生成内容的“推理效用”，改善长程信用分配，加快训练。

  - **模态原生策略梯度**：BRAID 对文本和图像分别使用各自模态的策略梯度机制，但共享一个轨迹级优势函数。实际实现时，可参照其设计，将优势值统一后注入不同生成模块的损失函数，避免为每个模态单独设计奖励。

  - **工程落地参考**：扩散模型策略梯度需计算 score function 与 denoising path 的关联，BRAID 提供的实现思路可直接复用到广告图片生成的在线优化中，提升点击率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：统一多模态模型（UMM）在多轮文本-图像推理上表现良好，但现有 RL 方法仅优化文本步骤，图像生成仍用监督微调，导致跨模态策略梯度无法端到端传播，RL 潜力未被充分挖掘。

**方法关键点**：BRAID 将多轮文本-图像-文本推理形式化为统一的马尔可夫决策过程（MDP），把文本生成和图像生成（扩散去噪路径）都纳入策略优化，通过单一 RL 目标联合训练。具体地，计算整个轨迹的共享优势值，然后分别按文本 token 和图像去噪步骤的策略梯度进行回传，每种模态都用其原生机制接收梯度。为缓解长程信用分配困难，BRAID 引入一个 VLM judge，对每个中间图像在推理中的有用性评分，提供稠密的回合级反馈，在关键视觉分支加强学习信号。

**关键结果**：在空间推理和视觉感知基准测试上，BRAID 一致优于仅文本 RL、单独 SFT 图像等多种基线，证实统一 MDP 加视觉思维指导是多模态推理优化的有效框架。
