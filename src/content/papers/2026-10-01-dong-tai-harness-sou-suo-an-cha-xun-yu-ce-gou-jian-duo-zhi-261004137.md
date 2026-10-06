---
title: 'Dynamic Harness Search: Building Multi-Agent Systems Per-Query via Prediction'
title_zh: 动态 Harness 搜索：按查询预测构建多智能体系统
authors:
- Som Sagar
- Shasha Li
- Hejie Cui
- Ransalu Senanayake
- Sercan Ö. Arık
affiliations:
- Google
- Arizona State University
arxiv_id: '2610.04137'
url: https://arxiv.org/abs/2610.04137
pdf_url: https://arxiv.org/pdf/2610.04137
published: '2026-10-01'
collected: '2026-10-06'
category: MultiAgent
direction: 成本敏感的按 query 多智能体编排搜索
tags:
- Multi-Agent Systems
- MCTS
- LoRA
- Value Function
- Workflow Optimization
- Cost-Aware
one_liner: SHIFT 用本地小模型预测 harness 效用并以 MCTS 按查询构造多 Agent 系统，无需在线执行候选，精度与成本双优
practical_value: '- 把 agent harness 定义为可执行图（roles/directives/tools/edges），在请求级用本地小模型（如
  Gemma-2B + LoRA）做 MCTS 选择，而不是固定 pipeline；电商场景可按 query 决定是否需要「检索→规划→校验」多人链路，还是仅一个
  reader/单步商品查询，降低高耗时多 Agent 编排的无效消耗。

  - 成本敏感的价值函数值得直接复用：reward=成功项 - 归一化 token/latency/tool/agent 惩罚，用 binary cross-entropy
  + pairwise ranking loss 训练 value head；线上可选择 value 最高的 harness 而非最强 harness，类似路由/降级策略，在牺牲极小精度下大幅省
  token。

  - 搜索只在本地模型内完成，候选执行不进入在线路径；MCTS 用虚拟损失实现批量并行，H100 上构造 harness <1s，在线成本接近固定编排。适合已有
  workflow/Agent 编排平台做逐 query 编排，或作为 offline 训练 policy、online value 决策的两段式部署。

  - 动作空间从最小 harness（single Coder 无 tools）开始，40 个 action 共享跨 domain 的结构/指令，工具权限随 domain
  变化；这种冷启动方式可迁移到新的商品类目/垂直搜索，通过少量执行数据训练 architect，再迁移到更难任务。'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
多 Agent 系统的 harness（角色、指令、工具、通信结构）决定解决 query 的能力与成本，但最优设计随 query 不同，且组件间存在交互。传统 workflow 搜索或 prompt 优化要么复用固定结构，要么在线执行多个候选，成本高。SHIFT 把执行移出逐 query 搜索循环：本地小模型预测效用，MCTS 按 query 构造 harness，训练成本被后续查询摊销。

### 方法关键点
- 将 harness 表示为可执行有向图：节点为 agent（role/directives/tools），边为结果传递或反馈；从最小 harness（单个 Coder 无工具）经 40 个 action 增量添加 agent、指令、工具权限。
- Architect 用 Gemma-2B 骨干 + LoRA + policy/value 双头；输入 query、可行 action 集合和图序列化，输出动作 logits 和效用 logit。
- MCTS 用 policy prior + PUCT，批量推理以虚拟损失并行；只执行最终选中的 harness，构造约 <1s/H100。
- 效用 reward = 成功项 - token/latency/tool/agent/timeout 惩罚，按 benchmark 做缩放；value head 用 BCE + pairwise ranking loss 学习成本敏感效用。

### 关键实验
六个 benchmark 共 9193 tasks（GSM8K、HotpotQA、MBPP、SpreadsheetBench、OfficeQA、GAIA），统一 Gemini 3.5 Flash executor，对比 17 个基线。
- SHIFT-search 平均准确率 79.9%，超出最强基线 Trace 7.2 个点；OfficeQA +30.0，GAIA +15.0；两个 variant 均在准确率-成本 Pareto 前沿。
- SHIFT-value 平均准确率 74.5%，高于所有 baseline，执行 token 比 Trace 少 32%。
- 消融：联合选结构+指令+工具比只选工具/只选指令高至 9.1 个点；value 选择从同一候选池提升准确率并降低成本；GSM8K 训练的 architect 迁移到 MATH-500 提升最难题准确率。

### 最值得记住的一句话
将多 Agent 编排视为可搜索的 harness 图，用本地小模型的价值预测替代候选执行，按 query 动态分配 agent/工具/指令，能在提升准确率的同时显著降本。
