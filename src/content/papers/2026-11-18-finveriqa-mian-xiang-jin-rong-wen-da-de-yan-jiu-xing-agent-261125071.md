---
title: 'FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval,
  MCP Tool Use, and Provenance-Aware Evidence Verification'
title_zh: FinVeriQA：面向金融问答的研究型 Agent：路由、检索、MCP 工具使用与溯源证据验证
authors:
- Meenakshi Rajpurohit
- Anna Phan
- Ravikumar Komandur Narayanan
- Gunanidhi Ramakrishnan
- Nathan Howland
affiliations:
- San José State University
arxiv_id: '2611.25071'
url: https://arxiv.org/abs/2611.25071
pdf_url: https://arxiv.org/pdf/2611.25071
published: '2026-11-18'
collected: '2026-11-20'
category: MultiAgent
direction: 多 Agent 金融问答与溯源验证
tags:
- Agent
- LLM
- RAG
- MCP
- Verification
- Financial QA
one_liner: 金融 QA 多 Agent：小模型路由、Python 计算、检索与 MCP 工具取数，溯源验证须独立于共享证据
practical_value: '- 路由不要压在大模型上：用小型 typed-decision 模型做工具选择/意图分类/拒答拦截，可显著提升准确率并降低延迟；在电商导购、客服
  Agent 中可独立训练一个轻量路由模型，只输出结构化决策。

  - 所有数值计算交给 Python/工具，LLM 只负责文案与引用。价格、折扣、优惠券、KPI 等绝不能由 LLM 直接算，这是从 29% 到 100% 的确定性提升。

  - 验证必须独立于生成时所用的共享证据。不能只检查“引用的 ID 是否存在、数字是否与检索到的片段一致”，还要回原始数据源或实体维度做 provenance-aware
  比对，否则会漏掉实体错配（例如把 A 商品数据写成 B 商品）。

  - MCP 统一封装检索、工具、验证等能力，适合多业务线复用；实时行情、库存、价格等变化数据应通过工具获取，LLM 只消费工具结果。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM 写金融分析流畅，但会算错比率、使用旧价格、高置信度选错工具。需要明确在金融问答 Agent 中，每个组件该承担什么任务。

方法：FinVeriQA 开源多 Agent 原型：紧凑的 typed-decision 模型 Laya 负责问题路由和拦截投资建议；所有数值由 Python 计算；检索和工具抓取 SEC 文件与实时行情；Mistral-7B 撰写带引用答案；代码验证器检查引用 ID 是否存在、数字与计算笔记一致；MCP server 暴露流程。

结果：Laya 路由显著优于 Mistral-7B（0.85 vs 0.52；总体 0.86 vs 0.68，p=0.0003）；12B Mistral 无提升，DeepSeek-R1-8B 更好但慢 9.9 倍。Mistral-7B 在 100 个金融计算中仅对 29%，Python 为 100%；实时报价错误从 210% 降到 0.00%；混合检索 Hit@5 达 76%。但仍有验证通过的答案把 AMD 数据写成 NVIDIA/Alphabet。对照实验表明：共享证据被污染时，自洽性仍保持自信，共享证据检查只捕获 35% 错误，回原始文本核对捕获 77%（p=5.96e-8）。验证必须独立于生成时作者所见的证据。
