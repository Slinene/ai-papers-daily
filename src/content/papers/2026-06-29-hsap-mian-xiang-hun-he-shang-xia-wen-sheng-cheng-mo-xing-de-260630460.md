---
title: 'HSAP: A Hierachical Sequence-aware Parallelism for Hybrid-Context Generative
  Models'
title_zh: HSAP：面向混合上下文生成模型的分层序列感知并行方法
authors:
- Songxin Zhang
- Zejian Xie
- Zhuoyang Song
- Cong lin
- Junyu Lu
- Jiaxing Zhang
- Bingyi Jing
affiliations:
- Southern University of Science and Technology
- International Digital Economy Academy
arxiv_id: '2606.30460'
url: https://arxiv.org/abs/2606.30460
pdf_url: https://arxiv.org/pdf/2606.30460
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: 大规模模型训练并行优化
tags:
- sequence parallelism
- hybrid-context
- packed sequences
- causal attention
- JIT compilation
- distributed training
one_liner: 提出分层序列感知并行框架HSAP，解决混合上下文打包序列的因果注意力跨污染问题，性能优于现有方法
practical_value: '- 混合上下文打包（如将多个用户行为序列拼接训练）时，需确保因果注意力掩码正确，借鉴HSAP的序列感知并行策略可避免跨序列注意力污染，提高推荐模型训练效率。

  - 在分布式训练中，对于长序列模型（如用户长期行为Transformer），采用分层并行框架，结合张量并行和序列并行的混合策略，可优化通信和内存，加速训练。

  - 利用JIT编译优化NCCL通信，可应用于自定义分布式推荐模型训练，减少跨机通信开销。

  - 论文提出的内存和通信管理策略（如分片激活重计算）可迁移到大模型微调场景，降低显存占用。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有序列并行方法在处理混合上下文打包序列（如将多个文档或会话拼接训练）时，无法正确计算因果注意力，导致跨序列信息泄露，或通过牺牲并行度来避免，限制了训练效率。

**方法**：提出序列感知并行算法（Sequence-Aware Parallelism），通过精确控制每个设备的序列边界，保证因果注意力仅在序列内发生，同时利用JIT编译优化设备间NCCL通信，降低张量传输开销。在此基础上，构建分层序列感知并行框架（HSAP），无缝集成现有的序列并行范式（如Megatron-SP、DeepSpeed-Ulysses），通过分层协调不同设备组，平衡并行度和通信负担，并设计了内存与通信开销管理策略（如选择性激活重计算）。

**结果**：多项实验表明，HSAP在训练速度和内存效率上均超越现有SOTA序列并行方案（如Megatron-LM、DeepSpeed），尤其在大规模混合上下文场景下优势明显。
