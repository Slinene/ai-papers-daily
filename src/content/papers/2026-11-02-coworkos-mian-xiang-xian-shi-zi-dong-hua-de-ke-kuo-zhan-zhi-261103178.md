---
title: CoworkOS:Scaling Agent Coworkers for Real-world Automation
title_zh: CoworkOS：面向现实自动化的可扩展智能体同事框架
authors:
- Jiajie Jin
- Guanting Dong
- Chengjun Pan
- Xin Deng
- Zhuohui Sheng
- Guoqiang Wang
- Tao Gui
- Yutao Zhu
- Yujia Chen
- Shihong Yi
affiliations:
- Renmin University of China
- Fudan University
arxiv_id: '2611.03178'
url: https://arxiv.org/abs/2611.03178
pdf_url: https://arxiv.org/pdf/2611.03178
published: '2026-11-02'
collected: '2026-11-03'
category: MultiAgent
direction: 通用 Agent 运行时与多智能体协作
tags:
- Agent Harness
- Multi-Agent
- Long-horizon
- Human-in-the-loop
- Persistent Memory
- RSI
one_liner: 提出三层架构（Main、Coordinator、Subagents）的通用长时程智能体运行时，支持人机共享工件与持久状态，多个基准上超越主流框架
practical_value: '- **职责分离与异步委派**：借鉴 Main-Agent 保留全局上下文、Subagents 隔离执行长任务，通过 Coordinator
  的 durable queue/inbox 实现同步/异步委派，避免长上下文爆炸；可用于搜索推荐多 Agent 系统中的深度调研、批量数据分析、实验监控。

  - **持久工作区与语义记忆**：用 memory.md、task.json、checkpoint 记录目标、决策和未完成任务，支持跨会话恢复和上下文重建；适合电商推荐中跨天
  AB 测试跟踪、策略迭代和模型训练监控。

  - **共享应用资源与版本控制**：人类和 Agent 通过 revision protocol 直接编辑同一 artifact（如 query 规则表、策略配置），冲突检测保证可审计；可用于人工修正搜索
  query 模板或推荐策略，让专家反馈直达工作产物。

  - **后台 Jobs 与监测机制**：长时间训练/构建作为持久 Job，保留日志和状态，模型空闲时可唤醒；可迁移到推荐模型训练流水线、特征工程任务的状态管理，减少重复启动成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：Agent 系统正从工作流走向持续人机协作，但复杂生产力任务（软件、文档、设计）与长期监控决策（等待训练、跟踪项目）往往分离，现有框架难以同时满足。核心矛盾是模型需要自主策略，同时 runtime 必须保持状态、反馈和人类的持续参与。

**方法关键点**：
- 三层架构：Main Agent 作为用户界面和全局规划者，Coordinator Runtime 维护持久状态、消息队列和任务生命周期，Subagents 隔离上下文执行子任务，支持同步/异步委派。
- 共享应用生态：通过资源协议和 revision control，人类和 Agent 可以编辑同一文档、PPT、CAD 模型、Blender 场景，人类反馈既能通过对话也能通过直接修改 artifact 进入循环。
- 持久状态管理：分层 workspace 保存工作文件；语义记忆（memory.md）记录决策与未完成工作；后台 Jobs 保留日志与状态；上下文压缩、checkpoint 和 supervisor 支持中断恢复。
- RSI 实验：用 COWORKOS 自动分析模型弱点、优化数据管道、合成后训练数据，形成闭环自我改进。

**关键实验**：在 12 个基准、4 个领域（Tool Use、Productivity、Search、ML Coding）与 OpenHands、Codex、DeepSeek Harness 对比，COWORKOS 在 Productivity 域平均分 57.54 排名第一，ML Coding 域 56.26 第一，Tool Use 和 Search 均与前二接近，整体性能最强。定性 24 个案例覆盖网站、游戏、Office、可视化、CAD、Blender 六类真实工作。在五轮自动后训练中，Qwen3.6-35B-A3B 平均分从 33.19 提升至 42.95（+9.76）。

**一句话**：模型决定策略，runtime 保持状态，是长时程人机协作 Agent 的核心。
