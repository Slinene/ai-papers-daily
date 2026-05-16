---
title: 'Pause and Reflect: Conformal Aggregation for Chain-of-Thought Reasoning'
title_zh: 暂停与反思：思维链推理的共形聚合
authors:
- Yu Gu
- Zijun Yu
- Vahid Partovi Nia
- Masoud Asgharian
arxiv_id: '2605.14098'
url: https://arxiv.org/abs/2605.14098
pdf_url: https://arxiv.org/pdf/2605.14098
published: '2026-05-13'
collected: '2026-05-16'
category: Reasoning
tags:
- CoT
- Conformal Prediction
- Reasoning
- LLM
- Uncertainty
- Aggregation
one_liner: 用加权分数聚合与共形风险控制，在有限样本保证下控制自信错误率并提升选择性准确率
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：思维链（CoT）推理通过聚合多个采样路径提升性能，但聚合规则的不确定性常导致自信错误——当弃权比错答成本更低时，这种风险不可接受。多数投票等传统聚合方法无法量化此不确定性，也无法提供形式化保证。

**方法**：提出一种纯推理时的共形聚合框架。首先用加权分数聚合替代多数投票，捕捉各推理路径的相对置信度；其次利用共形风险控制校准弃权规则，保证在有限样本下，系统回答但错误的概率（自信错误率）不超过预设目标α。进一步识别“得分可分性”作为弃权可证明提升选择性准确率的关键条件，并给出从校准数据预测准确率增益的封闭解。整个过程无需微调或额外训练。

**关键结果**：在GSM8K、SVAMP等四个数学推理基准上，使用LLaMA-3和Mistral等四个开源模型，结合自洽性分数、幻觉概率等三类评分，所有场景的实测自信错误率均稳定在目标值附近（如α=5%）。当在GSM8K弃权不足5%时，选择性准确率达90.1%，显著超过多数投票基线（82%）。同时，得分可分性的理论预测与实际增益高度吻合，验证了方法的可靠性。
