---
title: 'Beyond Context Windows: Persistent Discovery Context for Data-Centric Agents'
title_zh: 超越上下文窗口：面向数据中心的智能体的持久发现上下文
authors:
- Jalal Mahmud
affiliations:
- Megagon Labs
arxiv_id: '2609.02129'
url: https://arxiv.org/abs/2609.02129
pdf_url: https://arxiv.org/pdf/2609.02129
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: Agent 记忆增强检索
tags:
- Persistent Discovery Context
- Agent Memory
- Data Discovery
- Retrieval
- Structured Data
one_liner: 引入持久发现上下文记忆层，复用任务意图到数据对象的映射，提升后续检索质量
practical_value: '- 在电商搜索/推荐场景，可把历史成功 query→item/attribute 映射作为轻量记忆层，避免每次请求重复做语义解析与召回；尤其适合长尾
  query 或数据目录频繁变化的场景。

  - 元数据稀疏或缺失时，记忆检索可能优于元数据检索。对商品冷启动、长尾类目、非标品可尝试用历史交互记忆补充召回，而不是只依赖属性倒排。

  - 自动生成记忆有效，意味着无需人工维护映射表，可通过 LLM 自动抽取意图-对象对并写入记忆；工程上可低成本落地，与现有 RAG/检索流程叠加。

  - 注意可复现的干扰失败模式：记忆冲突或错误映射会降低效果。建议加入置信度阈值、来源标记、过期淘汰或按任务域隔离机制，避免脏记忆污染检索结果。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机

Data-centric agents 在规划或执行前都需要做 discovery：识别与任务相关的数据对象。但这些成功的 discovery 结果通常用完即弃。作者认为，成功映射任务意图到数据对象的结果应该被保留为可复用上下文，而不是每次重新检索。

## 方法关键点

提出 persistent discovery context：一个轻量记忆层，存储 intent→object 映射，并在未来检索时作为补充信号。该记忆可以来自人工记录，也可以自动生成。在三类结构化数据环境、125 个 held-out tasks 上验证。

## 关键结果

- 相比仅用元数据检索，加入持久发现上下文后检索质量一致提升。
- 自动生成的记忆同样有效，降低维护成本。
- 发现可复现的 interference failure mode：某些记忆会干扰检索，需要处理。
- 在词法稀疏领域，仅用记忆检索甚至可以超过元数据检索。
