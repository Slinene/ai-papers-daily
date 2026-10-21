---
title: 'N-Gram Memories at Two Bits: Quantizing Lookup Tables in Large Language Models'
title_zh: N-Gram 记忆两比特量化：LLM 查找表压缩
authors:
- Donghoon Han
- Minseop Jung
- Dong Woo Kwak
- SeungJae Lee
- Junhoo Lee
affiliations:
- Dnotitia Inc.
- KAIST
arxiv_id: '2610.21810'
url: https://arxiv.org/abs/2610.21810
pdf_url: https://arxiv.org/pdf/2610.21810
published: '2026-10-15'
collected: '2026-10-21'
category: LLM
direction: LLM 条件记忆嵌入表压缩
tags:
- quantization
- lookup table
- conditional memory
- LLM
- embedding compression
- n-gram
one_liner: 共享 Gaussian trellis 与 norm restoration 将条件记忆行压缩为 2-bit 码，KL 较 2-bit RTN
  降低 41-63%，DeepSeek 表由 203GB 降至 51GB
practical_value: '- 大规模稀疏 embedding 表（用户/商品 ID、行为序列记忆、检索索引）可借鉴 CP 的“短码 + 局部 scale
  + 共享重建程序”：每行仅存 2-bit 码与 scale，离线共享解码器，线上仅解码被查行，显著降低 GPU 显存占用。

  - 独立可解码行记录对推荐推理友好；线上 batch 只查少量 ID，无需全局反量化，可将压缩表常驻 GPU 或高速存储，保持稀疏 lookup 延迟。

  - 先统计业务 embedding 坐标是否接近高斯，再选择非均匀量化/格码；若不满足，可先做归一化或白化，配合 norm restoration 使用，避免直接
  round-to-nearest 的精度损失。

  - 同等存储预算下，共享 trellis 优于 per-table 拟合码本和低秩残差；优先采用全局共享重建结构，训练时联合微调局部 scale，可进一步提升压缩效率。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：条件记忆通过选择性查表扩展 LLM 容量，但嵌入表必须整体常驻，存储成本高；现有 LLM 压缩方法主要针对稠密权重，未处理稀疏、输入依赖的查找访问。

方法关键点：Conditional Program (CP) 采用短码 + 局部 scale 表示每一行，重建程序在整表共享，只按输入请求重建对应行。实例化包括 Gaussian trellis、norm restoration、独立可解码行记录。与 2-bit round-to-nearest 相比，CP 的 2-bit 码将输出 KL 降低 41–63%。在三个训练好的 n-gram 记忆家族上分析显示，坐标统计近似高斯，同时行间存在学习关系；匹配存储预算下，共享 trellis 优于拟合码本和低秩残差变体。

关键结果数字：DeepSeek 表存储从 203GB 降至 51GB，为 GPU 常驻大表留出余量。
