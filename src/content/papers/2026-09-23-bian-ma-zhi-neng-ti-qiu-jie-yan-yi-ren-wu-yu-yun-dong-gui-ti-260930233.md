---
title: Coding Agents for Generalized Task and Motion Planning Problems
title_zh: 编码智能体求解广义任务与运动规划问题
authors:
- Matteo Merler
- Bowen Li
- Josh Roy
- Yichao Liang
- Qianwei Wang
- Yixuan Huang
- Tom Silver
arxiv_id: '2609.30233'
url: https://arxiv.org/abs/2609.30233
pdf_url: https://arxiv.org/pdf/2609.30233
published: '2026-09-23'
collected: '2026-09-26'
category: Agent
direction: Coding Agent 自动化 TAMP 程序合成
tags:
- coding agents
- TAMP
- program synthesis
- generalization
- LLM planning
- simulation
one_liner: 编码智能体在28个仿真环境中自动合成可泛化的TAMP程序，成功率56%–95%，超越手工规划器与LLM基线
practical_value: '- **合成与执行解耦，离线产出可部署策略**：LLM 在沙盒里把规则写成确定性代码，在线只跑代码而非每次 LLM 推理，文中平均每实例计算量降低一个数量级。电商
  Agent 做选品、出价、推荐策略时，可让 LLM 在历史日志或仿真环境中生成 Python/SQL 函数，离线验证后部署，节省线上 token 成本与延迟。

  - **固定合成预算 + 大规模留出评估**：用 980 个程序 × 100 实例做统计评估，比单次 one-shot 更有说服力。业务 Agent 评测可仿照：给每个
  agent 固定交互步数，在留出日志或 synthetic users 上跑多组实验，避免只报平均值而忽略环境难度分布。

  - **用交互校准模型、测试边缘 case**：日志显示 agent 会主动构造极端场景来修正物理模型。推荐/广告 Agent 可提供 shadow traffic
  或合成用户，允许其在受限交互中做反事实测试和自我纠错，而不是只做被动 rollout。

  - **保留完整 prompt 与程序 trace**：可复现性做法值得借鉴；业务中要求 Agent 输出中间程序并记录决策轨迹，便于审计、调优和上线回滚。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：TAMP 问题因离散决策与几何、运动、动力学约束高度耦合而难以求解；Generalized TAMP 希望利用跨实例规律降低新实例的规划成本，但现有方法依赖大量 TAMP 专门工程。本研究尝试用编码智能体自动合成可泛化的规划程序，替代人工工程。

方法：给定任务描述和仿真器访问权限，每个 agent 在固定合成预算内自主选择如何与环境交互，逐步开发一个程序；合成结束后冻结程序，在未见实例上评估。评估对象包括 Claude Code (Opus 5) 和 Codex (GPT-5.6 Sol、GPT-6 Astra)，覆盖 28 个仿真环境，来自 KinDER 和 PDDLStream，对象数量超出原基准。共评估 980 个生成程序，每个在 100 个 held-out 实例上运行，总计 98,000 个评估 episode。

结果：三个 agent 配置的平均成功率在 56%–95% 之间，显著高于手工规划器的 47%（仅限 16 个可用规划器的环境），也超过 one-shot 生成和基于 LLM 的 generalized planning 基线。随着对象数量增加，agent 程序保持更高成功率，且平均每实例计算量比规划器少一个数量级。日志显示 agent 会利用交互校准物理模型、测试边缘情况并优化策略。代码和完整 prompt 已发布。
