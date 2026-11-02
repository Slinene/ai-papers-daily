---
title: 'Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic
  Systems with Harnesses'
title_zh: 上下文即基础设施：面向带Harness的Agent系统检索的知识编译
authors:
- Zhichang Yu
- Baining Cao
- Sbaaoui Idriss
- Qi Wang
- Gangqiang Xu
- Ling Qin
- Xiaoling Jin
- An Liu
- Shaohao Cai
- Xiaoyang Bao
affiliations:
- InfiniFlow Inc.
- East China Normal University
arxiv_id: '2610.41172'
url: https://arxiv.org/abs/2610.41172
pdf_url: https://arxiv.org/pdf/2610.41172
published: '2026-10-30'
collected: '2026-11-02'
category: RAG
direction: Agentic RAG 的知识编译与检索纪律
tags:
- Agentic RAG
- Knowledge Compilation
- Claim-Evidence
- Token Efficiency
- BM25
- RAGFlow
one_liner: 在Agentic检索中，把文档编译为声明-证据叶子可让命中token省91%、平均省38%，盈亏平衡充分率仅2%
practical_value: '- 在Agentic检索/问答栈中，优先用BM25+grep+LLM harness做检索控制，不必引入向量索引；论文实测加dense
  leg反而降准确率，可降低系统复杂度和索引成本。

  - 对电商商品描述、政策文档、广告素材库等需要精确引用的场景，可仿照claim-evidence编译：用轻量模型抽取“声明+逐字证据span+源偏移”，召回后替换整chunk进上下文；命中节省91%
  token，未命中仅多1.9%，平均38%，适合token敏感的大规模Agent系统。

  - 增加决策gate（轻量决策模型）判断证据充分性，拒绝则丢弃整个块而不是塞入prompt；可显著降低端到端延迟（140s→30s），但token节省以检索轮次为代价，需在延迟和成本间权衡。

  - 结构化的RAPTOR/PageIndex/wiki/graph等artifact在强harness下对准确率无增益甚至负收益，不应作为召回卖点；应把它们当作治理/审计/跨源集成工具，用独立ledger（如审计覆盖率、集成成功率）评估，而不是benchmark准确率。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：RAG正变得agentic，搜索harness已解决准确率问题（仅BM25+grep+MiniMax M3在BrowseComp-Plus达85%、FRAMES达91%），但暴露上下文问题：无纪律的循环重复查询、重复阅读同一文档、把无关段落塞满窗口，消耗大量token却不成答案。缺失层是知识编译。

**方法关键点**：
- 知识编译定义为查询无关的ingestion变换，生成typed、versioned artifacts，保留到源span的lineage。
- Pipeline六阶段：parse、chunk、enrich（glm-4-flash抽取）、validate（证据span必须逐字匹配，否则丢弃）、assemble、register。
- 核心可测机制：navigation tree叶子是claim-evidence pairs，包含规范化声明c、逐字证据span e、源chunk/偏移s、时间元数据τ。派生通道与原始通道严格分离，派生只读不回写。
- 三种serving模式：E1 evidence-first retrieval直接BM25搜声明文本；E2 evidence substitution默认，召回chunk后替换为claim-evidence pairs进窗口，gate决定回答或打开原文；E3 decision-gated reading用轻量决策模型控制深读。
- 检索harness五站：capability check、evidence prefetch、evidence gate、tool loop、deterministic close；框架保证证据先于思考、不足则丢弃、工具门控、预算调用、交付引用、保证关闭。

**关键实验**：FRAMES 200题，baseline无编译BM25/grep harness达91%准确率。结构artifact（RAPTOR summary tree、PageIndex outline、wiki、graph）无检测到准确率提升，PageIndex在FRAMES规模为负。claim-evidence substitution：命中-91% token，未命中+1.9%，平均-38%；盈亏平衡充分率约2%，FRAMES约43%；决策gate延迟140s→30s，gate arm mean token -52%。BrowseComp-Plus harness only达85%。

**最值得记住的一句话**：检索是harness问题先于index问题；知识编译不是更好的retriever，而是supply层，其价值在更小、有来源、足够的上下文，不在准确率。
