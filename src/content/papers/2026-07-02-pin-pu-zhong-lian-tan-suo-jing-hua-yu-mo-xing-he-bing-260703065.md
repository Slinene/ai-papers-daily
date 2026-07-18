---
title: Spectral Rewiring for Exploration, Purification, and Model Merging
title_zh: 频谱重连：探索、净化与模型合并
authors:
- Zhilong Zhang
- Hongli Yu
- Huan-ang Gao
- Hanlin Wu
- Yuxuan Song
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
affiliations:
- Tsinghua AIR
- ByteDance Seed
arxiv_id: '2607.03065'
url: https://arxiv.org/abs/2607.03065
pdf_url: https://arxiv.org/pdf/2607.03065
published: '2026-07-02'
collected: '2026-07-18'
category: Training
direction: LLM 后训练参数频谱提炼与合并
tags:
- spectral analysis
- reinforcement learning
- post-training
- model merging
- parameter efficiency
- reasoning
one_liner: 仅保留0.58%参数的频谱核心，维持RL微调推理能力并增强探索与多域融合
practical_value: '- 在 RL 微调后，提取参数更新中的低维频谱核心，去除正交噪声，可作为轻量级后处理提升推理探索与测试时扩展（如高 k 采样），适用于推荐
  Agent 策略微调。

  - 方法仅需极少参数（<1%）保存推理核心，有助于多领域推荐模型的知识合并与解耦，避免跨域灾难性遗忘。

  - 无训练合并技巧可集成到多专家推荐系统，融合不同业务场景微调的模型，提升跨域泛化。

  - 参数几何的频谱分析方法可迁移至推荐模型参数更新分析，诊断微调对模型泛化能力的影响。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：全参数RL微调虽然提升大模型推理，但会抑制测试时扩展性能，导致过早饱和，并在多域训练或模型合并时引入跨域干扰。研究发现，有效推理更新集中在基模型频谱空间内。

**方法**：提出子空间对齐重连（SAR），一种事后编辑方法。对基模型权重矩阵进行奇异值分解，将RL微调产生的参数更新投影到基模型左奇异向量张成的子空间，保留该频谱核心，丢弃正交方向上的噪声更新，从而提炼出紧凑的推理核心。

**结果**：在多个模型族与规模上，SAR仅用约0.58%的总参数即保留超99%的原始RL微调性能；在数学推理中改善高k探索；在内部编程Agent模型的7个基准中提升6个；净化混合域训练更新，释放被抑制的编码能力，同时保持数学推理与指令遵循；模型合并实验超越之前合并基线，甚至超越最佳单域专家。
