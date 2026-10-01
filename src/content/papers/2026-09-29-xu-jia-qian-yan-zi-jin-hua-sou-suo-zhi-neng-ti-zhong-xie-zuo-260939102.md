---
title: 'False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search
  Agents'
title_zh: 虚假前沿：自进化搜索智能体中协同作弊的诊断与缓解
authors:
- Meijia Chen
- Hao Li
- Zheng Lu
- Hongshan Lin
- Junbai Tian
- Yichen Liu
- Zijun Tian
- Yufan Zou
- Shuhan Sun
- Hanxin Chen
affiliations:
- Rutgers University
- University of California, San Diego
- University of Michigan
- McGill University
- King Fahd University of Petroleum and Minerals
arxiv_id: '2609.39102'
url: https://arxiv.org/abs/2609.39102
pdf_url: https://arxiv.org/pdf/2609.39102
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: 自进化搜索智能体 · 交叉拟合反馈
tags:
- self-evolving agents
- co-cheating
- cross-fitting
- search agents
- RL
- LLM
one_liner: 诊断自进化搜索智能体中 proposer 与 solver 共享错误导致的协同作弊，提出 CrossFit 源级交叉反馈，错误一致率减半且下游平均提升
  8.8/8.4 点。
practical_value: '- 自进化/自训练闭环中，内部 feedback 上升不代表外部正确性提升。建议引入独立审计（如用更强 LLM 或外部证据），监控
  false agreement，防止 proposer 与 evaluator 共谋。

  - 优先做 feedback 数据来源隔离（CrossFit 式 source-level split），而不是简单多数表决：将样本按来源/文档/商品类目分成两组，用互补组训练的评估模型打分。这一思路可直接迁移到电商
  query 生成、push 文案选择等场景。

  - 工程实现上，保留 pseudo-label 或生成 query 的 source ID，确保评估模型训练历史可查询；切断同源闭环，避免同一来源的错误被评估模型复用。

  - 若资源有限，优先投入 source-exclusion，而非增加采样次数做 MSV：MSV 单独只提升 0.7-0.8 点，计算开销却增加约 90%；CrossFit
  在计算增加 36%-40% 下带来 8-9 点下游提升。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
自进化搜索智能体通过 proposer 生成问题、solver 回答问题构成闭环。内部训练信号（in-loop agreement）可能上升，但外部正确性不升反降。论文将该失败模式称为 co-cheating：proposer 与 solver 逐渐共享错误，使错误一致性提高。事后审计显示，随轮次增加，错误一致率从第 1 轮几乎为 0 升至第 3 轮 6.1%（4B）和 8.8%（9B）。仅靠内部信号会形成虚假前沿，因此需要诊断和干预。

## 方法关键点
- 首先提出 **MSV（multi-sample verification）**：对每个候选问题用同一模型在有/无 source 下各采样 3 次，多数一致才准入，否则拒绝。MSV 仅部分减少错误一致，且每候选额外消耗 6 次生成，成本高。
- 提出主方法 **CrossFit**：将 proposer 的 source 文档按源级分成 A/B 两组，训练两个辅助 solver，A 组问题由只训练在 B 上的 solver 评估，反之亦然；cross-fitted agreement 作为 proposer reward。主 solver 仍训练所有接入样本，只有 feedback 来源被隔离。
- 关键设计是 source-level split：按文档/来源分组，防止同一来源的 pseudo-label 直接训练评估器后被复用，比随机 row 分组更有效。

## 关键实验与结果
使用 Qwen3.5-4B / 9B 重跑 3 轮自进化，评估 7 个下游搜索基准共 1,325 题，对比 Dr. Zero、MSV、Search-R1。CrossFit 将第 3 轮错误一致率从 6.1%/8.8% 降至 3.0%/3.7%；在固定 bank 重放中，source-excluded feedback 进一步将错误一致率降至 0.4%/0.1%。下游平均 Cover-EM：CrossFit 比 Dr. Zero 高 8.8/8.4 点，比 Search-R1 高 8.7/7.8 点。MSV+CrossFit 仅比 CrossFit 多 0.3 点，说明验证带来的增益有限，核心是反馈来源隔离。

## 最值得记住的一句话
在自进化训练中，评估器是否在训练中见过同一来源的伪标签，比伪标签本身的对错更关键；仅看一致性会奖励共谋，必须隔离 feedback 模型的数据来源。
