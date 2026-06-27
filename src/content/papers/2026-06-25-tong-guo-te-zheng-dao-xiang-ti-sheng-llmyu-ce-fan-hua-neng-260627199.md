---
title: 'Forecasting With LLMs: Improved Generalization Through Feature Steering'
title_zh: 通过特征导向提升LLM预测泛化能力
authors:
- Humzah Merchant
- Bradford Levy
affiliations:
- University of Chicago
arxiv_id: '2606.27199'
url: https://arxiv.org/abs/2606.27199
pdf_url: https://arxiv.org/pdf/2606.27199
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: LLM 预测偏置纠正 · 特征干预
tags:
- feature steering
- sparse autoencoders
- look-ahead bias
- forecasting
- LLM interpretability
- temporal reasoning
one_liner: 用稀疏自编码器识别LLM的时间感知特征，通过放大这些特征减少预测中的前瞻偏差
practical_value: '- **避免时序泄露**：在推荐系统中用 LLM 做用户行为预测时，可通过类似特征干预方法，确保模型基于历史信息而非未来数据生成推荐，防止离线评估虚高。

  - **特征发现与调控**：利用稀疏自编码器探查模型内部是否包含“时间作弊”特征，并抑制这类特征，提升线上实时预测的可靠性。

  - **生成式推荐中的因果干预**：若使用 LLM 直接生成推荐列表（GenRec），可借鉴特征放大/抑制策略，强制模型依赖因果性更强的用户兴趣表征，减少流行度偏差。

  - **领域迁移稳健性**：论文展示跨领域干预有效，提示对电商多场景（如不同品类）下的 LLM 推荐，可共享时间感知特征，降低场景迁移时的重新训练成本。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 应用于预测任务时，容易利用训练数据中的未来信息（look-ahead bias）得到高离线性能，但无法泛化到真实在线预测场景，需要方法迫使模型基于历史信息进行推理。

**方法**：使用稀疏自编码器（sparse autoencoder）分析 LLM 在预测提示下的内部表征，识别出两类关键特征——时间感知（time-awareness）特征和前瞻偏置（look-ahead-bias）特征。通过在不同领域的任务上干预这些特征：放大时间感知特征，或抑制偏置特征，观察预测行为变化。

**关键结果**：放大时间感知特征能显著降低前瞻偏差（look-ahead bias），同时保持一般推理能力；而直接操控偏置特征无效。这表明可解释的时间特征可因果性地将 LLM 引导至更基于历史信息的推理方式。
