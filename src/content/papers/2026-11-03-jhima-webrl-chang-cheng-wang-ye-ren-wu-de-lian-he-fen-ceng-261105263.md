---
title: 'JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework
  for Long-Horizon Web Tasks'
title_zh: JHiMA-WebRL：长程网页任务的联合分层多智能体强化学习框架
authors:
- Shanka Subhra Mondal
- Jiayun Wang
affiliations:
- Center for Advanced AI, Accenture
arxiv_id: '2611.05263'
url: https://arxiv.org/abs/2611.05263
pdf_url: https://arxiv.org/pdf/2611.05263
published: '2026-11-03'
collected: '2026-11-04'
category: MultiAgent
direction: 多智能体分层RL训练网页Agent
tags:
- Hierarchical RL
- Multi-Agent
- Web Agent
- GRPO
- Task Decomposition
- Planning
one_liner: 教师生成子任务监督，分层GRPO联合训练7B规划器与7B执行器，WebArena-Lite-v2达37.2%，超32B RL基线13.2个百分点
practical_value: '- 用强模型从已有轨迹自动蒸馏 subtask 监督，人工零标注构建规划训练集：电商/搜索 Agent 可以拿历史会话或操作日志让
  GPT-5 级模型生成高阶子任务，训练轻量 decomposer，降低对闭源大模型推理依赖。

  - 角色分离 + 各自优势的 GRPO 扩展值得复用：actor 固定同一 plan 比较 rollout，decomposer 按 plan 平均 reward
  比较候选 plan，避免规划与执行 credit assignment 混在一起；工程上只用 terminal success，不需要 dense process
  reward。

  - 小模型分工成本效益明显：7B decomposer + 7B actor 超过 32B 单体 RL agent，适合电商/推荐场景里 QPS 敏感或需要私有化部署的
  Agent 系统。

  - 当前 decomposer 是一次性 open-loop planning，不能根据执行偏差 replan；业务里可加异步重规划或 subgoal 完成检测，作为后续优化点。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
长程网页任务既有高层规划（如取消订单要多步导航）又有低层视觉执行（点击、输入、滚动），单体策略难以同时学好。已有模块化系统虽然引入 planner，但 planner 参数不随执行结果更新，只靠 actor 单独 RL 或交替更新。

**方法关键点**
- 用 GPT-5.2-Codex 作为 teacher，从 ScaleCUA 多模态轨迹自动生成约 76K 有序子任务标注，并标记冗余动作。
- SFT 阶段：两个 Qwen2.5-VL-7B 分别训练 decomposer（指令+初始截图→子任务序列）和 actor（子任务+当前截图+历史动作→下一步 GUI action），actor 用 253 万条含 subtask 上下文的轨迹。
- 联合 RL 扩展 GRPO：每个任务 decomposer 采样 K=3 个候选分解，每个分解 actor 执行 M=7 条完整轨迹。actor advantage 比较同一 plan 下的执行好坏；decomposer advantage 用 plan 平均 terminal reward 比较不同计划；两个策略共享同一 rollout batch 更新 LoRA。
- 去除 GRPO 的标准差和长度归一化，降低优化偏差。

**关键结果**
在 WebArena-Lite-v2 154 个任务上，JHiMA-WebRL-14B 平均成功率为 37.2%（4 次评估均值），显著超过同协议训练的 ScaleCUA-32B RL 的 24.0%，提升 13.2 个百分点；GitLab 47.5%、Reddit 60.5%、Shopping 29.0%、ShoppingAdmin 44.3%，Map 仅 12.5%。消融显示：联合更新 decomposer 比只更新 actor 高 3.8pp（33.4%）；去掉 decomposer 的 actor-only RL 为 34.9% / 35.2%；去掉 RL 保留 SFT 模块化系统为 35.1%。子任务完成度可较好预测最终成功（AUROC=0.838），且成功率随完成比例单调上升（Kendall τ=0.516）。

**最值得记住的一句话**：小模型角色分解 + 联合 RL 能在长程网页任务上替代更大的单体 agent，关键是让规划器和执行器从同一批 rollout 中按各自角色优势同时更新。
