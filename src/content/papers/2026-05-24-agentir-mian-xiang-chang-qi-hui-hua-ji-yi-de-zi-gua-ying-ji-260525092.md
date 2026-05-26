---
title: 'AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational
  Memory'
title_zh: 'AgentIR: 面向长期会话记忆的自适应级联检索基底'
authors:
- Aojie Yuan
- Haiyue Zhang
- Shahin Nazarian
affiliations:
- University of Southern California
arxiv_id: '2605.25092'
url: https://arxiv.org/abs/2605.25092
pdf_url: https://arxiv.org/pdf/2605.25092
published: '2026-05-24'
collected: '2026-05-26'
category: Agent
direction: 自适应级联检索 · Agent 记忆工作负载
tags:
- agent memory
- hybrid retrieval
- cascade router
- recency bias
- BM25 acceleration
- GPU retrieval
one_liner: 针对 LLM Agent 记忆的强近期偏斜与查询异质性，设计自适应级联检索系统，实现次线性扩展与跨工作负载自动融合选择。
practical_value: '- **时间分区索引利用 recency skew**：将 Agent 记忆按时间窗口分桶，查询时仅检索最新分区，在典型近期偏斜分布下复杂度
  O(log 1/ε)，实测 5M 记录下子 100μs 延迟，可显著降低在线客服或推荐系统中长期历史查询的延迟。

  - **级联路由按查询置信度跳过稠密通道**：先跑廉价的 BM25，若Top-k 分数差跨过阈值则跳过耗时的 Dense 通道，在 LongMemEval 上跳过
  63% 查询仍保持同等精度，部署时可用少量标注数据（50样本）自动学习阈值，适用于电商 Agent 中多数查询为简单事实查找的场景。

  - **两轴控制面适配异质查询**：融合策略（BM25/Dense/RRF/带时效偏好的 RRF）和是否激活稠密通道均按查询决策，可应对同一个 Agent 会话中从事实查找、推理到时间查询的类型切换。可用于推荐系统中混合搜索（关键词
  vs 语义）的动态切换。

  - **BM25 工程加速与正确性坑点**：SIMD 向量化、MaxScore 剪枝、GPU 两段核函数及共享内存初始化问题等具体实现细节可直接复用到自研稀疏检索模块，避免因预归一化
  TF 或 nDCG 公式错误导致 6-8× 质量下降。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM Agent 在长期多轮交互中积累海量记忆记录（对话、工具调用、规划等），每次推理需实时查询记忆，要求亚 10ms 的检索延迟。传统的 IR 引擎（Lucene、FAISS）假定索引静态、查询分布平稳，未利用 Agent 记忆的强烈近期偏斜、单调增长和查询类型高度异构等特性，导致延迟高、资源浪费。

**方法关键点**：
- 设计 AgentIR，保持三条实时通道：SIMD 加速的 BM25 稀疏检索、HNSW 稠密检索、时间分区索引，对每条查询在**两轴**上做决策：用哪种融合（BM25、Dense、RRF 或带时效偏好和重要度加权的 agent_rrf）以及是否激活耗时的稠密通道（级联路由器）。
- 时间分区索引利用指数衰减的近期偏斜，按 7 天窗口分区，查询时仅搜索最近几个分区，理论期望工作量 O(log 1/ε)，独立于总语料规模。
- 稀疏检索采用 AVX2 向量化的 CSR 布局、MaxScore 剪枝，GPU 两段核函数（评分 + Top-k），并特别注意了 BM25 实现中的三个坑：预归一化 TF、线性增益 nDCG、GPU 共享内存未初始化。
- 运行时查询类型路由器：用 TF-IDF 或 BGE-small 特征 + 逻辑回归预测查询类型，路由到该类型最佳融合策略，仅需 <1 ms 额外开销。

**关键实验**：
- 在 LongMemEval（500 条问题，19K 会话）上，带时效偏好的 RRF 达到 R@10=0.978、LLM 严格准确率 0.254；级联路由器跳过 63% 查询，实现 2.67× 加速且准确率持平；配合查询类型阈值 5 折交叉验证下可达 5.76× 加速。
- 在 LoCoMo 对话 QA 上，同一触发机制自动学习到 BM25 单独即最优，跳过全部稠密通道，加速 132×，且 Hit@5 提升 0.089。
- BEIR 9 个数据集上，CPU 8 线程比 Pyserini 快 10 倍（几何平均），GPU 快 1.8-39 倍，nDCG@10 差异在 ±0.020 内；时间分区索引在 5M 记录下提供 1769× 加速，且语料增长 1234 倍时延迟仅增长 3.6 倍，单次查询 p50 延迟保持 90μs。
- 搭建了 SPLADE 到 CSR 格式的桥梁，验证了可无缝接入学得稀疏权重以提升质量，且不改动检索内核。

**最值得记住的一句话**：Agent 记忆检索不是“小 IR”，其极端的近期偏斜、异质查询和在线增长使专门的索引结构与自适应路由带来的收益远超通用引擎。
