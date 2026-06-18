---
title: 'Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture
  for LLM Agents'
title_zh: 解耦搜索与推理：LLM Agent 的供应商无关的接地架构
authors:
- Emmanuel Aboah Boateng
- Kyle MacDonald
- Amardeep Kumar
- Siddharth Kodwani
- Sudeep Das
affiliations:
- DoorDash, Inc.
arxiv_id: '2606.18947'
url: https://arxiv.org/abs/2606.18947
pdf_url: https://arxiv.org/pdf/2606.18947
published: '2026-06-17'
collected: '2026-06-18'
category: Agent
direction: Agent 搜索接地解耦与成本控制
tags:
- Grounding
- MCP
- Search
- Agent Architecture
- Cost Optimization
- E-commerce
one_liner: 将搜索接地从模型内部移出为可配置的 MCP 网关，在 Prompt 合规、成本、缓存和提供商选择上获得显式控制
practical_value: '- **将搜索定义为显式工具边界，而非模型内置功能**：在电商 agent 中，把搜索（如商品检索、Query 理解时的外部知识查询）做成独立工具，通过
  MCP 协议标准化输入输出，可避免 Prompt 中严格的输出格式被 native search 的冗长解释破坏，尤其适合需解析 JSON/实体/分类标签的流水线。

  - **使用提供商注册表 + 回退链实现搜索路由**：在推荐/搜索系统中，可以按成本、新鲜度、覆盖场景动态选择搜索提供商（如 Serper、BrightData），并配置超时回退，保证可用性同时大幅降低搜索
  API 开销（实验中成本降低 91%–98%）。

  - **利用精确+语义缓存减少重复检索**：对电商中高频查询（如热门商品、常见长尾意图），引入基于 embedding 的语义缓存，可达到 99.4% 的缓存命中率，将延迟降低
  68% 并接近零边际搜索成本，适合大规模 Agent 场景。

  - **将搜索成本、深度、延迟作为可调旋钮**：通过调整 max_results（检索结果数）在准确率和成本之间 trade-off（如 SimpleQA 从
  2 条增至 6 条后准确率快速上升，之后饱和），让接地层像推荐系统中的召回预算一样可配置，团队可按业务需求调优。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生产环境中的 LLM Agent 越来越依赖实时搜索，但原生搜索接地功能将检索策略、提供商选择、成本、延迟与生成行为耦合在模型 API 内部，导致难以审视、调优和移植，还会引发“搜索诱导冗长”（Search-Induced Verbosity），破坏严格的输出契约（如只返回实体）。在需要下游解析 JSON、布尔值或精确实体的电商 Query 理解、搜索推荐流水线中，这种冗长可能使语义正确的答案变得不可用。

**方法关键点**：
- **DSG 架构**：将搜索接地解耦为一个与供应商无关的网关，基于 MCP 协议，使推理模型完全可替换。
- **标准化工具格式化**：将不同搜索提供商的异构输出归一化为含标题、URL 和片段的来源感知上下文，保持检索与生成的边界。
- **提供商抽象与回退**：支持 Serper、BrightData、Firecrawl 等多种提供商，可配置回退链和成本元数据。
- **智能搜索层**：实现精确缓存、语义相似缓存（基于 embedding 余弦相似度，可配阈值）和提供商回退三级策略，跨请求复用证据。
- **可观测控制旋钮**：暴露检索深度（max_results）、缓存策略、提供商选择、回退顺序等，允许团队监控成本和延迟。

**关键实验与结果**：
- **公开 QA 基准**：在 SimpleQA 上，DSG+BrightData 准确率 86.1% vs 原生搜索 87.7%，但搜索成本降低 91%（$1.80 vs $20/1K 查询）；在 FreshQA 上原生搜索领先 4.6pp，体现解耦可按任务选择提供商。
- **生产电商 QIU 任务**：在零售查询上，DSG+Serper 准确率 93.90% 略超原生搜索 93.40%，成本从 $7.90 降至 $0.110/1K（降低 98%+）；长尾合成数据上同样接近或超过原生。
- **Prompt 合规诊断**：HotpotQA 上 Claude Sonnet 4 原生搜索输出 78.1% 以解释性文本开头，中位长度 353 字符 vs DSG 的 13 字符，DSG 有效避免格式漂移。
- **缓存效益**：重复查询重放达到 99.4% 缓存命中率，延迟从 4570ms 降至 1465ms（-68%），边际搜索成本趋近零。
