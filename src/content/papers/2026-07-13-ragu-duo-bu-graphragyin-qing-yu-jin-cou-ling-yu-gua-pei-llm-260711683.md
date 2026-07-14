---
title: 'RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM'
title_zh: RAGU：多步GraphRAG引擎与紧凑领域适配LLM
authors:
- Mikhail Komarov
- Ivan Bondarenko
- Stanislav Shtuka
- Oleg Sedukhin
- Roman Shuvalov
- Yana Dementyeva
- Matvey Solovyov
- Nikolay O. Nikitin
affiliations:
- ITMO University
- Novosibirsk State University
- Far Eastern Federal University
arxiv_id: '2607.11683'
url: https://arxiv.org/abs/2607.11683
pdf_url: https://arxiv.org/pdf/2607.11683
published: '2026-07-13'
collected: '2026-07-14'
category: RAG
direction: GraphRAG引擎优化 · 轻量模型
tags:
- GraphRAG
- Knowledge Graph Construction
- LLM Compression
- Multi-hop Retrieval
- Deduplication
- Community Detection
one_liner: 将知识图谱构建拆分为抽取与整合两步，用7B语言模型超越32B模型，实现更完整的证据检索
practical_value: '- **知识图谱构建流水线可复用**：两阶段有类型实体抽取 + DBSCAN 去重 + LLM 摘要 + Leiden 社区发现，适合电商商品库、搜索日志构建结构化知识图谱。

  - **业务专属轻量模型思路**：任务所需的语言技能（理解、抽取、推理）随参数增长有限，可针对性地训练 7B 模型替代大模型，降低成本与延迟，适用于线上抽取 pipeline。

  - **多跳检索的完整性验证**：GraphRAG 在医学领域取得证据召回 0.84，可迁移至电商多条件筛选或推荐解释场景，确保检索覆盖所有相关事实片段。

  - **工程化参考**：开源、pip 安装、单 GPU 运行，易于集成到现有 RAG 系统中，可直接作为商品问答、内容推荐的 GraphRAG 基座测试效果。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**

现有 GraphRAG 系统一次性地用 LLM 从文档中抽取实体和关系，知识图谱噪声大、实体重复，损害检索鲁棒性。

**方法关键点**

RAGU 将图谱构建分成抽取与整合两个阶段：
1. 两阶段有类型实体抽取——先识别实体粗类型，再细粒度抽取；
2. DBSCAN 向量聚类去重；
3. LLM 摘要合并重复实体描述；
4. Leiden 算法检测社区，用于检索时图遍历。

作者发现图谱构建所需的语言技能（理解、抽取、上下文推理）随模型规模增长微弱，于是训练了 7B 规模、领域适配的 Meno-Lite-0.1 模型，专门强化这些语言能力。

**关键结果**

- 在知识图谱构建任务上，Meno-Lite-0.1 的调和平均值比 Qwen2.5-32B 高 12.5%（相对提升）。
- 在 GraphRAG-Bench（医学）上，RAGU 在每个事实层级都取得最高证据召回率（最高 0.84，对比其他方法 ≤0.76），并在综合任务上超越 HippoRAG2。
- 整套系统可单 GPU 运行，pip 安装，MIT 开源。
