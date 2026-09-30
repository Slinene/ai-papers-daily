---
title: 'Follow the Entities: A Corpus Map for Agentic Search'
title_zh: 跟随实体：面向 Agentic Search 的语料地图
authors:
- Soyeong Jeong
- Sujay Kumar Jauhar
- Sung Ju Hwang
- Andrew Joohun Nam
affiliations:
- KAIST
- Microsoft
arxiv_id: '2609.37226'
url: https://arxiv.org/abs/2609.37226
pdf_url: https://arxiv.org/pdf/2609.37226
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 搜索 · 实体导航层
tags:
- Agentic Search
- Entity Resolution
- Corpus Navigation
- RAG
- LLM Agent
- Knowledge Graph
one_liner: 以跨文档实体为锚点构建离线可复用导航层，提升多文档 Agent 搜索证据发现并降低 token 消耗
practical_value: '- 把经常跨文档出现的业务实体（商品、活动、商家、项目）离线解析成 Entity Page，作为 agent 可读文件挂到原语料旁；查询时让
  agent 从实体页跳到相关文档，而不是每次都重新 grep/搜索，能稳定节省 34%–57% token。

  - 构建实体-文档二部图，而不是树形分类；同一文档可挂在多个实体下，避免 Corpus2Skill 这类层次聚类把相关证据拆散的问题，电商知识库中「活动/商品/商家」多对多关联尤其适合。

  - 离线构建可用 GLinker/GLiNER 等无 LLM 方案替代，成本低且可跨 LLM 复用；新增文档时增量更新 registry 并只重渲染受影响 Entity
  Page，适合持续增长的电商文档/工单/商品库。

  - Entity Page 将事实逐条归因到源文档，agent 读取页面后能沿链接打开源文档验证，减少幻觉；也可作为权限/隐私过滤边界，按权限生成分离 map。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
大型企业语料中，多文档问题的证据分散在不同应用、目录和时间段里。Raw-corpus agentic search 虽然能访问全量文档，但文档之间没有关系表示，agent 每次查询都要重新搜索、阅读并推理跨文档关联，既容易漏掉互补证据，又大量消耗 token。论文提出：与其反复改进 query-time 搜索策略，不如离线构建可复用的语料导航层。

**方法关键点**
- CORPUSMAP 以跨文档实体为锚点，离线将语料组织成实体-文档二部图 G=(E∪D,L)。
- 构建分四步：先归纳实体类型 catalog；再在每篇文档中抽取实体 mention；随后将同一实体跨文档 resolve 到共享 registry，只保留至少被两篇文档链接的实体；最后为每个实体生成 Entity Page，聚合事实、逐条归因到源文档，并链回所有相关文档。
- Entity Page 不替换原文档，而是以文件形式叠加在原语料旁，agent 仍可用相同 shell 工具搜索和打开原文档；查询时既可以从 query 相关实体页进入文档，也可以从文档反查实体页。
- 构建过程可用 LLM，也可用 GLinker/GLiNER 等 off-the-shelf 确定性方案；registry 支持增量更新，新文档到达时只需更新受影响实体页。

**关键结果**
在 EnterpriseRAG-Bench、WixQA、HERB 三个 benchmark 上，用 7 个 LLM 评估。相比 raw-corpus agentic search，CORPUSMAP 的 Overall Quality 提升 6.4–11.7 个百分点，输入 token 平均减少 34%–57%；同时超过 Document Page、Group Page、LLM Wiki、Corpus2Skill 以及 BM25/dense/HippoRAG/GraphRAG 等检索式方法。廉价 LLM 构建的 map 可跨模型复用，GLinker 离线构建的质量与 LLM 构建相当；增量更新相比全量重建节省 69%–71% token，并能让新纳入文档对应的问题正确率提升 30.4–40 个百分点。

**一句话**
语料组织方式本身比搜索策略更值得优化；可复用的实体-文档关系是 Agentic Search 的低成本高收益导航层。
