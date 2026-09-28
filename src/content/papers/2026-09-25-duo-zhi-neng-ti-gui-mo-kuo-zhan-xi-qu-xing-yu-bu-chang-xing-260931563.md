---
title: Multi-agent Scaling Across Disjunctive and Compensatory Tasks
title_zh: 多智能体规模扩展：析取型与补偿型任务分析
authors:
- Carolina Fortuna
- Blaz Bertalanic
arxiv_id: '2609.31563'
url: https://arxiv.org/abs/2609.31563
pdf_url: https://arxiv.org/pdf/2609.31563
published: '2026-09-25'
collected: '2026-09-28'
category: MultiAgent
direction: 多智能体协作任务结构分析
tags:
- Multi-agent scaling
- LLM ensemble
- Disjunctive tasks
- Compensatory tasks
- Plurality voting
- Fermi estimation
one_liner: 引入 Steiner 任务分类，发现多数投票在析取任务上几乎不随团队规模提升，同模型平均在补偿任务仅降 6% 误差
practical_value: '- 在电商 Agent 团队中，若任务是“从候选 query/文案/商品中找出正确或最优项”（析取型），同模型多实例多数投票基本无效：正确概率随团队规模增长
  5–20 点，但投票后几乎没实现（预测到 0.5 点内）。不要靠扩同模型实例数，优先用多轮 revision，且只需 1 个 peer 即可，可大幅节省算力成本。

  - 对于补偿型任务如 GMV/CTR/库存/响应时间估计，同模型多采样平均只能降低约 6% 误差，因为共享 item-level bias 占 87%。建议混合模型家族（不同训练/结构）来聚合，或先做
  bias 校准；单模型多采样收益很低。

  - 多智能体规模不是越大越好：机制与任务结构决定上限。在系统里可先判断任务属于析取还是补偿，再选择组合机制（投票 vs 平均 vs 混合）和团队大小；避免盲目
  29 agents 的工程浪费。

  - 多轮 revision 的收益来自 peer 存在而非团队规模，因此 2-agent debate 可能比 30-agent 更划算，适合在搜索推荐 Agent
  的决策或评估环节作为轻量级增强方案。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM 多智能体系统常被认为团队规模越大越好，但缺乏对任务结构的系统分析。作者引入 Steiner 群体任务分类，聚焦析取型（disjunctive，需要至少一个成员正确）和补偿型（compensatory，需要聚合多个估计）任务。

**方法关键点**：将独立采样 agent 视为给定 item 条件独立，得出大团队极限：plurality voting 趋于模型模态答案，averaging 趋于模型 item-level bias。实验用 13 个 open-weight 模型、最多 30 agents、代表性 benchmark。

**关键结果数字**：析取任务中至少一个 agent 正确的概率随团队规模增长 5–20 个百分点，但直接回答后的多数投票几乎无法实现该潜力，平均仅预测到 0.5 点内；多轮 revision 显著提升准确率，但 1 个 peer 与 29 个 peers 的收益几乎相同。在 Fermi estimation 这类补偿任务上，同模型 item-level bias 占约 87% 的平方误差，平均只能降低约 6% 误差；跨模型家族混合有帮助，但在析取任务上未超过最强单模型。结论：任务结构加上输出组合机制是团队扩展效果的根本决定因素。
