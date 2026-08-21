---
title: Quantization Beyond Uniform Bit Allocation
title_zh: 超越均匀位分配的量化
authors:
- K. S. Sreeramji
- Sabyasachi Basu
- Ravishankar Krishnaswamy
- Kirankumar Shiragur
- Yujia Wang
affiliations:
- Indian Institute of Science
- Microsoft Research
- Microsoft STCA
arxiv_id: '2608.19388'
url: https://arxiv.org/abs/2608.19388
pdf_url: https://arxiv.org/pdf/2608.19388
published: '2026-08-19'
collected: '2026-08-21'
category: Other
direction: 向量量化 · 非均匀位分配
tags:
- quantization
- MRL embeddings
- Product Quantization
- Scalar Quantization
- vector search
- recall optimization
one_liner: 针对MRL嵌入提出按连续桶非均匀分配位数的量化框架，等存储下PQ/SQ召回最高提升8%/18%
practical_value: '- 若线上 embedding 具备 MRL 结构（例如多任务/多模态训练或直接使用 MRL 训练），可以放弃 uniform
  bit allocation，按维度重要性分桶，将更多 bit 分配给高方差/高信息桶，特别在 int4/int8 等低比特压缩下能显著提升召回。

  - 工程落地风险低：分桶为 contiguous bucket，利于 cache 和 SIMD；贪心位宽搜索可离线执行，线上查询只使用预计算码本，无额外推理开销。可直接在
  DiskANN 等向量索引层实现，开源代码可参考。

  - 对商品/用户 embedding 大规模建库时，先做小样本统计分析维度方差/重要性，若存在递减或聚类结构，可考虑 variable bit allocation；存储预算固定下比加
  GPU 或换模型更容易提升 recall@k。

  - 该工作主要针对 MRL 嵌入；如果不确定业务 embedding 是否具备 Matryoshka 属性，可先训练或验证 MRL 特性，或在线收集维度重要性指标，再决定是否启用非均匀量化。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：嵌入维度不断增长，量化是控制存储的关键；现有量化方案大多与嵌入无关，对所有维度平均分配位宽。但现代模型产生的嵌入常具有明显几何结构，例如 Matryoshka Representation Learning (MRL) 嵌入，其维度重要性不均衡。

方法关键点：将嵌入划分为连续桶，桶间非均匀分配存储；结合贪心分配策略决定各桶位宽。框架分别在 Product Quantization (PQ) 与 Scalar Quantization (SQ) 上实例化，分配过程基于嵌入统计特性离线完成。

结果：在 MRL 嵌入上，相同存储预算下非均匀分配一致优于均匀基线；低比特区间收益最大。相同压缩率下，PQ 召回最高提升 8%，SQ 最高提升 18%。开源代码位于 DiskANN 的 variable_quantization 分支。
