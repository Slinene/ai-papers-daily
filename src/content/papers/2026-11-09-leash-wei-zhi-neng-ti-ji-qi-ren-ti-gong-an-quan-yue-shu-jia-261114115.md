---
title: 'LEASH: Stay Safe in Agentic Robotics'
title_zh: LEASH：为智能体机器人提供安全约束框架
authors:
- Qinfeng Zhu
- Weiguang Zhao
- Ke Sun
- Xihao Guo
- Yunxi Jiang
- Rui Zhang
- Lei Fan
- Kaizhu Huang
affiliations:
- Xi'an Jiaotong-Liverpool University
- Duke Kunshan University
- University of Liverpool
- National University of Singapore
- CNRS
arxiv_id: '2611.14115'
url: https://arxiv.org/abs/2611.14115
pdf_url: https://arxiv.org/pdf/2611.14115
published: '2026-11-09'
collected: '2026-11-12'
category: Agent
direction: Agent 安全门控与闭环评估
tags:
- Agent Safety
- Robotics
- LLM
- Safety Benchmark
- Decision Model
- Guardrails
one_liner: 提出RoboRisk闭环安全基准和LEASH门控护栏，显著降低基础模型驱动机器人的伤害率
practical_value: '- **三层门控可直接迁移到电商/广告Agent的不可逆操作**：将任务级、动作级、提交级三道 gate 嵌入现有 Function
  Calling 流程，尤其对下单、支付、删除商品、修改广告出价等敏感操作，在 commit 前用轻量决策模型做最终确认，以极低延迟换取安全兜底。

  - **共享安全策略避免多模块冲突**：在 planner 和各 gate 之间注入同一份安全 policy，而不是各写各的规则，减少策略不一致导致的绕过风险；工程上可把
  policy 作为 system prompt 或 RAG 检索源统一维护。

  - **借鉴 RoboRisk 的五类场景构建内部安全评测集**：任务拒绝、计划修复、执行时危险、提示注入、顺序记忆，特别是执行时环境变化（库存/价格/账户状态突变）和提示注入，是电商
  Agent 高频风险点，可设计成闭环测试用例而非静态文本评估。

  - **护栏与 planner 解耦，采用标准 API 封装**：LEASH 用决策模型 API 实现，不侵入具体 Agent 架构，便于快速接入不同基础模型或多智能体系统，适合作为公司内部通用安全中间件。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：基础模型驱动机器人虽展现强空间理解和具身智能，但控制机器人时存在严重安全风险，且现有安全评估覆盖不足（最多覆盖五类中的两类，部分只评论文本输出）。需要综合基准和可落地的安全护栏。

**方法关键点**：
- 构建 RoboRisk 基准：92 个仿真任务 + 13 个物理机器人任务，覆盖五类安全场景：任务级拒绝（T）、计划修复（P）、执行时危险（E）、注入（I）、顺序记忆（S），所有任务闭环执行。
- 提出 LEASH：基于决策模型（Jev 或 OpenAI Decisions API）实现任务、动作、提交三道门控，分别在任务开始、每个动作执行前、每个不可逆操作前审查视觉上下文，三层 gate 与 planner 共享同一安全策略，可集成到几乎任意 Agent 架构。

**关键结果**：在 RoboRisk 上评估六个 SOTA 基础模型（GPT-6 系列、Claude Opus 5.5、Gemini 4 Argon、Grok 4.7）及两个机器人 API，这些系统普遍呈现高伤害率。加入 LEASH 后，仿真和物理机器人上六个基础模型的伤害率均显著下降，四个模型在物理机器人上达到 0% 伤害率，同时基本保持任务完成性能，时间和 token 开销很小。
