---
title: 'Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document
  Deletion'
title_zh: Lightfoot：具备精确、免模型文档删除的图检索增强生成
authors:
- Uday Allu
arxiv_id: '2611.11010'
url: https://arxiv.org/abs/2611.11010
pdf_url: https://arxiv.org/pdf/2611.11010
published: '2026-11-07'
collected: '2026-11-10'
category: RAG
direction: GraphRAG · 文档删除与索引成本
tags:
- GraphRAG
- Document Deletion
- Multi-hop QA
- Provenance
- Indexing Cost
one_liner: 提出 Lightfoot GraphRAG，索引每篇文档仅一次模型调用，删除为纯数据库操作且图可精确复现
practical_value: '- 电商/广告知识库中商品下架、合同到期、合规删除是高频需求，Lightfoot 的 chunk 级 provenance +
  确定性构图，删除后图等于重建，可把 graph index 当作普通数据库表管理，避免重新 embedding 或 LLM 重算。

  - 索引成本是 GraphRAG 上线隐性瓶颈；每 passage 只调用一次 LM、retrieval 不做模型调用的设计，提示我们把实体/关系抽取结果物化成确定性图边表，查询走图遍历即可，在线推理成本接近零。

  - 删除后图与 fresh index 一致性可验证，适合作为线上知识库发布前的 CI check，避免文档摘要混合内容导致后续无法解释或合规隐患。

  - 注意其在 2WikiMultiHopQA 上 recall/F1 明显下降，说明确定性构图可能牺牲部分多跳表达能力；如果业务场景偏向该类型问题，仍需保留必要的全局摘要或二次抽取。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：GraphRAG 改善多跳问答，但部署环境中索引构建和文档删除的成本常被研究对比忽略。方法：Lightfoot 将实体、链接、事实、同义边全部定义为 per-passage 抽取结果的确定性函数，并携带 chunk 级 provenance；索引每篇文档只调用一次语言模型，检索阶段零模型调用，删除文档只是数据库操作。在 MuSiQue 全量 11,402 个 passages 上验证，删除 10% 文档后的图与幸存文档重新索引结果完全一致。结果：与 HippoRAG 2、LightRAG、fast-graphrag 保持相同抽取、答案、嵌入模型对比，Lightfoot 在三个数据集上索引成本均最低，比 HippoRAG 2 低 26–31%，比 LightRAG 和 fast-graphrag 低 3–6 倍。检索指标上，MuSiQue held-out split 的 recall@5 +2.8、recall@10 +4.3；HotpotQA 答案 exact match +7.7；但在 2WikiMultiHopQA 上显著变差（recall@2 -3.9，F1 -8.4）。删除同样文档，LightRAG 需要 2,187 次模型调用、3.7 小时，fast-graphrag 无删除路径。
