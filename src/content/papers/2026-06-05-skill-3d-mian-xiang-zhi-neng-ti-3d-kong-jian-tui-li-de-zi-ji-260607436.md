---
title: 'Skill-3D: Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning'
title_zh: Skill-3D：面向智能体 3D 空间推理的自进化场景感知技能框架
authors:
- Haoyuan Li
- Zhengdong Hu
- Jun Wang
- Hehe Fan
- Yi Yang
affiliations:
- Zhejiang University
- University of Technology Sydney
- OPPO Research Institute
arxiv_id: '2606.07436'
url: https://arxiv.org/abs/2606.07436
pdf_url: https://arxiv.org/pdf/2606.07436
published: '2026-06-05'
collected: '2026-06-08'
category: Agent
direction: 多模态 Agent · 场景感知工具使用
tags:
- 3D Spatial Reasoning
- MLLM Agents
- Tool Use
- Self-Evolving Skills
- Scene-Aware
one_liner: 通过场景记忆记录工具轨迹并蒸馏为可复用技能，配合失败教训，实现代理工具使用的自进化场景感知，大幅提升 3D 空间推理中工具利用率与任务成功率。
practical_value: '- **场景感知的技能复用**：在电商推荐或客服 Agent 中，可根据用户意图或商品类别动态选择调用不同的工具/模型（如价格比较、商品属性查询、3D
  试穿引擎），将相似场景的成功交互轨迹蒸馏为预置技能，避免每次都从零规划，减少工具误用。

  - **失败教训注入**：在 Agent 记忆模块中不仅存储成功案例，还附加失败尝试的教训总结，当相似场景再现时一并注入提示，可有效降低重复错误。例如在导购对话中，对无效推荐策略自动标注并修正。

  - **闭环自进化机制**：技能库与记忆协同更新的循环，可借鉴到线上 Agent 的持续学习中，通过真实交互数据不断优化工具调用策略，但需注意安全防护和人工审核。

  - **多任务异构适配**：直接启示是避免对多场景使用统一固定流程，应根据场景特征分而治之。在 3D 商品展示、AR 试穿等应用中，可根据商品类别（鞋、家具）自动选择测量或渲染工具，提升效率。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有 MLLM 代理在 3D 空间推理中常误用工具，且无视场景差异一律采用统一工具策略，导致代理范式收益甚微。作者揭示不同 3D 场景任务高度异构，需要场景感知的差异化工具选择。

**方法**：提出 Skill-3D 框架，核心是构建自进化的场景感知技能库。具体包括：
- 识别任务场景，将代理的工具调用轨迹记入 Scene Memory；
- 对来自相似场景的成功轨迹进行聚合蒸馏，形成可复用的场景感知技能；失败轨迹则作为教训附加到技能上；
- 当类似场景再次出现时，检索并注入对应技能，引导代理生成新轨迹，随后用新轨迹的成功/失败进一步精炼技能，形成记忆与技能库协同进化的闭环。
此外，利用技能引导的轨迹对基础模型实施代理后训练，从模型侧增强工具使用能力。

**关键结果**：
- 在 VSI-Bench 上，工具利用率从 39% 提升至 78%，代理工具调用更正确、充分；
- 在 MMSI-Bench 上，Gemini-3-Flash 提升 67%；
- 代理后训练使 Qwen3-VL-8B 在 VSI-Bench 上提升 43%。
