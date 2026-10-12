---
title: 'Stateless Language Agents: Scaling Long-Horizon Automated Research'
title_zh: 无状态语言智能体：扩展长程自动化研究
authors:
- Qizheng Zhang
- Changxiu Ji
- Isaac Sun
- Yuetai Li
- Shubhangi Upasani
- Sherry Ruan
- Boyuan Ma
- Fenglu Hong
- Vamsidhar Kamanuru
- Yoonho Lee
affiliations:
- Stanford University
- Carnegie Mellon University
- University of Washington
- SambaNova Systems
- UC Berkeley
arxiv_id: '2610.07625'
url: https://arxiv.org/abs/2610.07625
pdf_url: https://arxiv.org/pdf/2610.07625
published: '2026-10-05'
collected: '2026-10-12'
category: MultiAgent
direction: 长程 AutoResearch 无状态多智能体框架
tags:
- Stateless Agents
- Long-Horizon
- AutoResearch
- Context Management
- Multi-Agent
- Token Efficiency
one_liner: 无状态 Agent + 有状态 harness：每次调用重建角色化上下文，用更少 token 实现更强长程搜索
practical_value: '- 构建长程 Agent 系统（自动实验、策略搜索、query 迭代等）时采用“stateful harness + stateless
  agents”：候选、分数、日志放外部状态，每次调用只注入角色相关摘要，不要让 agent 携带完整历史滚动，避免 context rot 和 token 浪费。

  - 对规划者与执行者做角色化上下文隔离：中央规划者看全局结构化 evidence summary，执行单元只看自己的 assignment、本地候选和反馈。搜索推荐
  Agent 里可对应“策略器”与“渠道/实验执行器”，减少互相干扰和重复实验。

  - 给执行单元显式任务分配，而不是只共享记忆；论文 ablation 显示没有 assignment 时并行 Workers 会重复实现同一功能。多 Agent
  做选品、文案、素材生成时，应由 coordinator 把“该试什么”变成具体实验。

  - 评估 Agent 系统至少按多个 token 预算点报告；短预算可能逆转方法排名。内部评估搜索/推荐 Agent 如果只跑短预算，很可能选错架构。协调器可以非常便宜（<0.6%
  tokens），强 Advisor + 弱 Worker 在部分任务上更划算。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前 LLM 自动研究系统在长 horizon 下，更多推理并不自动带来更多进展。原因集中在两点：研究状态存在 agent 对话里，历史不断膨胀并导致上下文退化；累积证据没有被转化为下一轮实验，多个 agent 重复劳动或停止尝试。多数评测预算短、benchmark 早饱和，掩盖了这些失效模式。

**方法关键点**：
- 核心原则是 stateful search with stateless agents：agent 不跨调用保留对话，harness 拥有研究状态（候选解 + 评测结果），每次调用重建全新且角色专属的上下文。
- Advisor 每个 epoch 接收任务说明、全局最佳代码/分数、结构化 evidence summary（按方向汇总近期尝试、Worker 状态、进展，并区分失败与非改进）。
- Worker 只接收自己的 assignment、保留候选和本地反馈，工作区隔离，无法访问其他 Worker 或完整历史。
- Advisor 基于全局证据做显式任务分配，可分散或集中探索；Workers 专注实现与局部细化。
- 实现上使用 Codex / Claude Code，Worker 通过 Landlock 隔离，评测器受保护，并支持 checkpoint 做共享起点 ablation。

**关键实验与结果**：在 FrontierSWE 四个任务、Anthropic kernel optimization、SOL-ExecBench 三题、FrontierCS Structured-LWE 上对比 EvoX、CORAL、SwarmResearch，预算最高 1B tokens。SLA 在所有任务上取得最佳最终结果；Anthropic kernel Codex 下 3 次 SLA 运行均优于 9 次基线，达到最强基线最终性能仅需 67.9M tokens，比 SwarmResearch 的 986.3M 少 93.1%；Claude Code 下少 84.4%。FrontierSWE 在 25% 预算时落后，但 700M 时全面领先，较最强单任务基线平均 +4.95 分。Advisor 消耗仅 0.24–0.51% tokens，而 SwarmResearch Shepherd 为 8.39–10.70%。ablation 显示删除 Worker 隔离在完整 1B run 中损失 224 cycles，远高于短 continuation 的 5–11 cycles。

**最值得记住的一句话**：把持久研究状态移出 agent 对话；agent 每次看到什么应是一个显式设计选择，而不是不断累积的历史。
