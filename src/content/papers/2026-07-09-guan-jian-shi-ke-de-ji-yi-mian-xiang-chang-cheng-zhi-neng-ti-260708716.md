---
title: 'Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents'
title_zh: 关键时刻的记忆：面向长程智能体的主动记忆智能体
authors:
- Yifan Wu
- Lizhu Zhang
- Yuhang Zhou
- Mingyi Wang
- Bo Peng
- Serena Li
- Xiangjun Fan
- Zhuokai Zhao
affiliations:
- Meta AI
arxiv_id: '2607.08716'
url: https://arxiv.org/abs/2607.08716
pdf_url: https://arxiv.org/pdf/2607.08716
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: Agent 记忆干预策略优化
tags:
- memory agent
- proactive intervention
- behavioral state decay
- long-horizon
- LLM agents
- RL fine-tuning
one_liner: 提出将记忆视为主动干预策略，通过独立的记忆代理有选择地注入遗忘关键状态，解决长程任务中的行为状态衰减
practical_value: '- 在对话式推荐、客服等长程 Agent 场景中，可引入独立记忆代理监测用户约束和系统状态，在决策点选择性注入提醒，防止模型遗忘关键要求

  - 借鉴记忆银行的分层结构（状态进度、环境事实、过程经验），清晰区分固定约束与试探性经验，方便管理与更新，避免记忆混乱

  - 训练记忆干预策略时，先用 SFT 冷启动教会基本的记忆管理操作，再用 GRPO 校准何时保持沉默（null intervention），以减少不必要干扰，该方法可迁移到自研
  Agent 系统

  - 消融表明被动暴露全部记忆或强制每次注入反而降低稳健性，提示在实际系统中需设计专门的选择性干预逻辑，而不是简单的记忆暴露'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：在长程任务中，决策相关的状态（任务要求、环境事实、失败诊断、进展追踪）往往散落在不断延伸的轨迹里，即使仍留在上下文中也有可能失去对行为的控制，导致智能体重复犯错或违背早先的约束。作者将这种现象命名为行为状态衰减（behavioral state decay），并指出记忆不应仅是被动存储与检索，更关键的是决定何时将已记住的状态重新注入决策回路。

**方法**：
- 提出双阶段记忆干预架构：一个独立的记忆智能体（memory agent）与不改变的行动智能体（action agent）并行运行。
- 记忆智能体按固定步数触发，先通过工具调用管理结构化的记忆银行，包含状态（进度与风险）、知识（稳定事实）和过程记录（尝试与结果）三类条目。
- 第二阶段基于更新后的银行，决定输出一条简洁的记忆提醒或主动保持沉默（null intervention），仅当可能影响行动智能体的下一步决策时才注入上下文。
- 分别使用 SFT 蒸馏和 GRPO 优化来训练开源记忆智能体，强化学习专门校准介入时机与沉默决策。

**实验**：
- 在 Terminal-Bench 2.0 和 τ²-Bench 两个长程基准上测试，Claude Sonnet 4.5 搭配 Claude Opus 4.6 记忆代理后，pass@1 分别提升 +8.3 pp 和 +6.8 pp；对更强的 Opus 4.6 行动代理仍分别有 +2.4 pp 和 +2.5 pp 收益。
- 消融实验显示，选择性干预优于全量记忆暴露、强制每次注入以及不带记忆银行的顾问式指导，Mem0 检索式记忆层则未能提升航空领域且宏平均较低。
- 将 Qwen3.5-27B 作为记忆代理在 SETA 上进行 GRPO 训练，验证奖励从 0.709 提升至 0.734，迁移到 Terminal-Bench 2.0 获得 +3.5 pp 提升。

**核心洞见**：记忆是主动干预的控制问题，不仅要选择记什么，更要学会何时、如何让关键状态重新进入决策回路。
