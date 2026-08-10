---
title: Exact Adaptive Hybrid Retrieval Without Fixed Top-L Cutoffs
title_zh: 无需固定截断深度的精确自适应混合检索
authors:
- Chunran Zhang
affiliations:
- Southwest Jiaotong University
arxiv_id: '2608.07152'
url: https://arxiv.org/abs/2608.07152
pdf_url: https://arxiv.org/pdf/2608.07152
published: '2026-08-07'
collected: '2026-08-10'
category: RAG
direction: 自适应混合检索 · 精确Top-K无截断
tags:
- Hybrid Retrieval
- Adaptive Fusion
- Exact Top-K
- RAG
- Efficiency
- Vector Quantization
one_liner: 提出可按需继续的精确稠密-稀疏融合方法，保证完全列表Top-K一致且避免固定截断，平均加速23-30倍
practical_value: "- **多路召回免截断融合**：电商/推荐场景中，embedding 召回与倒排召回融合时，可借鉴 EAHR 的按需增量获取机制，不再硬性固定每条通道的截断数，避免截断过小丢失关键文档或过大引入冗余计算。\
  \  \n- **可恢复的精确排序**：使用 PVS 量化向量索引 + PBM 块最大索引，支持随时恢复并继续拉取下一个未读高分项，工程上可设计成流式/游标式接口，方便在多路融合中按需拉取。\
  \  \n- **边界裁剪节省算力**：计算未读候选的融合分数上界，仅当上界可能挤入当前 Top-K 时才继续请求，多数 easy query 可提前终止，大幅降低平均延迟（实测加速\
  \ 23-30 倍），同时保证融合结果与完整列表完全一致。  \n- **无需依赖历史查询调参**：实验证明固定深度无法从历史查询可靠迁移，EAHR 的自适应策略省去了繁重的离线参数调优，更适合动态语料与长尾查询。"
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统 RAG 系统混合检索常为稠密和稀疏通道各自截取固定 Top-L 结果再融合，但截断后的融合可能不等于完整列表融合，即使已观察到的候选已包含完整 Top-K，未读的跨列表排名仍可能改变 Top-K 组成与顺序。固定深度依赖历史查询统计，在分布变化时不可靠。  

**方法**：EAHR 将完整列表加权 RRF 产生的有序 Top-K 作为精确检索目标，将通道深度视为请求级执行状态。利用 Per‑Vector Scalar Quantization (PVS) 和 Posting Block‑Max (PBM) 构建可恢复的稠密与稀疏精确排序，能随时按需继续拉取下一个未读项。融合时计算各通道未读贡献的融合分数上界，仅当上界仍可改变当前 Top-K 时才向该通道请求下一批结果，否则终止。  

**结果**：在 5 个测试集合 ×5 个语料快照的全部 150 个查询-快照组合上，EAHR 均能重现完整列表融合的有序 Top-20。完整列表加权 RRF 效果稳定，而固定深度无法跨查询可靠迁移。在 TREC-DL 2019/2020 上，相比穷举批处理执行，配对几何平均加速比分别为 23.35 和 30.28。但反相关排名会触发全部列表穷举，困难查询可能更慢。方法不保证每次加速，但保证结果精确性并自适应执行深度。
