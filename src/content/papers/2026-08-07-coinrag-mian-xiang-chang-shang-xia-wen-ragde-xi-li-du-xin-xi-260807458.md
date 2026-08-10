---
title: 'CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context
  RAG'
title_zh: CoinRAG：面向长上下文RAG的细粒度信息块KV缓存复用
authors:
- Gyuwan Kim
- Cheoneum Park
- Tao Yang
affiliations:
- University of California, Santa Barbara
- Hanbat National University
arxiv_id: '2608.07458'
url: https://arxiv.org/abs/2608.07458
pdf_url: https://arxiv.org/pdf/2608.07458
published: '2026-08-07'
collected: '2026-08-10'
category: RAG
direction: KV缓存复用 · 细粒度信息块 · 低延迟RAG
tags:
- KV cache reuse
- nugget extraction
- long-context RAG
- multi-hop QA
- latency-efficiency
- position alignment
one_liner: 通过离线提取细粒度信息块并复用其上下文KV缓存，在低延迟预算下显著提升多跳问答准确率
practical_value: '- 细粒度信息块离线提取与缓存复用：在电商/内容推荐中，可对商品描述或文档预先提取关键事实块并缓存KV，在线仅加载所需片段，大幅降低预填充延迟，适配严格的SLA。

  - 两阶段检索缩小候选范围：先粗粒块召回，再在块内针对查询做细粒度块排序，可迁移到多路召回或Rerank场景，减少噪声同时提升效率。

  - 位置对齐实现非连续缓存拼接：利用RoPE旋转偏移对齐来自不同块的缓存片段，保持紧凑的连续位置编码，减少内存占用并加速解码，适用于动态组合多种证据的生成式推荐或广告文案生成。

  - 块感知微调（nugget‑aware fine‑tuning）：在训练中直接注入拼接的非连续缓存结构，能大幅缩小训练‑推理偏差，类似方法可用于在业务中微调模型以接受结构化的检索增强输入，如structured
  prompt+商品属性片段。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现代RAG系统面临严格的交互延迟要求（如P99≤100ms），标准RAG因在线编码长上下文的预填充延迟过高，只能缩减检索量，牺牲准确率。现有块级KV缓存复用虽加速推理，但粗粒度块仍携带大量噪声与冗余。为在低延迟预算下最大化答案质量，本文提出CoinRAG，用离线提取的细粒度信息块（nugget）替代完整块，并复用其上下文KV缓存，实现高信息密度、低延迟的长上下文RAG。

**方法关键点**  
- **离线信息块提取**：用LLM从每个文本块中抽取关键事实片段，通过精确匹配或模糊匹配定位到块内的token span，保留其上下文KV缓存切片，避免孤立编码损失语篇信息。  
- **两阶段在线检索**：先以稠密检索取top-kc个块，再在块内候选块中按与查询的相似度排序取top-k个块，缩小搜索空间，提升检索精度。  
- **上下文KV缓存组合与位置对齐**：将选中块的KV缓存切片与系统前缀缓存拼接，利用RoPE位置旋转将各片段的绝对位置平移成连续序列，形成紧凑的prefix cache，同时保持原块内的上下文依赖，大幅降低GPU内存占用。  
- **块感知微调**：在训练时动态构造与推理一致的非连续缓存拼接方案，微调语言模型以消除位置嵌入偏移造成的训练‑推理结构差异。

**关键实验**  
在LongBench多跳问答（HotpotQA、2WikiMQA、MuSiQue）上，与Standard RAG、CacheBlend、TurboRAG、KVLink对比。  
- 在P99 TTFT ≤100ms的预算下，CoinRAG平均F1达到41.7，比最强基线TurboRAG（39.6）高5.3%，且平均预填充长度仅为TurboRAG的0.54倍。  
- 取消延迟限制后，平均F1仍领先5.2%（42.7 vs 40.6），上下文长度短6.8倍。  
- 消融实验：上下文KV切片比独立编码峰值F1高3.9‑6.3点；两阶段检索比单阶段高9.6‑17.5%；位置对齐在75ms预算下带来3‑8.5%的提升；块感知微调贡献6.3‑11.3点提升。  

**一句话精华**  
“CoinRAG用离线切块取精、在线拼片对齐的方式，在100ms内用更短的上下文跑出更强的多跳QA，证明了‘少而精’的缓存复用能同时赢得延迟与准确率。”
