---
title: 'EvoOntology: A Self-Evolving Ontology Layer for Data Agents'
title_zh: EvoOntology：面向数据 Agent 的自进化本体层
authors:
- Meiduo Chong
- Shaolei Zhang
- Ju Fan
- Xiaoyong Du
affiliations:
- Renmin University of China
arxiv_id: '2609.15779'
url: https://arxiv.org/abs/2609.15779
pdf_url: https://arxiv.org/pdf/2609.15779
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: 数据 Agent 自进化本体语义层
tags:
- Data Agent
- Ontology
- MCP
- Self-Evolution
- LLM
- Semantic Layer
one_liner: 将本体封装为 MCP 三层服务，通过自进化循环持续优化，显著弥合数据 Agent 与异构数据间的理解鸿沟
practical_value: '- **用 MCP server 而不是 prompt 注入语义层**：把商品表结构、字段含义、口径说明拆成 schema/content/tool
  三层，Agent 按需查询，避免 prompt 过长和上下文浪费，适合电商多数据源场景。

  - **自动构建 + 自进化代替人工维护 ontology**：用 builder agent 从已有查询日志和表结构自动生成本体，再通过 attribution-guided
  typed edits 持续修正字段语义，可迁移到广告投放数据、用户行为日志等语义层的自动化维护。

  - **backbone-conditional paired evaluation 保证编辑质量**：只有在新 LLM backbone 上同时评估新旧本体且新本体胜出才接受编辑，避免单个模型偏好导致的退化，适合多模型混合部署的推荐系统语义层场景。

  - **把专家知识变成 Agent 可调用的工具而非一次性文档**：将规则、口径、映射关系封装为 tool layer，让 Agent 在运行时主动查询，对多业务线知识管理有直接复用价值。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：数据 Agent 需要理解并操作表、文件、数据库等异构数据，但原始数据在外部，Agent 只能通过通用工具访问列名、路径等浅层信息，形成 agent-data gap。直接探索原始数据成本高，手动注入语义层又难以扩展到大规模数据源，且不能适应不同 Agent 的行为差异。

**方法**：提出 EvoOntology，将本体封装为 MCP server，包含 schema 层（结构元数据）、content 层（值域与业务含义）和 tool 层（可操作工具），让 Agent 在运行时按需查询。先用 builder agent 从数据源自动构建本体；再通过自进化循环，基于 attribution-guided typed edits 生成候选编辑，并用 backbone-conditional paired evaluation 在相同 LLM backbone 上比较新旧本体，只有新本体胜出才接受编辑。

**结果**：在三个主流数据 Agent benchmark 和四种 LLM backbone 上，EvoOntology 一致优于强基线与现有语义层方法，证实其能有效弥合 agent-data gap，提升异构数据上的任务完成效果。
