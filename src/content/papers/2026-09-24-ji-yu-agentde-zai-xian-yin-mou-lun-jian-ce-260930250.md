---
title: Agentic Detection of Online Conspiracies
title_zh: 基于Agent的在线阴谋论检测
authors:
- Lior Biton
- Oren Tsur
affiliations:
- Department of Computer and Information Science, Ben-Gurion University of the Negev,
  Israel
arxiv_id: '2609.30250'
url: https://arxiv.org/abs/2609.30250
pdf_url: https://arxiv.org/pdf/2609.30250
published: '2026-09-24'
collected: '2026-09-26'
category: Agent
direction: Agent结合社交上下文的意图推断
tags:
- Agentic Framework
- Social Context
- Conspiracy Detection
- Tool Use
- Illocutionary Force
- Social Media
one_liner: 提出Agentic框架按需查询社交上下文，在希伯来推文阴谋论检测中显著优于纯文本和非Agentic上下文模型
practical_value: '- 在内容安全/评论审核场景，纯文本分类难以识别反讽、阴阳怪气、隐晦攻击；可引入用户历史行为、商品上下文等作为额外信号，构建工具化上下文查询，让Agent按需取用。

  - 架构上不要一次性把所有上下文塞进prompt（token爆炸且干扰推理），而是设计轻量检索工具+逐步推理，每次只拉取与当前判断最相关的证据；论文的token
  economy分析可指导生产中的成本控制。

  - 该工作显示Agentic工作流优于非Agentic但暴露相同上下文的模型，说明动态控制上下文获取过程本身有价值，可用于电商用户意图识别、评论情感分类等需要意图推断的任务。

  - 工程落地可设置max tool calls、缓存高频查询或预计算用户/商品侧索引，平衡效果与推理开销。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：社交媒体阴谋论表述常无明确词汇标记，同一表面文本可能表达支持、担忧、批评、讽刺或嘲讽。核心挑战不仅是识别阴谋相关言论，而是推断说话者意图（illocutionary force）。

**方法**：提出Agentic框架，配备支持社交查询的工具。模型不再是纯文本分类，而是可根据需要查询相关社会上下文（如用户历史、社群互动），并按需调用工具、逐步推理。在希伯来推特数据集上评估，该数据集覆盖2018末至2023初80%-90%的公共希伯来推文，包含多次选举、COVID疫情和疫苗相关讨论。对比包括纯文本分类、非Agentic但能访问相同上下文的模型等设置。

**关键结果**：上下文感知工作流一致优于纯文本分类；Agentic框架显著优于其他框架和设置，包括暴露相同上下文的非Agentic模型。分析显示，性能提升来自自适应推理：Agent按个案使用工具，仅查询当前推理步骤所需的证据，而非一次性输入所有上下文。同时论文分析了错误模式与效率（token economy）权衡，证明动态上下文检索能以可控开销换取分类效果提升。
