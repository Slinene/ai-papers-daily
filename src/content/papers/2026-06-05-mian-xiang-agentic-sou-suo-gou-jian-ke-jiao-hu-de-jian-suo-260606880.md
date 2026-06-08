---
title: Towards Retrieving Interaction Spaces for Agentic Search
title_zh: 面向 Agentic 搜索构建可交互的检索工作区
authors:
- Shengyao Zhuang
- Yuansheng Ni
- Hengxin Fun
- Jimmy Lin
- Xueguang Ma
arxiv_id: '2606.06880'
url: https://arxiv.org/abs/2606.06880
pdf_url: https://arxiv.org/pdf/2606.06880
published: '2026-06-05'
collected: '2026-06-08'
category: Agent
direction: Agentic Search · 检索交互界面设计
tags:
- interaction space
- agentic search
- BM25
- retrieval interface
- DCI
one_liner: 将检索角色从片段选择重构为构建代理可通过 shell 工具探索的交互空间，显著降低 agentic 搜索成本并保持稳定性
practical_value: '- **工作区边界代替全量扫描**：用 BM25 多查询并集构建问题相关的文件工作区，代理只在该区内执行 grep/read，避免全库扫描，在
  1M 语料下精度稳定 (81%) 而纯 DCI 退化到 60%。可直接用于电商搜索代理的场景，如将商品召回列表作为可交互的文件系统，代理用 bash 类工具精细化筛选。

  - **离线目录索引降低阅读成本**：对文档生成行号目录，代理可跳转到相关段落，避免通读全文。这种轻量预处理（$0.0014/文档）可迁移到电商知识库或商品详情页，让
  Agent 快速定位关键信息。

  - **多查询并集提升召回**：代理一次性下发多个互补子查询，BM25 召回并集作为工作区，既提高覆盖又不增加代理上下文窗口负担。可用于电商长尾查询的意图分解与召回增强。

  - **明确的检索输出接口设计**：RISE 分离了工作区构建（检索）与验证（shell），可借鉴到生成式推荐的交互设计中，例如将召回物品集合作为 agent
  的“玩具沙盘”，供其跨会话操作，而非仅读片段。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
传统搜索代理的检索输出是固定片段列表，限制了代理对证据的重新探索；而直接语料交互 (DCI) 让代理通过 shell 工具操作全库，但随着语料增大，全库 grep 扫描导致延迟爆炸和精度下降。本文认为检索应构建一个**交互空间**——一个代理可以迭代探索的有界子集，其中文档经过预处理以支持导航。

**方法关键点**  
- **边界机制 (RISE-BM25)**：代理使用多查询 BM25 检索，每次取 top-K 文档并集作为工作区（文件系统），代理只能在该区内使用 bash/grep/read 工具。检索返回的文档被硬链接到工作目录，而非放入上下文。  
- **导航对象处理 (RISE)**：离线阶段，用小型 LLM 为每篇文档生成行号目录（TOC），通过精确锚点验证插入到原始文本前，代理可读取 TOC 定位段落，再用行范围读取验证事实，避免全文扫描。  
- **工具与预算**：search 工具返回 top-10 预览但所有 top-K 文档已可用，bash 输出截断到 4000 字符，子进程限时 60 秒；代理模型调用上限 100 次，墙钟上限 1 小时。

**关键实验**  
- **数据集**：BrowseComp-Plus（100 个混淆问题），100k 和 1M（添加 90 万 FineWeb-Edu 干扰）两种规模。  
- **对比基线**：纯 shell DCI、片段检索代理、RISE-BM25（无 TOC 处理的消融）。  
- **主要结果**：在 100k 语料上，RISE 用 gpt-5.4-mini 达到 78% 精度，成本 $0.28/查询，而 DCI 同样精度下成本为 $1.10/查询。扩展到 1M 时，RISE-BM25 精度上升至 81%（gpt-5.4-mini），DCI 降至 60% 且有 33/100 次因超时而失败。  
- **消融**：BM25 top-K 默认 1000 提供最佳精度–导航权衡，TOC 处理在 100k 上贡献 1–4 点精度提升。

**核心结论**  
代理搜索系统的检索输出应是一个边界可重复探索的工作区，而非排名片段。这一设计将语料交互重新定义为“检索返回什么以及如何结构化”的工程问题。
