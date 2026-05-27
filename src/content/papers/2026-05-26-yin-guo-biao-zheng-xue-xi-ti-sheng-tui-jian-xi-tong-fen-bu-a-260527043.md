---
title: Causal Representation Learning for Generalisable Recommendation
title_zh: 因果表征学习提升推荐系统分布外泛化：从信息解耦到线上A/B验证
authors:
- Yorgos Felekis
- Michael O'Riordan
- Oriol Corcoll
- Ciarán M. Gilligan-Lee
affiliations:
- University of Warwick
- Spotify
- University College London
arxiv_id: '2605.27043'
url: https://arxiv.org/abs/2605.27043
pdf_url: https://arxiv.org/pdf/2605.27043
published: '2026-05-26'
collected: '2026-05-27'
category: RecSys
direction: 因果表征学习 · 分布偏移优化
tags:
- causal representation learning
- mutual information
- distribution shift
- debiasing
- A-B test
- recommender systems
one_liner: 提出互信息解耦准则去除表征中的非因果依赖，在Shopify线上A/B测试中显著提升用户参与度，而离线指标不起变化
practical_value: '- 直接在标准排序损失上增加一个互信息惩罚项（通过梯度反转实现去相关），无需额外数据、不改推理架构，即可消除物品表征中的非因果泄露，适用于任何现有监督模型。

  - 离线指标（如AUC）可能完全反映不出线上收益：论文三种场景下CRL模型在偏置训练集上离线指标与基线持平，但在随机曝光测试集和线上A/B中均显著胜出。建议多用随机曝光测试集或小流量线上实验评估分布外真实效果。

  - 调参安全：理论表明存在“无损耗”区间，较小的惩罚权重λ即可去掉非因果信息，不损害预测效用；实践中可用NCE-CLUB上界监控互信息下降量。

  - 工程落地简单：方法与具体模型解耦，无需干预数据或多环境分划，仅用现有观测日志训练，适合大规模推荐系统快速部署。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机
推荐系统训练数据受部署策略和曝光偏差影响，训练分布与服务分布严重偏移，导致离线指标无法可靠预测线上表现。因果表征学习可从原理上解决该问题，但经典方法多依赖干预数据、多环境假设或具体偏置结构。本文提出一种仅用观测日志、信息论驱动的解耦准则，通过移除表征中与混淆变量（用户表示）相关的非因果信息，使模型在分布偏移下更具鲁棒性。

## 方法关键点
- **解耦准则**：最大化条件互信息 `I(g(T);Y|Z)`（预测效用）并惩罚 `I(g(T);Z)`（与混淆变量Z的依赖），即 `J(g)=I(g(T);Y|Z) – λ·I(g(T);Z)`，从混杂的输入T中分离出纯因果成分。
- **理论性质**：证明最优表征仅保留因果隐变量TC，丢弃非因果TnC，且存在一个λ区间（“无损耗区”）完全保留TC而不牺牲预测力。
- **变分下界实现**：效用项用InfoNCE下界（即常规排序损失），惩罚项用NCE-CLUB上界；实际优化中用梯度反转降低InfoNCE下界来替代上界计算，简单且有效。
- **部署友好**：方法不影响模型无关，只需在标准监督模型上添加一个互信息惩罚头，无推理时延或额外数据需求。

## 关键实验
- **合成SCM**：CRL模型在干预非因果维度后的预测变化近乎为零，而基线受严重干扰；两模型MAE持平，验证方法有效去除非因果泄露。
- **KuaiRand基准**：DeepFM基线在偏置训练集AUC 0.757 vs. CRL 0.751，但在随机曝光测试集上AUC提升+0.013，Recall@5提升+0.009，NDCG@5提升+0.017，展现分布外鲁棒性。
- **Spotify线上A/B测试**（数百万用户）：CRL变体使曲目流播+0.75%，跳过率-0.61%，播放分钟+0.50%，均达到95%显著水平。值得注意的是，离线指标与基线无差异，线上增益完全不可见。

## 核心结论
一个极简的互信息惩罚，能让推荐模型在分布偏移下取得显著线上收益，而离线评估对此完全失明——这应是所有推荐工程师记住的关键教训。
