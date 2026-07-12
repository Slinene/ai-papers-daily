---
title: 'The Context Access Divide: Interaction-Level Architecture as a Complementary
  Dimension of Agentic Inequality'
title_zh: 上下文访问鸿沟：交互级架构作为AI Agent不平等的补充维度
authors:
- Masahiro Fujita
affiliations:
- Kansai University
arxiv_id: '2607.08495'
url: https://arxiv.org/abs/2607.08495
pdf_url: https://arxiv.org/pdf/2607.08495
published: '2026-07-09'
collected: '2026-07-12'
category: Agent
direction: Agent 交互架构与知识访问不平等
tags:
- Agentic Inequality
- Context Access Divide
- RAG
- MCP
- cognitive load
- knowledge workers
one_liner: 提出“上下文访问鸿沟”概念，揭示动态检索与手动附加上下文在知识工作中的任务成功概率差异
practical_value: '- **设计知识密集型Agent时，优先采用动态上下文检索（RAG）架构**，避免让用户手动选择并附加文档，降低认知负担，防止任务成功率随知识库规模扩大而崩溃。

  - **在电商运营、广告创意等需要处理大量多源文档的场景中，集成MCP（Model Context Protocol）**，让Agent自主从用户知识库中检索相关上下文，提升任务完成效率。

  - **在Agent产品需求定义阶段，量化评估上下文访问模式的影响**，参考论文中“语料规模×任务接合性”的风险公式，为不同用户规模设计合适的检索粒度与上下文窗口。

  - **警惕“手动上下文依赖”造成的隐形能力分层**，在平台治理时监控用户实际上下文集成方式，避免因架构差异导致部分用户AI效用显著受损，形成新的数字鸿沟。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有Agent不平等研究关注可用性、质量、数量等个人/组织层面的维度，忽略交互层面的架构差异。知识工作者日常处理数万份文件，若AI系统每次都需要用户手动附加相关文档，认知负担将严重降低任务成功率，形成“上下文访问鸿沟（CAD）”，这加剧了知识工作的阶层分化。

**方法关键点**：
- 引入“上下文性”概念，指AI系统自主访问用户知识资本的程度，作为补充Agent不平等的分析维度。
- 借鉴认知心理学中的“扇效应”，构建概率模型：手动附加下，任务成功概率随语料库规模$N$和任务接合因子$k$指数下降$P \propto (1/N)^k$；动态检索架构（如RAG、MCP）则结构性避免这种组合崩溃。

**关键结果**：
- 形式化证明动态检索较手动附加在知识密集型任务中的结构性优势，尤其当$N>10^4$, $k>2$时，手动模式几乎必然失败。
- 指出MCP等协议从架构层面实现了自主上下文访问，但部署差异可能造成新的不平等，需在AI平台治理中纳入交互层架构的考量。
