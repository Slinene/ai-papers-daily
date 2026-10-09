---
title: 'SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference'
title_zh: 解码感知剪枝：面向 LLM 高效推理的 SparseDecoding
authors:
- Qitong Wang
- Xinwei Niu
- Mingluo Su
- Shanwei Zhao
- Shiai Zhu
- Huan Wang
affiliations:
- Westlake University
- Ant Group
arxiv_id: '2610.12327'
url: https://arxiv.org/abs/2610.12327
pdf_url: https://arxiv.org/pdf/2610.12327
published: '2026-10-07'
collected: '2026-10-09'
category: LLM
direction: LLM 推理剪枝与稀疏计算优化
tags:
- LLM inference
- pruning
- N:M sparsity
- SpMV
- decoding
- memory-bound
one_liner: 提出解码感知的剪枝框架，用生成过程激活校准并优化N:M稀疏SpMV内核，实现1.48x解码加速
practical_value: '- 校准数据选择：剪枝/量化 LLM 时，让 dense 模型自回归生成并从各层收集激活作为校准集，而非离线静态文本，能缓解分布偏移导致的性能下降；在电商推荐理由生成、Agent
  长回复等 decode 为主场景尤其适用。

  - 系统内核优化：线上 LLM 以 decode 为主时，应重点优化 SpMV；采用 N:M 结构化稀疏配合 bitmask 索引与固定步长遍历，可有效降低 memory-bound
  延迟，在商品描述生成、对话式推荐等长输出服务中提升吞吐。

  - 训练后剪枝无需微调，工程成本低，适合对已有搜索推荐 LLM 服务做快速压缩迭代，保留任务性能的同时降低 A100/H100 推理成本。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM 长输出应用受限于解码阶段 memory-bound；基于 Hessian 的训练后剪枝减少非零参数读取，但现有方法用自然序列计算 Hessian，与自回归生成 token 分布不一致，导致剪枝后激活分布偏离校准分布，精度下降；且现有稀疏加速主要面向 SpMM，解码主要 SpMV 支持不足。

### 方法
SparseDecoding 框架：算法上，在 dense 模型自回归生成过程中逐层收集激活（排除 prefill）构造校准矩阵，对齐剪枝目标与解码激活；系统上，开发 N:M 稀疏矩阵向量内核，采用 bitmask 索引与固定步长遍历，加速 SpMV。

### 结果
在 Llama-3.1-8B、Llama-3.3-70B、Qwen3-14B/32B 上，长文本生成基准优于固定文本校准，A100 端到端解码加速最高 1.48x。
