---
title: Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter
  Data
title_zh: 工业智能电表数据的隐私保护自然语言访问
authors:
- Carlos Martín-Abellán
- Mark Kröll
affiliations:
- Valencian Research Institute for Artificial Intelligence (VRAIN), Universitat Politècnica
  de València
- Know Center Research GmbH
arxiv_id: '2611.09372'
url: https://arxiv.org/abs/2611.09372
pdf_url: https://arxiv.org/pdf/2611.09372
published: '2026-11-06'
collected: '2026-11-09'
category: MultiAgent
direction: 多智能体协同 Text-to-SQL 与隐私本地执行
tags:
- Multi-Agent Systems
- Text-to-SQL
- LLM Orchestration
- Privacy-Preserving
- Local LLM
one_liner: OpenMeter多智能体系统在隐私受限本地环境完成Text-to-SQL，全编排较最强单智能体EX-R提升6.1pp
practical_value: '- 面向企业内部敏感数据取数，可参考 OpenMeter 的多智能体 Text-to-SQL 编排：把 schema 发现、SQL
  生成、执行解释拆成独立 agent，在本地小模型上全编排增益最大（+6.1pp EX-R），不要因资源受限就退化为单 agent。

  - 对电商/广告多库多表且 schema 频繁变动的场景，可直接借鉴 schema-agnostic 设计：不把表结构写死在 prompt 里，而是让 agent
  动态发现和校验 schema，减少维护成本。

  - 前沿闭源大模型上不必默认全编排，可按查询复杂度或隐私要求选择性启用组件，用消融评估每个 agent 的增量价值，避免多智能体成本和延迟浪费。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：智能电表产生高频遥测数据，运营人员需要从异构数据库中提取异常、绩效和决策洞察，但写 SQL 门槛高；同时能源基础设施的隐私约束禁止把敏感用电数据发往云端 LLM。

**方法关键点**：OpenMeter 是一个 schema-agnostic 的多智能体系统，将自然语言查询转换为可执行代码和可读结论。架构中拆分多个 agent 组件，负责数据库 schema 发现、SQL 生成、执行与解释等环节，并通过编排在本地完成隐私安全的推理。评估使用多场景消融，对比单 agent 配置与不同子集编排，指标包含执行准确率 EX-R。

**关键结果**：在资源受限的本地硬件上，完整多智能体编排相比最强单智能体配置准确率提升 6.1 pp EX-R，说明隐私要求本地执行时全编排成本是值得的；在前沿规模模型上，各组件仍有效但应选择性启用，全编排收益不总是覆盖其开销。
