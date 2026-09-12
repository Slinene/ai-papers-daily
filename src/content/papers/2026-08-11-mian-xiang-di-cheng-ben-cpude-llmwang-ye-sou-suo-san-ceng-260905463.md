---
title: A Three-Layer Caching Architecture for Low-Latency LLM Web Search on Commodity
  CPU Hardware
title_zh: 面向低成本CPU的LLM网页搜索三层缓存架构
authors:
- Ayushman Bhattacharya
- Nihal Gazi
affiliations:
- pollinations.ai
arxiv_id: '2609.05463'
url: https://arxiv.org/abs/2609.05463
pdf_url: https://arxiv.org/pdf/2609.05463
published: '2026-08-11'
collected: '2026-09-12'
category: LLM
direction: LLM搜索缓存与推理降本
tags:
- LLM caching
- semantic query cache
- session management
- Redis
- embedding dedup
- web search
one_liner: 用三层缓存复用会话上下文、语义查询与URL嵌入，在单台CPU服务器上实现89.3%命中
practical_value: '- 语义查询缓存对电商Agent很有用：把用户query做embedding后按cosine相似度去重，能拦截大量换说法但同意图的重复请求，直接省掉远程LLM调用成本；阈值需要根据业务容忍度调，电商场景建议搭配query分类或意图识别做二次校验。

  - 会话上下文窗口采用Redis热数据+磁盘Huffman压缩冷数据的两级存储，适合商品导购、客服Agent等长会话场景；LRU后台迁移能保持内存占用低（仅1.38MB），同时支持小时/天级恢复会话。

  - URL/item embedding缓存可迁移到推荐系统的向量召回：对同一item的图片/描述向量跨会话复用，避免重复embedding计算；在商品库变更不频繁时收益明显。

  - 工程实现上证明了单8-vCPU+32GB RAM即可支撑30个worker的低延迟服务，对预算有限的团队是可直接复制的架构基线。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：AI搜索产品（ChatGPT search、Perplexity等）API按次收费且需注入大量网页上下文，成本高；同时自建系统在用户增长后出现会话上下文丢失、等价查询重复触发LLM、URL被跨会话重复embedding等问题。

**方法关键点**：
- 会话上下文窗口：Redis中维护滚动消息窗口，溢出时自动压缩为Huffman编码的磁盘归档，LRU守护进程负责闲置会话迁移与按需恢复。
- 语义查询缓存：对查询embedding做cosine相似度匹配，识别改写后的重复意图，消除冗余LLM调用。
- URL嵌入缓存：跨会话去重URL embedding计算。

**关键结果数字**：部署在单台8-vCPU Intel Cascade Lake服务器（32GB RAM，30个Hypercorn worker，三副本），聚合Redis keyspace命中率89.3%，读取延迟0.1ms，内存开销仅1.38MB。
