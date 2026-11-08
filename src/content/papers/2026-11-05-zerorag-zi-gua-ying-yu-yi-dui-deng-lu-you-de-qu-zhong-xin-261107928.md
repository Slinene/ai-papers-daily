---
title: 'ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented
  Generation'
title_zh: ZeroRAG：自适应语义对等路由的去中心化检索增强生成
authors:
- Petru Neague
- Quinten Stokkink
- Martijn de Vos
- Rafael Pires
- Mathis Randl
- Anne-Marie Kermarrec
- Johan Pouwelse
affiliations:
- Delft University of Technology
- EPFL
arxiv_id: '2611.07928'
url: https://arxiv.org/abs/2611.07928
pdf_url: https://arxiv.org/pdf/2611.07928
published: '2026-11-05'
collected: '2026-11-08'
category: RAG
direction: 去中心化RAG · 语义对等路由
tags:
- RAG
- Decentralized
- Peer-to-Peer
- Semantic Routing
- Self-organization
- Retrieval
one_liner: 提出ZeroRAG，在去中心化对等网络中通过语义查询路由与自适应重连，无需全局结构即可逼近集中式RAG的召回与答案准确率
practical_value: '- **跨组织/跨部门数据不能集中时可借鉴**：电商广告场景常有多方数据（如品牌方、平台、第三方数据商）因隐私或合规无法物理汇聚，ZeroRAG
  表明可以在不共享原始文档的前提下，通过语义路由和对等网络实现联合检索，支撑 RAG 问答或推荐理由生成。

  - **语义路由替代全局索引**：其核心思想是用轻量级邻居广告和查询缓存做 best-first walk，逐跳逼近语义相关节点，而非维护 DHT 或中心协调器。这种“路由即检索”的思路可迁移到大规模分布式
  ANN 检索或召回层，降低索引维护成本与协调开销。

  - **自适应重连提升长期召回**：网络根据历史查询逐步重连到语义相似邻居，类似在线学习索引。在推荐系统中可借鉴为：基于用户行为反馈动态调整召回通路或索引结构，让热门语义区域优先被探索。

  - **故障自愈与扩展性**：论文展示 10 万节点规模与灾难性节点失效后的恢复能力，对需要高可用、弹性伸缩的线上检索服务有参考价值，但实现复杂度较高，落地前需评估业务收益。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有 RAG 系统依赖集中式文档存储，但文档常因隐私、版权或法规限制无法集中托管。已有去中心化检索要么引入协调权威，要么依赖 DHT 等全局结构，需要全网协调，扩展性和鲁棒性受限。

**方法关键点**：ZeroRAG 提出一个纯对等网络上的语义路由层。每个节点仅维护有界邻居广告和最近查询缓存，不保存全局索引。查询通过 best-first walk 在覆盖网络中逐跳转发，每一步选择语义上最相关的邻居，同时根据查询结果动态重连邻居关系，使网络随时间自组织成语义聚类结构，提高后续查询的召回效率。

**关键结果**：在三个真实工作负载上与两个去中心化基线对比，ZeroRAG 在召回率和所需网络消息数上均优于基线，召回率与 LLM 答案准确率接近集中式文档存储；在灾难性节点故障后能自愈，并扩展至 100,000 节点。
