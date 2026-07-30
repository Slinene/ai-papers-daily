---
title: 'GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding'
title_zh: GPTQ-2D：立方时间双边自适应舍入
authors:
- Jiale Chen
- Torsten Hoefler
- Dan Alistarh
affiliations:
- Institute of Science and Technology Austria (ISTA)
- ETH Zürich
- Red Hat AI
arxiv_id: '2607.27042'
url: https://arxiv.org/abs/2607.27042
pdf_url: https://arxiv.org/pdf/2607.27042
published: '2026-07-29'
collected: '2026-07-30'
category: Training
direction: 矩阵量化 · 双边自适应舍入加速
tags:
- GPTQ
- Quantization
- Adaptive Rounding
- Two-Sided
- Kronecker Product
- Cubic Time
one_liner: 将 GPTQ 自适应舍入扩展到双边情形，通过反对角线并行化实现立方时间复杂度
practical_value: '- 当推荐模型（如双塔 embedding 或交互矩阵）存在双侧线性变换时，可用 GPTQ-2D 做联合量化，比分别单侧量化精度更高

  - 反对角线并行化机制可直接用于加速大规模 embedding 矩阵的离线量化压缩过程

  - 如果业务中有 Kronecker 结构误差度量（如特征交叉矩阵压缩），可复用该立方时间算法

  - 对于需要同时考虑输入/输出基变换的权重量化场景（如 attention 的 QK 投影），该方法提供了可工程化的快速实现思路'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：传统 GPTQ 单边自适应舍入只能处理左边基矩阵 A，但实际应用中（如某些推荐模型参数矩阵）需要同时考虑左右两个基矩阵 A、B 下的量化误差 ∥A(Z−X)B∥²ₒ。直接向量化会导致 Gram 矩阵为 Kronecker 积形式，算法复杂度高达 O(n⁴)，不可接受。

方法：提出 GPTQ-2D，利用双边度量的结构特性，将矩阵元素按反对角线分组。每组反对角线上的元素在给定已处理元素后相互独立，因此可以并行舍入。整体流程仍为贪婪自适应舍入，产生与向量化版本完全等价的整数矩阵 Z，但复杂度降为 O(n³)。

关键结果：理论复杂度从四次降为三次，大量反对角线元素可并行处理，大幅提升实践中大规模矩阵（如 LLM 权重或推荐模型 embedding）的量化效率，且不损失精度。
