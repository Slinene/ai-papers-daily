---
title: A Tree-based RAG Framework for Evidence-Intensive QA via Adaptive Planning
  and Topology-Aware Evidence Gathering
title_zh: 基于树结构的 RAG 框架：自适应规划与拓扑感知证据收集用于证据密集型 QA
authors:
- Songeun Lee
- Kyungjin Min
- Injae Na
- Suyeong Lee
- Chiyoung Kim
- Woohwan Jung
affiliations:
- Korea University
- Hanyang University
- Hyundai Motor Company
arxiv_id: '2609.04981'
url: https://arxiv.org/abs/2609.04981
pdf_url: https://arxiv.org/pdf/2609.04981
published: '2026-09-04'
collected: '2026-09-08'
category: RAG
direction: RAG 结构化推理 · 自适应证据收集
tags:
- RAG
- Tree-based Reasoning
- Evidence-Intensive QA
- Adaptive Planning
- Topology-Aware Evidence Gathering
- Multi-hop QA
one_liner: 提出 APT-RAG，通过自适应规划扩展推理树和拓扑感知证据收集，提升证据密集型问答性能。
practical_value: '- 在复杂查询或商品长尾问答场景中，用树结构动态分解任务并自适应扩展节点，比固定多步流水线更能应对证据分散的需求，可借鉴其节点扩展策略。

  - 利用推理树拓扑关系（兄弟节点证据共享、子节点证据聚合）减少重复检索、提升证据覆盖，适用于多文档、跨类目信息整合的推荐解释或客服问答。

  - 证据引导的批量答案生成（evidence-guided batched answer generation）可以降低 LLM 推理次数与成本，在高并发搜索或推荐场景中可尝试将多个子问题合并生成。

  - 该框架强调证据需求驱动规划，可作为电商 Agent 在商品对比、规则解释等需要多跳信息收集时的设计参考。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
结构化 RAG（如树/图推理）在证据密集型 QA 中面临两个主要问题：结构僵化，无法根据证据需求动态扩展推理路径；拓扑忽视，证据收集时未利用推理树节点间的关系，导致证据覆盖不足，难以有效综合数十甚至数百篇文档的信息。

**方法关键点**  
提出 APT-RAG：
- 自适应规划：根据问题依赖和证据需求动态扩展推理结构，而非固定节点数。
- 拓扑感知证据收集：利用兄弟节点证据重用、直接检索和子节点证据聚合三种机制提升证据覆盖。
- 证据引导的批量答案生成：将多个子问题的证据合并后批量生成答案，减少 LLM 调用次数和生成开销。

**关键结果**  
在证据密集型 QA 基准（如需要跨多文档综合的问题集）上，APT-RAG 优于现有结构化 RAG 方法，具体指标见论文实验部分，核心优势体现在证据覆盖率和答案生成效率的平衡上。
