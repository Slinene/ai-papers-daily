---
title: 'Detecting an Effect Is Not Learning to Act on It: A Reward-SNR Floor for LLM
  Acquisition Agents'
title_zh: 检测效果不等于学会按例行动：LLM采集智能体的奖励信噪比下限
authors:
- Ying Yuan
affiliations:
- University of California, San Diego
arxiv_id: '2608.10441'
url: https://arxiv.org/abs/2608.10441
pdf_url: https://arxiv.org/pdf/2608.10441
published: '2026-08-11'
collected: '2026-08-12'
category: Agent
direction: LLM信号获取决策 · 奖励信噪比下限
tags:
- LLM Acquisition
- Reward-SNR
- Causal Inference
- Offline Policy Learning
- Recommendation
- Structured Hypothesis Embeddings
one_liner: 揭示LLM信号平均有效但无法学习按例决策的信噪比下限，噪声占位符可复现虚假增益
practical_value: '- 在电商 Agent 决策（如是否调用 LLM 生成推荐文案）前，先计算信号效应的信噪比 ρ=μ/σ，并确保 ρ>2.8/√N，否则学习路由策略将退化为随机。

  - 当信噪比不足时，放弃学习动态按例获取策略，改用设计时的静态分片（如按用户群体、场景开关）来规避无效学习。

  - 验证 Agent 决策可学习性时，必须加入噪声占位符对照：用匹配矩的独立噪声替换信号，若仍能复现≥100%的 Oracle 增益，说明原始“可学习结构”实为噪声排序伪象。

  - 结构化假设嵌入（SHE）提供了一种可解释的用户意图注入方式：用冻结 LLM 生成带置信度的意图列表并嵌入召回或排序模型，适合电商中长短期兴趣解耦，但需注意其对模型
  backbone 敏感，建议先在特定 regime 内验证提升。'
score: 8
source: arxiv-cs.IR
depth: abstract
---

**动机**：推荐系统常引入 LLM 辅助信号（如推理链、意图标签），并希望训练一个 Agent 决定何时获取该信号。但作者发现，即使信号整体显著（平均效果好），也不代表能学出按例决策的策略，因为存在一个关键的信噪比门槛。\n\n**方法**：定义了信号获取决策问题的奖励信噪比（ρ=μ/σ），从理论上推导出离线学习路由策略的必要条件：ρ 必须超过约 2.8/√N，否则任何学习所得策略都不会优于随机，且增益仅来自噪声排序。同时提出结构化假设嵌入（SHE）：用冻结的 LLM 从用户历史中提取 K 个带置信度的意图假设，嵌入后与推荐模型协同训练。在 MIND、REES46、Amazon-Beauty 三个公开数据集上验证。\n\n**关键结果**：SHE 在忠实度、可校准性上表现良好，但与 GRU backbone 相比整体提升微弱（+0.0114），且冗余间隙不显著。更关键的是，在所有粒度（per-instance、cluster、regime）上学习获取策略均失效，因为三个数据集的 ρ 分别为 0.048、0.138、0.014，均低于所需下限。噪声占位符实验证实，增益可被随机噪声完全复现。结论：目前条件下，可行的单元是设计时的分群开关，而非实时按例决策策略。
