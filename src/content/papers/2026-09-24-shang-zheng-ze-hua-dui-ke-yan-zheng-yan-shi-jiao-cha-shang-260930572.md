---
title: 'Entropy Regularization: A Free Correction to Cross-Entropy for Verified Demonstrations'
title_zh: 熵正则化：对可验证演示交叉熵的免费修正
authors:
- Mihir Dhanakshirur
- Adam Ousherovitch
- Ambuj Tewari
affiliations:
- Department of Statistics, University of Michigan
arxiv_id: '2609.30572'
url: https://arxiv.org/abs/2609.30572
pdf_url: https://arxiv.org/pdf/2609.30572
published: '2026-09-24'
collected: '2026-09-28'
category: Training
direction: LLM 后训练 · 熵正则化
tags:
- Entropy Regularization
- Cross-Entropy
- Verifiable Tasks
- Post-training
- LLM
- Reasoning
one_liner: 提出 ER-CE，用 token 级熵正则化防止概率质量扩散到未支持的输出，提升可验证任务 verifier 准确率
practical_value: '- 在生成式推荐/文案生成等多正确解可验证场景（如商品标题是否符合规则、推荐理由是否准确），后训练若只用 CE 模仿单一 gold
  答案，可能学到次优分布。可尝试在 loss 中加入 token 级熵正则项，实现只需对 logits 计算熵再加权合并，几乎零额外成本，避免模型过度自信于某一路径。

  - 若任务有可验证的 reward（如搜索 query 改写后召回率、广告文案离线规则校验），而训练数据每个样本只给一个专家解，直接 CE 可能偏离最大化 verifier
  准确率。可借鉴 ER-CE 思路，使策略保留更多样化的正确输出概率，而非只模仿给定演示。

  - 注意熵正则化会鼓励输出分布更均匀，可能降低生成确定性，影响线上体验（如推荐文案需风格稳定）。实际落地时需小范围调熵系数，先在线下验证集评估 verifier
  acc 与多样性的 trade-off。

  - 该文主要针对数学/代码，部分思路可迁移，但电商/推荐场景的 verifier 往往较弱或缺失，需先定义好规则校验器再使用此正则化。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**
LLM 后训练普遍用交叉熵（CE）模仿专家演示，但在可验证领域（数学推理、代码生成）常有多个正确解，下游目标应是产出任何通过验证器的输出，而非复现特定解。CE 最小化可能与 verifier risk 不一致：两个策略可对观测演示赋予相同似然，却在错误输出上分配了不同概率质量。文中给出学习理论反例，CE 会选出次优策略。

**方法关键点**
核心问题是学习策略的支持集过度扩散到未获演示支持的错误输出。解决思路是控制支持集大小，但支持大小不可微且计算不可行，因此用 token 级 Shannon 熵作为可处理代理，提出熵正则化交叉熵（ER-CE）：在标准 CE loss 上加上 token 级熵正则项，间接约束支持集，防止概率质量扩散到错误输出。

**关键结果**
在数学推理和代码生成基准上，ER-CE 相比标准 CE 一致提升 verifier accuracy，验证了该目标与产出正确输出更好对齐，且实现简单、额外成本极低。
