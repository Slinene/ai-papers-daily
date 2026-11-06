---
title: 'CORE: Coarse-to-Fine Search with Context Management for Deep Research'
title_zh: CORE：面向深度研究的粗到细搜索与上下文管理
authors:
- Hoang Tran Vuong
- Ngoc Quan Pham
- Hung Bui
- Fatih Porikli
- Dat Quoc Nguyen
affiliations:
- Qualcomm AI Research
- Qualcomm Vietnam Company Limited
arxiv_id: '2611.07859'
url: https://arxiv.org/abs/2611.07859
pdf_url: https://arxiv.org/pdf/2611.07859
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Deep Research Agent 检索与上下文管理
tags:
- Deep Research
- Agent Harness
- Coarse-to-Fine Retrieval
- Context Management
- ColBERT
- Snippet Extraction
one_liner: 训练无关的 deep research harness，通过 coarse-to-fine 检索返回最相关 snippet，并用上下文扩展与去重提升证据质量与效率
practical_value: '- 在电商 Agent / 客服 / 导购搜推场景，可以把工具返回从整段商品详情或评论压缩为 snippet：先 dense 召回，再用
  ColBERT-like late-interaction reranker 的 token 相似度定位最相关片段；不需要额外编码，能显著降低 agent 上下文占用，适合长会话多轮查询。

  - 搜索结果维护一个 (docid, snippet_hash) 去重集合，跨 query 重复只返回引用占位，保留 rank/metadata；这对推荐解释、商品对比、多子查询并行搜索很实用，可避免上下文膨胀和重复证据稀释。

  - 提供 context expansion 工具：agent 针对已检索到的商品/文档给出 goal，在文档内部做受限语义检索并返回相邻 chunk，而不是全文
  summarization；可以省掉一次全局搜索，也可作为商品详情二次探查的工程实现。

  - 评估时同时看 answer accuracy 和 evidence recall，并注意语料规模：CORE 的优势在 5.5 亿文档上更明显，说明大规模商品库/知识库中
  coarse-to-fine + snippet 返回比直接 passage 返回更有必要。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：Deep research agents 通过多轮搜索积累 evidence，但现有 harness 在文档/段落级返回大量文本，agent 上下文被冗余内容稀释；而检索又需要较长 passage 才能可靠匹配，形成粒度矛盾。CORE 把“定位相关文本”的负担从 LLM 转移到检索模型，训练无关地解决这一矛盾。

**方法关键点**：
- 两阶段 coarse-to-fine：先用 AgentIR-4B dense retriever 召回 300 个 passage；再用 late-interaction Reason-ModernColBERT 对 passage 重排，并用同一个 token-level similarity matrix 在 passage 内定位最高分 segment，作为 snippet 返回；不增加额外编码。
- 片段选择：在 ColBERT token 空间构造约 20 个 50% 重叠窗口，MaxSim 打分，映射回文本并扩到 whitespace 边界。
- 上下文管理：context expansion 让 agent 对已见 docid 提交 reading goal，在文档内用 embedding 找最佳 passage，返回其相邻 passage 合并的连续摘录；cross-search deduplication 用 (docid, snippet hash) 去重，重复片段只保留引用。
- 训练无关，可搭配任意 agent 模型。

**关键结果**：在 BrowseComp-Plus / BrowseComp-Wikipedia / BrowseComp-PlusCM（语料规模从 10 万到 5.53 亿文档）上，结合 GPT-5.4、Tongyi-DeepResearch-30B-A3B、Qwen3.8-27B 三个 agent，CORE 在所有 model-benchmark 组都取得最高 answer accuracy 与 evidence recall；相比 OpenResearcher，BrowseComp-Plus 上 Qwen3.8-27B 准确率 +6.39、召回 +7.40，BrowseComp-PlusCM 上 Tongyi agent 准确率 +14.03。同时搜索返回 tokens 明显低于 Tongyi baseline。消融：coarse-to-fine 带来 +8.23，context management 再加 +9.28。

**一句话**：在把证据送入 agent 上下文之前，用检索模型完成“定位相关片段”，并让 agent 按需扩展上下文和去重，比直接塞全文更准且更省 context。
