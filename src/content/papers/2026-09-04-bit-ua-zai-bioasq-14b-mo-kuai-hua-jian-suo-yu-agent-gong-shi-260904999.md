---
title: 'BIT.UA at BioASQ 14B: Modular Retrieval with pg_textsearch and Qdrant, and
  Agent-Based Answer Generation'
title_zh: BIT.UA 在 BioASQ 14B：模块化检索与 Agent 共识答案生成
authors:
- André Ribeiro
- Rúben Garrido
- Alexander Christiansen
- Richard A. A. Jonker
- Sérgio Matos
affiliations:
- IEETA/DETI, LASI, University of Aveiro, Aveiro, Portugal
- IT, University of Aveiro, Aveiro, Portugal
- Aalborg University Business School, Aalborg, Denmark
arxiv_id: '2609.04999'
url: https://arxiv.org/abs/2609.04999
pdf_url: https://arxiv.org/pdf/2609.04999
published: '2026-09-04'
collected: '2026-09-08'
category: Agent
direction: 多Agent共识生成 · 模块化RAG检索
tags:
- Agent Quorum
- HyDE
- Dense Retrieval
- BM25
- LLM-as-a-Judge
- RAG
one_liner: 将 PostgreSQL BM25、Qdrant 稠密检索与多 Agent 辩论共识机制引入生物医学问答，取得竞争性 MAP 排名
practical_value: '- **混合检索架构模块化拆分**：BM25 倒排用 PostgreSQL pg_textsearch，稠密向量单独用 Qdrant
  GPU 索引，各自独立扩展与调优；电商搜索/推荐可以借鉴这种拆分，避免绑定单一检索引擎，降低替换成本。

  - **HyDE 做 query 扩展**：用 LLM 生成假设性文档再检索，缓解 query 与文档词汇不匹配问题；在电商搜索 query 改写或长尾词召回中，可尝试
  HyDE 生成伪商品描述，提升稀疏召回覆盖。

  - **Reranker 训练负采样用 dense retrieval 挖掘难负例**：比随机负样本更能提升排序模型判别力；推荐精排阶段的负样本采样可以参照，用当前召回模型检索难负例。

  - **多 Agent 共识生成机制**：多个不同 prompt 的 agent 辩论并迭代收敛，配合 adaptive document retention
  保留相关文档，可迁移到商品推荐理由生成、搜索结果摘要或客服问答，提升生成一致性与事实性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：生物医学文献快速增长，研究者需要高效检索相关文档并生成有证据支撑的答案。BioASQ Task B 为此提供严格评测，团队在 14 届重构系统，重点改善检索效率与答案生成的可靠性。

**方法关键点**：
- Phase A 检索：用 PostgreSQL pg_textsearch 替代 PyTerrier PISA 做 BM25 检索，Qdrant 负责稠密嵌入索引与 GPU 加速相似度搜索；探索 HyDE 查询扩展与 Context-1 检索策略；新增 reranker 训练流水线，用 dense retrieval 挖掘难负例。
- Phase A+/B 答案生成：引入 LLM-as-a-judge 框架与多 Agent quorum 机制，多个不同 prompt 的 Agent 辩论、迭代收敛至共识答案，并自适应保留相关文档；首次参与 snippets 生成子任务。

**关键结果**：所有批次取得竞争性成绩，Phase A 系统在 Batch 1 和 Batch 3 的 MAP 排名均为第 5；代码完全开源。

**未来方向**：计划集成 SPLADE 与 ColBERT 进一步强化检索。
