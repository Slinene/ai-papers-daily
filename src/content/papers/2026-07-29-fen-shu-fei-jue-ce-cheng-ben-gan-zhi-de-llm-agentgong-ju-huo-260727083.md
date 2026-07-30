---
title: 'Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM
  Agents'
title_zh: 分数非决策：成本感知的LLM Agent工具获取停止
authors:
- Yicheng Feng
- Yan Zhang
- Yan Cheng
- Wei Qi
affiliations:
- Peking University
- McGill University
- Shanghai University of Finance and Economics
- Tsinghua University
arxiv_id: '2607.27083'
url: https://arxiv.org/abs/2607.27083
pdf_url: https://arxiv.org/pdf/2607.27083
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: 代价感知的Agent工具前缀截止学习
tags:
- Cost-Aware Stopping
- Tool Acquisition
- LLM Agents
- Decision-Focused Learning
- Prefix Stopping
- Regret-Weighted Classification
one_liner: 将工具获取形式化为代价感知的前缀停止，用后悔加权目标学习截止深度，以更少工具实现更高收益
practical_value: '- 在工具调用前加一层代价感知截止策略：根据工具排序和成本动态决定前缀深度，可减少不必要的外部调用、上下文消耗和延迟，适用于搜索推荐中的知识检索、API
  路由等环节。

  - 后悔加权训练目标直接优化下游收益：错误按 payoff 差距加权，比先预测充分性再阈值截断更鲁棒，尤其在工具成本异质时（如不同数据源查询价格不同）。

  - 特征设计需融合边际成本与剩余价值：除工具相关性分数外，引入边际成本、剩余候选集积分等特征，实现成本感知的停止决策。

  - 轻量级解耦插件形式：CAM-DF 不修改上游排名器与下游 LLM，可快速接入现有 Agent 系统，适用于电商场景中动态选择商品信息源、实时调整工具预算。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM Agent 的工具生态日益膨胀，获取过多工具浪费上下文、延迟与成本，过少则导致任务信息不足。现有排名器只给出工具顺序，不决定获取深度。本文将该决策建模为代价感知的排名前缀停止问题。

**方法关键点**
- 定义 payoff 为「充分性 − λ×工具成本和」，在给定工具评分排序下，每步状态决定 stop 或继续获取下一个工具。
- 训练目标：计算当前前缀 payoff 与最佳后续前缀 payoff 之差 ∆，用 sign(∆) 作 stop/continue 标签，|∆| 作样本权重，训练后悔加权 logistic 分类器（CAM-DF）。该目标 Bayes 对齐停止决策边界。
- 理论证明：在异质成本下，仅靠分数单调性的规则必然次优；边际价值-成本比才决定停止时机。
- 轻量变体 CAM-DF-lite 仅用 10 个理论驱动特征，可解释且保留大部分收益。

**关键结果**
- 在 τ-bench Retail 等 5 个领域 1343 项任务上评估。Retail 均匀成本下，CAM-DF 平均 payoff 0.400，显著优于 tuned fixed-k（0.277）和 predict-then-threshold（0.352）。
- 异质成本下优势更大，λ=0.20、d=1.5 时 payoff 增益达 0.21。
- 跨 5 种 LLM 排名源、10 个成本设置，CAM-DF 在 9 个设置中显著优于强基线。
- 端到端实时执行中，工具曝光从 7 个减至 4.4 个（−37%），任务成功率与全量工具无显著差异。

**一句话**：对工具排名做代价感知的后悔加权停止，能用更少的工具拿到更高的净收益——尤其当工具成本差异大时，分数本身不足以正确决策。
