---
title: 'Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries'
title_zh: Stellar：面向自然语言查询的可扩展多模态文档检索
authors:
- Yuxiang Guo
- Zhonghao Hu
- Yuren Mao
- Yuhang Liu
- Congcong Ge
- Xiaolu Zhang
- Jun Zhou
- Yunjun Gao
arxiv_id: '2606.19960'
url: https://arxiv.org/abs/2606.19960
pdf_url: https://arxiv.org/pdf/2606.19960
published: '2026-06-18'
collected: '2026-06-20'
category: RAG
direction: 多模态检索 · 高效延迟交互
tags:
- Multimodal Retrieval
- Late Interaction
- Scalability
- RAG
- Document Filtering
- Disk-based Retrieval
one_liner: 通过词法过滤与磁盘驻留延迟交互，将多模态检索的内存和延迟降低1-2个数量级且效果不降。
practical_value: '- 词法表示过滤（LRF）：微调多模态大模型作为稀疏编码器生成高质量词法表示，可用于商品搜索的第一阶段候选过滤，大幅减少需深度计算的候选集。

  - 磁盘支持的延迟交互（DLI）：将商品/文档的多向量 token 级 embedding 存于磁盘，按需动态加载，可有效降低内存占用，适合百亿级商品索引。

  - 平衡聚类的存储布局：根据负载模式设计磁盘存储结构，可借鉴到推荐模型的大规模稀疏特征存储，减少随机 I/O。

  - 成本模型驱动加载：通过简单代价模型选择必要的 token embedding 参与最终评分，在实时推荐中可用于选择性计算用户与物品的细粒度交互特征。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**  
多模态文档检索是 RAG 的关键环节，但主流的基于 token-level 多向量延迟交互方法内存开销巨大，难以横向扩展至大规模语料。  

**方法**  
Stellar 包含两个核心设计：  
1) **词法表示过滤（LRF）**：微调多模态大模型（MLLM）作为稀疏编码器，为文档生成高质量词法表示，用于高效过滤候选文档，将候选集缩小 1-2 个数量级。  
2) **磁盘支持的延迟交互（DLI）**：将文档的 token 级 embedding 持久化存储在磁盘，通过平衡聚类算法优化存储布局，并利用一个简单代价模型动态决定哪些 token embedding 需要加载至内存参与最终的迟交互计算，从而避免全量加载。  

**结果**  
在 4 个公开基准及一个新建的大规模数据集上，Stellar 相对于现有 SOTA 方法，内存开销和查询延迟均降低 1-2 个数量级，同时检索效果（NDCG、Recall 等）无显著下降。
