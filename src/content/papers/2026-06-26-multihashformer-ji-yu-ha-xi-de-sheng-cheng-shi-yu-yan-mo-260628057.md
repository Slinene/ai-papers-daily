---
title: 'MultiHashFormer: Hash-based Generative Language Models'
title_zh: MultiHashFormer：基于哈希的生成式语言模型
authors:
- Huiyin Xue
- Atsuki Yamaguchi
- Nikolaos Aletras
affiliations:
- School of Computer Science, University of Sheffield
arxiv_id: '2606.28057'
url: https://arxiv.org/abs/2606.28057
pdf_url: https://arxiv.org/pdf/2606.28057
published: '2026-06-26'
collected: '2026-06-29'
category: LLM
direction: 基于哈希的生成式语言模型
tags:
- hash-based LM
- parameter efficiency
- vocabulary bottleneck
- autoregressive generation
- embedding compression
- multilingual expansion
one_liner: 用多哈希函数生成唯一 token 签名，实现哈希自回归生成，在保持低参数量的同时超越标准 Transformer
practical_value: '- **商品 / 搜索词嵌入压缩**：在推荐或搜索系统中，物品 ID 或 query 的词汇表极大，可以利用多哈希签名代替全量
  embedding 矩阵，大幅降低参数量与内存。

  - **生成式推荐中的物品解码**：对于 GenRec 场景，可将物品编码为哈希签名，由解码器自回归生成签名序列，再映射回具体物品，实现无固定词表的生成式推荐。

  - **动态词表扩展**：新商品、新搜索词随时上线时，无需重新训练或增加参数即可通过哈希映射加入，适合电商环境下频繁变动的 item 库。

  - **多语言 / 多模态统一表示**：若业务涉及多语言商品描述或多模态实体，可用相同哈希框架统一编码，避免为每种语言或模态单独维护 embedding 表。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：标准 Transformer LM 的嵌入矩阵随词表线性增长，造成严重的参数与内存瓶颈，且词表固定，难以动态扩展。已有的哈希方法（如 HashFormer）虽能压缩参数，但多对一冲突使其仅适用于编码器，无法用于自回归生成。

**方法**：提出 MultiHashFormer，为每个 token 分配一个由多个独立哈希函数生成的**哈希签名**（短序列哈希 ID），保证唯一性。一个 Hash Encoder 将该签名压缩为潜向量，送入标准 Transformer 解码器进行自回归建模；输出端则由 Hash Decoder 逐步生成下一个 token 的哈希签名，最后通过查找表恢复为文本。整个流程无需维护完整的词表嵌入矩阵，参数规模不随词表扩大而增长。

**结果**：在 100M、1B、3B 三种参数量级下，MultiHashFormer 在多个语言建模基准上一致超越标准 Transformer LM。此外，在恒参数条件下直接支持多语言词表扩展，无需改动模型结构，展现出极强的实用性与扩展性。
