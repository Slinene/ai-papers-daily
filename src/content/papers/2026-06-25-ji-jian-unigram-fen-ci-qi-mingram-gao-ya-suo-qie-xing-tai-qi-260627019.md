---
title: 'MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive
  Morphological Alignment'
title_zh: 极简 Unigram 分词器 MinGram：高压缩且形态对齐
authors:
- Sander Land
affiliations:
- Writer, Inc.
arxiv_id: '2606.27019'
url: https://arxiv.org/abs/2606.27019
pdf_url: https://arxiv.org/pdf/2606.27019
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: 分词器训练优化 · 极简 Unigram
tags:
- Unigram
- Tokenization
- Compression
- Morphological Alignment
- BPE
- Language Model
one_liner: 用 BPE 种子与硬 EM 简化 Unigram 训练，实现更高压缩与形态对齐，下游 LM 训练优于 BPE
practical_value: '- **在特定领域语料上训练高效 tokenizer**：电商/广告/搜索文本（商品名、查询词）往往有特殊频率分布，MinGram
  可利用 BPE 种子快速训练出高压缩且形态更合理的 tokenizer，降低序列长度，从而加速 Transformer 推理与训练。

  - **优化生成式推荐中的 token 化策略**：若将物品表示为 Semantic ID 或序列生成，tokenizer 直接影响序列长度和解码效率。MinGram
  的高压缩与对齐特性可减少 token 数，提升生成速度且可能改善 ID 表示质量。

  - **多语言场景下的轻量 tokenizer 训练**：对于跨国电商或搜索，MinGram 简化训练流程，去除后缀数组等重操作，易于对不同语言快速定制 tokenizer，同时保持优于
  BPE 的压缩和下游 bits-per-byte。

  - **直接复用压缩优先模式**：若需要极致压缩以降低存储/带宽成本（如客户端模型、实时搜索），可使用其压缩导向变体，在保持合理对齐的前提下匹配最强分词压缩器。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：标准 Unigram 分词器表示优雅（token 列表+分数），易于编辑词汇，但训练复杂（需要后缀数组、前向后向传播、迭代剪枝循环）。BPE 虽简单，但压缩和形态对齐较差。

**方法**：MinGram 保留 Unigram 的 token 列表表示，但大幅简化训练：1) 用 BPE 构建的种子词表初始化；2) 用硬 EM 算法搜索最小 token 数分段路径（替代概率模型）；3) 单次 flat score 剪枝（省略多次迭代）。以 token 数量为主要目标，Unigram 分数仅用于打破平局。

**结果**：在英语、芬兰语等六种语言上，MinGram 的压缩率优于 BPE 和标准 Unigram；压缩导向变体在保持更高形态对齐的同时，和最强基于 token 数的压缩器效果相当。在控制条件下的 LM 训练中，Unigram 家族分词器（MinGram 居于前列）的 bits-per-byte 一致优于 BPE。该方法训练代价低，几乎只需 tokenizer 推理能力，且代码已开源。
