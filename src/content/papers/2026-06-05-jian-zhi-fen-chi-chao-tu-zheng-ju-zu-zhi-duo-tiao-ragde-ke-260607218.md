---
title: 'HKVM-RAG: Key-Value-Separated Hypergraph Evidence Organization for Multi-Hop
  RAG'
title_zh: 键值分离超图证据组织：多跳RAG的可复用控制机制
authors:
- Mingyu Zhang
- Ying Ma
affiliations:
- Faculty of Computing, Harbin Institute of Technology
arxiv_id: '2606.07218'
url: https://arxiv.org/abs/2606.07218
pdf_url: https://arxiv.org/pdf/2606.07218
published: '2026-06-05'
collected: '2026-06-08'
category: RAG
direction: 多跳RAG证据组织
tags:
- Multi-hop RAG
- Hypergraph
- Key-value retrieval
- Evidence indexing
- ColBERTv2
one_liner: 提出HKVM-RAG，用超图键值分离组织多跳证据链，作为独立于密集检索的证据控制信号，在三个多跳QA基准上显著提升F1。
practical_value: '- **商品关系路径管理**：电商中商品间存在“配套/替代/互补”等多跳关系（如手机→充电器→快充协议）。可借鉴超图建边将多条关系链聚合为高维键，分离存储商品描述文本作为值，检索时直接从键定位完整关系路径，避免中间实体断裂。

  - **Agent决策链缓存与复用**：多Agent协作时，单代理的推理链（如“用户意图→查询改写→API调用”）可视为多跳证据。将成功执行链的LLM中间结果缓存为超边键，对应执行结果作为值，形成经验库。新任务时用查询匹配超边键，直接拉取完整决策链，降低重复推理开销。

  - **结构化信号与密集检索融合**：本工作证明超图检索分数可作为有效控制信号，与冻结的密集检索器（ColBERTv2）配合。在推荐场景，可将知识图谱子图结构分数与语义向量召回分数简单融合，用轻量控制器（如XGBoost）学习组合权重，提升召回相关性而不必重训检索器。

  - **固定子层实验协议**：论文固定了证据元组缓存、候选段落、Reader等变量，仅改变键结构，这种对照实验设计范式可用于评估公司内部不同知识组织方式（如图索引vs向量索引），快速定位瓶颈。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多跳RAG的本质是证据组织问题：在固定检索预算下，需将检索到的文本组织成能暴露答案链的证据单元。现有密集检索器独立评分段落，基于图的记忆显式关联但常用成对或实体中心键，割裂多跳证据。

**方法**：HKVM-RAG引入键值分离的证据组织层。它从缓存的段落级LLM证据元组中组合出答案路径超边作为检索键，保留段落文本作为答案值。通过固定子层协议（缓存、候选段落、Reader、评估预算相同），隔离键空间设计，对比成对图与超图变体。加权超图键值检索（WHG-KV）在2WikiMultiHopQA（+3.426 F1）和MuSiQue（+3.592 F1）上优于KG-PPR，但HotpotQA显示更高结构化覆盖并不直接提升答案F1。进而将WHG-KV视为证据控制信号而非替代密集检索。用冻结的ColBERTv2和HKVM排序/分数特征，基于out-of-fold预测训练一个密集感知控制器，最终在三个基准上分别达到88.846、65.073、85.810 F1，比ColBERTv2分别提升+11.084、+6.763、+5.966。消融实验表明，其他匹配的非WHG结构化信号无法复现同等增益，证明键值分离超图组织的独特作用。
