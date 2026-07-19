---
title: 'The Energy Society: A Simulation Environment for Studying Agent Cooperation
  under Survival Pressure'
title_zh: 能源社会：在生存压力下研究LLM智能体合作的模拟环境
authors:
- Lucas Bergholdt Hansen
- Federico Torrielli
- Filippo Tonini
- Lukas Galke Poech
affiliations:
- University of Southern Denmark
- University of Turin
arxiv_id: '2607.14865'
url: https://arxiv.org/abs/2607.14865
pdf_url: https://arxiv.org/pdf/2607.14865
published: '2026-07-16'
collected: '2026-07-19'
category: MultiAgent
direction: 多智能体生存压力下的合作与竞争模拟
tags:
- Multi-Agent Systems
- LLM Agents
- Emergent Behavior
- Simulation
- Resource Constraints
- Cooperation
one_liner: 构建极小生存经济模拟环境，揭示推理成本与模型规模挂钩时合作激励如何改变多智能体行为
practical_value: '- 可借鉴''能量消耗与模型规模挂钩''的成本约束设计，用于多Agent推荐系统中的资源分配和预算控制。

  - 允许Agent间相互推荐行动（行动建议）能促进协调和任务选择，可应用于分布式推荐Agent的协作机制。

  - 记忆模块帮助Agent从历史结果校准风险，可复用到Agent的长期记忆设计，提升决策稳健性。

  - 合作激励（如能量捐赠）改变行为模式，可启发在广告竞价或搜索Agent中设计激励对齐策略，避免纯粹自利导致的系统崩溃。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：多智能体环境中激励设计如何影响基于LLM的智能体的行为？尤其当推理成本直接与模型规模关联，且生存依赖于能量时，竞争与合作会导致怎样的涌现行为？

**方法关键点**：设计「能源社会」最小化生存经济——智能体每生成一个token消耗与模型大小成比例的能量，通过完成工作获得能量，也可相互捐赠，能量归零则失活。设置基线（无特殊激励）、竞争（最大化个人生存）和合作（最大化群体生存）三种目标，以及移除成本、移除记忆、移除行动建议等消融变体。所有智能体基于LLM（如GPT-4o-mini）与环境交互。

**关键结果**：大模型在所有设置中消耗最多能量且净能量为负，即使token成本不与模型大小挂钩时亦然；合作激励下智能体主动捐赠能量复活他人，有时牺牲自身生存，任务分配更均衡；消融显示，允许相互推荐行动促进了协调和风险任务选择，记忆帮助智能体从过去结果校准风险；竞争环境中几乎无直接破坏行为，但存在微妙的自我服务倾向。
