---
title: 'FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead
  Sparse Attention'
title_zh: FlashMemory：基于前瞻稀疏注意力的超长上下文KV缓存压缩
authors:
- Yan Wang
- Qifan Zhang
- Jiachen Yu
- Tian Liang
- Dongyang Ma
- Xiang Hu
- Zibo Lin
- Chunyang Li
- Zhichao Wang
- Jia Li
affiliations:
- Tencent
- The Hong Kong University of Science and Technology (Guangzhou)
- Tsinghua University
- Independent Researchers
arxiv_id: '2606.09079'
url: https://arxiv.org/abs/2606.09079
pdf_url: https://arxiv.org/pdf/2606.09079
published: '2026-06-07'
collected: '2026-06-09'
category: LLM
direction: LLM 推理优化 · 稀疏注意力
tags:
- Sparse Attention
- KV Cache Compression
- Long Context
- Neural Memory Indexer
- LLM Inference
one_liner: 提出前瞻稀疏注意力与神经记忆索引器，将KV缓存压缩至13.5%且准确率无损
practical_value: '- 借鉴“前瞻记忆索引”思想，在需要维护长历史对话或用户行为的电商推荐Agent中，可训练轻量级索引器预测未来需要的记忆片段，而非保存全量状态，大幅降低内存开销。

  - 解耦训练策略值得工程化：索引器作为双编码器，用标准检索训练框架单独训练，无需加载主模型，可快速迭代，特别适合将记忆管理模块插入已有生产模型。

  - 稀疏注意力去噪效应提示：在长序列推荐建模（如用户长期行为序列）中，只保留与当前查询相关的关键交互，可能去除无关噪声，提升模型精度。

  - 对于超长上下文场景（如多轮Agent对话、长文档分析），KV缓存压缩率超90%且稳定性保持，可直接指导自研LLM推理引擎的显存优化。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：大模型在超长上下文推理时，完整KV缓存造成GPU显存瓶颈，限制实际部署。

方法关键点：提出前瞻稀疏注意力（LSA），引入神经记忆索引器，它不依赖被动关注所有历史token，而是主动预测未来上下文需求，仅保留查询关键的KV块在显存中。索引器采用独立于主模型（backbone-free）的解耦训练策略，被设计为标准双编码器架构，利用检索训练框架独立训练，无需加载巨大的主模型到GPU。

关键结果：在LongBench-v2、LongMemEval、RULER等权威长上下文评测中，物理KV缓存压缩到全量基线的13.5%，下游准确率平均绝对提升0.6%。在极端50万token长度下，抑制KV缓存开销超过90%，且不破坏主模型的核心推理能力，实现高效与降噪双赢。
