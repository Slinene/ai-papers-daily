---
title: 'Distillation with Errors: Sparse Unbiased Backpropagation for Knowledge Distillation'
title_zh: 带误差的蒸馏：知识蒸馏的稀疏无偏反向传播
authors:
- Yuyang Zhang
- Yuxin Li
affiliations:
- University of Science and Technology of China
arxiv_id: '2611.27131'
url: https://arxiv.org/abs/2611.27131
pdf_url: https://arxiv.org/pdf/2611.27131
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 高效知识蒸馏 · 稀疏无偏梯度估计
tags:
- Knowledge Distillation
- Unbiased Gradient Estimation
- Sparse Backpropagation
- Efficient Training
- LLM
one_liner: 提出稀疏配对梯度估计 DWE，利用 logit 梯度零和结构实现无偏低方差的 KD 输出头反传，加速蒸馏训练
practical_value: '- 在 LLM4Rec 蒸馏（如生成式商品 ID、query 生成）中，teacher 到 student 的 KD 输出头词汇量大，可用
  DWE 稀疏无偏梯度替代 full-softmax 反传，显著降低训练 GPU 成本，适合大规模生成模型迭代。

  - 零和结构与几何感知配对很实用：在采样部分负样本时，将高相似 logit 配对（如语义相近的商品 token 或 query）再估计梯度，可抵消偏差并压低方差，比简单重要性采样更稳定。

  - 工程上可在分布式训练中实现配对策略：每个 micro-batch 内随机采样配对 token，反向只传播所选 token 的梯度，省去 dense head
  的梯度计算；论文代码已开源，可适配 Hugging Face 训练框架。

  - 对在线蒸馏（On-policy distillation）同样有效，可在线部署 student，用 DWE 加速更新，适合推荐系统在线学习场景。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：全词表知识蒸馏（KD）训练语言模型时，输出头反向传播开销大；现有 Top-k 选择引入偏差，重要性采样方差高。

**方法关键点**：本文提出的 DWE 核心观察是 minibatch 训练本身已经近似训练梯度，因此逐位置反传不必精确。DWE 利用 logit 梯度的零和结构，构造稀疏配对梯度估计，使其期望等于全词表梯度。通过几何感知配对（将相似 logit 配对抵消）和分层采样进一步降低方差；理论证明估计器无偏。

**关键结果**：在相同采样预算下，DWE 相比重要性采样，隐藏状态梯度 MSE 降低 63.5%，输出权重梯度 MSE 降低 57.9%。在 off-policy KD 中，输出头加速最高 1.95×，总训练时间减少 10.4-15.7%；在 on-policy distillation 中，输出头加速最高 2.20×，且下游性能保持竞争力。
