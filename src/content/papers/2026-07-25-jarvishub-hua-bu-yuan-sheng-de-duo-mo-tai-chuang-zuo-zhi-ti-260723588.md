---
title: 'JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents'
title_zh: JarvisHub：画布原生的多模态创作智能体开放框架
authors:
- Yunlong Lin
- Zixu Lin
- Zhaohu Xing
- Biqiang Li
- Chenxin Li
- Haonan Wang
- Haitao Wu
- Hengyu Liu
- Jianghai Chen
- Kaituo Feng
affiliations:
- JarvisX Team
arxiv_id: '2607.23588'
url: https://arxiv.org/abs/2607.23588
pdf_url: https://arxiv.org/pdf/2607.23588
published: '2026-07-25'
collected: '2026-07-28'
category: Other
direction: 多模态创作智能体架构
tags:
- Creative Agents
- Multimodal
- Canvas-Native
- Human-AI Collaboration
- Agent Harness
one_liner: 将可编辑画布作为智能体的记忆、动作空间与共享项目状态，支持长程多模态创作中的持续规划、生成、修订与人工干预。
practical_value: '- 本工作在电商/推荐领域直接应用价值有限，主要面向创意生产工具。

  - 可借鉴点：将「画布式可编辑状态」抽象用于推荐系统调试（如召回/排序策略的可视化编排与回溯），用节点和链接表示策略版本、AB 实验分支、指标反馈，便于 Agent
  辅助调试与人工介入。

  - 在 Agent 协作产品中，可参考三层架构（画布状态、协议桥、智能体运行时）将复杂任务状态显式化，提升可解释性与可控性，尤其适合需要多版本素材管理、人工共同决策的场景（如营销文案、商品图生成）。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有生成式 AI 工具多聚焦单次提示输出，忽略真实创作中持续演化的项目状态，包括参考素材、草案、版本、失败尝试、评价信号与人工反馈。聊天式或节点式界面无法有效保留上下文、支持非线性修订与长程协作。
**方法**：提出 JarvisHub，以**可编辑画布**作为创作智能体的工作空间、外部记忆、动作空间与共享项目状态。画布中的多模态素材、依赖关系、版本、反馈被建模为带类型的节点和链接。系统采用三层架构：画布状态层维护结构化项目状态，协议桥负责状态同步与动作传递，智能体运行时驱动规划、生成、修订等行为。用户可随时查看、引导、干预整个过程。
**结果**：论文为系统框架性工作，未报告量化指标，重点展示设计理念与架构开放性，旨在为长程多模态创作智能体研究提供可检查、可共享的实验平台。
