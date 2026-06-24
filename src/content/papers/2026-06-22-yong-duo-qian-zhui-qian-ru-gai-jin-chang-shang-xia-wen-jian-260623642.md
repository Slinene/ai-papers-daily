---
title: Improving Long-Context Retrieval with Multi-Prefix Embedding
title_zh: 用多前缀嵌入改进长上下文检索
authors:
- Zhenglin Yu
- Xueguang Ma
- Shengyao Zhuang
- Zhichao Xu
- Luyu Gao
- Crystina Zhang
- Jimmy Lin
affiliations:
- University of Waterloo
- University of Queensland
- University of Utah
- Carnegie Mellon University
arxiv_id: '2606.23642'
url: https://arxiv.org/abs/2606.23642
pdf_url: https://arxiv.org/pdf/2606.23642
published: '2026-06-22'
collected: '2026-06-24'
category: RAG
direction: 长上下文检索 · 多前缀嵌入
tags:
- Long-Context Retrieval
- Multi-Prefix Embedding
- Dense Retrieval
- MaxSim
- Causal Language Models
one_liner: 在单次因果前向传播中用EOS分块抽取前缀嵌入，实现细粒度检索且保留跨块上下文
practical_value: '- 在电商搜索中，若使用基于因果语言模型的检索编码器（如 LLaMA），可采用 MPE 将商品长描述按 EOS 分块，一次编码得到多个前缀嵌入，通过
  MaxSim 实现细粒度匹配，兼顾上下文感知，避免独立编码分块带来的信息割裂。

  - 训练时仅需文档级相关性标注，无需分块级细标注，显著降低标注成本，适合电商快速迭代场景。

  - 查询与文档匹配时可定位到具体分块的贡献分数，天然提供证据归因，可用于排序结果可解释性或辅助人工审核。

  - 存储开销远低于 token 级多向量方法（如 ColBERT），同时保持较好的细粒度匹配能力，适合大规模商品库的近似检索。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
长上下文检索面临两难：单向量嵌入压缩丢失细粒度信息，token 级多向量方法（如 ColBERT）虽精细但索引存储和检索代价过高。独立分块编码又丢失跨块上下文。

## 方法
提出 **Multi-Prefix Embedding (MPE)**，将长文档按需切分为若干块，块间插入 EOS token，在单次因果前向传播中编码整个序列。每个 EOS token 的隐藏状态作为对应前缀的嵌入向量，形成文档的多向量表示。查询与文档的相似度通过 MaxSim（查询向量与各前缀嵌入的内积最大值）计算。训练只需文档级相关性标签，采用对比学习框架。

## 关键结果
在 MLDR-en、BrowseComp-Plus 和 LongEmbed 等长上下文检索基准上，MPE 性能优于或匹配单向量、独立分块和 token 级多向量基线，同时仅需文档级标签，并自然支持证据块定位。
