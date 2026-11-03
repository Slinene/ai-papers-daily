---
title: 'RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory'
title_zh: RoboArchitect：自动化设计带持久记忆的机器人 Agent
authors:
- Shengguang Wu
- Suning Huang
- Cherie Ho
- Ria Doshi
- Hao Zhu
- Serena Yeung-Levy
affiliations:
- Stanford University
arxiv_id: '2610.42141'
url: https://arxiv.org/abs/2610.42141
pdf_url: https://arxiv.org/pdf/2610.42141
published: '2026-10-29'
collected: '2026-11-03'
category: Agent
direction: Agent 自动化设计与持久记忆
tags:
- Agent Harness
- Automated Design
- Persistent Memory
- Robot Manipulation
- LLM
- Policy Optimization
one_liner: 用 coding model 自动迭代优化机器人 agent harness，无需更新策略权重，大幅提升跨场景成功率
practical_value: '- **借鉴「冻结模型 + 外围 harness 优化」范式**：在推荐/搜索场景中，可以把已训练好的排序模型或 LLM 当成
  frozen policy，通过代码化的决策逻辑（何时调用模型、如何融合特征、如何处理输出）进行自动迭代优化，避免频繁重训模型，尤其适合快速适配新业务场景或新数据分布。

  - **持久记忆机制可迁移到对话式推荐 Agent**：论文中 harness 会积累成功经验（如有效抓取深度）供后续决策参考。在电商导购或客服 Agent 中，可以设计类似的
  memory 结构，记录用户偏好、历史成功推荐策略或交互模式，作为额外上下文注入下一次决策，提升个性化与连贯性。

  - **失败诊断 + 代码修改的闭环值得复用**：用 LLM 分析 rollout 失败原因并生成改进代码，这种「诊断-修订-评估」循环可以用于自动优化推荐系统外围逻辑，例如召回过滤规则、曝光策略、重排规则等，用代码表示策略比调权重更灵活且可解释。

  - **工程实现上，harness 与 policy 解耦便于快速实验**：将模型调用封装在可控代码层，可以轻量地切换不同底层模型或策略，同时通过 held-out
  场景评估泛化，适合在电商推荐中构建可插拔的 Agent 框架。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：机器人策略在 agent harness（控制代码决定何时调用策略、视觉工具或直接控制机械臂）中表现远好于裸策略，但 harness 目前依赖手工设计，且每个新机器人或基准都要重做。作者提出 harness 设计可以自动化，作为微调模型权重的替代方案。

**方法关键点**：RoboArchitect 使用一个 coding model 观察机器人 rollout，诊断失败原因，并迭代修改围绕 frozen policy 的 harness 代码。harness 不仅包含控制逻辑，还会演化出持久的记忆模块，把学到的经验（如有效抓取深度）带入后续决策。优化在一组 episodes 上进行，评估则在 held-out scenes 和 tasks 上开展，全程不更新任何模型权重。

**关键结果**：跨多个基准和策略，平均成功率从 9.7% 提升到 43.3%（未见场景，4.5×），从 12.7% 提升到 40.2%（未见任务，3.2×）。当基准与策略训练数据差异较大时提升最明显：给通用策略包上演化出的 harness，得到的专用 agent 往往超过微调版本。系统自动设计出直观控制策略，例如抬起卡住的机械臂或从水平方向绕过上方障碍物。
