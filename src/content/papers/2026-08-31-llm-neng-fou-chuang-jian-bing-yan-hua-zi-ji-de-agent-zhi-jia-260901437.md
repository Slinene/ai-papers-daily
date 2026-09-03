---
title: 'HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?'
title_zh: LLM 能否创建并演化自己的 Agent 执行框架？
authors:
- Yuhao Wu
- Jingyuan Zhang
- Jiajun Shi
- Xinping Lei
- Qingshui Gu
- Yuxuan Zhang
- Zexuan Wang
- Chen He
- Chen Huang
- Maojia Song
affiliations:
- ByteDance Seed
- Singapore University of Technology and Design
- Georgia Institute of Technology
- M-A-P
- TokenWave.AI
arxiv_id: '2609.01437'
url: https://arxiv.org/abs/2609.01437
pdf_url: https://arxiv.org/pdf/2609.01437
published: '2026-08-31'
collected: '2026-09-03'
category: Eval
direction: Agent 基础设施自动构建与演化评测
tags:
- Agent Harness
- Benchmark
- Self-Evolution
- LLM Evaluation
- Execution Cost
one_liner: HarnessDev 基准评估 LLM 从零构建并迭代优化 Agent 执行基础设施的能力，发现领域差异大且跨模型迁移受限
practical_value: '- 把 agent harness 当作与模型权重同等重要的优化变量：在电商搜索/推荐 Agent 中，执行循环、工具选择、上下文管理、失败恢复等基础设施设计可直接改变下游任务成功率和
  token 成本，建议建立 harness 级 A/B 评测，而不是只换模型或调 prompt。

  - 借鉴 Creation/Evolution 两阶段范式：可尝试用强 LLM 基于少量示例自动生成 RAG/推荐 Agent 的执行代码，但必须在 held-out
  任务上验证，防止只在开发集上过拟合；对代码、搜索等复杂领域，自动生成 harness 仍落后于人工参考，不要盲目全自动替换。

  - 重视执行效率：论文中生成 harness 的执行 token 成本差异很大，实际业务中可把 token 成本作为约束纳入 harness 优化目标，避免高性能但高成本的
  harness 上线。

  - 注意跨模型迁移性：如果 harness 是为某个 runtime 模型优化得到的，换用其他 LLM 后性能增益可能消失。在多模型混合部署的推荐/搜索服务中，需要按模型或模型族分别评估和调优
  harness。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
Agent 能力越来越依赖模型外执行基础设施（agent harness），但现有评测只关注下游任务表现，忽略模型开发 harness 的能力。为评估 LLM 能否自行构建和演化 harness，HarnessDev 将评测对象从任务输出转向可运行基础设施。

**方法**  
HarnessDev 包含两阶段：Creation 阶段，LLM 从最小种子和少量示例出发构建完整执行系统；Evolution 阶段，LLM 基于下游执行反馈迭代修订自身创建的 harness。评测维度包括能力（隐藏任务成功率）与效率（执行 token 成本）。覆盖 6 个 creator LLM、4 个领域、5 个下游基准、2207 个下游实例，隐藏任务不参与开发。

**关键结果**  
生成的 harness 在代码、搜索与研究领域落后于成熟人工参考；但在写作和机器学习实验领域匹配或超过所选参考，执行成本差异很大。Evolution 带来部分性能提升但不稳定，且仅部分迁移到 held-out 任务。固定 runtime 模型实验表明，性能增益强依赖执行 harness 的模型，跨模型迁移有限。
