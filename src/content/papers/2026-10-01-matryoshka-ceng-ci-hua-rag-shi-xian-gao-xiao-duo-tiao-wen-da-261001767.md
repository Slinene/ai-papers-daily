---
title: A Matryoshka Hierarchical RAG for Efficient Multi-Hop Question Answering
title_zh: Matryoshka 层次化 RAG 实现高效多跳问答
authors:
- Gianluca Bonifazi
- Christopher Buratti
- Michele Marchetti
- Federica Parlapiano
- Giulia Quaglieri
- Davide Traini
- Domenico Ursino
- Luca Virgili
affiliations:
- Polytechnic University of Marche
- University of Modena and Reggio Emilia
arxiv_id: '2610.01767'
url: https://arxiv.org/abs/2610.01767
pdf_url: https://arxiv.org/pdf/2610.01767
published: '2026-10-01'
collected: '2026-10-02'
category: RAG
direction: 层次化 RAG · Matryoshka 与实体预算
tags:
- Matryoshka Representation Learning
- Hierarchical RAG
- Multi-hop QA
- Entity-aware Retrieval
- Query Drift
- Efficient Retrieval
one_liner: 结合 Matryoshka 嵌套表示与层次聚类 DAG，用实体预算与锚定控制实现高效多跳检索，在三个多跳 QA 基准上取得最佳质量与效率
practical_value: '- **用 Matryoshka embedding 做分层索引替代重型图索引**：电商商品/内容知识库可按类目→子类目→商品构建层次聚类，上层用低维前缀（如
  64/128 维）、底层用全维（768 维），响应时间比 FAISS 全维检索降低约 35-47%，聚类质量不降。无需 LLM 摘要或 KG 构建，离线成本比
  GraphRAG/LightRAG 低几个数量级。

  - **实体预算迭代检索替代 LLM planning**：在商品多跳场景（如“某系列配件的兼容型号”）中，用查询和已检索文档的实体数量控制每轮检索文档数，用实体
  Jaccard 重排候选，避免多次 LLM 调用，同时保持多跳覆盖能力。可迁移到 Agent 的检索工具中，降低 query 成本。

  - **锚定机制防 query drift**：迭代检索时动态提高原始 query 权重 β_t = |R_{t-1}|/K，平衡累积上下文和原问题，防止语义漂移。在
  Agent 多轮检索或 PRF 场景中可直接复用，作为轻量正则。

  - **p-nearest 冗余覆盖容错**：每个节点关联多个父簇（p=2）可缓解贪婪自顶向下无回溯导致的漏检；在类目体系不完美或边界模糊的电商知识库中，保留多条路径能提高召回鲁棒性。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
多跳 QA 的 RAG 系统面临两难：图方法离线需实体链接、关系抽取，层级方法离线需 LLM 递归摘要；在线则依赖 LLM 迭代规划或昂贵 KG 遍历。要同时维持检索质量与计算效率，需要新的索引结构。

**方法关键点**  
- **Matryoshka 对齐的分层索引**：用 nomic-embed-text-v1.5 的 MRL 嵌入，HDBSCAN 构建 5 层 DAG。内部节点按层截断为 64/128/256/512 维质心，叶子保留 768 维全量文档嵌入；每节点可关联 p=2 个最近父簇，提供冗余覆盖。离线只做向量平均和实体抽取（GLiNER），无 LLM 摘要或 KG 构建。  
- **实体预算的迭代检索**：每轮检索文档数由上一轮新出现实体数决定（k_t = min(K-|R_{t-1}|, max(1, |B_{t-1}|))），K=10 总预算；查询与已检索文档拼接成累积查询，逐层自顶向下贪心选择最相似簇。  
- **双信号评分与锚定**：遍历时 S_l = β_t·Sim(q) + (1-β_t)·Sim(q_c)，β_t 从 0 递增到 |R_{t-1}|/K，防止伪相关反馈式 query drift；到叶子层用 R(d)=α·S_L+(1-α)·Jaccard(新实体, 文档实体)，α=0.5 平衡语义与实体一致性。

**关键实验与数字**  
在 HotpotQA、2WikiMultiHopQA、MuSiQue 上与 7 个代表性 baseline 比较。MatRAG 取得全部基准的最高 EM 和 F1；MuSiQue 上 R@2 比 NaiveRAG 高 14.48%，R@5 高 13.37%；响应时间比 NaiveRAG FAISS 全维检索快 47.44%（HotpotQA）、35.82%（2Wiki）、35.14%（MuSiQue）；索引时间比 HippoRAG2 降低 99.6% 以上。消融表明短前缀聚类质量（DB/Silhouette）不差于全维，甚至更优。

**最值得记住的一句话**  
将 MRL 多尺度表示与索引深度对齐，无需 KG 或 LLM 摘要即可获得接近图检索的质量，并用实体信号替代 LLM planning 实现低成本多跳检索。
