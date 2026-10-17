---
title: Private Retrieval Augmented Generation via Random Projection
title_zh: 基于随机投影的隐私保护检索增强生成
authors:
- Dixi Yao
- Tahseen Rabbani
- Tian Li
affiliations:
- University of Chicago
arxiv_id: '2610.22297'
url: https://arxiv.org/abs/2610.22297
pdf_url: https://arxiv.org/pdf/2610.22297
published: '2026-10-15'
collected: '2026-10-17'
category: RAG
direction: 隐私保护 RAG · 随机投影
tags:
- RAG
- privacy
- random projection
- differential privacy
- data extraction
one_liner: 用随机投影同时处理知识库与查询嵌入，在保持语义相似度的同时缓解数据抽取攻击，优于DP方案
practical_value: '- 在涉及用户/商家敏感数据的 RAG 场景（如客服知识库、内部文档问答）中，可对 datastore embedding 和
  query embedding 用同一个随机投影矩阵降维后再做检索；无需复杂 DP 机制，工程实现简单，还能降低向量维度、省存储与计算。

  - 随机投影矩阵可以按租户或定期更换，增加攻击者从泄露的投影向量恢复原文的难度；但要注意它不能替代访问控制与审计，对强背景知识的成员推断攻击防护有限。

  - 对电商搜索/推荐中跨团队共享商品或用户行为 embedding 的场景，可以先随机投影再共享，在 cosine/点积检索损失较小的前提下减少原始 embedding
  泄露风险。

  - 论文表明随机投影在检索与生成质量上优于 DP baseline，可作为轻量隐私基线；若业务需要正式合规保障，仍需结合差分隐私或其他审计机制。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**  
RAG 系统查询外部知识库时会泄露敏感信息，攻击者通过构造接近合法查询的 prompt 可抽取 datastore 中的个人身份等内容。现有差分隐私（DP）方法提供形式化保证，但往往导致输出质量下降（如高困惑度）且实现复杂，可能“杀鸡用牛刀”。

**方法关键点**  
对 datastore embedding 和 query embedding 应用同一个随机投影矩阵，利用随机投影在低维空间中天然保持输入间成对相似度的特性。额外的随机性改变 datastore 向量，使攻击者难以恢复原文，同时让正常用户仍能获得准确检索结果。相比 DP，不需要注入噪声或复杂机制。

**关键结果**  
在多个 RAG 架构和数据集上，随机投影方法在检索与生成性能上优于带 DP 保证的 baseline，且在强攻击模型下经验隐私表现与 DP 相当。论文首次表明随机投影可作为隐私保护 RAG 的实用轻量 baseline。
