---
title: 'QESChunker: A Single Objective Unifies Overlapping and Non-Overlapping Chunking
  for RAG'
title_zh: QESChunker：用问答证据监督统一重叠与非重叠 RAG 分块
authors:
- Yifan Zhao
- Qianyang Zhao
- Xinyu Guan
- kai wei
- Yuming Deng
affiliations:
- Alibaba Group
- Taobao (China) Software Co., Ltd.
arxiv_id: '2610.36557'
url: https://arxiv.org/abs/2610.36557
pdf_url: https://arxiv.org/pdf/2610.36557
published: '2026-10-27'
collected: '2026-10-29'
category: RAG
direction: RAG 分块 · 监督式索引构建
tags:
- RAG
- chunking
- question-evidence supervision
- dynamic programming
- submodular optimization
- retrieval
one_liner: 将 RAG 分块形式化为问答证据效用最大化的监督组合优化，非重叠用 DP 精确解，重叠用贪心近似解
practical_value: '- RAG 知识库/商品文档分块别再只用固定长度或段落：沉淀业务侧 question–evidence pairs（客服问句-答案片段、售后手册标注、商品属性问答），用
  QESChunker 思路以“完整证据召回率”为预算约束优化每个文档的 chunk 边界；非重叠版可用 DP 解，适合电商知识库规模。

  - 重叠 chunk 的组合优化是 monotone submodular，贪心有 (1-1/√e) 近似，工程上可先用 LLM 生成 question-evidence
  对，再做监督式 chunking，不必等真实 query 日志，冷启动友好。

  - 论文验证指标是 complete-evidence recall，对应客服/导购 Agent 中“是否一次检索取回完整答案证据”，建议在业务评估里加这个指标，而不只看
  top-k 命中。

  - 混合 retriever 固定条件下该方法优于 heuristic，可作为 Agent 检索底座预处理：先离线构建 document-specific chunk
  index，不增加在线复杂度，适合商品手册、店铺政策等更新频率低的语料。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 的分块几乎靠启发式（固定长度、段落、语义），但 chunk 边界决定证据能否被完整召回。现有方法缺少利用问答证据监督的静态索引构建。

**方法关键点**：QESChunker 将分块视为在 question–evidence 对上的效用最大化组合优化。非重叠约束下，目标可按 chunk 分解，用动态规划在多项式时间内求精确解；允许重叠时目标单调子模，精确优化 NP-hard，贪心可达 (1−1/√e) 近似。无需 held-out test queries，只需人工标注或 LLM 生成的 question–evidence pairs。

**关键结果**：在 2 个自建 + 3 个公开数据集上，相同重叠率和固定混合 retriever 下，两种变体在 complete-evidence recall 上几乎全部优于现有分块方法。结论把分块重新定义为监督式、预算感知的证据索引构建。
