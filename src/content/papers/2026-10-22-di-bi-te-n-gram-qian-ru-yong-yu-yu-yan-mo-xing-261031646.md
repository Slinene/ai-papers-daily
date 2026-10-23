---
title: Low-Bit N-Gram Embeddings for Language Models
title_zh: 低比特 N-Gram 嵌入用于语言模型
authors:
- Stephen Chung
- Wenyu Du
affiliations:
- DualverseAI
arxiv_id: '2610.31646'
url: https://arxiv.org/abs/2610.31646
pdf_url: https://arxiv.org/pdf/2610.31646
published: '2026-10-22'
collected: '2026-10-23'
category: Training
direction: n-gram 嵌入低比特量化与内存优化
tags:
- n-gram embeddings
- quantization
- low-bit
- memory optimization
- LLM
one_liner: 低精度存储 n-gram 嵌入表，4-bit 可节省约 75% 表内存且几乎不损失性能
practical_value: '- 若推荐/搜索模型中使用 n-gram 特征嵌入表（如用户行为序列中的连续 token 片段），可尝试 4-bit 量化存储，通常能节省约
  75% 内存且性能损失极小，是性价比很高的工程优化。

  - 量化后若精度下降，可加入短时微调恢复大部分性能；若内存预算不变，可将节省的内存用于扩大嵌入表容量，反而可能超过原全精度表效果。

  - 对于线上已有大模型（如 DeepSeek、Qwen 系列），其 n-gram 模块可直接做低比特量化，实测困惑度增加 <1.2%，下游任务基本不降，适合对内存敏感的场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：近期开源权重语言模型（如 DeepSeek-V4.1-Flash）通过 n-gram 嵌入表大幅提升性能，但表内存开销巨大——DeepSeek-V4.1-Flash 的 Engram 模块独占 196B 参数。降低该内存成本同时保留性能增益，是实际部署的关键需求。

**方法**：提出将 n-gram 嵌入表以低精度存储，系统研究不同量化方法（如 int4/int8 等）和表间比特分配策略。在 nanochat、Llama、GPT-2 家族模型上从头训练，并评估多种位宽；进一步在大型已训练模型上直接量化。

**结果**：从头训练时，4-bit 表节省约 75% 表内存，保留超过 99% 的验证损失改善；更低比特（如 2-bit）性能下降明显，但短时微调可显著恢复。将节省的内存用于扩大表容量，可超越原全精度表效果且总内存更少。在 DeepSeek-V4.1-Flash 和 Qwen3.8-Flash-Next 上，低比特表节省 47–55% 表内存，困惑度增加 <1.2%，下游任务性能基本保持。

**结论**：低比特精度是降低 n-gram 嵌入内存的实用手段，且释放的容量可反哺模型性能。
