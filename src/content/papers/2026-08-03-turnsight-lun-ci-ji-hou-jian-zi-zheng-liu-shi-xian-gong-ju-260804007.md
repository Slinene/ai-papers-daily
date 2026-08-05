---
title: 'TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning'
title_zh: TurnSight：轮次级后见自蒸馏实现工具推理细粒度信用分配
authors:
- Changle Qu
- Sunhao Dai
- Hengyi Cai
- Yuqi Zhou
- Xinran Chen
- Simon
- Jun Xu
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- Baidu Inc.
arxiv_id: '2608.04007'
url: https://arxiv.org/abs/2608.04007
pdf_url: https://arxiv.org/pdf/2608.04007
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent 后见自蒸馏 · 轮次信用分配
tags:
- Tool-Integrated Reasoning
- Hindsight Self-Distillation
- Turn-Level Credit Assignment
- GRPO
- On-Policy RL
- Agent Training
one_liner: 利用多前瞻视野的执行条件后见信号调制 RL 优势，实现多轮工具推理的精准轮次信用分配
practical_value: '- 在多轮 Agent 决策（如搜索推荐系统中的多步查询、工具调用）中，可直接将环境执行结果作为自然的后见监督，无需依赖外部参考轨迹或人工标注，实现状态对齐的细粒度信用分配。

  - 通过多前瞻视野（例如 d=1,2,3）构建互补的后见教师，利用方向一致性投票选择最可靠的监督信号，既能捕捉即时执行质量，又能反映延迟影响，避免单一视野的偏差或噪声。

  - 组内规范化（prompt-group normalization）将有界后见权重与 RL 基础优势对齐，仅调制幅度而不改变优化方向，可与 GRPO 等策略梯度算法无缝集成，无额外模仿损失。

  - 工程实现上，所有教师和参考分支可冻结，仅需在训练时计算一次后见信号，部署时仅用到学生策略，开销低且易于扩展。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
在多轮工具集成推理（TIR）中，传统 RL 仅依据整个轨迹的最终奖励向所有 token 分配相同信用，无法区分每个交互轮次的质量，导致长程任务优化困难。现有细粒度监督方法要么依赖外部参考轨迹（与 on-policy 状态偏移），要么采用全局特权上下文（如正确答案）而不反映实际执行状态，且多数在 token 级别产生冲突的信号，忽略了工具调用「推理–选工具–填参」天然是一个轮次整体。

### 方法
TurnSight 提出一种**轮次级后见自蒸馏**框架，从学生自己的工具执行结果中提取监督，并用来调制 RL 优势，核心组件：
- **执行条件后见构造**：对每个轮次，使用不同前瞻深度 d 收集未来工具调用与响应作为特权上下文，在冻结的参考模型上计算 token 级 log 概率差，再按轮聚合成一个后见信号，保证状态对齐且轮次一致。
- **多前瞻教师选择**：同时构建 d=1,2,3 三种视野，将各教师信号映射为方向（+1/−1），通过多数投票确定共识方向，选择该方向上信号最强的教师，排除孤立或冲突的监督。
- **组规范化有界权重**：在同一 prompt 的 16 条 rollout 内规范化所选后见信号，与 GRPO 基础优势的符号相乘后经 tanh 限幅，形成 w ∈ [1-ε, 1+ε] 的调制因子，最终优势 = 基础优势 × [(1-λ) + λw]，不改优化方向。

### 关键结果
在 FTRL（域内）和 BFCL、ToolHop（域外）三个基准上，基于 Qwen3-4B/8B 训练后，TurnSight 全面超越 GRPO、MatchTIR、RLSD、SDPO 等方法：8B 模型平均性能提升 7.7%，尤其在 BFCL 的 LongContext、Missing Parameter 等需要精准跨轮信用分配的子集中增益显著；消融证实轮次聚合、组规范化和多教师选择各自带来约 2～3 个点的提升。

### 一句话
该工作证明，**用 Agent 自己的执行结果作为后见信号、并聚合到轮次的信用调制，是提升多步工具推理 RL 训练效率与泛化性的关键**。
