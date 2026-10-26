---
title: 'HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games'
title_zh: HiSTEVE 1.0：面向开放世界游戏的通用人机接口 VLA 智能体
authors:
- Zecong Tang
- Zian Guan
- Yuncheng Guo
- Zhanqiu Zhang
- Yiwen Guo
- Bo Dai
affiliations:
- The University of Hong Kong
- Zhejiang University
- Fudan University
- LIGHTSPEED
- Independent Researcher
arxiv_id: '2610.31162'
url: https://arxiv.org/abs/2610.31162
pdf_url: https://arxiv.org/pdf/2610.31162
published: '2026-10-21'
collected: '2026-10-26'
category: Agent
direction: 层级 VLA 智能体原生界面控制
tags:
- VLA
- Hierarchical Agent
- Minecraft
- Imitation Learning
- Reinforcement Learning
- GUI Interaction
one_liner: 分层 VLA 智能体结合 VLM 规划与原生键鼠控制，在 Minecraft 原子与长程任务上达到 SOTA
practical_value: '- 层级式 Agent 设计可借鉴：VLM 仅做高层子任务规划，低层 VLA 执行具体动作，中间用结构化记忆跟踪进度；在电商导购/广告投放操作助手中可采用「规划-执行-记忆」分离，降低单模型长程推理负担。

  - 能力边界感知的 harness 值得落地：规划器只在执行策略能力范围内选择子任务，避免下达无法执行的动作；对应到推荐对话 Agent，可维护「可调用技能/工具白名单」，让
  LLM 规划时显式约束候选动作。

  - 完成状态检测器耦合策略上下文：不只靠视觉或 LLM 判断子任务是否完成，而是以 VLA 策略隐状态为条件；在电商 RPA/浏览器自动化中可参考用执行策略的中间表示辅助判断任务完成，减少误判和重复执行。

  - 异构交互分支处理可复用：GUI 操作与非 GUI 操作使用不同 RMSNorm 分支和独立鼠标移动 token embedding，避免相互干扰；统一 Agent
  同时操作网页、调用 API/工具时，可对不同 action 类型分域建模，降低冲突。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：开放世界游戏中构建像人类玩家一样的虚拟具身智能体，需要长期自主规划和可靠的原始界面控制。现有方法或只提供缺乏长期规划的视觉运动控制，或依赖 API/预定义技能进行高层规划，难以像人类一样直接用键盘鼠标操作。Minecraft 提供了过程化生成的测试场景。

方法：HiSTEVE 采用分层 VLA 架构，带能力感知的 agent harness。编排层包含结构化记忆和 VLM 规划器，仅选择 VLA 能力范围内的子任务；引入策略耦合的任务完成状态检测器，以策略上下文为条件判断子任务是否完成。控制层由单个 VLA 仅凭视觉感知执行所有子任务，输出原生键盘鼠标动作。为缓解 GUI 与非 GUI 交互的干扰，设置 regime-specific RMSNorm 分支和独立鼠标移动 token embedding。训练结合世界知识注入、模仿学习与基于环境反馈的强化学习，提升可靠性与恢复能力。

结果：在 MineStudio Bench 原子任务上达到 85.0%，OpenHA 平均成功率 37.4%，并可完成从零合成铁镐等长程任务，达到该领域 SOTA。
