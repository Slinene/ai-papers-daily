---
title: 'Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That
  Organizes Before It Retrieves'
title_zh: 面向多智能体系统的企业 RAG 知识层：先组织后检索
authors:
- Garima Agrawal
- Prasun Das
- Akshay Sarvade
- Priyanka L
- Minisha N
- Sravani Joshna
- Hemath Manivannan
- Lavanya Korada
- Sambhrit Pattanayak
- Srashti Gupta
affiliations:
- Cognizant, Plano, Texas, USA
arxiv_id: '2610.32851'
url: https://arxiv.org/abs/2610.32851
pdf_url: https://arxiv.org/pdf/2610.32851
published: '2026-10-23'
collected: '2026-10-26'
category: RAG
direction: 企业 RAG · 多 Agent 知识组织
tags:
- RAG
- Multi-Agent
- Metadata Registry
- Hypergraph
- Artifact Provenance
- Enterprise AI
one_liner: 将本体置于 artifact 层，用元数据注册表与导航超图先组织后检索，实现结构化消歧避免跨服务规则混淆
practical_value: '- **结构化过滤优于向量排序**：在电商/广告 RAG 中，同名词如「优惠券」「活动价」在不同业务线含义不同，向量检索容易返回高相似但错误上下文的片段。可先解析查询到
  artifact ID 或业务域，用元数据约束候选集，让错误来源的内容不进入排序，而非依赖打分压过。

  - **轻量元数据注册表替代重型本体**：不要一开始就构建内容级实体关系图，成本高且难以维护。利用生成式语料自带的 provenance（来源服务、组件、域、类型）做稀疏元数据索引，几天内即可上线，适合快速迭代的推荐/广告知识库。

  - **超图定义在文档/规则 artifact 而非实体上**：跨服务旅程查询（如从商品详情到订单到售后）可以用 artifact 超图导航，先确定相关 artifact
  集合，再做向量检索，避免实体链接爆炸。

  - **新服务按约定接入**：设计一套轻量 schema（服务名、域、类型），新接入业务线只要按约定注册元数据即可扩展，无需重新训练或构建图，适合多业务线快速扩展的
  Agent 工作流。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：企业部署 agentic AI 时，代理需要的是系统行为逻辑，而非面向干系人的文档。一个七代理逆向工程管线处理了 241 个仓库、18 个服务，产出数千 artifact，但恢复不等于可用。业务实体如 offer、eligibility、activation 跨服务共享词汇，名称相近但操作不同；端到端旅程涉及上千条近同规则，平面向量检索会返回错误服务的高相似规则且无出错信号。传统内容级本体构建成本高、无法跟上发布周期。

**方法关键点**：将本体放在 artifact 层，利用机器生成语料自带的 provenance（producer、component、service、domain、type）先消歧。构建三个组件：自描述目录、稀疏元数据注册表、基于 artifact 而非实体的导航超图。查询先解析为 artifact 标识符，再约束向量检索，使错误服务规则不出现在候选集，消歧是结构化的而非统计性的。

**关键结果**：知识层不到一周建成，新服务可按约定接入，服务 SDLC 代理、开发者、QA 和分析师。支撑 100+ 生产缺陷根因分析与解决，并将 35 个发布回归失败归因到具体规则和服务。
