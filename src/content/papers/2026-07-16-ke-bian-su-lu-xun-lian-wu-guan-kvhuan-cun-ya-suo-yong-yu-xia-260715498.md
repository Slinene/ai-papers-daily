---
title: 'VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context
  LLMs'
title_zh: 可变速率训练无关KV缓存压缩用于长上下文大模型
authors:
- Shahrzad Esmat
- Dhawal Shah
- Ali Jannesari
affiliations:
- Iowa State University
arxiv_id: '2607.15498'
url: https://arxiv.org/abs/2607.15498
pdf_url: https://arxiv.org/pdf/2607.15498
published: '2026-07-16'
collected: '2026-07-20'
category: LLM
direction: 长上下文LLM推理优化 · 可变速率KV缓存压缩
tags:
- KV cache compression
- low-rank
- training-free
- variable-rate
- long-context
- LLM inference
one_liner: 提出无训练可变秩KV缓存压缩方法VarRate，按显著性分配预算并保留所有token，实现接近无损的长上下文推理
practical_value: '- 在线LLM服务可直接部署VarRate作为无训练的KV缓存压缩插件，减少长上下文推理内存占用，支撑更长的用户历史（如推荐理由生成、Agent对话历史理解）。

  - 在多查询复用预填充缓存的场景（如批量用户查询），VarRate避免丢弃token导致的精度崩溃，保障关键信息不丢失，提升推荐或搜索结果的稳定性。

  - 显著性得分可基于注意力权重快速计算，适合流式处理，能集成到实时推理管线中，无需额外模型或微调，降低工程复杂度。

  - 可变秩分配思想可推广到特征存储、用户画像压缩等模块，通过保留所有数据点但差异化精度，实现更好的资源效率平衡。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：长上下文LLM推理中，KV缓存成为主要内存瓶颈。现有无训练方法分两类：token选择（如SnapKV）会不可逆丢弃token，导致查询不可知复用下精度崩溃（下降11-15点）；统一低秩编码保留所有token但平均分配秩，浪费预算。两者缺陷均源于“丢弃”而非“智能分配”。

**方法**：VarRate是一种训练无关的可变速率KV缓存编解码器。它根据token的查询显著性计算重要性得分，为每个token分配可变低秩预算：重要token获得更高秩，次要token获得较低但非零秩，保留全部token。秩分配通过截断SVD在预填充阶段完成，解码时直接使用压缩后的缓存，无需额外训练。

**结果**：在LongBench（16个任务）上，20%缓存预算下，Llama-3.1-8B和Qwen2.5-7B平均精度仅比无损模型低0.8点。查询不可知场景下退化仅3.5-5.5点，远优于token选择。相比统一低秩基线显著更优，与专用方法KVzip精度相当，但预填充开销仅其八分之一。
