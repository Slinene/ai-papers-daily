---
title: Deliberate Latent Reasoning for Sequential Recommendation
title_zh: 序列推荐的审慎潜在推理
authors:
- Haobo Zhang
- Qiannan Zhu
- Yutao Zhu
- Zhicheng Dou
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- School of Artificial Intelligence, Beijing Normal University
- Engineering Research Center of Intelligent Technology and Educational Application,
  MOE
arxiv_id: '2611.06521'
url: https://arxiv.org/abs/2611.06521
pdf_url: https://arxiv.org/pdf/2611.06521
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 序列推荐 · 个性化潜在推理
tags:
- Sequential Recommendation
- Latent Reasoning
- Self-Distillation
- Personalization
- Transformer
one_liner: 提出个性化潜在推理深度选择与自蒸馏压缩最优状态，避免固定步数过推理或欠推理。
practical_value: '- 可在用户塔引入轻量推理步数选择器，按行为序列复杂度动态决定 latent reasoning 深度，避免固定步数过/欠推理；适合线上序列长度分布广的推荐/广告模型，降低平均推理成本并提升长尾用户建模。

  - 训练时用自蒸馏把最优中间状态压缩到最终表示，线上只走固定路径，不增加推理开销；可迁移到广告排序/召回的用户编码器，作为复杂训练、简单推理的通用范式。

  - 渐进偏好提取按用户历史动态分段为可变数量 latent milestone，替代固定时间窗或 session 切割；适合电商场景分阶段总结长期兴趣，显式建模兴趣漂移。

  - 该 latent 推理不生成自然语言，可作为生成式推荐 semantic ID 解码前的用户表示增强模块，提升个性化生成质量。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有 latent reasoning 序列推荐对所有用户采用固定推理步数，简单历史可能过度思考、复杂历史思考不足，导致用户表示学习次优。  
**方法**：DESRec 引入两部分：一是推理步数选择模块，训练阶段为每条用户序列识别最优推理步数；通过自蒸馏机制，将最优中间状态压缩到最终推理步，推理时仅用最终用户表示做商品排序。二是渐进偏好提取，将用户历史动态分割为可变数量的时期，每段汇总成一个 latent milestone 表示该阶段偏好，并作为后续推理输入。milestone 数量随用户历史变化，实现个性化兴趣演进建模。  
**结果**：在 6 个公开数据集、4 个 backbone 推荐器上验证，优于 8 个基线模型。
