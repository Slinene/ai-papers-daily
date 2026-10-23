---
title: Rethinking Sequence Compression with Test-time Regression
title_zh: 基于测试时回归的序列压缩方法
authors:
- Sihan Yang
- Jie Huang
- Hanxuan Li
- Yifan Guo
- Weigao Sun
- Yiran Zhong
- Weiyang Liu
affiliations:
- The Chinese University of Hong Kong
- Token Foundry, Alibaba Group
arxiv_id: '2610.31574'
url: https://arxiv.org/abs/2610.31574
pdf_url: https://arxiv.org/pdf/2610.31574
published: '2026-10-22'
collected: '2026-10-23'
category: LLM
direction: 高效序列压缩 · test-time regression
tags:
- Sequence Compression
- Sparse Attention
- Visual Token Merging
- Test-time Regression
- MLLM
one_liner: 提出 TTR-Compressor，将序列压缩视为测试时回归并用闭式解聚合 token，在稀疏注意力和视觉 token 合并上优于 pooling/投影
practical_value: '- 长用户行为序列压缩：电商推荐中用户历史行为 token 通常很长，进入 LLM 前可用 TTR 替代 mean/attention
  pooling；它联合拟合所有 token，保留交互，闭式解推理开销可控。

  - 多模态商品信息合并：商品图、标题、属性等多模态 token 合并进 LLM 时，可借鉴 TTR visual merger 减少视觉 token 数并保持理解性能，适合多模态搜索或商品描述生成。

  - Agent 长程记忆与上下文管理：面向 LLM agent 的对话推荐/搜索助手，用可学习回归压缩替代固定窗口截断或摘要，可能提升长上下文检索与推理（如 RULER）；工程上可将回归维度设小、分块计算闭式解。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：序列压缩是高效语言/多模态模型的关键瓶颈；现有 pooling 或 learned projection 逐 token 独立处理，忽视 token 间交互，性能欠佳。

方法关键点：TTR-Compressor 将序列压缩重新定义为测试时回归问题。输入序列的 token 作为回归数据，拟合的系数构成压缩表示。其核心是：在 forward pass 中通过闭式解高效计算压缩表示，而回归问题本身（如投影矩阵或注意力权重）通过反向传播端到端学习。该设计使所有 token 被联合拟合，能捕捉 token 间的相互作用，同时避免迭代优化，保持推理效率。

结果：作为块稀疏注意力的压缩器，TTR 在 RULER 基准上相较基于注意力的压缩器有大幅提升；作为视觉 token 合并器（visual token merger），它持续超越标准 MLP merger，并在仅使用 55.6% 视觉 token 时达到相同性能。
