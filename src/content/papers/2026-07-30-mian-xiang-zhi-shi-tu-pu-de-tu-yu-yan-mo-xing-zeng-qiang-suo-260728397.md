---
title: 'GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation'
title_zh: 面向知识图谱的图语言模型增强检索生成
authors:
- Maya Arseven
- Anette Frank
- Beni Egressy
- Johann Higl
- Moritz Plenz
affiliations:
- Institute of Computational Linguistics, Heidelberg University
- Aleph Alpha Research
arxiv_id: '2607.28397'
url: https://arxiv.org/abs/2607.28397
pdf_url: https://arxiv.org/pdf/2607.28397
published: '2026-07-30'
collected: '2026-08-02'
category: RAG
direction: 图增强检索生成 · 多跳推理
tags:
- GLM
- GNN
- RAG
- Knowledge Graph
- Multi-hop QA
- Graph Retrieval
one_liner: 微调图语言模型检索器在多跳知识图谱RAG中取得跨领域SOTA，泛化性优于GNN和向量检索
practical_value: '- **图增强召回**：在商品知识图谱上构建GLM检索器，将商品、属性、类目作为节点，微调后可直接用于多跳推理类推荐（如“适合露营的防晒帐篷”），提升跨品类泛化。

  - **检索器架构选择**：单跳场景优先用高效向量检索（如双塔）；涉及多关系推理时改用GLM或GNN检索器，并关注图覆盖度与推理深度的权衡。

  - **跨域迁移能力**：若业务需快速扩展到新领域（如从服装到美妆），可利用GLM检索器的语言理解优势做zero/few-shot迁移，减少重新标注成本。

  - **训练效率与覆盖的平衡**：GNN检索器能用更少训练资源达到更高图覆盖率，适合冷启动或图谱频繁更新的场景；GLM检索器在充足数据下随参数量增大性能提升明显，适合主赛道长期投入。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：知识图谱RAG任务中，检索器需要同时理解图结构和语义信息。现有方法多基于GNN或向量搜索，而图语言模型（GLM）融合了图推理与语言模型能力，尚未被系统对比。

**方法**：
- 提出GLM-RAG，用GLM作为知识图谱检索器，输入子图与问题，输出相关事实；
- 与GNN检索器（GFM-RAG）、传统向量检索器全面对比，评估单跳/多跳问答、域内/域外泛化；
- 探索模型规模、子图覆盖率对性能的影响。

**关键结果**：
- 微调GLM检索器在跨领域多跳基准（MuSiQue、2WikiMultihopQA）上达到SOTA，域外泛化显著优于GNN和向量检索；
- 域内多跳性能与已有工作持平，且随参数量增大、子图覆盖提升呈正向 scaling；
- GNN检索器训练效率高、图覆盖率更优；向量检索在单跳任务中表现最好。
