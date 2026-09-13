---
title: 'PlannerForge: LLM Agents for Scenario-Based Testing of Motion Planners in
  Autonomous Driving'
title_zh: PlannerForge：自动驾驶运动规划场景测试的LLM Agent框架
authors:
- Yuan Gao
- Sebastian Müller
- Mattia Piccinini
- Marc Kaufeld
- Yuchen Zhang
- Finn Rasmus Schäfer
- Qunying Song
- Johannes Betz
affiliations:
- Technical University of Munich
- Munich Institute of Robotics and Machine Intelligence (MIRMI)
- University College London
arxiv_id: '2609.08965'
url: https://arxiv.org/abs/2609.08965
pdf_url: https://arxiv.org/pdf/2609.08965
published: '2026-09-07'
collected: '2026-09-13'
category: Agent
direction: LLM Agent 自动化测试流水线
tags:
- LLM Agent
- Scenario-Based Testing
- Autonomous Driving
- Prompt Engineering
- Open-Source LLM
- Evaluation
one_liner: 用统一LLM Agent框架覆盖自动驾驶场景测试全流程，开源中小模型媲美商业API
practical_value: '- **LLM Agent 编排模块化 pipeline**：把场景生成、检索、修改、执行、评估统一成可链式调用的 agent
  任务。电商/搜索推荐中可借鉴类似框架，将 query 推荐、召回、排序、评估串成端到端 LLM 工作流，减少碎片化工具切换。

  - **开源中小模型足够匹配商业 API**：论文显示 20–35B 开源模型在多数任务上媲美商业 API。对成本敏感的业务，可以用 Qwen 等开源模型替换
  GPT-4 类接口，经过 prompt 调优后接近商业效果，大幅降低推理成本。

  - **自动 cost-tuning 提升下游指标**：LLM 自动调整模块参数，将规划器成功率从 50.4% 提升到 70.2%、碰撞率从 19.0% 降至
  8.4%，无需领域微调。推荐系统中可让 LLM 自动调 rerank 权重、召回阈值等，用在线指标反馈做闭环优化。

  - **模块路由（Module Routing）**：用 LLM 根据输入场景选择最合适的下游模块/模型。在推荐架构中可实现动态路由，例如不同用户群体或 query
  类型分发到不同精排模型，提升整体效果与资源利用率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
自动驾驶安全验证中，场景测试是碎片化模块流程：场景生成、检索、修改、ADS 执行与结果分析由独立工具完成，缺乏交互。LLM agent 在感知、规划、控制等子系统中已展现潜力，但此前没有统一框架覆盖整个场景测试 pipeline。

**方法关键点**
PlannerForge 用 LLM agent 扩展所有场景测试阶段（生成、选择、修改、模块路由、规划器测试、增强），并新增 ADS 增强与基准测试两个 LLM 增强阶段。评估使用 10 个现成 LLM，在 5 种 prompt 条件下完成全部任务，重点考察不同模型能力与 cost-tuning 对下游规划器的影响。

**关键结果数字**
各任务最佳得分 0.88–1.00，开源 20–35B 模型在多数任务上匹配商业 API，Qwen3.6:35B 在五个任务中三个达到商业 API 水平。端到端链式调用保留 83%（商业）/ 78%（开源）的种子查询。自然语言生成可执行率 193/200 vs Scenario Factory 2.0 的 144/200，属性实现率 92–96%。Rank-1 选择准确率 92.0% vs BM25 的 67.5%，物理有效编辑 ≥94% vs 31%。在 N=400 时，cost-tuning 将规划器成功率从 50.4% 提升到 70.2%，碰撞率从 19.0% 降至 8.4%，且无需领域微调。
