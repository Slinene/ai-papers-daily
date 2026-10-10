---
title: 'HarnessSQL: Harness-Native Training for SQL Agents in Realistic Database Environments'
title_zh: HarnessSQL：真实数据库环境中 SQL Agent 的 Harness 原生训练
authors:
- Haolin Yang
- Jipeng Zhang
- Jian Xie
- Shuaishuai Gong
- Sirui Han
- Yike Guo
affiliations:
- Hong Kong University of Science and Technology
- Microsoft Research
- Tsinghua University
- University of Macau
arxiv_id: '2610.12274'
url: https://arxiv.org/abs/2610.12274
pdf_url: https://arxiv.org/pdf/2610.12274
published: '2026-10-08'
collected: '2026-10-10'
category: Training
direction: SQL Agent 原生训练 · 执行奖励 RL
tags:
- Text-to-SQL
- Harness-Native Training
- Execution-Reward RL
- SQL Agents
- SFT
- RL
one_liner: 提出 HarnessSQL 训练框架，在 SFT 和 RL 中保留完整 SQL 交互结构，大幅提升小模型在真实数据库任务中的执行准确率
practical_value: '- 借鉴 harness-native 训练思想：在电商搜索/推荐 agent 训练时，让模型直接调用线上同构工具（商品检索 API、数据库查询、排序服务），保留完整交互轨迹做
  SFT，而不是只输入问题输出答案，缩小训练与线上推理差距。

  - 使用 execution-reward RL：以可验证的结果（如商品是否被正确召回、SQL 是否返回正确结果、用户是否点击）作为奖励信号，只对最终成功轨迹给予正奖励，能有效提升长程
  agent 任务表现，且无需逐步骤标注。

  - 引入 hidden oracle 自动过滤高质量轨迹：在业务中可构建规则或脚本验证任务完成情况，从海量交互日志中筛选成功样本用于训练，降低人工标注成本。

  - 隔离可执行沙箱环境：在离线训练时为 agent 提供稳定、可控的数据库/服务沙箱，避免真实环境波动导致训练不稳定；同时可模拟错误注入，增强错误恢复能力。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：传统 Text-to-SQL 模型训练时直接映射问题到静态 SQL，但真实数据库 agent 依赖有状态多轮交互：查看 schema、执行探测查询、诊断错误、修正假设。这导致训练与部署不匹配，执行 harness 只在推理时引入，模型无法适应复杂长程数据库工作流。

方法关键点：HarnessSQL 提出 harness-native post-training 框架，在 SFT 和 RL 阶段都保留完整交互结构。具体：构建隔离可执行的数据库环境，配 hidden execution oracle 验证轨迹；在目标 SQL harness 内推出 teacher，只保留验证通过的轨迹做全序列 SFT；随后用 execution-reward RL 优化，让模型在真实执行反馈下学习。

关键结果：在 Spider 2.0-SQLite 上，Qwen3-8B 执行准确率从 15.5% 提升到 45.2%，Qwen3-14B 从 22.2% 提升到 54.8%；并在 OOD 交互基准 BIRD-Interact 和 LiveSQLBench 上有效迁移，证明在 harness 内训练对掌握复杂长程数据库工作流至关重要。
