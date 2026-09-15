---
title: Competence-Gated Pooling of Language Models and Priors for Event Forecasting
title_zh: 基于能力门控的 LLM 与先验融合预测
authors:
- Aditi Tiwari
- Aashrith Bandaru
- Heng Ji
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2609.12101'
url: https://arxiv.org/abs/2609.12101
pdf_url: https://arxiv.org/pdf/2609.12101
published: '2026-09-09'
collected: '2026-09-15'
category: LLM
direction: LLM 预测融合与门控校准
tags:
- competence gating
- forecast combination
- calibration
- LLM forecasting
- Brier score
- abstention
one_liner: 提出 competence gate 依据边际价值选择性融合 LLM 与外部先验，显著降低 Brier 损失
practical_value: '- 在多信号融合场景（如商品 CTR 预估中融合 LLM 打分与传统模型打分），不要只看单个模型 AUC，改用历史 outcome
  估计每个源的边际贡献（例如增量 NDCG 或 Brier），并按领域/场景学习一组 gate 权重，对不确定的领域权重向全局权重 shrinkage，避免小样本过拟合。

  - 当外部先验信号较强（如成熟推荐系统、市场预测）时，可让 gate 学会 defer，而非强制融合；在 baseline 很强时 LLM 融合可能无显著收益，可提前做
  ablation/显著性检验决定是否上线复杂的混合模块。

  - 论文发现 verbal confidence（模型自己说“置信度”）不能可靠判断模型何时优于外部预测，因此别用 LLM 输出的“信心分”作为路由/采纳依据；应基于可观测结果（如成交、点击后的
  label）回估 competence，驱动 abstention 或降权。

  - 融合后对 pooled forecast 做 recalibration（如 temperature scaling / isotonic regression）是低成本的稳定提升，尤其在各源校准不一致时；部署时可作为标准后处理。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：混合预测系统中，LLM 只是多个可用信号之一，已有市场/群体/统计先验时，关键问题不是模型单独精度，而是相对能力（边际价值）。已有研究多关注 standalone accuracy，缺少系统方法判断何时融合、何时忽略。

**方法**：在 Brier loss 下，分析模型与外部预测 disagreement 可改善外部预测的条件，推导 domain-specific pooling 相比 global pooling 的增益。提出 competence gate：用 resolved outcomes 估计 domain-level source weights，对不确定估计向全局权重 shrinkage，再对 pooled forecast 做 recalibration。保留 defer 选项。

**结果**：在 2,357 个 resolved binary questions、5 个 LLM 上，gate 将外部 baseline Brier 从 0.0771 降至 0.0732，显著优于 global combination；在 leakage controls 下仍显著。但在 ForecastBench official market subset 上无显著提升，因为 gate 主要 defer 到市场。四个 Qwen 模型上，verbal confidence 不能可靠识别模型何时优于外部预测，而 outcome-estimated competence 支持更好的 abstention。
