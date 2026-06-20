---
title: 'MonaVec: A Training-Free Embedded Vector Search Kernel for Edge and Offline
  AI Systems'
title_zh: MonaVec：面向边缘与离线AI的训练无关嵌入式向量搜索内核
authors:
- Oğuzhan Yenen
arxiv_id: '2606.19458'
url: https://arxiv.org/abs/2606.19458
pdf_url: https://arxiv.org/pdf/2606.19458
published: '2026-06-17'
collected: '2026-06-20'
category: RAG
direction: 嵌入式向量搜索 · 确定性量化
tags:
- embedded vector search
- training-free quantization
- Randomized Hadamard Transform
- edge AI
- determinism
- recall
one_liner: 训练无关、确定性的嵌入式向量搜索内核，4位量化达高召回，如SQLite般随处运行
practical_value: '- 无需训练的量化技巧：采用随机Hadamard变换将任意embedding分布转为近高斯，配合预计算Lloyd-Max表做4位量化，无码本、无训练数据，可直接用于电商推荐系统的物品/用户embedding压缩，节省存储与传输。

  - 单文件持久化与确定性：索引存为单个.mvec文件，内嵌ChaCha20种子保证跨架构字节一致性，对离线Agent或移动端推荐场景的结果可复现、调试友好。

  - 轻量易集成：纯Rust实现，Python绑定，API极简（类似SQLite），适合嵌入到边缘端推荐或检索模块，无须依赖重型服务端向量数据库。

  - 多种后端兼容：提供BruteForce、IVF、HNSW，覆盖从小规模高精度到百万级语料库的检索需求，可直接替换现有方案中FAISS等组件，降低服务器依赖。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有向量搜索系统需服务器、大内存或训练数据，无法满足边缘/离线AI场景下的嵌入式检索需求。

**方法**：MonaVec 借鉴 SQLite 设计哲学——“一个文件，一次调用，随处运行”。核心量化采用训练无关的随机Hadamard变换（RHDH），将任意输入分布调整为近似标准正态分布，再利用预计算的Lloyd-Max表直接4位量化，无需学习码本，体积缩小8倍。索引保存为单个 `.mvec` 文件，内置ChaCha20种子保证在不同架构上字节级一致的可复现结果。支持余弦距离，通过单次全局标准化同样适配L2距离。提供BruteForce、IVF、HNSW三种后端，满足不同规模需求。实现为纯Rust库，带Python绑定，CPU运行时自动调度AVX-512/AVX2/NEON指令。

**结果**：在AG News 45K×1024维BGE-M3语义嵌入上，4位量化暴力搜索仅占27 MB便取得0.960 Recall@10，超越float32 FAISS-IVF和8位usearch，同时保证了确定性。
