---
title: 'HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration for
  LLM Decoding'
title_zh: HiKV：面向 LLM 解码的分层重要性感知 KV 缓存与硬件加速
authors:
- Chao Fang
- Jun Yin
- Man Shi
- Marian Verhelst
affiliations:
- KU Leuven
- UC Berkeley
arxiv_id: '2607.22389'
url: https://arxiv.org/abs/2607.22389
pdf_url: https://arxiv.org/pdf/2607.22389
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: LLM 推理 · KV 缓存压缩与硬件加速
tags:
- KV cache compression
- hardware-software co-design
- importance-aware pruning
- LLM decoding
- element-level sparsity
- chunk-based sorting
one_liner: 分层 token 与元素双粒度重要性感知压缩，结合可重构硬件排序器，在 1% 精度损失内实现 7.95 倍加速和 90% 能耗降低
practical_value: '## 业务可借鉴点


  - **分层重要性思想可迁移至推荐系统稀疏化**：HiKV 证明 KV 缓存冗余同时存在于 token 和元素两个粒度，建议在推荐模型（如 transformer-based）的长期行为序列建模中，尝试类似的「先筛重要交互、再筛每项交互中重要特征维度」的二阶段稀疏策略，用更少的存储/计算维持精度。

  - **双银行 + 最小堆维护重要 token**：Stage I 的 recent / important 银行与 min-heap 更新方式（HEAPIFY_UP/DOWN），可应用于
  Agent 场景下的多轮对话历史管理：始终保留最近的若干交互，同时动态淘汰历史中重要性低的对话轮次，用 O(log B) 的代价保持固定预算。

  - **分块并行排序近似全局 selection**：Stage II 的 chunk-based sorting 可将 P 向量的 top-k 选择从 O(N
  log N) 降至 O(N log d_h)，且召回率超 95%，可直接用于在线推理中需要选取重要 token/特征的场景（如长上下文中的关键 token 挑选），避免全局排序的高延迟。

  - **硬件－算法协同设计视角**：如果业务计划自研推理加速硬件，可参考「可重构重要性排序器（RIS）」的设计：同一电路通过配置支持堆操作和分块排序，面积仅增
  8%。这提示在对延迟敏感的检索/推荐系统中，专用排序单元能以较低成本换取端到端效率。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机

LLM 自回归解码时，KV 缓存随序列长度和批处理规模线性增长，逐渐成为主要内存带宽瓶颈。现有重要性感知方法（如 H2O）仅从 token 粒度压缩缓存，忽略了 token 内部向量元素的冗余。HiKV 观察到 KV 缓存在 token 级和元素级同时存在稀疏性，可以正交压缩。

## 方法关键点

- **分层重要性建模**：Stage I 粗粒度 token 选择，Stage II 细粒度元素选择，两者独立正交，总压缩比 = token 压缩比 × 元素压缩比。
- **Stage I（token 级）**：固定缓存预算，维护 recent 银行（FIFO）和 important 银行（min-heap）。仅对 recent 银行累积注意力权重作为重要性分数，离开 recent 银行时通过比较进入 important 堆（HEAPIFY_UP/DOWN），将 token 级维护复杂度降至 O(log B)。
- **Stage II（元素级）**：基于 Q 向量做全局 Top-B 选择，选取 K 缓存的关键维度；对 P 向量按 head 维度大小分块，各块内部做 Top-B 选择，挑选 V 缓存中每块最重要的 token 行，避免全局排序的高昂开销，召回率稳定在 95% 以上。
- **硬件加速器**：设计可重构重要性排序器（RIS），通过组合 16 输入 bitonic 排序器、部分归并器与最大最小选择器，以统一电路支持 Stage I 的堆操作和 Stage II 的全局/分块排序，面积仅增加 8%。

## 关键实验

在 Mistral-7B、LLaMA3-8B、LongChat-7B、Qwen2.5-0.5B 等模型上，用 LongBench 子集评估。基线为无压缩 FP16、StreamingLLM、H2O 以及硬件方案 Token-Picker。在 1% 精度损失约束下：
- HiKV 比仅 token 级别的方法额外获得 1.82–4.87× 的外部内存访问减少。
- 对比无压缩基线，注意力计算达到最高 7.95× 加速和 90% 能耗降低。
- 硬件实现（TSMC 16nm, 300 MHz）在相同计算平台下，HiKV 的内存流量和端到端性能均显著优于 SotA。

## 核心洞察

分层重要性感知（token + element）能以最小开销同时减少 cache 容量与带宽需求，且通过 chunk-based 局部排序近似全局 selection 在硬件友好前提下几乎无损，是算法－硬件联合设计的一条高效路径。
