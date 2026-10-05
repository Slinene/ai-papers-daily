---
title: Adaptive Sparsity Optimization with Learnable Soft Top-K and Per-Term Thresholding
  for Efficient Retrieval
title_zh: 可学习软Top-K与逐项阈值自适应稀疏优化用于高效检索
authors:
- Wentai Xie
- Parker Carlson
- Shanxiu He
- Tao Yang
affiliations:
- University of California, Santa Barbara
arxiv_id: '2610.02572'
url: https://arxiv.org/abs/2610.02572
pdf_url: https://arxiv.org/pdf/2610.02572
published: '2026-10-01'
collected: '2026-10-05'
category: RecSys
direction: 神经稀疏检索自适应稀疏化
tags:
- Learned Sparse Retrieval
- Sparsification
- Efficiency
- Soft Top-K
- Per-Term Thresholding
- FLOPs Regularization
one_liner: 提出可学习软Top-K、逐项阈值和FLOPs正则化联合稀疏化方案，大幅缩短LLM稀疏检索向量长度并保持效果
practical_value: '- 可学习软Top-K替代硬Top-K：将稀疏化过程变成可微操作，允许端到端训练时动态调整保留项数量，避免离散选择带来的梯度断裂，适合嵌入到现有召回模型的训练流程中。

  - 逐项阈值（per-term thresholding）：为每个词项学习独立的剪枝阈值，而非全局统一阈值，能更好适应长尾词频分布，在电商搜索词表极大且稀疏的场景下尤其有效。

  - FLOPs正则化直接约束推理计算量：相比仅用L1正则，显式优化FLOPs能更精准地控制延迟和资源消耗，可以在保持召回质量的前提下，为线上服务设定计算预算。

  - 工程收益明确：在MS MARCO和BEIR上显著降低平均查询/文档长度，可直接迁移到大规模电商搜索或推荐召回，减少倒排索引存储开销和查询延迟，适合对延迟敏感的生产环境。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM用于神经稀疏检索虽提升了相关性，但产生过长文档/查询向量，大词表导致存储和检索开销巨大。

方法关键点：提出自适应稀疏优化方案，包含三个协同组件：1) 可学习软Top-K，用可微函数逼近Top-K选择，使稀疏化可端到端训练；2) 逐项阈值，为每个词项学习独立剪枝阈值，替代全局阈值；3) FLOPs正则化，直接对检索计算量（浮点运算次数）进行正则，显式控制推理成本。三者联合优化，同时增加查询和文档向量的稀疏性。

关键结果：在MS MARCO和BEIR数据集上，基于Lion-SP模型实验，方案显著减少平均查询和文档长度，大幅降低检索延迟和存储成本，同时保持与基线高度竞争的相关性。
