---
title: 'Asymmetric Dynamic Routing: Balancing Reasoning Depth and Computational Efficiency
  in Hypergraph RAG'
title_zh: 非对称动态路由：平衡超图RAG中的推理深度与计算效率
authors:
- Qi Sun
- Yijia Zhang
- Xingliang Hou
- Caibo Li
- Qiang Li
- Yu Guo
affiliations:
- School of Software Engineering, Xi’an Jiaotong University
- State Key Laboratory of Human-Machine Hybrid Augmented Intelligence, Institute of
  Artificial Intelligence and Robotics, Xi’an Jiaotong University
- EHV Power Transmission Company of China Southern Power Grid Co., Ltd
arxiv_id: '2609.29282'
url: https://arxiv.org/abs/2609.29282
pdf_url: https://arxiv.org/pdf/2609.29282
published: '2026-09-24'
collected: '2026-09-27'
category: RAG
direction: 查询自适应超图RAG路由
tags:
- RAG
- Hypergraph
- Dynamic Routing
- Efficiency
- GraphRAG
- Query Classification
one_liner: 提出意图条件路由框架ADR，用轻量分类器动态调度三种非对称拓扑遍历算子，减少48.7% token和45.3%延迟
practical_value: '- 在电商知识问答/导购Agent中，对用户query做轻量意图分类：事实型查询（如“某商品材质”）走局部事实锚定，减少全图遍历；对比/推荐理由类查询走自底向上邻接扩散，获取关联实体；策略/选品建议类查询走自顶向下洞察接地，引入高层抽象知识。

  - 可复用“非对称遍历算子”设计：不同意图对应不同图计算代价，避免静态RAG对所有查询执行同等深度检索，显著降低prompt token和端到端延迟，适合高并发在线推荐场景。

  - 若已有商品知识图谱或用户-商品异构图，可参考ADR的层次路由思路：在召回/排序前置一个轻量分类器，动态决定图扩散深度与方向，平衡效果与算力，尤其利于边缘部署或成本敏感业务。

  - 结果表明动态路由能在保持推理质量前提下节省近50% token，对依赖LLM做导购解释、推荐理由生成的业务，可降低API成本并提升响应速度。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：图/超图RAG虽然能缓解LLM幻觉，但现有系统对任意query采用静态遍历策略，忽视查询复杂度，导致简单查询计算冗余、复杂查询上下文不足——“静态检索谬误”。

**方法关键点**：提出Asymmetric Dynamic Routing (ADR)，在层次知识图谱上做意图条件检索。用轻量结构化分类器将查询动态分派到三种非对称拓扑遍历算子：
- 局部事实锚定：处理简单事实型查询，只锚定局部节点；
- 自底向上邻接扩散：从具体实体向上层抽象扩散，获取关联信息；
- 自顶向下洞察接地：从高层概念向下游实体传递洞察，支持复杂推理。
三个算子构成双向信息流，覆盖不同复杂度需求。

**关键结果**：在五个领域语料上，ADR保持强推理性能的同时，prompt token消耗最高降低48.7%，端到端查询延迟降低45.3%，实现质量-效率的有利平衡。
