---
title: 'Stop Guessing When to Stop Testing: Efficient Model Evaluation with Just Enough
  Data'
title_zh: 不再猜测何时停止测试：用恰到好处的数据高效评估模型
authors:
- Ofir Arviv
- Kristjan Greenewald
- Yotam Perlitz
- Hadar Mulian
- Michal Shmueli-Scheuer
- Leshem Choshen
affiliations:
- IBM Research
arxiv_id: '2607.08522'
url: https://arxiv.org/abs/2607.08522
pdf_url: https://arxiv.org/pdf/2607.08522
published: '2026-07-09'
collected: '2026-07-11'
category: Eval
direction: 自适应评估 · 顺序测试
tags:
- Sequential Testing
- Model Evaluation
- Confidence Interval
- Early Stopping
- Efficiency
- LLM-as-Judge
one_liner: 提出自适应顺序测试框架，用 CI 宽度和递减收益动态停止评估，节省最高 80% 计算成本并保持统计显著性
practical_value: '- **LLM-as-Judge 评估成本削减**：在使用 LLM 评估推荐结果或 Agent 生成质量时，设置目标 CI 宽度或最小可检测效应量，动态决定何时停止评估，可大幅减少推理计算开销。

  - **A/B 测试早期停止**：在线对照实验中，当所需置信度已达成或效应量已无法进一步显著时提前终止，加速迭代，原理与框架中的递减收益检测一致。

  - **模型选择与排行榜构建**：在多个候选召回/排序模型对比时，用顺序测试自适应分配流量，避免固定测试集浪费，尤其适合需频繁重新评估的场景。

  - **工程实现注意**：需预设停止准则（如 CI 半宽 < 2.5 个百分点或效应量低于阈值），并确保重采样/数据顺序随机，防止偏差；可集成到现有评估管线中。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：固定大小的基准测试无法适应不同评估目标（排名、选择、开发中测试）所需的统计功效，要么浪费计算资源，要么牺牲可靠性。尤其在使用昂贵评估手段（如 LLM-as-Judge、高分辨率 VLM 推理）时矛盾突出。

**方法**：引入**顺序测试（sequential testing）** 到模型评估，提出自适应评估框架。核心是根据实时计算的置信区间（CI）宽度和性能增益趋势动态决定停止点：
- **目标 CI 宽度停止**：当 CI 半宽缩至预设阈值（如 2.5 个百分点）时停止，以保证足以区分模型或检测效应。
- **递减收益检测**：若新增样本带来的性能估计改善趋于平缓，提前终止，避免无效计算。
- 框架基于重采样和渐进有效推断，保证最终结论的统计有效性。

**关键结果**：在 Open VLM Leaderboard 上，允许 2.5 点 CI 宽度放宽时，评估成本最高减少 **80%**，同时维持统计显著性；即使是追求更窄 CI 的场景也能显著节省。该方法面向多模型、多数据集的排行榜场景，通用性强。
