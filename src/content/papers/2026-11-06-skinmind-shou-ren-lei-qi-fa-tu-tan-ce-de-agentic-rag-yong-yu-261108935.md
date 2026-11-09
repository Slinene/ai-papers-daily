---
title: 'SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable
  Dermatology AI'
title_zh: SkinMind：受人类启发图探测的 Agentic RAG 用于皮肤科 AI
authors:
- Jing Hao
- Weinan Zhou
- Zhihong Lu
- Yaling Shen
- Yiming Xu
- Yefeng Liu
- Siyuan Yan
- Shuaibo Li
- Ming Dai
- Junjun He
affiliations:
- Ant Group
- The University of Hong Kong
- Monash University
- University of Science and Technology of China
- Southeast University
arxiv_id: '2611.08935'
url: https://arxiv.org/abs/2611.08935
pdf_url: https://arxiv.org/pdf/2611.08935
published: '2026-11-06'
collected: '2026-11-09'
category: RAG
direction: Agentic RAG · 图探测检索
tags:
- Agentic RAG
- Knowledge Graph
- Multimodal Reasoning
- Graph Probing
- Dermatology AI
- Evidence Retrieval
one_liner: 提出 SkinMind 多模态 Agentic RAG，通过分层图探测工具在皮肤病知识图谱上自主探索证据，提升 VQA 性能与可靠性
practical_value: '- 借鉴层级图探测工具的“渐进式披露”设计：在电商推荐/问答中，将检索拆为实体识别、属性查询、关系游走、多模态证据收集等子步骤，让
  LLM 自主决定下一步探索方向与粒度，避免一次性召回过粗或过细。

  - 构建 query-specific 证据子图：在商品/用户知识图谱中，可让 Agent 围绕当前会话动态构建关联子图（用户-商品-属性-评论-图片），用于生成可解释推荐理由或辅助排序，提升透明度。

  - 多模态统一存储与检索：将文本、关系、图像等证据统一入图，支持跨模态证据融合；电商中可整合商品标题、属性、用户评论图片、视频帧等，用于回答复杂商品咨询。

  - 冲突解决机制（专家 schema + 冲突消解）可迁移到多源商品知识合并，如处理不同商家属性冲突、价格矛盾、用户评论矛盾，保证知识图谱质量，提升下游任务稳定性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：可靠皮肤科AI需要获取分布在异构文本和视觉来源中的可验证证据，但传统RAG一次性从平面语料检索，无法调整检索粒度、探索多跳关系、融合多模态临床证据。

**方法**：构建 SkinMind-KG 知识图谱（1.0M+ 节点、2.0M+ 边），从 62M token 皮肤科指南/教科书和 423K 图像中构建，由皮肤科专家指导 schema 和冲突消解机制统一文本、关系、视觉证据。SkinMind 采用多模态 agentic RAG 框架，将检索组织为 orchestrator 与图环境之间的迭代交互：通过 8 个分层图探测工具，逐步识别相关实体、检查节点级信息、遍历关系和路径、检索源文本和视觉证据。该渐进式披露设计使模型自适应确定检索模态、探索方向和证据粒度，并构建 query-specific 证据子图。

**结果**：在 6 个皮肤病 VQA 基准和两个策略模型设置上，SkinMind 的平均分数比直接回答分别提高 8.70（GPT-5.4-mini）和 8.89（Gemini-2.5-Flash）分，并一致优于其他 RAG 方法。
