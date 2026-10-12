---
title: 'Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence'
title_zh: 超越最终 Embedding：从 Token 级证据中检索记忆
authors:
- Han Luo
- Zhan Zhuang
- Xu He
- Jujia Zhao
- Yu Li
- Suqin Yuan
- Dong Li
- Lei Feng
affiliations:
- Southeast University
- MemoraX AI
- Leiden University
- University of Sydney
arxiv_id: '2610.13277'
url: https://arxiv.org/abs/2610.13277
pdf_url: https://arxiv.org/pdf/2610.13277
published: '2026-10-09'
collected: '2026-10-12'
category: RAG
direction: RAG 记忆检索 · token 级匹配
tags:
- token-level retrieval
- memory retrieval
- frozen embeddings
- sparse token matching
- query adapter
- long-term memory
one_liner: 冻结 embedding 的 token 级稀疏匹配融合整句相似度，无需训练提升记忆检索
practical_value: '- 可复用现有 embedding 模型已经算好的 token hidden states：给商品/内容/会话记忆建 token
  级 HNSW 索引，query token 检索后按 source memory ID 聚合，再与整向量相似度做 query-wise 标准化融合。无需训练 encoder
  或重建文档索引，适合快速在现有召回链路上加一层局部证据信号。

  - 工程实现上，保留 token 到 memory/item 的 ID 映射，聚合时用检索到的最后一个 token 的 clipped similarity 作为缺失分
  floor，能显著减少 HNSW 漏召回的影响；k=64、α=0.5 在多个 backbone 上稳定，可直接作为默认参数。

  - 可选的 LoRA query adapter 只训练 query token states，保持 item/memory 侧索引完全不变，对商品库频繁更新、多租户场景很友好；上线只需替换轻量
  query 头。

  - 存储与延迟权衡：token 索引不压缩会大很多，但 SQ4 可压缩 81–85%，质量几乎不降；大规模商品/内容索引可优先上 SQ4，进一步降本可试 RP128+SQ4，但质量损失更明显。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

Memory-augmented assistant 需要从历史会话/文档中检索证据来回答问题。主流的 single-vector retrieval 只比较 query 与 memory 的整体 embedding，但答案往往只依赖 memory 中的一小段局部信息，不同 query 关注的局部也不同。同一 encoder 其实已经算好了 contextual token representations，只是 single-vector scoring 没有直接利用这些 token 级证据。

**方法关键点**

- 冻结 encoder，每个 memory 存储归一化后的 content-token hidden states，并保留 source memory ID；同时保留原 pooled embedding。
- 每个 query token 在全局 memory token 上做 HNSW top-k 检索，用最后一个检索到的 token 的 clipped similarity 作为缺失分 floor，再按 memory ID 聚合得到 sparse token-matching score。
- 对 sparse score 和 whole-memory pooled score 做 query-wise 标准化，并以 α=0.5 融合，得到 training-free 的最终排序分。
- 可选 LoRA 风格 rank-32 query adapter，只作用于 query token states，用 MaxSim + 多正例交叉熵训练；encoder 和已存 memory index 始终不变。

**关键实验**

在 LoCoMo、LongMemEval、REALTALK、ESG-Reports、QASPER、PeerQA、CovidQA、MLDR 共 8 个 benchmark，以及 Qwen3-Embedding、Llama、EmbeddingGemma、Jina 等 8 个 backbone 上评估。Qwen3-Embedding-4B 上 training-free 融合把平均 Recall@10 从 62.5 提到 73.8，NDCG@10 从 48.0 提到 59.9；query adaptation 进一步到 75.7 / 62.3。LoCoMo Recall@10 从 41.6 提升到 67.8，LongMemEval 从 59.2 提升到 95.9。下游 QA 准确率在多个 backbone 上同步提升。SQ4 压缩可减少 81–85% 存储，质量几乎不变。

**最值得记住的一句话**：冻结 embedding 模型的 token states 本身携带被 single-vector 忽视的局部证据，配合全局稀疏 token 匹配和 query-only adapter，是性价比很高的检索增强路径。
