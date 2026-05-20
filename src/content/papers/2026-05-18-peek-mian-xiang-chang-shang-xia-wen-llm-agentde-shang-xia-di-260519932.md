---
title: 'PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents'
title_zh: PEEK：面向长上下文LLM Agent的上下文地图缓存
authors:
- Zhuohan Gu
- Qizheng Zhang
- Omar Khattab
- Samuel Madden
affiliations:
- MIT CSAIL
- Stanford University
arxiv_id: '2605.19932'
url: https://arxiv.org/abs/2605.19932
pdf_url: https://arxiv.org/pdf/2605.19932
published: '2026-05-18'
collected: '2026-05-20'
category: Agent
direction: Agent长上下文交互的上下文知识缓存与更新
tags:
- Context Map
- Orientation Cache
- LLM Agents
- Cache Policy
- Long Context
- Prompt Engineering
one_liner: 将可复用定向知识缓存为固定大小的上下文地图，显著提升Agent在重复长上下文任务上的准确率和效率。
practical_value: '- 在电商场景（如反复查询商品库、用户评论语料）中，可以维护一个轻量级上下文地图，存储语料结构、关键实体、常用常量等可复用知识，避免每次推理都从零探索。

  - Distiller从Agent执行轨迹中自动提取可迁移的上下文知识，而不引入任务特定噪声，这一思路可借鉴为Agent经验回放与知识累积模块。

  - Cartographer与Evictor的分离设计（结构化编辑+优先级驱逐）确保缓存紧凑且更新不产生重复/冲突，适合需要固定token预算的生产环境。

  - 即使只需极少轮次（m≤4）的缓存更新就能带来显著收益，这对成本敏感的在线推理系统极具参考价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent越来越多地反复查询大型外部上下文（如文档集、代码库），但现有上下文管理方法（共享聊天、RAG、压缩、提示学习等）或保留对话历史，或被动访问材料，或优化任务策略，无一主动维护**可复用的定向知识**——比如上下文包含什么、如何组织、哪些实体/常量曾有用。这导致每次新任务都要重新发现上下文结构，浪费推理轮次和成本。

### 方法
PEEK将这类定向知识封装为**上下文地图**：一个固定大小的系统提示片段，作为Agent对长上下文的“一瞥”缓存。
- **地图结构**：包含上下文路标、关键理解、域常量、可重用结果、解析模式等节，各条目有唯一ID。
- **缓存策略**：由三个模块组成——**Distiller** 从Agent执行轨迹中诊断定向信息的有效性并提取可迁移的上下文知识；**Cartographer** 将诊断结果转化为对地图的结构化编辑（ADD/DELETE/REPLACE），去重并最小化编辑集；**Evictor** 按累积分数和条目重要性实施优先级驱逐，确保不超token预算。
- 分离蒸馏与编辑是关键，否则任务特定信息会泄露、更新噪声大且易重复。

### 实验结果
在长上下文推理（OOLONG的三组 hardest splits）和上下文学习（CL-bench）上，以GPT-5-mini为基座，RLM为骨干Agent：
- **质量**：PEEK在所有基准上完胜所有基线，OOLONG提升6.3–34.0%，CL-bench解决率提升6.0–14.0%、Rubric准确率提升7.8–12.1%，比SOTA提示学习方法ACE提升7.8–15.0%（OOLONG）和6.0/9.9%（CL-bench）。
- **效率**：PEEK位于迭代–质量 Pareto前沿，在OOLONG上比ACE少93–145次迭代，成本低1.7–5.8倍。
- **泛化**：切换基座模型（GPT-5.5、Qwen3-Coder-Next-FP8）或换用Codex Agent，增益均保持。

### 核心洞察
一个固定、可演进的上下文地图能让Agent“记住”长期重复上下文的结构与关键知识，从而在后续任务中快速定位所需信息，大幅提升推理效率与质量。
