---
title: 'ORCH: Organizational Principles Enable Collective Intelligence in Embodied
  AI'
title_zh: ORCH：用组织原则实现具身AI集体智能
authors:
- Zhengran Ji
- Jonathan Hyun
- Boyuan Chen
affiliations:
- Duke University, Department of Computer Science
- Duke University, Department of Electrical and Computer Engineering
- Duke University, Department of Mechanical Engineering and Materials Science
arxiv_id: '2609.11737'
url: https://arxiv.org/abs/2609.11737
pdf_url: https://arxiv.org/pdf/2609.11737
published: '2026-09-10'
collected: '2026-09-11'
category: MultiAgent
direction: 多智能体组织设计 · 层级协作
tags:
- Multi-Agent Systems
- LLM
- Hierarchical Organization
- Embodied AI
- Collective Intelligence
- Task Planning
one_liner: ORCH 将人类组织理论中的角色与层级协调引入具身多智能体，在50个异构智能体、25个野火任务上大幅超越四种基线框架
practical_value: '- 在多 Agent 搜索/推荐 pipeline 中不要写死固定顺序；借鉴 ORCH 的 pooled + sequential
  组合：多路召回、不同品类/人群画像等可并行子任务放入 pooled 组并发执行，召回→粗排→精排等有前置依赖的环节用 sequential 层级协调，降低整体时延。

  - 用 LLM 自动生成任务特定的角色与层级，而不是手动设计固定多 Agent 拓扑；在复杂 query 或多目标广告投放中，可由 Planner 先分析意图与依赖关系，动态生成临时“角色-协调层级”，再分派给子
  Agent。

  - 层级组织适合长程任务：按“专门小组”封装并行子任务（选品、文案生成、关键词扩展、出价调整），用 coordinator 做阶段门控，在保持组内并发的同时控制阶段间有序切换，避免全局混乱。

  - 性能不随 LLM 规模单调提升：工程上不必盲目上最大模型，可为不同子 Agent 分配不同规模模型，通过组织设计补偿个体能力，降低 token 成本与推理延迟。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有多智能体系统大多采用固定组织结构，但物理任务对协调方式的要求差异很大，个体能力再强也未必形成高效集体。人类组织理论中的角色分工与层级协调尚未被系统引入具身多智能体。

**方法关键点**：ORCH 根据任务需求构建层级组织，将两种相互依赖模式结合：pooled interdependence 用于可并行推进的工作，sequential interdependence 用于有前置依赖的工作。在野火响应模拟中覆盖侦察、救援、运输、资源管理、遏制与扑灭六类子任务，最多 50 个异构智能体，使用 8 种 LLM 作为底层模型。组织可由人类设计，也可由 LLM 自动生成。

**关键结果**：在 25 个野火任务上，人类设计的 ORCH 组织相比四个代表性具身多智能体框架，最终得分平均提升 63.97%，执行效率提升 74.29%；LLM 自动生成的组织分别提升 43.63% 和 52.53%。优势跨任务与底层模型稳定存在。值得注意的是，集体性能并不随模型规模单调提升。长程任务分析显示，层级组织能保留专门小组内的并发活动，同时协调阶段间有序切换。
