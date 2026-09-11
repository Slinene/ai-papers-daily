---
title: 'VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over
  Structured Documents'
title_zh: VikingRAG：结构化文档的高精度低 token 检索增强生成
authors:
- Peiyuan Gao
- Gaoyuan Zhang
- Haojie Qin
- Yahui Sun
- Qianyi Zhang
- Yunhao Zhang
- Zeyu Wang
- Wei Lu
affiliations:
- Renmin University of China
- Independent Researcher
- Fudan University
arxiv_id: '2609.11390'
url: https://arxiv.org/abs/2609.11390
pdf_url: https://arxiv.org/pdf/2609.11390
published: '2026-09-10'
collected: '2026-09-11'
category: RAG
direction: 结构化文档 RAG · 目录感知存储与经验复用
tags:
- RAG
- structured documents
- token efficiency
- experience edges
- adaptive escalation
- multi-round retrieval
one_liner: 目录感知语义存储结合经验边与自适应升级，使结构化文档 RAG 精度持平 SOTA 而 token 降至 5.1%-32.5%
practical_value: '- 将商品/政策/售后文档按目录树 URI 化，构建多粒度摘要（chunk 与 section abstract）的向量索引；语义召回结果带回
  URI 路径，后续检索/读取限定在该子树，避免每次把完整目录序列化进 prompt，显著降 token。

  - 用 Search/List/Grep/Read 四种工具切分检索动作：先语义粗定位到商品/政策条目，再按 URI scope 做关键词精确匹配，最后只读需要的内容验证证据；适合售后规则问答、广告审核政策、商品属性答疑等易漏召回场景。

  - 把多轮 agent 检索成功的轨迹物化为 query-conditioned experience edges，相似 query 直接走边扩展召回，避免重复探索；可借鉴为在线服务中的“会话检索缓存/知识捷径层”，随真实
  query 增量更新，降低重复路径 token 与延迟。

  - 自适应 escalation：先用一轮 experience-augmented retrieval 生成候选答案，并要求 LLM 先列关键约束再判定证据是否充分，不充分才升级多轮
  agent。工程上能把大多数 easy query 留在低成本路径，hard query 才触发高成本 agent。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
结构化文档广泛用于企业问答、法律/金融文本、科学文献等场景。现有 RAG 要么将文档扁平化为 chunk 丢失结构，要么把完整目录序列化进 prompt 导致 token 过高；很多方法也缺少证据缺口驱动的多轮检索，难以应对跨章节、跨文档证据分散的问题。DeepRead 虽支持多轮但 token 消耗大，因此需要在保持高精度的同时降低结构上下文和交互 token。

**方法关键点**
- 目录感知分层语义存储：抽取文档目录树，按结构边界 chunk，自底向上生成多粒度摘要（叶子摘要与内部节点摘要）；所有目录节点、chunk、abstract 赋予 URI，路径编码层级；向量索引记录 URI、类型、深度、预览，使语义检索直接返回结构入口。
- 四个访问工具 Search/List/Grep/Read：Search 返回语义匹配 chunk/abstract 及 URI；List 查看目录局部；Grep 在 URI scope 内精确关键词匹配；Read 读取具体对象。结构信息按需暴露，不序列化完整目录。
- 证据缺口驱动多轮检索：agent 每轮观察已有证据，决定回答或继续调用工具补缺，设有轮数预算。
- 经验边（VikingRAG-E）：把历史多轮检索轨迹物化为从初始 Search URI 指向最终支持证据 URI 的带查询摘要边；相似 query 激活这些边，一步扩展召回，将多轮探索压缩成少轮。
- 自适应升级（VikingRAG-E+）：先做一轮经验增强检索并生成候选答案，LLM 先列关键证据约束再判定是否充分；充分则直接回答，不充分才升级多轮 agent 检索。

**关键结果**
在 VersionQA、SyllabusQA、QASPER、HotpotQA、LegalBench-cuad、FinanceBench 六个真实结构化文档数据集上，对比 MoDora、BookRAG、DeepRead、KohakuRAG、LightRAG、HippoRAG-2、SQL-AgenticRAG、NaiveRAG。VikingRAG 精度匹配 SOTA，token 仅为 SOTA 的 11.6%–51.9%；VikingRAG-E+ 进一步降至 5.1%–32.5%，延迟也低于 DeepRead。在文档存储性能上，LightRAG、HippoRAG-2 在 FinanceBench 上 24h 摄入失败，BookRAG 仅完成 VersionQA 和 SyllabusQA，VikingRAG 系列能在预算内完成更大文档集合。更换 GPT-5.5、Seed-2.0、GLM-4.7 等 backbone LLM 结论一致。
