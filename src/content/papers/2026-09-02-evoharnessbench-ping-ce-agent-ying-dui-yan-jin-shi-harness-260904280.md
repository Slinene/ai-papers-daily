---
title: 'EVOHARNESSBENCH: Can Your Agents Keep Pace with an Evolving Harness?'
title_zh: EVOHARNESSBENCH：评测 Agent 应对演进式 Harness 的基准
authors:
- Zixuan Ke
- Vaidehi Patil
- Haizhou Shi
- Yang Li
- Ye Liu
- Sarath Shekkizhar
- Anurag Koul
- Jiayu Wang
- Xuan Phi Nguyen
- Semih Yavuz
affiliations:
- Salesforce AI Research
arxiv_id: '2609.04280'
url: https://arxiv.org/abs/2609.04280
pdf_url: https://arxiv.org/pdf/2609.04280
published: '2026-09-02'
collected: '2026-09-10'
category: Eval
direction: Agent 评测基准 · Harness 演化
tags:
- LLM Agents
- Harness Evolution
- Continual Learning
- Benchmark
- Forgetting
- Self-evolving
one_liner: 首个将非平稳性置于外部 Harness 的 Agent 评测基准，揭示工具/技能/智能体扩充带来的遗忘与适应冲突。
practical_value: '- 在电商 Agent 系统中新增工具、技能或子 Agent 时，必须配套回归评测：将旧任务集作为固定验证集，持续监控新版本上线是否导致旧能力退化（harness-induced
  forgetting）。

  - 工具/技能库应按版本管理，支持回滚；新增能力时优先采用可插拔、模块化设计，避免全局改写路由或提示导致旧行为被覆盖。

  - 自演化经验回放并非总能提升适应能力，尤其在工具/技能高速迭代时；可考虑按能力轴隔离经验池，或对历史经验做衰减加权，而不是简单均匀回放。

  - 业务中“保留旧能力”与“快速适应新能力”可能冲突：部署评估（只测旧任务）和适应评估（只测新任务）需同时报告，不能仅看总体分数。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent 的能力高度依赖外部 Harness（工具、可复用技能、专家 Agent），而生产环境中 Harness 持续演进，如新增工具或技能。现有 Agent 持续学习基准把非平稳性放在任务流上、Harness 固定，无法刻画真实部署中 Harness 扩充带来的影响。

**方法关键点**：提出 EVOHARNESSBENCH，将非平稳性置于外部 Harness 本身，沿三个轴（tools、skills、agents）构建 17 条多阶段 Harness 流，包含 802 个任务、520 个工具、42 个技能、62 个 Agent。设置两种互补评估：部署评估（deployment evaluation）隔离 Harness 扩张对旧任务保持能力的影响；自演化适应评估（self-evolving adaptation evaluation）检验历史经验在新能力引入后是否仍然有用。

**关键结果数字**：1）Harness 单纯扩张即可导致旧任务性能下降，出现 harness-induced forgetting；2）自演化适应带来的增益在不同演化阶段、能力轴和环境间高度不一致；3）保留旧能力与适应新能力可能相互拉扯，保留得好不代表适应得好，反之亦然。
