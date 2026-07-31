---
title: 'AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis'
title_zh: AskChem：以声明为中心的化学文献合成基础设施
authors:
- Bing Yan
- Gregory Wolfe
- Stefano Martiniani
- Kyunghyun Cho
affiliations:
- New York University
- Matterstack, Inc.
arxiv_id: '2607.28618'
url: https://arxiv.org/abs/2607.28618
pdf_url: https://arxiv.org/pdf/2607.28618
published: '2026-07-29'
collected: '2026-07-31'
category: RAG
direction: 声明为中心的科学文献RAG基础设施
tags:
- claim-centered retrieval
- RAG
- evidence graph
- faceted taxonomy
- AI agents
- provenance
one_liner: 将文献检索单元从论文改为携带出处的原子声明，构建分面分类与证据图，提升AI代理答案可追溯性
practical_value: '- 将商品详情、用户评论等非结构化内容拆分为原子事实声明，携带来源ID（如评论锚点），构建可溯源的“商品知识库”，AI导购或客服可直接引用出处，增强可解释性与信任感。

  - 建立商品证据图（如用户反馈 ↔ 产品参数声明），当用户查询“哪些手机在弱光下拍照好”时，系统检索相关声明并聚合显示，而非仅返回商品列表，提升多跳推理问答能力。

  - 利用分面分类法动态组织商品属性（品牌、价格、材质等），支持层级浏览与过滤，类似电商导航栏的自动生成，方便探索式购物。

  - 借鉴MCP接口设计，将内部搜索/推荐系统封装为Agent可调用的工具，使第三方AI Agent能直接访问结构化声明数据，实现跨平台智能助手的快速集成。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：化学文献合成常需从多篇论文中收集特定发现，但现有系统仅返回文档列表，科学家或AI代理需手工定位证据、验证并组合答案，效率低下。
**方法**：提出以声明（claim）为检索单元的基础设施AskChem。每篇论文被自动转换为原子化、类型化的声明，每个声明附带源DOI和原文引用或证据定位器。在此声明库之上，构建三种结构：① 稳定的分面分类法，支持层级检索与浏览；② 证据图，通过关系链接声明；③ 探索性动态分类法，按科学原理组织论文。系统提供Web界面、REST/SDK/MCP接口，方便AI代理访问。当前索引2.4M条声明，覆盖147K篇论文。
**结果**：在AskChem-Bench上，基于AskChem增强的GPT-5.5阅读器实现100%可解析DOI（无检索时为88.3%），引用密度在五个系统中最高，证明声明为中心的检索能有效提升答案的完整性与来源可追溯性。
