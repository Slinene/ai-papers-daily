---
title: 'ChronoVision: Temporal Reasoning via Latent State Reconstruction'
title_zh: ChronoVision：通过潜在状态重建实现时序推理
authors:
- Yifan Shen
- Jian Xu
- Boyi Li
- Yuner Zhang
- Tianjiao Yu
- Bingxuan Li
- Houze Yang
- Rushi Wang
- Xu Cao
affiliations:
- University of Illinois Urbana-Champaign
- PediaMed AI
- University of Pennsylvania
arxiv_id: '2608.05631'
url: https://arxiv.org/abs/2608.05631
pdf_url: https://arxiv.org/pdf/2608.05631
published: '2026-08-05'
collected: '2026-08-08'
category: Reasoning
direction: 多模态时序推理 · 潜在状态重建
tags:
- temporal reasoning
- latent reconstruction
- RLHF
- visual attention
- multimodal
- process alignment
one_liner: 通过重建潜在状态与强化学习对齐过程，增强多模态模型的时序推理能力
practical_value: '- 潜在状态重建可作为一种辅助任务用于用户行为序列建模，预测未来购物意图的隐状态演进，辅助动态兴趣捕捉。

  - ROI 注意力定位模块可迁移至搜索或推荐中，对用户行为序列的关键片段（如点击、加购）进行聚焦，增强模型可解释性。

  - 强化学习后训练对齐中间过程的做法，可借鉴到多步推荐 Agent 的决策优化，通过奖励中间状态一致性提升策略稳定性。

  - 将视频推理转化为严格图像排序任务的评估思路，可启发推荐系统中序列预测能力的评测设计，如评测下一次物品预测的时序逻辑一致性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多模态大模型在需要多步时序推理的视觉任务上表现不佳，主要因为语言描述的模糊性难以捕捉连续视觉变换的精确过程。

**方法关键点**：
- 提出 ChronoVision 框架，在监督微调时引入**重建视觉头**，直接预测最终状态的潜在表示，迫使模型内化视觉演化逻辑。
- 设计 **ROI 注意力定位模块**，通过可学习的语义跨度查询，引导模型关注关键视觉证据区域。
- 后训练阶段采用**强化学习**，以复合奖励函数同时评估答案正确性、潜在过程对齐质量和无监督视觉焦点，实现隐式过程接地。
- 构建 **Vbvr-VQA 数据集**，将视频推理转换为严格的图像排序任务，专门评估时序跟踪能力。

**关键结果**：
- Vbvr-VQA 域内准确率 74.8%，域外 71.6%，超越已有方法。
- 跨领域基准 IntPhys2 上达 55.0%，展示强泛化性。
