---
title: 'Lacuna: A Research Map for Machine Learning'
title_zh: Lacuna：机器学习研究地图
authors:
- Martin Weiss
- Miles Q. Li
- Alejandro H. Artiles
- Yacine Mkhinini
- Chris Pal
- Hugo Larochelle
- Nasim Rahaman
affiliations:
- Tiptree Advanced Systems Corporation
- Mila
- Polytechnique Montreal
- McGill University
- Universite de Montreal
arxiv_id: '2606.26246'
url: https://arxiv.org/abs/2606.26246
pdf_url: https://arxiv.org/pdf/2606.26246
published: '2026-06-24'
collected: '2026-06-27'
category: LLM
direction: 科研文献知识图谱构建 · LLM Agent
tags:
- Research Map
- LLM
- Literature Retrieval
- Deep Research Agent
- Knowledge Graph
one_liner: 用LLM将论文转化为可导航研究地图，在文献检索和深度调查报告任务上超越OpenScholar与GPT-Researcher
practical_value: '- **商品知识地图构建**：借鉴Lacuna用LLM将非结构化论文转化为结构化摘要、概念、方向的方法，可对商品描述、评论、问答生成商品知识图谱（核心卖点、使用场景、竞品对比、搭配提案），作为推荐系统的可解释索引。

  - **多阶段深度推荐代理**：Lacuna Deep Research的检索→分析→报告流水线可直接迁移至复杂购物决策场景（如“帮我选一台适合视频剪辑的笔记本”），通过多轮检索商品知识、对比分析、生成个性化购买指南，提升用户体验。

  - **可追溯证据增强推荐可信度**：每个知识条目保留原始论文链接的设计，可改为在推荐解释中附带用户评论原文、评测视频等来源，增强推荐的可信度与透明度。

  - **MCP接口集成现有链路**：论文开放的MCP接口设计，允许将地图作为工具接入任意LLM代理，电商系统可参照此模式，将商品知识库封装为标准化工具，供客服机器人或购物助手调用。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：科学文献爆炸增长，研究人员需要更高效地浏览、引用和构思。现有工具仍将论文视为孤立PDF，缺乏可重用的结构化中间知识。Lacuna意图构建一个可导航、可扩展的研究地图，让人和代理能直接基于论文衍生的结构化概念开展研究。

**方法关键点**：
- 用LLM将每篇论文转化为**论文摘要、概念元素、研究方向、研究提案**四类结构化对象，并保留与原始论文的双向链接。
- 构建成大规模知识地图，提供Web、Markdown和**MCP接口**（Model Context Protocol），方便人类浏览和代理调用。
- 在此基础上开发了**Lacuna Deep Research**代理：它是一个多阶段报告生成系统，先检索地图中的相关概念和论文，再逐步分析、综合，最终生成带有引用的深度调查报告。

**关键结果**：
- 在**LitSearch检索任务**上，Lacuna的Recall@10达**0.538**，显著优于OpenScholar v3的0.424。
- 在**Multi-XScience-CS/ML**和**ScholarQA-CS-ML**上也全面优于OpenScholar。
- 在**ReportBench-ML**的25项调查任务中，Lacuna Deep Research获得**0.052 citation F1**（GPT-Researcher仅0.039），**0.339 citation precision**（vs. 0.290），**99次专家引用命中**（vs. 72），报告质量**RACE评分7.82/10**（vs. 5.24）。
