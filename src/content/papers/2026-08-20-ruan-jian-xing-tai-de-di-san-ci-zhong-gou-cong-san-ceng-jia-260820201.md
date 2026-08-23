---
title: 'The Third Restructuring of Software Form: From the Three-Tier Architecture
  to Storage, Models, and Agents'
title_zh: 软件形态的第三次重构：从三层架构到存储、模型与智能体
authors:
- Wei Lin
- Tao Zhou
- Zhaofei Xie
- Changgui Hong
affiliations:
- Nanjing Liancheng Intelligent Technology Group, Nanjing, China
arxiv_id: '2608.20201'
url: https://arxiv.org/abs/2608.20201
pdf_url: https://arxiv.org/pdf/2608.20201
published: '2026-08-20'
collected: '2026-08-23'
category: Agent
direction: LLM + Agent 软件架构收敛
tags:
- Software 3.0
- LLM OS
- Agentic Computing
- Generalized Database
- Software Architecture
one_liner: 提出 Software 3.0 收敛为广义数据库、大模型与 Agent 三要素，按可表达性与关键性重划业务逻辑层
practical_value: '- 借鉴“可表达性×关键性”划分业务逻辑：在搜索/推荐系统中，将 query 理解、解释生成、对话式交互等可表达且非关键环节交给
  LLM+Agent，而排序打分、计费、风控等确定性高、关键性强的逻辑保留为工具或存储约束，实现渐进式迁移。

  - 参考“广义数据库”统一状态与记忆：构建有状态的推荐 Agent 时，可将特征存储、用户会话记忆、商品知识图谱、上下文等整合为统一存储抽象，由 Agent 读写维护，提升跨轮次一致性和个性化。

  - 应用其边界分析框架：在引入 LLM 前，评估任务域是否满足可表达、可验证、有外部状态、工具完备；对确定性、成本、安全、可验证性风险量化，避免在关键链路盲目替换。

  - 最小参考架构可作为电商推荐系统后端演进蓝图：UI 由模型按需生成，减少定制化前端；业务逻辑按上述原则分割，数据层作为唯一持久层，逐步向“存储+模型+Agent”形态收敛。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：软件形态已历经指令决定行为（Software 1.0）与数据决定行为（Software 2.0）两次转变，大语言模型大幅降低自然语言到可执行行为的表达成本，引发第三次重构——Software 3.0，其中上下文与推理决定行为。

方法关键点：论文论证 Software 3.0 终态收敛为三要素：广义数据库（统一所有持久状态与记忆）、大模型（推理与生成核心）、Agent（连接前两者的执行循环）。传统三层架构发生重组：UI 层被模型按需生成界面吸收；业务逻辑层按“可表达性×关键性”重新划分——可表达且非关键的部分由模型推理承担，强确定性部分表现为存储约束，残余确定性逻辑保留为工具；数据层成为唯一持久基础设施。论文给出最小参考架构，并界定适用条件：任务域需可表达、可验证、有外部状态、工具完备；失效边界包括确定性、成本、安全与可验证性。

关键结果数字：论文报告了真实原型与线上模型的证据，但未提供具体量化指标；核心贡献在于架构收敛论点与边界分析，并预判将重塑开发者角色、数据库行业及软件工程学科。
