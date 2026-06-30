---
title: 'C$^{2}$R: Cross-sample Consistency Regularization Mitigates Feature Splitting
  and Absorption in Sparse Autoencoders'
title_zh: C2R：跨样本一致性正则化缓解稀疏自编码器特征分裂与吸收
authors:
- Haoran Jin
- Xiting Wang
- Shijie Ren
- Hong Xie
- Defu Lian
affiliations:
- University of Science and Technology of China
- State Key Laboratory of Cognitive Intelligence
- Renmin University of China
arxiv_id: '2606.30609'
url: https://arxiv.org/abs/2606.30609
pdf_url: https://arxiv.org/pdf/2606.30609
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: LLM可解释性 · 稀疏自编码器正则化
tags:
- Sparse Autoencoder
- Mechanistic Interpretability
- Feature Splitting
- Feature Absorption
- Regularization
- Cross-sample Consistency
one_liner: 通过惩罚方向相似潜变量的共激活强制一致表示，缓解特征分裂与吸收，同时保持重构保真度
practical_value: '- 在电商推荐中的特征分解（如用户兴趣编码）时，可借鉴跨样本一致性惩罚，防止同一语义概念被多个潜变量碎片化表示，提升特征可解释性与迁移鲁棒性。

  - 对于使用稀疏编码或 VQ-VAE 生成 Semantic ID 的生成式推荐，C2R 的思想可约束码本方向，避免 absorption（一个码承载过多无关概念），提升
  ID 语义纯度。

  - 在 Agent 状态表示（如任务规划）中，若使用稀疏自编码器提取可解释状态，加入 C2R 正则化可确保关键决策因子的一致激活，减少噪声干扰。

  - 将 C2R 实现为损失函数中的简单余弦相似度惩罚项，可直接嵌入现有推荐模型训练流程，无需复杂架构改动，并兼容 TopK 等稀疏约束。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：稀疏自编码器（SAE）用于解释大语言模型内部表征时，随字典扩大暴露出特征分裂（同一概念被分割为多个非原子潜变量）和特征吸收（一个潜变量吸收多个不相关概念），严重损害可解释性。根本原因是跨样本缺乏约束，导致同一概念被不一致地分配到不同潜变量。

**方法**：提出 C2R（跨样本一致性正则化），在训练批次内，强制语义相似的样本对同一概念的激活集中在相同潜变量上。具体通过**惩罚方向相似的潜变量同时激活**来实现：若两个潜变量余弦相似度高，则抑制它们在同一批次中被频繁共激活，从而促使每个概念被统一的潜变量表示。C2R 天然兼容现有稀疏约束（如 TopK），且不牺牲重构质量。

**结果**：实验表明，C2R 有效缓解了特征分裂与吸收，同时保持重构保真度；对比现有约束（ℓ1、TopK、BatchTopK、Matryoshka、Ort），C2R 首次同时提供理论保证、直观解决方案并保留重构能力。
