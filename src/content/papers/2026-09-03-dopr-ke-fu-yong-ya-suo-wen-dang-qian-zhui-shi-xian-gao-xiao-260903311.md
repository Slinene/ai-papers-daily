---
title: 'DoPR: Reusable Compressed Document Prefixes for Efficient LLM Reranking'
title_zh: DoPR：可复用压缩文档前缀实现高效 LLM 重排序
authors:
- Beiya Dai
- Yifan Wei
- Guang Yang
- Xing Shi
- Xinbing Wang
- Zhouhan Lin
affiliations:
- 上海交通大学 LUMIA Lab
- 字节跳动
- 上海交通大学
arxiv_id: '2609.03311'
url: https://arxiv.org/abs/2609.03311
pdf_url: https://arxiv.org/pdf/2609.03311
published: '2026-09-03'
collected: '2026-09-04'
category: RecSys
direction: LLM 重排序 · 文档前缀复用
tags:
- LLM reranking
- prefix caching
- pointwise reranking
- document compression
- Qwen3
- efficiency
one_liner: 离线压缩文档为可复用前缀状态，在线仅编码 query 与打分 token，保留 97%+ 排序效果并提速最多 8 倍
practical_value: '- 在电商搜索/推荐精排或广告 rerank 环节，将商品详情、广告创意、用户评价等长文档的 LLM 编码结果离线压缩成 prefix
  KV cache，在线只算 query+score token，固定 8x 压缩比可保留 97%+ NDCG@10，适合文档重复召回的稳定商品库或内容库。

  - 用 self-attention 列向注意力集中度作为 salience 信号选择 top-K 文档 token，无需额外参数，可作为 item 文本压缩或生成式推荐中
  item 侧表示选择的轻量方案；部署时 inference prefix 长度可与训练长度解耦，动态权衡成本与效果。

  - 训练时用 structured attention mask 强制 query 只能通过选中的 item 表示获取信息，并先做 200 步无压缩 warmup
  再激活瓶颈，能稳定收敛；这一 trick 可迁移到需要构造 query-dependent 瓶颈的检索/推荐模型训练。

  - 注意该方法收益依赖文档重复使用率：对新闻、实时竞价创意等快速更新 corpus 摊销有限，更适合静态商品库、内容库的离线索引+在线加速。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

Pointwise LLM reranking 效果好，但同一文档被不同 query 重复编码，文档侧计算冗余严重，成为实时系统延迟瓶颈。已有压缩方法主要降低单次推理成本，或预计算表示用于检索/交互，未在 LLM reranker 内部复用文档侧计算。

## 方法关键点

- **训练阶段**：利用文档最后一层 self-attention 矩阵的列向注意力集中度作为 salience 信号，无需额外参数选出 top-K（默认 Ktrain=32）文档 token 状态作为压缩文档表示 Cd。
- **结构化注意力掩码**：训练输入为 [d; Cd; q; t_score]，query 和 score token 只能通过 Cd 访问文档信息，强制 Cd 成为唯一文档信息通道。
- **离线压缩**：对每个文档选出 Kinfer 个 salient positions 作为 prefix inputs，前向得到多层 KV states 并存储；该 prefix 与 query 无关，可跨查询复用。
- **在线重排序**：注入存储的 prefix states，模型只处理 query 和 score token，文档侧预算从 n 降为 Kinfer（默认 8x 压缩）。
- **训练目标**：RankNet pairwise loss + MLP score head，端到端优化表示选择与排序。

## 关键实验

- 数据集：TREC DL19/20、BEIR 8 个子集、BRIGHT 12 个子集。
- 对比 matched Qwen3-Rerank 0.6B/4B/8B 以及 MonoBERT、MonoT5、RankT5、RankLLaMA、RankZephyr、E2Rank 等。
- 结果：TREC DL/BEIR 平均 NDCG@10 retention 97.1% / 99.3% / 99.5%；BRIGHT retention 98.6% / 99.1% / 98.8%；DL19 speedup 1.21–1.84x，Covid（长文档）2.85–8.04x；固定 8x 压缩，文档侧 memory 降 8x。
- 消融：attention-guided Top-K 优于 First-K/Uniform-K/Random-K 及 Raw Last-K；200 步无压缩 warmup 最佳；在 Llama-3.2-1B 上 retention 97.48%，说明架构无关。

最值得记住的一句话：文档侧的 LLM 计算可以离线变成可复用前缀状态，在线只编码 query 和打分 token，在几乎不损失排序质量的前提下，将长文档重排序延迟降低数倍——适合文档重复召回的稳定场景。
