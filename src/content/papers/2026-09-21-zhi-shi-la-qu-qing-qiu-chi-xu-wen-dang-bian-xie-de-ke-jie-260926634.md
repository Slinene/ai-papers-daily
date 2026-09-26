---
title: Knowledge Pull Requests for Continual Document Authoring
title_zh: 知识拉取请求：持续文档编写的可解释更新框架
authors:
- Alexander Martin
- Benjamin Van Durme
affiliations:
- Johns Hopkins University
arxiv_id: '2609.26634'
url: https://arxiv.org/abs/2609.26634
pdf_url: https://arxiv.org/pdf/2609.26634
published: '2026-09-21'
collected: '2026-09-26'
category: RAG
direction: RAG 文档维护 · 可解释知识更新
tags:
- Continual Document Authoring
- Knowledge Update
- ChangeLog
- RAG
- Claim Extraction
- Wikipedia
one_liner: 提出 KPR 框架，将文档更新拆为 Claim Proposal 与 Document Diff，使每次知识变更可审计，并显著提升信息整合与内容保留
practical_value: '- 可以把知识更新与文本改写解耦：类似电商商品详情页、帮助中心、政策文档的持续维护，先产出 Claim Proposal（新增/冲突事实），再产出
  Document Diff，让运营/审核先确认“改了什么知识”，再确认“改了什么文字”，降低审核成本。

  - Claim 抽取 + 路由到 section 的机制可复用到多来源商品信息整合：例如从不同供应商、不同语言描述中抽取结构化卖点，自动匹配到详情页对应模块，并标记冲突价格、规格、功效等。

  - 对 RAG 知识库动态更新有直接参考价值：与其定期全量重建索引，不如维护一套主文档，用 KPR 方式增量合并新来源/新语言信息，同时保留 ChangeLog，便于溯源和回滚。

  - 评估中“per token generated 的信息增量”值得借鉴：在生成式推荐/文案场景中，不仅看最终文本质量，还可以追踪每次修改的知识增量，避免大模型冗长改写却未新增有效信息。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
持续维护的文档（Wikipedia、技术文档、报告）需要不断吸收新来源、新语言、新时间点的知识。现有方法要么直接编辑但不记录知识变化，要么从零重新生成，难以审计每次更新到底改变了哪些事实。Wikipedia 虽记录编辑，但也只是文本 diff，不体现知识 diff。

**方法关键点**
KPR 将更新过程分为两部分：先从新来源抽取 claims，过滤并路由到文档对应 section，检测与现有内容的冲突，形成 Claim Proposal（新增/冲突的源声明）；再据此生成具体文本改动，形成 Document Diff。最终输出一个 ChangeLog，实现“知识变了什么”与“文本怎么变”的分离。

**关键结果**
在跨语言 Wikipedia 修订和 RAGTIME query-driven 报告更新上，KPR 相比从来源重写或从零重新生成，集成了更多信息，同时更好保留现有内容；每生成一个 token 带来的信息增量最高。经 KPR 修订的文章在问答 grounding 上优于带搜索的前沿模型，因为后者无法利用仅在其他语言中记录的知识。
