---
title: 'AutoPersonas: A Multi-Timescale Loop Engine for Open-Ended Persona Evolution'
title_zh: AutoPersonas：开放人物演化的多时间尺度循环引擎，缓解角色自我锁定
authors:
- Mengchen Li
affiliations:
- Latrix
arxiv_id: '2607.08252'
url: https://arxiv.org/abs/2607.08252
pdf_url: https://arxiv.org/pdf/2607.08252
published: '2026-07-09'
collected: '2026-07-11'
category: Agent
direction: Agent 多时间尺度演化 · 防行为锁定
tags:
- persona evolution
- self-locking
- OSO loop
- LLM agents
- context gravity
- divergence targeting
one_liner: 发现并缓解长期角色智能体的自我锁定行为——事件看似合理但生活坍缩，通过分离事件、观察与状态并引入发散目标减少重复
practical_value: '- **分离观察与状态更新**：在电商对话、客服或用户模拟Agent中，可借鉴OSO循环（Occurrences→Observations→State），要求新事件累积为“观察”并经证据验证后才写入状态，避免每一次交互都直接改变人格或偏好，防止行为漂移。

  - **廉价多样性干预**：使用上下文切片掩码（context-slice masking）和每样本发散目标（per-sample divergence targeting），在不修改模型本体的情况下降低回复或动作的主题重复率。对于推荐理由生成、多轮对话等场景，可低成本提升输出多样性。

  - **采用诊断审计而非基准刷分**：通过压缩仿真暴露“水印壳层”、“关系弱化”、“慢变量累积失败”等系统性问题，再针对性设计缓解方案。在推荐Agent长期运行评估中，这种审计思路比A/B测试更能发现隐蔽的坍缩模式。

  - **多时间尺度架构**：将环境事件、观测、状态分离在不同时间尺度上处理，可迁移到用户长期模拟器或生命周期推荐中，用于生成合理且非坍缩的用户行为序列，支撑更真实的仿真环境。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：长期生命化的LLM角色智能体在持续运行中会出现“自我锁定”——局部事件看起来合理，但整体生活坍缩到熟悉环境、弱关系、决策停滞、阶段停滞。根源在于模型倾向输出高概率行为通道（model-level convergence）与系统上下文引力（State、记忆、历史摘要积累导致的context gravity）。

**方法**：提出AutoPersonas多时间尺度循环引擎。关键设计是OSO循环：将环境事件（Occurrences）与累积观察（Observations）及角色状态（State）分离。未来导向的发散性材料可以进入循环，但必须经证据驱动的吸收（evidence-governed absorption）后，才允许改变状态或可达关系。实验干预包括上下文切片掩码和逐样本发散目标，以对抗主题重复。

**结果**：在8模型40天压力测试中，无干预时5天滚动动作类别重复率高达95.2%-97.6%，语义主题重复79.0%-88.0%。使用掩码+发散目标干预后，在同样40天运行中，宏主题重复从61.8%降至36.3%，累积主题数从55翻倍至102。压缩三年仿真与虚构世界运行均验证了系统能减少自我锁定的同时保持身份连续性。
