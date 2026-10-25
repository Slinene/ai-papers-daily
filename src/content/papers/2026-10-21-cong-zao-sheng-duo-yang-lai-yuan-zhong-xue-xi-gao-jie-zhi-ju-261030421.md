---
title: High-Value Training Data from Noisy, Diverse Sources
title_zh: 从噪声、多样来源中学习高价值训练数据权重
authors:
- Hedi Driss
- Evan Frick
- Anastasios N. Angelopoulos
- Cho-Jui Hsieh
- Yejin Huh
- Tijana Zrnic
- Andrew Ilyas
affiliations:
- Hiddenweights
- Arena
- UCLA
- Stanford
- CMU
arxiv_id: '2610.30421'
url: https://arxiv.org/abs/2610.30421
pdf_url: https://arxiv.org/pdf/2610.30421
published: '2026-10-21'
collected: '2026-10-25'
category: Training
direction: 训练数据加权 · 元梯度学习
tags:
- Data Weighting
- Meta-Learning
- Reward Modeling
- Synthetic Data
- Domain Adaptation
one_liner: 用目标域小数据集元梯度优化训练样本权重，学得可泛化、可迁移的加权规则，提升奖励模型对噪声与合成数据的利用效率
practical_value: '- 在电商/广告的 LLM 奖励模型或偏好对齐中，维护一个高质量目标域评测集（如人工标注的偏好对、业务 KPI 相关的判分），用元梯度自动学习每个训练样本的权重，替代手工噪声过滤规则，尤其适合点击日志、用户评论等噪声多样的数据。

  - 参数化加权规则可以部署为流式数据选择器：对新到达的样本实时预测权重，做过滤或重采样，适合推荐系统的大规模 UGC、曝光点击日志等持续数据流，降低存储与训练成本。

  - 合成数据与人工数据混合时不再依赖固定比例，而是学习每个样本的权重，让混合数据超过任一单独来源；可复用到生成式推荐的物品描述、query 改写、广告文案生成的合成数据利用场景。

  - 先在小模型上学习数据权重规则，再迁移到更大模型，能显著降低大规模训练的数据清洗与调参成本，是一种工程上可行的 Data-Centric AI 方案。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

动机：现代模型训练依赖大规模异构数据，质量、领域相关性、监督来源参差不齐，手工设计过滤或混合策略成本高且依赖人类判断。数据加权是通用控制手段，但大规模学习有效权重仍困难。

方法关键点：给定一个小的高质量目标数据集，通过训练过程的元梯度（meta-gradients）直接优化每个训练样本的权重，目标是在目标域上获得最佳性能。为解决扩展到新样本和流式数据的问题，进一步学习参数化的加权规则，该规则能对新样本进行泛化，并能从小模型迁移到大模型。方法在奖励建模任务上验证：偏好数据可能包含噪声、对抗、合成或与目标域不匹配的情况。

结果：学习到的数据权重提升了 held-out 性能，自动将奖励模型适配到特定领域，并让人类与合成监督的数据混合在效果上超过单独使用任一来源。
