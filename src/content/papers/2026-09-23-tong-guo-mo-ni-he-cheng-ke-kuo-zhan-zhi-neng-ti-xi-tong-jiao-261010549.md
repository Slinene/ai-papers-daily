---
title: 'Synthesis Through Simulation: Generating Coherent Enterprise Data via Scalable
  Agent-System Interaction'
title_zh: 通过模拟合成：可扩展智能体-系统交互生成一致企业数据
authors:
- Yipeng Li
- Ashutosh Hathidara
- Jane Lo
- Harshavardhan Abichandani
- Gunraj Singh
- Atin Ghosh
affiliations:
- SAP Labs
arxiv_id: '2610.10549'
url: https://arxiv.org/abs/2610.10549
pdf_url: https://arxiv.org/pdf/2610.10549
published: '2026-09-23'
collected: '2026-10-10'
category: Training
direction: Agent 训练数据合成 · 模拟环境交互
tags:
- synthetic data
- tool-calling agents
- simulation
- LLM
- enterprise data
- data synthesis
one_liner: 提出 schema-free 模拟数据合成范式，LLM agent 通过 policy-enforcing APIs 生成结构有效且高保真企业数据
practical_value: '- 在电商/客服 Agent 训练数据构造中，可部署 policy-enforcing API 模拟器定义合法状态，让 LLM
  通过交互生成轨迹，天然保证结构有效性，避免大量人工标注与无效状态。

  - schema-free 生成降低接入成本：不必提供完整数据库 schema，适合多业务线快速复用，尤其适合推荐解释生成、搜索 Query 改写等工具调用 Agent
  的训练数据生产。

  - 将约束验证与分布建模解耦：业务侧可独立优化分布保真，不必改动环境约束；模拟交互能生成长尾/边缘场景，弥补统计合成需种子数据的不足。

  - 采用通用 Populator 而非逐领域定制，单一 agent 适配多个 API 环境，可迁移到多域推荐系统，减少重复开发。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：企业 tool-calling agents 的训练与评估严重受限于真实系统数据难以获取，隐私、合规与 schema 限制使数据合成成为必要选择。但现有表格合成方法依赖 schema 和种子数据，过程导向方法又缺乏分布保真度且需领域定制。

**方法关键点**：提出 Synthesis Through Simulation (STS)，一种 schema-free 数据合成范式。LLM agent 在模拟企业环境中通过 policy-enforcing APIs 执行操作生成数据；环境本身定义合法状态，因此结构有效性由构造保证，并将有效性验证与分布建模解耦。Generalist Populator (GP) 作为领域无关 agent 负责分布保真与扩展性。

**关键结果**：在十个企业环境中，GP 达到 0.88 平均边际保真度和 100% 约束满足率，且无需访问数据库 schema；统计合成器在七个环境中因缺少种子数据不可用；拥有 schema 先验的 agent 在航空环境紧密耦合工作流中 82% 轨迹失败。框架、环境与数据集已开源。
