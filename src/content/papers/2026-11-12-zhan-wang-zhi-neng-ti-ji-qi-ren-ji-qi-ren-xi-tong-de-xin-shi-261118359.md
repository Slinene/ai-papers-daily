---
title: 'Envisioning Agentic Robotics: A New Era of Robotic Systems'
title_zh: 展望智能体机器人：机器人系统的新时代
authors:
- Grid Robotics
- Qingfeng Lan
- Duo Li
- Siyao Li
- Yiheng Lyu
- Shijian Lu
- Zhenghao Qi
- Shizun Wang
- Xinchao Wang
- Ming Yang
affiliations:
- Grid Robotics
arxiv_id: '2611.18359'
url: https://arxiv.org/abs/2611.18359
pdf_url: https://arxiv.org/pdf/2611.18359
published: '2026-11-12'
collected: '2026-11-16'
category: Agent
direction: 具身智能体 · 评估与自主性路线图
tags:
- Agentic Robotics
- Embodied System 2
- Evaluation Framework
- Autonomy Levels
- Foundation Models
- Closed-loop
one_liner: 提出 Embodied System 2 概念与评估框架，规划从单步技能到持续角色的具身智能体路线图
practical_value: '- 借鉴 Embodied System 2 的闭环架构：将电商推荐/广告 Agent 拆成「感知环境→理解用户意图→推理策略→调用技能/工具→验证效果→调整策略」的
  pipeline，每次推荐或投放后增加效果校验与策略回滚，避免端到端黑盒失控。

  - 用 L1–L4 责任分级评估业务 Agent 的自主程度：L1 单步操作（如选词/改出价）、L2 完整任务（如生成一组广告文案）、L3 工作流（如跨渠道 campaign
  调度）、L4 角色（如长期托管选品库存），可按分级逐步放开权限并设置安全边界。

  - 论文强调物理动作的不可逆后果与实时约束，对应广告竞价、价格修改、库存扣减等高风险动作：在 Agent 执行前加入本地检查、预算/频控校验、人工审批等 harness
  层 safety checks，降低误操作影响。

  - 评估框架区分模型能力与闭环系统性能：业务中也要分开评测 LLM 单元能力（意图识别、策略生成）和整个推荐/广告 Agent 的长期业务指标（GMV、ROI、留存），避免只刷公开榜而忽略系统级收益。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：GPT-6 Astra 发布后，前沿模型配合 agentic harness 在多个实体基准上追平或超过任务专用策略，但社区对 agentic robotics 仍缺乏统一定义、可靠评估框架和研究路线图。

**方法关键点**：论文提出 Embodied System 2 作为 agentic robotics 的决策核心，由基础模型与 embodied harness 共同构成；其核心挑战是在有限反应时间、机械限制、不可预测环境变化和不可逆后果下，将通用推理转化为可验证的物理动作。为此，提出评估框架同时测量模型能力与闭环系统性能，识别从数字 Agent 迁移到物理 Agent 的原则与挑战，并规划 L1–L4 持续自主路线图：L1 原语（秒级）、L2 任务（分钟级）、L3 工作流（小时级）、L4 角色（持续责任）。

**关键结果数字**：本文为立场/路线图论文，无实验数据；核心贡献是概念框架、评估维度与自主性分级。
