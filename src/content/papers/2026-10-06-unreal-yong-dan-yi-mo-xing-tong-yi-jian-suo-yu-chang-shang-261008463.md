---
title: 'UNREAL: Unifying Retrieval and Long-Context with a Single Model'
title_zh: UNREAL：用单一模型统一检索与长上下文证据选择
authors:
- Edan Kinderman
- Elad Hoffer
- Yochai Blau
- Brian Chmiel
- Ron Banner
- Daniel Soudry
- Boris Ginsburg
affiliations:
- NVIDIA
- Technion
arxiv_id: '2610.08463'
url: https://arxiv.org/abs/2610.08463
pdf_url: https://arxiv.org/pdf/2610.08463
published: '2026-10-06'
collected: '2026-10-07'
category: RAG
direction: 模型内证据选择统一检索与长上下文
tags:
- RAG
- Long-context
- Contrastive learning
- Late interaction
- LLM
- Evidence selection
one_liner: 冻结LLM内部表征统一语料检索与长上下文去噪，仅训练<500K参数即超SOTA检索器
practical_value: '- 搜索/推荐 RAG 场景可尝试冻结主模型只训练 retrieval tokens 和 layer-mixing 权重，把 embedding/retriever
  与生成模型统一，省去独立 embedding 大模型和 reranker，降低跨模型不一致与维护成本。

  - 用 LLM 内部中间层 residual stream 做多向量 late-interaction 检索，配合 mean-pool 压缩，可平衡检索效果与索引大小；类似做法可用于商品描述、用户评论、广告素材的
  candidate retrieval。

  - 长上下文用户行为建模中，可以把长期行为序列或搜索日志分块后用内部 evidence selector 去噪，只喂 top-n chunks 给生成器，避免无关历史干扰并降低
  prefill/KV cache 成本；从 32K tokens 起 FLOPs 和 TTFT 优于 full-context。

  - 训练用多正例 InfoNCE + hard negatives 而非简单 in-batch negatives；query 侧加入 BM25 初始上下文和
  soft prompt tokens，保留检索模式，适合冷启动或小样本微调。局限是当前主要基于 Wikipedia QA，跨域迁移需验证，多向量存储成本较高。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现代 LLM 处理稀疏证据有两种范式：长上下文内部隐式选择，易受 distractor 干扰且序列成本高；RAG 外部显式检索，需额外训练、部署并维护 retriever/ranker 多模型。两者本质都是 query-conditioned 证据选择，只是规模不同。此前 INTRA 证明了 encoder-decoder 内部表征可检索，但无法用于主流 decoder-only LLM。UNREAL 要回答：能否用单一冻结 decoder-only LLM 的内部表征统一语料检索与长上下文证据选择。

## 方法关键点
- **chunk 编码**：用冻结 LLM 的中间层 residual-stream token 表示编码每个 chunk，形成多向量表示。
- **query 侧检索状态**：将 BM25 初检上下文、原始 query、R 个可学习 retrieval tokens 拼接；retrieval tokens 放在末尾，利用 causal mask 条件化；从多个 attention 层读出其 residual states，用可学习权重 α 线性融合。
- **相似度计算**：对融合 query 表示与 chunk 表示做 MaxSim late interaction；用 mean-pool 压缩 chunk 到 Lp 组、query 到 G 组，平衡精算与存储。
- **训练**：多正例 InfoNCE + hard negatives，温度 τ；仅更新 retrieval tokens 和 layer-mixing 权重（<500K 参数），backbone 全冻结。
- **生成**：top-n chunks 选中后与 query 拼接，交给同一个 LLM 生成答案。

## 关键实验与结果
- 在 3B token、21M chunk 的 Wiki-2018 全量索引上，4 个 backbone 均超过 BM25、dense retriever、reranker 与 late-interaction 系统。
- HotpotQA complete-evidence recall@10 从 49.1% 提升到 73.2%；2WikiMultiHopQA 从 31.7% 到 60.1%；MuSiQue 从 8.8% 到 14.4%。
- 长上下文：NoLiMa 128K accuracy 从 1.0% 提升到 24.83%；LV-Eval 256K F1 从 49.97% 到 54.66%；HELMET RAG subset 也最优。
- 效率上，UNREAL 从约 32K tokens 起 FLOPs 与 time-to-first-token 优于 full-context，随上下文增长收益扩大。

**最值得记住的一句话**：用一个冻结 decoder-only LLM 的内部表征做多向量 late-interaction 检索，可以同时处理长上下文去噪和全量语料检索，且只需训练不到 50 万参数。
