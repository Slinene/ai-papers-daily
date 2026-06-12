---
title: Uncertainty-Aware Hybrid Retrieval for Long-Document RAG
title_zh: 面向长文档 RAG 的不确定性感知多粒度混合检索框架
authors:
- Hoin Jung
- Xiaoqian Wang
affiliations:
- Purdue University
arxiv_id: '2606.13550'
url: https://arxiv.org/abs/2606.13550
pdf_url: https://arxiv.org/pdf/2606.13550
published: '2026-06-11'
collected: '2026-06-12'
category: RAG
direction: 检索增强生成 · 多粒度混合检索与不确定性估计
tags:
- RAG
- Hybrid Retrieval
- Uncertainty Estimation
- Document Chunking
- Entropy-based Fusion
one_liner: 提出无需训练的 UMG-RAG，利用检索得分分布的熵动态估计各检索源与粒度的置信度，并通过父块提升生成连贯的紧凑上下文。
practical_value: '- **多路召回动态融合**：借鉴基于熵的置信度估计，电商搜索/推荐的多路召回（如语义向量 + BM25）可以不再使用固定权重融合，而是根据查询的得分分布“锐度”自适应分配权重，提升不同类型
  query 的召回质量。

  - **细粒度定位 + 父块返回**：在商品描述或用户评价的长文本检索中，可用句子级精准召回证据，再通过 parent promotion 返回段落级上下文，保持生成理由或答案的局部连贯性，同时用重叠去重避免冗余。

  - **零训练即插即用**：整个方法不修改现有检索器和生成器，只做检索后处理，可以极低成本集成到现有 RAG 管线中，适合快速验证和上线。

  - **长度惩罚控制上下文体积**：通过长度惩罚（除以 sqrt(token 数)）在最终排序中倾向紧凑 chunk，能缓解大模型“lost-in-the-middle”问题，减少生成延迟和内存占用，对实时性要求高的推荐文案生成场景尤其有用。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG 面临检索粒度权衡：粗粒度（长段落）保留上下文但引入大量噪声，容易造成生成器忽略关键证据（“lost-in-the-middle”）；细粒度（句子级）紧凑但可能缺失语义或词汇匹配信号，导致证据被漏检。现有长上下文干预方法（位置校准、压缩提示）假设证据已被检索，而多粒度检索方法又常依赖额外结构（知识图谱、多层次索引）。本文聚焦于一种即插即用、无需训练的解决方案：根据查询自适应地融合不同粒度、不同检索源的证据。

### 方法关键点
- **多粒度分块**：将文档按 {2,4,8,16,32} 个句子重叠切块，构成多粒度检索空间。
- **互补检索专家**：同时使用 dense 检索器（语义匹配）和 sparse 检索器（词法/实体匹配），每对 expert-granularity 独立检索 Top-100 候选。
- **不确定性感知融合**：对每个候选集归一化得分并转换为证据分布，用归一化熵衡量检索不确定性。熵越低→分布越尖锐→置信度越高。据此计算各 expert-granularity 对的权重，加权混合得到最终证据分数。
- **长度惩罚与 top-K 选择**：证据分数除以 sqrt(token 数) 惩罚长 chunk，选 top-5 组成最终上下文。
- **父块提升（UMGP-RAG）**：将细粒度命中（2/4 句）提升到更宽的父块（8 句），并基于重叠比例去重，确保返回的上下文紧凑且连贯。

### 关键实验结果
在 Natural Questions 和 HotPotQA 数据集上，使用 BERT/BGE-M3/Qwen3-Embedding-4B 作为 dense 检索器、SPLADEv3 为 sparse 检索器，Qwen2.5-3B 和 Llama-3.2-3B 为生成器。主要结论：
- UMGP-RAG 在生成指标上全面超越固定融合的 Hybrid RRF 以及标准 RAG、LongRAG 等基线。以 NQ + Qwen3-Emb-4B + Llama-3.2-3B 为例，UMGP-RAG 获 F1=0.522、AR=0.498，而 Hybrid 为 0.492/0.474，标准 RAG 仅 0.494/0.462。
- 更高的检索召回率（AR@5）并不保证更好生成：LongRAG 经常获得更高 AR@5，但因返回冗长上下文导致生成质量反而下降。
- 父块提升显著优于纯融合（UMG-RAG），说明细粒度定位 + 连贯上下文返回是有效模式。
- 方法虽增加检索预处理时间（5.36s/query vs 0.15s），但大幅减少生成耗时和内存。

**核心洞见**：最优的 RAG 上下文不是最长或只要包含答案的文本，而是紧凑、局部连贯且与查询高度匹配的证据片段。
