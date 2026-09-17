---
title: 'HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness'
title_zh: HarnessVLN：统一免训练具身导航的 Agent Harness 框架
authors:
- Yang Chen
- Lirong Che
- Zhenyu Huang
- Wenbo Fu
- Chuang Wang
- Xu Cao
- Daqi Liu
- Yuzhe Yang
- Jian Su
- Lan-Zhe Guo
affiliations:
- Nanjing University
- AGIBOT
- Tsinghua University
arxiv_id: '2609.15195'
url: https://arxiv.org/abs/2609.15195
pdf_url: https://arxiv.org/pdf/2609.15195
published: '2026-09-13'
collected: '2026-09-17'
category: Other
direction: 具身导航 · 训练免 Agent 框架
tags:
- Embodied Navigation
- Training-Free
- MLLM
- Agent Harness
- Spatiotemporal Graph
- Tool Interface
one_liner: 提出训练免的 Agent Harness 框架，通过统一工具接口、三重验证与时空图记忆，统一指令跟随与物体目标导航并刷新 SOTA
practical_value: '- 统一工具接口与 Harness 分层：将感知、检索、接地、执行等封装为工具，由 Harness 统一校验、派发、更新，可复用到电商
  Agent 中，把商品召回、意图识别、策略执行等模块解耦为工具，降低切换模型/场景的成本。

  - 规划结果的多重验证：在派发动作前用空间证据、几何可行性、子目标一致性做校验，可借鉴到搜索广告投放 Agent：对出价、选品、文案等 proposal 做规则/模型校验，减少无效执行与资源浪费。

  - 分层事件记忆与持久时空图：将任务进度、执行历史、失败标注沉淀为结构化图，类似用户 session 内的行为轨迹 + 商品关系图，可用于推荐/对话 Agent
  的状态追踪、失败恢复与增量证据累积。

  - 可替换 Navigation Executor：把高层计划与底层执行解耦，同一 Harness 协议可跨模拟器与真机迁移，可借鉴到推荐实验平台：策略层统一，执行层适配不同流量/线上环境。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：具身导航中训练方法泛化有限，而现有训练免方法虽利用 MLLM，但缺乏将规划动作与空间证据、任务进度、执行失败对齐的机制，导致动作提案可能偏离实际环境。

**方法关键点**：
- Agent Harness 统一管理感知、检索、接地、导航、恢复、终止等工具，通过统一工具接口协调各模块。
- 规划 proposal 在派发前经过三重验证：证据支撑、几何可行性、子目标一致性；结构化工具反馈被纳入后续决策，形成闭环。
- 分层事件记忆跟踪任务进度与执行历史；持久 Spatiotemporal Graph 保存可复用空间证据和失败标注，支持验证与恢复。
- 可替换 Navigation Executor 将验证后的目标转换为可执行动作，使同一 Harness 协议同时支持指令跟随和物体目标导航。

**关键结果**：在 R2R、RxR、HM3D-v2、HM3D-OVON 四个基准上成功率分别达到 60.8%、53.9%、76.0%、59.3%，全面超过此前训练免 SOTA；人形机器人部署验证了真实环境下的任务适用性。
