---
title: 'ColBERTSaR: Sparsified ColBERT Index via Product Quantization'
title_zh: ColBERTSaR：通过乘积量化实现ColBERT索引稀疏化
authors:
- Eugene Yang
- Andrew Yates
- Dawn Lawrie
- James Mayfield
- Saron Samuel
- Rohan Jha
affiliations:
- Johns Hopkins University
arxiv_id: '2606.05568'
url: https://arxiv.org/abs/2606.05568
pdf_url: https://arxiv.org/pdf/2606.05568
published: '2026-06-04'
collected: '2026-06-07'
category: RecSys
direction: 神经检索 · 索引压缩与稀疏化
tags:
- ColBERT
- Product Quantization
- Inverted Index
- Sparse Retrieval
- Index Compression
one_liner: 利用乘积量化将ColBERT密集索引转化为真正的倒排索引，在保持效果的同时缩小索引50-70%
practical_value: '- **多向量检索索引压缩**：如果业务中使用类似ColBERT的多向量检索（如商品多模态嵌入匹配），可直接借鉴乘积量化将每篇文档的Token嵌入离散化为码本ID，构建经典倒排索引，大幅降低存储和查询时的解压开销。

  - **平衡效果与存储**：该方法在保持检索质量的前提下，索引大小仅为1-bit PLAID的30%-50%，对于资源受限的电商搜索或推荐系统，可作为一种轻量级部署方案。

  - **查询效率优化**：传统ColBERT查询瓶颈在于“收集-解压”阶段，本工作通过量化将直接倒排查询，省去了在线解压和MaxSim的全量聚集，适合要求低延迟的实时推荐或搜索场景。

  - **学习稀疏化思路**：文中指出的“嵌入量化等价于学习稀疏检索”观点，启发我们可以用类似方法将其他稠密检索模型压缩为稀疏表示，方便与现有搜索引擎基础设施集成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：ColBERT 作为高效神经检索架构，需要庞大索引来支持近似匹配和 MaxSim 计算，PLAID 等实现需要5-10倍于原始文本的存储，且查询时文档Token的收集和解压是主要瓶颈，限制了大规模可扩展性。

**方法**：提出 ColBERTSaR，利用乘积量化（Product Quantization）将 ColBERT 的稠密Token嵌入量化为一组离散码本ID，从而将索引转化为真正的倒排索引结构，类似于传统稀疏检索。查询时直接使用倒排索引进行匹配，避免了在线解压和全量 Token 收集，仅保留轻量的近似分数计算。

**结果**：在 MS MARCO 段落检索等基准上，ColBERTSaR 的索引大小比 1-bit PLAID 缩小 50-70%，同时保持相当甚至更好的 MRR@10 效果（例如在测试集上 MRR@10 仅下降不到1%）。理论分析表明，嵌入量化的 ColBERT 在评分机制外等同于学习到的稀疏检索方法。
