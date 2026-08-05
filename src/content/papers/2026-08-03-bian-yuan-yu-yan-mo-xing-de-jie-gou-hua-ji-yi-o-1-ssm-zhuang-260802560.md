---
title: 'Structured Memory for Edge Language Models: Persistent Context and Corpus
  Retrieval via O(1) SSM State Injection'
title_zh: 边缘语言模型的结构化记忆：O(1) SSM 状态注入实现持久上下文与语料检索
authors:
- Anusha Madan Gopal
- Aras Pirbadian
- Kristofor D. Carlson
- M Anthony Lewis
- Jonathan Tapson
affiliations:
- BrainChip Inc.
arxiv_id: '2608.02560'
url: https://arxiv.org/abs/2608.02560
pdf_url: https://arxiv.org/pdf/2608.02560
published: '2026-08-03'
collected: '2026-08-05'
category: RAG
direction: SSM 状态注入实现 O(1) RAG
tags:
- SSM
- RAG
- structured memory
- edge inference
- state injection
- O(1) prefill
one_liner: 利用 SSM 固定大小隐藏状态实现 O(1) 预填充的语料检索与记忆巩固，在边缘设备上实现 4500 倍加速
practical_value: '- 高并发低延迟场景可直接复用：将商品/广告语料库离线预编码为 SSM 隐藏状态，线上查询时注入匹配状态，跳过在线重编码，显著降低首
  token 延迟

  - 多 Agent 协作中共享记忆体：各 Agent 可维护各自的结构化记忆，查询时动态融合检索到的语料状态与自身瞬时状态，实现 O(1) 会话初始化

  - 用户长期偏好建模：借鉴 SMC 分层记忆机制，将短期交互序列浓缩为固定大小语义状态，持久化存储，与新检索上下文状态直接融合，无需重新处理历史

  - 轻量级边缘推荐：在手机或 IoT 设备上部署小型 SSM，预编码推荐知识库作为隐藏状态，实现端侧零上下文实时推荐'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Transformer RAG 的预填充成本与检索上下文长度成线性关系，且 KV-cache 随生成 token 增长，导致边缘设备无法实时交互。SSM 天然避免了 KV-cache，但检索语料仍需在线重编码，延迟居高不下。  
**方法**：提出 PRECOG，利用 SSM 隐藏状态的位置无关性与固定大小特性——它本身就是模型已读内容的完整总结。将文档语料离线预编码为这些隐藏状态，查询时直接注入最佳匹配状态，将预填充复杂度从 O(L) 降为 O(1)。进一步提出 SMC（结构化记忆巩固），将瞬时状态分层聚类为长期语义记忆，查询时同时融合检索状态、短期上下文与长期记忆，全程 O(1) 初始化。  
**结果**：在 1.2B 参数的 TENNs-LLM（门控 SSM）上，PRECOG 达到与上下文 RAG 相同的答案质量，边缘硬件预填充延迟从约 27 秒降至 <6 毫秒，加速约 4500 倍，整体响应时间从无法使用变为即时交互。
