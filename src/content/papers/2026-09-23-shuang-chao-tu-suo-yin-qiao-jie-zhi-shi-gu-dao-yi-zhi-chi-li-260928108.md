---
title: 'Dual-Hypergraph Indexing: Bridging Knowledge Islands for Multi-Hop Reasoning
  in Retrieval-Augmented Generation'
title_zh: 双超图索引：桥接知识孤岛以支持 RAG 多跳推理
authors:
- Qi Sun
- Xingliang Hou
- Caibo Li
- Yijia Zhang
- Qiang Li
- Yu Guo
affiliations:
- School of Software Engineering, Xi'an Jiaotong University
- State Key Laboratory of Human-Machine Hybrid Augmented Intelligence, and Institute
  of Artificial Intelligence and Robotics, Xi'an Jiaotong University
- EHV Power Transmission Company of China Southern Power Grid Co., Ltd
arxiv_id: '2609.28108'
url: https://arxiv.org/abs/2609.28108
pdf_url: https://arxiv.org/pdf/2609.28108
published: '2026-09-23'
collected: '2026-09-27'
category: RAG
direction: RAG 索引 · 超图聚合
tags:
- Dual-Hypergraph
- RAG
- Multi-hop Reasoning
- Knowledge Aggregation
- Temporal Aggregation
one_liner: 提出 Dual-Hypergraph Indexing，以双层超图与双路径聚合提升多跳 RAG 的逻辑连贯性与推理能力
practical_value: '- 在商品/内容知识库 RAG 中，可显式分离实体-关系事实层（商品属性、品牌、活动事实）与深层洞察层（增长归因、趋势结论），避免单条事实孤岛导致多跳推理断裂。

  - 用 5 维拓扑指标 + adaptive thresholding 做 hub 聚合，可迁移到用户-商品异构图或类目树，自动发现核心类目/品牌/场景簇，提升召回与解释性。

  - 对于时效敏感场景（大促、热销榜、活动节奏），采用滑动窗口 + greedy exploration 聚合时间链，让索引保留时序演变，防止旧事实污染新推理。

  - 评估多跳 RAG 时，除了单条证据命中，应增加逻辑连贯性、因果链完整性等指标，可设计跨 session/行为链的业务 QA 集。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有 hypergraph-based RAG 虽能捕获多实体高阶关系，但将超边视为孤立事实断言，形成结构碎片化与“知识孤岛”，阻碍多跳因果推理、时序追踪与叙事合成。

**方法关键点**：DHI 引入分层表示，底层为实体-关系事实超图 H_K，上层为深度洞察超图 H_D，通过双路径聚合连接两层。路径一采用 importance-driven hub aggregation，基于 5 种拓扑指标 profiling 与自适应阈值，聚合空间语义簇；路径二采用 temporal chunk-chain progressive aggregation，通过滑动窗口 greedy exploration 追踪时间演化。整个过程将离散事实提升为可分析的深层洞察。

**关键结果数字**：在 5 个 benchmark 上达到 SOTA；多学科 Mix benchmark 上逻辑连贯性 +1.53；复杂医学病理推理任务得分 85.78%。
