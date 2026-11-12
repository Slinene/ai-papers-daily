---
title: Embodied First Exam
title_zh: 具身第一考：编码智能体机器人控制统一评估框架
authors:
- Kangrui Wang
- Qineng Wang
- Changhe Chen
- Pingyue Zhang
- Chi Gui
- Feishi Wang
- Canyu Chen
- Wenli Xiao
- Xiaoyu Huang
- Tonghe Zhang
affiliations:
- Northwestern University
- Carnegie Mellon University
- UC Berkeley
- University of Washington
- Stanford University
arxiv_id: '2611.12177'
url: https://arxiv.org/abs/2611.12177
pdf_url: https://arxiv.org/pdf/2611.12177
published: '2026-11-08'
collected: '2026-11-12'
category: Eval
direction: Agent 具身智能评估基准
tags:
- Embodied AI
- Coding Agents
- Robotics Benchmark
- Agent Evaluation
- LLM Agents
one_liner: 推出1156任务、35套件、47机器人的编码智能体机器人控制评估基准，最强智能体标准设置成功率仅34%
practical_value: '- 评估框架分层设计：Standard（仅局部观测、不可重置）与 Privileged（全量状态、无限重置）双设置可迁移到推荐/广告
  Agent 离线评测——先用 Privileged 找理论上界，再在 Standard 下衡量真实能力，避免成功率虚高。

  - 失败阶段标注与归因：论文将失败按阶段分类对比，业务中可为购物助手、广告投放 Agent 建立类似错误追踪，区分意图理解、工具调用、策略执行等失败来源，针对性优化。

  - Agent-native 一键评测基础设施：一个命令即可运行不同 coding agent，适合把 LLM Agent 纳入 CI，持续监控模型或 prompt
  变化对下游任务的影响。

  - Realtime 设置让环境在 Agent 推理时继续运行，可借鉴到实时竞价、动态推荐场景的 Agent 评测，衡量推理延迟与动态环境下的决策鲁棒性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有机器人基准主要围绕 visuomotor policy learning，无法回答编码智能体能否在物理世界约束下可靠控制多样机器人。

**方法**：提出 Embodied First Exam，一个统一、全面、agent-native 的评估框架。编码智能体可选择直接控制、代码控制或训练策略控制。基准包含 1,156 个任务、35 个套件、47 种机器人，其中 9 个新套件超越简单 pick-and-place，覆盖空间拼图、灵巧操作、多机器人交互、全身动态控制与 sim-to-sim 工程。每个任务最多可运行三种评估设置：Standard 模拟真实世界，仅给智能体传感器观测且默认无法重置环境；Realtime 在智能体推理时环境持续运行；Privileged 提供完整仿真状态与无限重置，用于搜索 oracle 解，其成功率可作为近似上界。

**结果**：在 456 个核心任务上，8 个智能体中 GPT-6 Astra in Codex 表现最强，Standard Setting 成功率仅 34%，仍有很大提升空间。论文进一步标注失败发生阶段，跨智能体、设置和阶段类别比较错误分布。
