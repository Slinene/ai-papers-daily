---
title: 'GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted
  Indices'
title_zh: GPUSparse：GPU并行倒排索引加速学习稀疏检索
authors:
- Ashutosh Sharma
affiliations:
- MIT-IBM Watson AI Lab
arxiv_id: '2606.26441'
url: https://arxiv.org/abs/2606.26441
pdf_url: https://arxiv.org/pdf/2606.26441
published: '2026-06-24'
collected: '2026-06-27'
category: RecSys
direction: GPU加速稀疏检索系统
tags:
- Learned Sparse Retrieval
- GPU Inverted Index
- Triton Kernels
- SPLADE
- Scatter-Add
- Parallel Scoring
one_liner: 通过GPU并行倒排索引与批量scatter-add融合核实现SPLADE精确评分，在MS MARCO上较CPU加速235倍
practical_value: '- 若业务使用稀疏模型（如电商搜索中的商品文本召回），可将倒排索引与评分逻辑移植到GPU，通过块对齐posting list及warp-coalesced访问优化内存带宽，大幅降低延迟。

  - 批量scatter-add核融合思想可直接借鉴：将query-term匹配的score累加到doc-tensor，省去中间遍历开销，适用于类似向量化召回评分的场景。

  - 系统设计上，采用query-batch并行处理提升GPU利用率，在实时服务中结合动态batch组装，可平衡延迟与吞吐。

  - Triton编写的融合kernel权衡了工作效率与带宽效率，对自研CUDA kernel的团队有参考价值，避免逐term展开导致利用率低下的问题。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：SPLADE等学习稀疏检索模型虽然质量媲美稠密模型，但推理阶段仍依赖CPU倒排索引遍历算法（WAND、Block-Max WAND），大规模在线服务遇到瓶颈。  
**方法**：GPUSparse提出三项技术：① GPU并行的、块对齐且warp合并的倒排索引结构；② 批量scatter-add评分算法，可同时处理数百个查询；③ 基于Triton的融合kernel，并分析工作效率与硬件利用率的权衡。评分过程被重构为在倒排索引上执行scatter-add，与SPARe的迭代模式一致，但通过融合核实现，比SPARe再实现快23-270倍。  
**结果**：在MS MARCO段落排序（8.8M文档）上，GPUSparse精确评分与CPU实现完全一致（MRR@10=0.383，Recall@1000≥0.999），单查询延迟1.27ms vs. 298ms（235×加速）。相较于牺牲25%召回换速度的最快CPU系统Seismic，GPUSparse在保持精确结果的条件下达到787 QPS（batch=500，每查询1.3ms）。文档并行kernel达到H100峰值带宽的62.6%，揭示了GPU稀疏检索中工作效率与带宽效率的根本折衷。
