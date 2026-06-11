---
title: 'miniReranker: Efficient Multimodal Reranking through Visual Cache Reuse and
  Interaction Sparsity'
title_zh: 迷你重排序器：通过视觉缓存复用与交互稀疏性实现高效多模态重排序
authors:
- Yingqi Fan
- Xuan Lu
- Anhao Zhao
- Junlong Tong
- Ping Nie
- Kai Zou
- Yunpu Ma
- Wei Zhang
- Xiaoyu Shen
affiliations:
- Eastern Institute of Technology, Ningbo
- Netmind.ai
- Munich Center for Machine Learning, LMU
arxiv_id: '2606.10759'
url: https://arxiv.org/abs/2606.10759
pdf_url: https://arxiv.org/pdf/2606.10759
published: '2026-06-09'
collected: '2026-06-11'
category: Multimodal
direction: 多模态重排序 · 视觉缓存复用与稀疏交互
tags:
- MLLM
- Reranking
- Visual Cache
- Prefix Caching
- Early Exit
- Token Pruning
one_liner: 通过视觉优先格式、提前退出、交互带及token剪枝，将单查询多模态重排序时间降至原来的不到1%，同时保持96%以上性能。
practical_value: '- **视觉优先的 prefix 缓存复用**：在电商图片搜索重排中，将图片（视觉 token）放在输入序列前面，可利用 prefix
  caching 复用绝大多数计算，仅替换文本 query，大幅降低 KV cache 重复生成开销。

  - **提前退出与交互限制**：对于候选量大的商品重排序，可在模型浅层插入相关性头，仅对 top-K 候选执行深层交互，或只在少数层启用跨图文注意力，有效平衡精度与延迟。

  - **视觉 token 剪枝**：利用 embedder 引导的 token 剪枝，在图文对比前预先剔除冗余视觉信息，减少输入长度，适合移动端或高吞吐的轻量级多模态重排场景。

  - **工程融合思路**：三项优化（early exit + interaction band + token pruning）可叠加使用，根据业务延迟预算灵活配置，例如先剪枝再浅层打分，最后仅对少量候选进行完整多模态交互。'
score: 8
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态大模型（MLLM）作为点式重排序器能精细建模查询-文档相关性，但每个查询需与大量候选文档逐一配对，导致视觉编码等重复计算严重。传统 query-first 或 document-first 格式未能充分利用前缀缓存，与 MLLM 原生 prompt 范式及计算复用需求脱节。

**方法**：提出 miniReranker，包含三个层次优化：1）**vision-first 重排格式**：将视觉 token 置于序列前方，使视觉表征可被前缀缓存复用，且对齐 MLLM 预训练格式；2）**提前退出**：利用模型深度冗余，在浅层插入相关性头，让简单样本提前结束；3）**交互带**：限制跨图文注意力仅发生在少数中间层，其余层只做自注意力，减少交互成本；4）**embedder 引导的视觉 token 剪枝**：通过对齐 embedder 重要性分数剪除冗余视觉 token，降低序列长度。三者分别针对模型深度、跨段交互和视觉 token 三个冗余来源。

**结果**：基于 Qwen3-VL 实现，在重排序 top-100 候选时，推理时间降至密集实现的 <1%，性能保持 >96%；活跃参数减少到 58%；训练加速近 3 倍。验证了在几乎不损失效果的前提下，通过缓存复用与稀疏交互大幅降低多模态重排序成本。
