---
title: 'H3D: Benchmarking Unsupervised Text Hashing for Fine-Grained Document Deduplication'
title_zh: H3D：面向细粒度文档去重的无监督文本哈希基准
authors:
- Qianren Mao
- Jiaxun Lyu
- Junnan Liu
- Zhijun Chen
- Jingzheng Li
- Hanwen Hao
- Bo Li
affiliations:
- Zhongguancun Laboratory
- Beihang University
- Monash University
- Hong Kong Polytechnic University
arxiv_id: '2607.08382'
url: https://arxiv.org/abs/2607.08382
pdf_url: https://arxiv.org/pdf/2607.08382
published: '2026-07-09'
collected: '2026-07-10'
category: Eval
direction: 文档哈希基准 · 去重评测
tags:
- document hashing
- deduplication
- benchmark
- unsupervised
- fingerprinting
- embedding-based hashing
one_liner: 提出统一基准H3D，比较无监督非学习哈希与预训练嵌入量化哈希在细粒度文档去重上的效果、效率与鲁棒性
practical_value: '- **商品描述去重选型**：在电商平台中，对于近似抄袭或刷单生成的商品描述，MinHash/SimHash等结构指纹方法速度快、效果好，适合大规模近重复检测；若需识别改写或翻译后的同义描述，可选用BGE嵌入+LSHash，但需权衡计算开销。

  - **内容去重的工程化评估**：参考H3D的统一评测框架（map、ndcg@20、效率、鲁棒性），可在自有业务数据上快速对比不同哈希方法的适用性，避免盲选。

  - **冷启动场景**：无监督非学习哈希无需训练数据或相似对标注，部署简单，适合新业务线快速启动文本去重。

  - **相似度度量的等价性分析**：论文对不同哈希码下不同相似度度量（如Jaccard、Hamming）何时排序等价的分析，可指导实际系统中度量函数的选择，减少实验开销。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有文档哈希研究缺少统一基准，方法比较口径不一，尤其缺乏对细粒度科学文档去重的有效评测。  
**方法**：构建H3D基准，涵盖代表性无监督非学习哈希（MinHash、SimHash、Winnowing、FuzzyHash、FlyHash），以及基于冻结BGE嵌入的两种量化策略：BGE‑BIHash（二值哈希）和BGE‑LSHash（局部敏感哈希）。在CSFCube（分面级科学文档相似度）和RELISH（大规模生物医学相似搜索）两个互补数据集上，报告排序质量（MAP、NDCG@20）、效率与文本压缩下的鲁棒性。  
**结果**：词汇与结构指纹在近似重复匹配上表现有竞争力；语义敏感表示在内容改写后相似度保持更优，但计算成本更高。同时分析了不同相似度度量在特定哈希表示下的排序等价性，提升了方法对比的可解释性和可复现性。
