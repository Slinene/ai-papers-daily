---
title: Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench
  2.0
title_zh: 代理优化器增益能否复合？基于 Terminal-Bench 2.0 的持续学习评估
authors:
- Wenxiao Wang
- Priyatham Kattakinda
- Soheil Feizi
affiliations:
- RELAI.ai
arxiv_id: '2607.14004'
url: https://arxiv.org/abs/2607.14004
pdf_url: https://arxiv.org/pdf/2607.14004
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent 持续优化与回归感知搜索
tags:
- agent-optimization
- continual-learning
- harness-optimization
- regression-aware
- Terminal-Bench
- prompt-engineering
one_liner: 两阶段持续学习协议揭示：仅回归感知的优化器 RELAI‑VCL 能同时实现正向迁移与二次提升，终身平均通过率达 76.4%
practical_value: '- **在 Agent 自优化流水线中强制回归控制**：每次接受候选更新前，校验其在已解决任务上的表现，拒绝退步的更新。不要等到部署后才回滚。

  - **用两阶段评价暴露过拟合与停滞**：开发阶段应采用“静态优化 → 迁移到新任务 → 二次优化”的协议，避免仅凭单阶段 benchmark 分数被误导。

  - **作为隐式泛化过滤器的回归约束**：回归感知搜索会自然排斥仅针对当前任务集的捷径，因此对未见任务有更好的迁移性，这对于推荐/搜索 agent 的 prompt
  或工具链优化尤其有益。

  - **工程实现时可参考 RELAI‑VCL 的思路**：在 agent 框架中内置一个任务类型分类器与完成前的一致性检查门，无需硬编码任务样本即可提升鲁棒性。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
现有 Agent 优化方法（如 GEPA、Meta‑Harness）的成果多在静态 benchmark 上报告，而生产环境中 agent 需要反复优化以适应新任务和失败案例。这引出一个核心问题：**优化增益能否复合？** 即，Agent 已被优化一次后，再次优化新任务时会不会破坏之前获得的能力？本文通过两阶段持续学习协议回答此问题。

## 方法关键点
- **两阶段持续学习评估协议**：选用 Terminal‑Bench 2.0 的 22 个困难任务（T1:12 个，T2:10 个）。第一阶段只在 T1 上优化，评估静态提升；随后在不额外优化的情况下评估 T1∪T2 的迁移表现；第二阶段在 T1∪T2 上再次优化，衡量二次提升。
- **对比三种优化器**：① GEPA（进化式提示优化，允许注入任务特定经验）；② Meta‑Harness（直接编辑 agent 代码，变更保守且通用）；③ RELAI‑VCL（回归感知搜索，在搜索循环内拒绝导致旧任务退步的候选）。所有优化器使用相同 LLM（GPT‑5.5）和每阶段 200 次 rollout 预算。
- **评估指标**：阶段一通过率、迁移通过率、最终通过率及终身平均通过率（三者均值）。

## 关键实验与结果
- **静态优化（Phase 1）**：RELAI‑VCL 通过率 **79.2%**，GEPA 70.8%，Meta‑Harness 66.6%，基线 62.5%。三者均有提升，但 GEPA 的优化提示中硬编码了任务特定细节（如文件路径、期望输出），存在过拟合风险。
- **迁移测试（Transfer）**：GEPA 降至 **54.5%**（低于基线 56.8%），完全暴露过拟合；Meta‑Harness 升至 68.2%（通用改动带来迁移性）；RELAI‑VCL 达 **72.7%**，且对未见 T2 任务单独通过率比基线高约 15 个百分点。
- **二次优化（Phase 2）**：GEPA 恢复到 72.7%（仅当纳入 T2 搜索后），Meta‑Harness 反而降至 **59.1%**（所有新候选均劣于已有 agent），RELAI‑VCL 继续提升至 **77.3%**。
- **终身平均通过率**：RELAI‑VCL **76.4%** > GEPA 66.0% > Meta‑Harness 64.6% > 基线 58.7%。

## 核心结论
**只有将回归控制内置到搜索循环中，才能同时获得迁移能力和连续提升**——事后检查不足以让优化增益复合。回归感知优化隐式过滤了任务特定捷径，从而产生更具泛化性的 agent 改进。
