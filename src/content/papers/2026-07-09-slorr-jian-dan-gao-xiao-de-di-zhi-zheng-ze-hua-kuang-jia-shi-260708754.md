---
title: 'SLORR: Simple and Efficient In-Training Low-Rank Regularization'
title_zh: SLORR：简单高效的低秩正则化框架，实现训练中压缩友好
authors:
- David González-Martínez
- Shiwei Liu
affiliations:
- Max Planck Institute for Intelligent Systems
- University of Tübingen
- ELLIS Institute Tübingen
- Tübingen AI Center
arxiv_id: '2607.08754'
url: https://arxiv.org/abs/2607.08754
pdf_url: https://arxiv.org/pdf/2607.08754
published: '2026-07-09'
collected: '2026-07-10'
category: Training
direction: 训练时低秩正则化压缩
tags:
- low-rank
- regularization
- compression
- Hoyer
- nuclear norm
- training efficiency
one_liner: 在训练中施加低秩正则化，使模型压缩后更易保持性能，训练开销极低
practical_value: '- 推荐模型训练时加入低秩正则化，可提升后续低秩分解压缩的质量，减小推理开销，且不改变模型结构，易于在现有Pipeline中插入。

  - 使用Hoyer近似或核范数近似，避免直接计算SVD，计算开销低（LLM训练中<1%），适合大规模推荐模型或Agent模型的训练。

  - 对于基于LLM的生成式推荐（GenRec），在预训练阶段施加SLORR，后续压缩时能更好保留语义ID生成质量。

  - 无状态、架构不变的设计，可将其作为插件添加到现有训练流程，用于任何权重矩阵的低秩偏好学习。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：低秩分解是压缩神经网络的常用手段，但现代模型在激进压缩下容易损失精度。现有训练时低秩正则化方法通常需要计算大权重矩阵的SVD、修改架构或依赖状态缓存，不够高效或灵活。

**方法**：提出SLORR，一种简单、无状态、架构保持的训练中低秩正则化框架。其核心是直接对原始权重矩阵施加正则化，促使奇异值稀疏，从而增强低秩可压缩性。正则项基于两种变体：Hoyer稀疏度量和核范数。为前反向传播设计了GPU友好的高效近似，并给出了近似保证，避免昂贵的SVD操作。

**结果**：在ImageNet-1K上对ResNet和ViT进行续训练和预训练，SLORR诱导的低秩结构使压缩后模型性能显著优于无正则化模型，训练额外开销低于8%。在135M和560M参数的LLM预训练中，SLORR-Hoyer保持压缩模型性能大幅领先无正则化方法，平均训练开销不到1%。
