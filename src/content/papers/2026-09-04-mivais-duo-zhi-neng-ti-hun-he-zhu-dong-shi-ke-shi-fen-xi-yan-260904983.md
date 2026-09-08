---
title: 'MIVAIS: A Study Environment for Multi-Agent Mixed-Initiative Visual Analytics
  Applications'
title_zh: MIVAIS：多智能体混合主动式可视分析研究环境
authors:
- Tobias Stähle
- Simon Schneider
- Rita Sevastjanova
- Mennatallah El-Assady
affiliations:
- ETH Zürich, Switzerland
arxiv_id: '2609.04983'
url: https://arxiv.org/abs/2609.04983
pdf_url: https://arxiv.org/pdf/2609.04983
published: '2026-09-04'
collected: '2026-09-08'
category: MultiAgent
direction: 多智能体混合主动可视分析平台
tags:
- Mixed-Initiative
- Visual Analytics
- Multi-Agent
- Human-AI Collaboration
- Provenance
- Study Platform
one_liner: 提出MIVAIS双层平台，标准化多智能体状态同步与通信，并自动记录多模态人机协作溯源数据
practical_value: '- 借鉴其**集中式 World State + Agent Registry + Communication Channels**
  架构，将多智能体推荐/搜索系统中的状态同步从各服务私有化改为共享“世界状态”，降低 agent 开发与联调成本；特别是加入 Permission Guard 可统一控制人机协作中
  agent 的写权限，适合电商导购/客服等半自主场景。

  - 采用**声明式实验配置（YAML 定义任务、角色、数据采集）**与自动多模态溯源（应用状态、屏幕录制、音频、传感器）建设 Agent 系统的用户研究/在线评估闭环，避免为每次实验重复埋点。

  - 其**自动回放与交互时间线**可用于事后分析用户与推荐/搜索 agent 的协作过程，定位“用户在何时拒绝或修正 agent 建议”的序列模式，对优化生成式推荐交互有直接参考价值。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：混合主动可视分析系统开发需处理异步多智能体状态同步、权限与通信，评估需捕获多模态溯源数据，工程门槛高。

**方法**：MIVAIS 提供双层平台。基础设施层通过 Agent Registry、World State、Communication Channels、Audit Logs 等标准化人机/软件 agent 交互与状态同步；研究环境层用声明式 YAML 配置实验，自动采集应用状态、屏幕、音频、传感器等多模态遥测，并支持交互时间线、回放与标注分析。

**结果**：通过复现 Podium、Voyager2、ProactiveVA 三个 SOTA 系统完成技术验证，并由 HCI/VA 专家案例研究评估表达性与效率，证明该平台能显著降低智能协作界面原型与评估门槛。
