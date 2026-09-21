---
title: Accelerating Dense LLMs via L0-regularized Mixture-of-Experts
title_zh: L0 正则化混合专家加速稠密大模型
authors:
- Zhenyu Zhang
- Jiudong Yang
- Zhaowen Tao
- Meng Chen
affiliations:
- YWZ, Chengdu, China
- FuTu AI, Shenzhen, China
- Wise AI, Melbourne, Australia
arxiv_id: '2609.21672'
url: https://arxiv.org/abs/2609.21672
pdf_url: https://arxiv.org/pdf/2609.21672
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: LLM 推理加速 · L0 稀疏 MoE
tags:
- L0-regularization
- Mixture-of-Experts
- LLM acceleration
- sparse MoE
- model compression
one_liner: 提出 L0-MoE，用 L0 正则化将稠密 LLM 转为稀疏 MoE，实现最高 2.5 倍加速且性能几乎不降
practical_value: '- 在需要低延迟、高吞吐的 LLM 推理场景（如电商搜索 Agent、对话式推荐），可借鉴 L0-MoE 把已有 dense 模型快速转为稀疏
  MoE，无需从头训练 MoE，节省大量计算资源。

  - 动态 batching 与 domain-aware 数据集构建方法可迁移到垂直领域小模型的加速训练：先用聚类混淆矩阵挑选领域代表性数据，再动态组 batch，提升训练效率。

  - 若业务中需要同时覆盖多领域（如搜索、广告、推荐），可考虑用 L0 正则化自动学习专家路由，减少手工设计 MoE 结构的工作量，同时获得 2 倍以上推理加速。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 推理成本高，现有量化、剪枝等加速方法常带来明显性能下降；从头训练 MoE 资源消耗巨大，难以普及。

**方法关键点**：提出 L0-MoE，将 L0 正则化引入稠密 LLM 的 FFN 层，训练时鼓励激活稀疏专家结构，推理时仅激活部分专家，实现加速。具体包括：
- 用 cluster confusion matrix 做 domain-aware 数据集筛选，使训练数据覆盖不同领域且易混淆样本，提升稀疏专家分配质量；
- 动态 batching 策略提升训练效率；
- 在已有 dense 模型基础上微调，无需改变模型主干结构。

**关键结果**：在多个 LLM 上实验，L0-MoE 相比 dense 模型最高实现 2.5 倍推理加速，性能保持竞争水平，优于现有 LLM 加速基线。
