---
title: 'WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning'
title_zh: WIDE：Token 级动态宽度剪枝实现自适应 LLM 推理加速
authors:
- Haozhe Hu
- Hao Wu
- Peiran Yin
- Chao Han
- Yunpu Ma
- Xiaoyu Shen
affiliations:
- Ningbo Institute of Digital Twin, Eastern Institute of Technology, Ningbo
- Munich Center for Machine Learning, LMU Munich
arxiv_id: '2607.28418'
url: https://arxiv.org/abs/2607.28418
pdf_url: https://arxiv.org/pdf/2607.28418
published: '2026-07-30'
collected: '2026-08-01'
category: LLM
direction: LLM 动态剪枝 · 推理加速
tags:
- dynamic pruning
- token-level sparsity
- LLM inference
- structured pruning
- kernel co-design
- width pruning
one_liner: 首个端到端可微分的 token 级动态宽度剪枝框架，支持预填充与解码场景，细粒度分配注意力头组与 FFN 通道组
practical_value: '- **在线 LLM 推理降本**：在电商搜索的 query 理解、商品描述生成、RAG 检索等环节部署 LLM 时，可将 WIDE
  的 token 级动态宽度剪枝迁移到自有模型中，按 token 难度动态分配算力，显著降低延迟与成本。

  - **两阶段训练策略复用**：先通过可微分掩码学习 token-wise 稀疏模式，再冻结掩码进行微调，该流程可应用于自有 Transformer 模型，无需大量校准数据即能保持精度。

  - **细粒度结构剪枝方案**：将动态剪枝从层级下推到注意力头组和 FFN 通道组，相比粗粒度弃层更细粒度，可模仿该分组设计，在推荐模型的 Transformer
  层中实现更柔性的算力分配。

  - **剪枝-内核算子协同设计**：提出的 mask 重排序、block 级跳过、intra-block 跳过等工程化加速技巧，可作为部署端优化参考，有效将动态稀疏转化为实际加速。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有 LLM 静态剪枝输入无关，高稀疏度下精度损失大；动态剪枝多局限于粗粒度层级决策，且实际推理加速困难。亟需细粒度、可实际加速的动态剪枝方案。

**方法关键点**：
- **Token 级动态宽度剪枝**：每个 token 动态选择注意力头组（head groups）和 FFN 通道组（channel groups），将细粒度控制下推到神经元块级别。
- **两阶段训练**：第一阶段通过可微掩码学习 token-wise 稀疏模式，第二阶段固定掩码进行微调，确保质量保留。
- **剪枝-内核算子协同设计**：将动态稀疏加速分解为掩码重排序、硬件无关的块级跳过、硬件相关的块内跳过，实现跨粒度的有效加速。

**关键结果**：50% 稀疏度下，WIDE 在仅校准设置中比 SOTA 动态深度剪枝性能提升 55.1%。在预填充和解码工况下，核级加速分别最高达 1.98× 和 4.95×，端到端加速 1.68× 和 1.55×。
