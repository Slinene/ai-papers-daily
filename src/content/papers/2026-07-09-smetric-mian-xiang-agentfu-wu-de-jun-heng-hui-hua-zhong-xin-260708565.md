---
title: 'SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric
  Scheduling'
title_zh: 'SMetric: 面向Agent服务的均衡会话中心LLM调度'
authors:
- Jiahao Wang
- Kaizhan Lin
- Kaixi Zhang
- Jinbo Han
- Xingda Wei
- Sijie Shen
- Chenguang Fang
- Wenyuan Yu
- Rong Chen
- Haibo Chen
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
- ShanghaiTech University
arxiv_id: '2607.08565'
url: https://arxiv.org/abs/2607.08565
pdf_url: https://arxiv.org/pdf/2607.08565
published: '2026-07-09'
collected: '2026-07-11'
category: Agent
direction: Agent 服务调度优化 · 会话中心负载均衡
tags:
- LLM Serving
- Agent Workload
- KV Cache Reuse
- Load Balancing
- Session Scheduling
one_liner: 利用Agent工作负载的会话内局部性，通过会话首请求负载均衡+后续请求缓存亲和路由，在不牺牲KV重用下实现高吞吐
practical_value: '- 在电商/搜索Agent系统中，会话内多步请求KV重用率极高（>80%），可采用SMetric的调度策略：每个session的首次请求做简单轮询或最少连接调度实现负载均衡，后续请求固定路由到缓存了前缀KV的实例，兼顾吞吐与延迟。

  - 若已有全局KV存储（如分布式缓存层），可将调度策略与缓存分层结合：本地实例缓存热数据，全局存储兜底，使负载均衡不再以完全牺牲重用为代价。

  - 会话轮次信息可直接从请求中的`session_id`或轮次号提取，无需额外状态维护，调度器可保持无状态、易扩展，适合生产环境快速落地。

  - 对于采用prefill-decode混部或disaggregation架构的大型Agent服务，该调度方法可提升整体吞吐10-30%，同时降低每token延迟，有效应对突发流量。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM服务Agent与传统聊天负载不同，请求由Agent发出，具有两大特征：(1) Agent仅使用完整回复，吞吐量（TPS）是首要指标，每token延迟要求可适当放宽；(2) 请求间KV重用率极高（生产trace中>80%），远高于对话场景（~54-62%）。现有调度器为提升缓存重用，常将请求路由到持有对应KV的实例，导致热点负载严重失衡，反而限制集群TPS。

**方法**：提出SMetric，一种均衡的会话中心调度策略。核心洞察：利用全局KV存储层，无需牺牲所有重用换负载均衡；工作负载具有会话内局部性，只需将每个session的首次请求做纯负载均衡路由，后续请求按缓存亲和性路由，即可保持整体负载均衡，同时保留大部分本地KV重用。会话轮次信息可从用户输入中高效、精确推导，无需调度器保存状态。

**结果**：在生产级Agent trace上，SMetric相比最优调度器，在prefill-decode混部+全局存储下集群TPS提升10-16%，在disaggregation架构下prefill TPS提升2-34%，同时每token延迟更优。
