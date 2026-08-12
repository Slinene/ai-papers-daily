---
title: 'OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching'
title_zh: OasisKV：通过前瞻稀疏预取将解码KV缓存扩展至HBM之外
authors:
- Can Xiao
- Sukmin Cho
- Junbong We
- Zhixiong Niu
- Jianyi Cheng
- Yiren Zhao
- Youngjin Kwon
- Yongqiang Xiong
- Rui Ma
- Junyi Liu
affiliations:
- Imperial College London
- KAIST
- Microsoft Research
- University of Edinburgh
arxiv_id: '2608.08097'
url: https://arxiv.org/abs/2608.08097
pdf_url: https://arxiv.org/pdf/2608.08097
published: '2026-08-07'
collected: '2026-08-12'
category: LLM
direction: LLM推理优化 · 稀疏KV缓存与层次化预取
tags:
- KV cache
- speculative decoding
- sparse attention
- prefetching
- LLM inference
- memory hierarchy
one_liner: 利用推测解码提前预测重要KV块，实现稀疏注意力与多级预取，在有限HBM下提升推理吞吐达2.1倍
practical_value: '- 结合推测解码与KV缓存管理：生成lookahead tokens时记录注意力，预测未来重要token，仅将稀疏的KV保留在HBM，可大幅减少显存占用，适用于长上下文服务（如用户行为序列、商品详情等需要长文本理解的场景）。

  - 多级存储分层设计：冷KV块存于主机内存，通过异步流水线预取到HBM，避免解码延迟，可将HBM视为KV缓存的“热数据”缓存，类比推荐系统中的特征缓存策略。

  - 基于vLLM实现，易于集成：工程上可直接在vLLM中扩展，业务中若使用vLLM部署LLM推理服务，可通过该稀疏预取方案提升吞吐，尤其适合批量推理和长序列场景。

  - 显著降低KV传输与主机内存压力：在prefill-decode分离架构下，传输KV量减少6.5-9.7倍，解码节点内存减少2.2-2.6倍，可降低跨节点通信成本，利于大规模推荐Agent系统部署。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：大模型推理中，解码阶段的KV缓存占用大量HBM，成为批量大小和吞吐的瓶颈，尤其在长上下文和推理型任务中。HBM容量昂贵且有限，亟需减少其KV缓存需求。

**方法**：提出OasisKV，利用**推测解码（SD）**生成的前瞻token（lookahead tokens）提前预测未来注意力模式，仅将稀疏的重要KV块保留在HBM，其余冷KV块存储于更大容量的主机内存。通过高效的注意力后台流水线，异步预取即将需要的KV块到HBM，确保解码时命中。系统基于vLLM实现，支持多GPU与prefill-decode分离架构。

**结果**：在2048 token KV预算下，准确率损失控制在0.7点以内；在推理任务上，相比密集vLLM吞吐提升**1.69倍**（准确率损失0.1点），多GPU长上下文服务最大加速**2.1倍**；在分离架构下，吞吐约**2倍**，同时KV传输量减少**6.5-9.7倍**，解码节点主机内存占用减少**2.2-2.6倍**。
