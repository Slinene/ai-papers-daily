---
title: 'Search, Inspect, Fetch: Exploiting Boolean Retrieval for Deep-Research Agents'
title_zh: 搜索、检查、提取：利用结构化布尔检索提升深度研究智能体
authors:
- Shuai Wang
- Haodong Chen
- Yu Yin
- Shengyao Zhuang
- Bevan Koopman
- Guido Zuccon
affiliations:
- The University of Queensland
- CSIRO
arxiv_id: '2608.02751'
url: https://arxiv.org/abs/2608.02751
pdf_url: https://arxiv.org/pdf/2608.02751
published: '2026-08-02'
collected: '2026-08-06'
category: Agent
direction: 搜索智能体 · 结构化布尔检索与选择性获取
tags:
- Deep-Research Agent
- Boolean Retrieval
- Structured Search
- Token Efficiency
- Selective Fetching
- BQL
one_liner: SIEVE 通过布尔查询语言实现网页结构感知的按需抓取，较传统全文检索减少 20-50% 上下文 Token 并提升准确率
practical_value: '- 在电商搜索 Agent 或多轮导购场景，可借鉴结构化字段过滤：仅提取商品标题、关键属性或指定评论片段，避免整页全量输入 LLM，大幅节省
  Token。

  - 实现类 BQL 的轻量查询接口，让 Agent 通过约束式语法精准筛选候选（如“标题含‘夏季’且价格低于 100”），提升检索意图对齐度。

  - 先检索列表展示结构化摘要（inspect），再按需提取详情（fetch）的模式，适合需要从大量商品中逐步筛选的对话式推荐 Agent，有效控制上下文长度与成本。

  - 该方法与底层检索器（BM25/向量检索）及 LLM backbone 解耦，可快速集成到现有搜索推荐系统的 Agent 管道中，工程实现成本低。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有深度研究 Agent 的 Search-Visit 模式抓取整个网页，忽略标题、小节等结构信息，导致大量无关内容挤占上下文，既浪费 Token 又降低回答准确率。

**方法关键点**：
- 提出 **SIEVE**：一种 **search-inspect-fetch** 策略，以 **布尔查询语言（BQL）** 为核心。
- BQL 支持在网页字段（标题、小节标题、元数据）上进行布尔过滤，先筛选候选文档；再用可替换的排序器排序；展示包含结构信息的结果卡片供 Agent 检查（inspect）；最后 Agent 仅抓取选中的网页片段（fetch），而非整个页面。
- 该流程将检索粒度从整页降至段/节，且排序、抓取步骤解耦，可灵活插拔不同检索器和 LLM。

**关键结果**：
- 在三个 QA 数据集（BCP-S、HotpotQA、MuSiQue）上，SIEVE 比最强 Search-Visit 配置准确率更高，同时 Token 使用量减少 20.7–50.6%。
- 布尔过滤提升了所有被测排序器（BM25 等）的效果；准确率优势在不同检索器和 Agent backbone 下保持稳健。
