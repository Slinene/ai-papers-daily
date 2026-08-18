---
title: 'Noesis: Bidirectional Graph-RAG with Adaptive Parallelism and Cross-Knowledge-Base
  Semantic Discovery'
title_zh: Noesis：双向图 RAG 与自适应并行及跨知识库语义发现
authors:
- Nicola Cogotti
affiliations:
- Alpha Cogs
arxiv_id: '2608.15919'
url: https://arxiv.org/abs/2608.15919
pdf_url: https://arxiv.org/pdf/2608.15919
published: '2026-08-16'
collected: '2026-08-18'
category: RAG
direction: Graph-RAG 架构 · 多跳推理与跨知识库路由
tags:
- Graph-RAG
- RAG
- MoE quantization
- Multi-hop QA
- Knowledge Graph
- Adaptive Parallelism
one_liner: 提出解耦 Graph-RAG 架构，结合双向图遍历、AIMD 并发控制、MoE 量化与跨 KB 路由，HotpotQA 超 GraphRAG
  +27.8 EM
practical_value: '- 知识图谱构建时参考双向遍历 + 带记忆衰减的 context resolver，可改善电商场景中商品详情、用户评价、售后政策等长文本的跨段落关系抽取，尤其适合“多商品对比”“政策条款与商品页关联”等需要跨
  chunk 因果链的任务。

  - 借鉴 AIMD 并发控制器：将文档 ingestion 或模型服务的并发从固定线程改为类似 TCP 的加性增/乘性减自适应策略，能自动跑满硬件且避免 OOM，适合大促前全量商品知识库刷新。

  - MoE 模型上线采用领域感知选择性量化而非全局量化：对高频/关键专家保持高精度，对冷门专家激进量化，可在 12GB 消费级 GPU 部署大模型，降低电商 RAG
  assistant 或投放助手的推理成本。

  - Mesh 的跨 KB 语义路由可直接迁移：多个业务知识库（商品、活动、广告、客服）不必合并成单一大图；路由层做运行时结构发现与自适应阈值切分，让一个较小模型完成跨域多跳推理，适合构建统一购物助手或广告投放问答系统。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有 Graph-RAG 受限于静态分块导致长文档跨节语义断裂；ingestion 无法自适应扩展；多域部署要么用单一 KB 稀释检索精度，要么依赖手动路由。

**方法**：Noesis 采用解耦 Graph-RAG，包含四个算法模块：
(a) 双向图遍历 + Graph-Feedback Context Resolver，模拟带记忆衰减的人类阅读，能捕获跨章节长程关系；
(b) AIMD 并发控制器，从 TCP 拥塞控制迁移到 RAG pipeline 编排，实现自适应并行；
(c) Moesis，面向 MoE 模型的领域感知选择性量化，可在 12GB 消费级 GPU 上运行；
(d) Mesh，跨 KB 语义路由，具备运行时结构发现与自适应 Natural Break 阈值，支持小模型多跳跨域推理。

**结果**：13.4MB 语料 ingestion 仅 1min6s，对比顺序处理 25min；AIMD 并发控制带来 23× 加速且零 OOM；Moesis 在消费 GPU 上 prompt 处理加速 6.3×；跨 KB 路由延迟 <2ms。HotpotQA 1000 问题上 EM 59.5 / F1 74.7，超过 GraphRAG +27.8 EM，且图构建用 35B 本地模型而非 GPT-4o；193 页文档的长程因果边抽取精度 90%。
