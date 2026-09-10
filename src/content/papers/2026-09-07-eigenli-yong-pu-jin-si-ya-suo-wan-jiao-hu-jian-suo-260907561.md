---
title: 'EigenLI: Spectral Approximations to Late Interaction'
title_zh: EigenLI：用谱近似压缩晚交互检索
authors:
- Archish S
- Sabyasachi Basu
- Ankit Garg
- Ravishankar Krishnaswamy
- Kirankumar Shiragur
affiliations:
- Temple University
- Microsoft Research India
arxiv_id: '2609.07561'
url: https://arxiv.org/abs/2609.07561
pdf_url: https://arxiv.org/pdf/2609.07561
published: '2026-09-07'
collected: '2026-09-10'
category: RecSys
direction: 多向量检索压缩 · 谱方法
tags:
- Late Interaction
- Multi-Vector Retrieval
- Spectral Compression
- EigenLI
- ANN
- ColBERT
one_liner: 利用文档 token 的低秩结构，以 top-k 特征子空间替代聚类压缩多向量表示，并可转成单向量 ANN 召回
practical_value: '- 多向量召回（商品/内容/广告）可把每个文档 token 序列压缩为文档特定的 top-k 特征子空间，训练无关；相比 k-means/Ward
  pooling，构造更快（约 6.8x/17.5x），且在 ColBERTv2、AnswerAI 等模型上 nDCG@10 相对提升 8%–15%。

  - EigenLI 评分可精确转成单向量点积：对 query token 做二次核 K(qi)，对文档 top-k 特征向量做 K(wj)，得到 d(d+1)/2
  维向量，直接接入现有 ANN 系统；在 d=128 时维度 8256，比 MUVERA 10240 维更低，但 BEIR 上 nDCG@10 相对 MUVERA
  提升 78.9%（AM）。

  - 评分时不要用特征值加权，只用 top-k 特征向量；用 λ_j 加权会退化为所有 query-doc token 相似度求和，偏离 MaxSim，效果明显变差。

  - 模型几何差异要作为模型选型依据：强各向异性模型如 GTE-ModernColBERT 上 EigenLI-32 不如 Ward pooling，可对 embedding
  做去均值 centering 后再压缩，或对这类模型保留聚类方案。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多向量 / late-interaction 模型（ColBERT 等）用大量 token 级向量表示文档，检索质量强但索引、存储和 MaxSim 评分成本高。现有训练无关压缩主要是剪枝和聚类 pooling，把向量集合压成更小的向量集合；这类方法在部分模型上有效，但未利用 token 向量本身的结构。

**方法关键点**
- 观察：文档 token 向量近似落在低维子空间，二阶矩矩阵 M_D = Σ d_i d_i^T 特征值快速衰减。
- 核心：对每个文档计算 M_D 的 top-k 特征向量 w_1...w_k，用子空间表示文档；评分 s_k(Q,D) = Σ_i Σ_j ⟨q_i, w_j⟩²，等于每个 query token 投影到该子空间的能量。
- 不用特征值加权；作者证明加权版本退化为所有 token 相似度求和，偏离 MaxSim。
- EigenLI-SV：将评分改写为 ⟨Σ q_i⊗q_i, Σ w_j⊗w_j⟩，通过二次核 K(x) 得到 d(d+1)/2 维单向量，数学上等价；d=128 时维度 8256，可与 ANN 系统直接兼容。

**关键实验**
- 数据集：BEIR 13 个开发集、ViDoRe-v3 8 个多模态集；模型：ColBERTv2、AnswerAI-ColBERT-small、GTE-ModernColBERT、视觉 ColQwen3 4B。
- 多向量对比：k=32 时，ColBERTv2 上 EigenLI 对 k-means++ 的 nDCG@10 AM 相对提升 15.0%，对 Ward 提升 8.0%；AnswerAI-small 同样优于聚类；GTE-ModernColBERT 则 Ward 更好；ColQwen3 对 k-means++ 提升 5.5%、Ward 3.4%。
- 单向量对比：EigenLI-SV-32 在 ColBERTv2 上 nDCG@10 对 MUVERA 的 AM 相对提升 78.9%，维度更低；且在 center 后的各向异性模型上仍大幅领先 MUVERA。
- 压缩成本：EigenLI 比 k-means++ 快约 6.8x，比 Ward 快约 17.5x。

**值得记住的一句话**
把文档从“一组 token 向量”压缩为“低维特征子空间”，评分上直接逼近 MaxSim，还可无痛转成单向量 ANN 召回。
