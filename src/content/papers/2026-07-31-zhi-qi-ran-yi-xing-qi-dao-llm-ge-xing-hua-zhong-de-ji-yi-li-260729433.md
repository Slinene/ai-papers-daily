---
title: 'Know It, Act on It: Investigating Memory Utilization in LLM Personalization'
title_zh: 知其然，亦行其道：LLM 个性化中的记忆利用研究
authors:
- Zhaoxin Feng
- Jianfei Ma
- Emmanuele Chersoni
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2607.29433'
url: https://arxiv.org/abs/2607.29433
pdf_url: https://arxiv.org/pdf/2607.29433
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 记忆利用评估
tags:
- memory utilization
- personalization
- Agent evaluation
- Know-Act gap
- LLM agents
one_liner: 解耦“知道”与“行动”的评估范式揭示：LLM agent 能记住用户偏好却常不据此行动，健康领域尤甚。
practical_value: '- 构建个性化推荐或客服 agent 时，应设置成对的 Know/Act 测试用例，分别验证偏好召回与行为应用，避免“记住但不用”的盲区。

  - 对高风险偏好（如过敏、健康约束）应提升测试密度与强度，并考虑在 prompt 或记忆检索后追加显式的“偏好-行动”一致性检查模块。

  - 记忆架构（如摘要、向量检索）能缩小 Know-Act 差距，但无法根除，需配合针对性微调或 RLHF 强化从记忆到行为的转化。

  - 工程上可将用户敏感属性标记为“强制遵循”类型，在推理阶段由策略层校验生成内容是否符合已知偏好，防止危险建议。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机：** LLM agent 正从无状态工具演变为长期个性化伴侣，记忆成为核心能力。但这类 agent 存在“知识利用”问题：即使用户偏好完全存在于上下文，agent 也可能不按此调整回应。现有评估难以区分是模型“忘记”还是“记而不用”，导致无法针对性优化。

**方法：** 提出解耦评估范式，为同一用户偏好设计成对的 Know 测试（直接回忆）和 Act 测试（在对话场景中自然应用）。实验覆盖 16 个系统、5 种记忆架构、1000 条偏好，并嵌入三种表达强度（显式陈述、隐式推断、混合）。

**关键结果：** Know 与 Act 之间存在显著缺口：agent 常能通过回忆测试，却在行为场景中不反映同一偏好。记忆架构可缩小缺口，但利用困难在健康/治疗类偏好上尤为突出——这类偏好恰是行动失败风险最高的领域。结果说明单纯增强存储与检索不足以保障个性化安全，必须专门强化从记忆到行为的转化。
