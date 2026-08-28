---
title: 'Pointing the Way, Hiding the Destination: Practical Private Dense Retrieval
  at Scale'
title_zh: 指路藏终点：大规模实用私有密集检索
authors:
- Peichun Hua
- Danyang Chen
- Junan Zhang
- Haifeng Sun
- Jingyu Wang
- Diwen Xue
- Mingyu Li
- Yunming Xiao
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- State Key Laboratory of Internet Architecture, Tsinghua University
- Beijing University of Posts and Telecommunications
- The Chinese University of Hong Kong
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2608.25735'
url: https://arxiv.org/abs/2608.25735
pdf_url: https://arxiv.org/pdf/2608.25735
published: '2026-08-26'
collected: '2026-08-28'
category: RAG
direction: 隐私保护向量检索 · 深度哈希短列表
tags:
- Private Retrieval
- Dense Retrieval
- Deep Hashing
- Differential Privacy
- RAG
- Shortlist
one_liner: 用可学习深度哈希生成短候选列表，结合加密重排与不经意传输，在保持检索质量的同时将全库密码学搜索成本降至可部署水平
practical_value: '- 在需要隐私保护的 RAG 或私有知识库检索中，可将「可学习深度哈希 shortlist」作为预筛层：只对哈希命中的 200-500
  个候选做加密重排，避免全库同态计算，检索质量接近全库向量检索。

  - 将连续 embedding 映射为二元哈希码后，不再直接暴露原始向量，配合 directional metric DP 可显著降低 embedding inversion
  / property inference 泄露；对电商用户行为、广告素材、商品描述等敏感语料检索有直接参考价值。

  - 工程上可采用两阶段漏斗：哈希粗筛得到短列表，再用 oblivious key transfer 和加密 reranking 保护具体 query 与最终 item
  选择；这比单纯用聚类或 LSH 粗扫更贴合私有检索的隐私与质量平衡。

  - 在 10Gbps 网络、数百万文档规模下，该协议额外延迟约 0.73s，适合在线 RAG 服务；但需要额外训练/微调深度哈希模型，并接受候选短列表带来的召回上限。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**

托管 RAG 与语义搜索需要同时满足两个矛盾需求：既要隐藏用户查询和最终选中的结果，又要只暴露用户有权获得的文档。现有密码学方案要么对每个查询处理全库导致开销过大，要么为了效率只扫描少量聚类、牺牲检索质量。

**方法关键点**

把可学习深度哈希重新用作私有过滤器：随机化二进制码将 provider 指向一个 200-500 条的短候选列表，后续用加密重排和 oblivious key transfer 保护精确查询与最终选择。这样短列表绕开了全库密码学搜索，而质量损失很小。

**结果**

在 5 个零样本语料（25K 到 5.4M 文档）上，200-500 候选的短列表检索质量与全库密集检索接近。在 2.68M passage 的 NQ 语料、10Gbps 链路下，整个协议只增加 0.73 秒，相当于 128-token Qwen3-32B RAG 管线的 10%。释放的代码满足 directional metric DP，并显著降低 embedding-inversion 和 property-inference 泄露，证明精心学习的短列表能让私有密集检索既准确又实用。
