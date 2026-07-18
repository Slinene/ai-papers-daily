---
title: Long-Context Fine-Tuning with Limited VRAM
title_zh: 有限显存下的长上下文微调：结合分层全局注意力与分段反向传播
authors:
- Vladimir Fedosov
- Aleksandr Sazhin
- Artemiy Grinenko
- Frank Woernle
affiliations:
- BMW Group
arxiv_id: '2607.15105'
url: https://arxiv.org/abs/2607.15105
pdf_url: https://arxiv.org/pdf/2607.15105
published: '2026-07-16'
collected: '2026-07-18'
category: Training
direction: 长文本微调显存优化
tags:
- QLoRA
- Hierarchical Global Attention
- long-context
- VRAM-efficient
- attention
- KV-cache
one_liner: 用分层全局注意力、分段反向传播和分级KV缓存，在16GB显卡上将可训练上下文长度从2K扩展到16K，评估时支持131K tokens
practical_value: '- 在电商推荐场景中，用户长期行为序列或长商品描述经常超过2K tokens，本方法可直接用于消费级GPU（16GB）上微调长上下文模型，大幅降低硬件门槛。

  - 分段反向传播与历史KV转存RAM/NVMe的策略，可以借鉴到其它长序列训练中（如序列推荐模型），将不可微历史状态移出显存，只保留当前段可训练，节省显存。

  - HGA通过为每个查询块加载有限的历史token，保持每个token的关注量近似恒定，训练速度随上下文长度线性增长，而密集注意力是二次增长，这一特性可在在线学习或增量训练Agent时提升效率。

  - 训练得到的适配器可与标准密集注意力生成框架兼容，这意味着可以将高效的HGA训练与成熟的推理引擎结合，在保证模型质量的同时让推理也受益于长上下文。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：参数高效微调（如QLoRA）虽降低了模型与优化器内存，但密集注意力仍需处理完整历史，使得在消费级GPU上训练长上下文仍不可行。
**方法**：提出Hierarchical Global Attention (HGA) + 分段反向传播 + 分级KV存储。训练时仅当前段保持可微并驻留显存；历史段的KV被detach后卸载到RAM或NVMe。HGA对每个查询块，先检索相关历史块，再从中抽取固定的少量精确token进行注意力计算，从而避免全量历史注意力。
**关键结果**：在16GB Quadro RTX 5000上使用Qwen3-8B 4-bit QLoRA，密集训练仅支持2048 tokens，HGA达到16384 tokens（峰值显存15.28GB）。评估时适配器可处理131072 tokens，显存随摘要块缓慢增长，极限受RAM/NVMe容量限制。在共享2K训练长度下，HGA训练得到的适配器困惑度与密集训练相当（2.7405 vs 2.7383 nat），且吞吐量略高（217.75 vs 207.02 tokens/s），并随上下文增长优势扩大。训练得到的权重可直接用于标准密集注意力生成。
