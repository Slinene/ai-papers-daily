---
title: 'Learning Style, Forgetting Semantics: A Case Study of SFT and RFT on Classification
  Tasks'
title_zh: 学习风格，遗忘语义：SFT与RFT分类任务案例研究
authors:
- Haodong Liang
- Yanhao Jin
- Krishnakumar Balasubramanian
- Lifeng Lai
affiliations:
- University of California, Davis
arxiv_id: '2610.02437'
url: https://arxiv.org/abs/2610.02437
pdf_url: https://arxiv.org/pdf/2610.02437
published: '2026-10-01'
collected: '2026-10-05'
category: Training
direction: 微调遗忘机制 · SFT vs RFT
tags:
- SFT
- RFT
- forgetting
- fine-tuning
- style drift
- theory
one_liner: 理论证明SFT因风格漂移导致语义遗忘下界为正，而RFT保持零语义误差
practical_value: '- 在业务中持续微调LLM（如搜索/推荐文案生成、query改写）时，若教师数据存在风格偏好，SFT可能把模型带偏到风格维度而遗忘底层语义能力；可监控风格漂移指标，或对提示分布做均衡化。

  - 当任务需要保持跨风格一致性（如同一语义的多种表达），优先考虑RFT/策略梯度或加入风格不变正则，避免SFT因非均匀教师产生离轴漂移。

  - 理论框架可指导混合训练：在已有较好拟合的checkpoint上继续SFT时，注意前几步更新的方向，防止在风格上过拟合；必要时用RFT微调或对SFT更新做投影约束。

  - 该工作主要偏理论学术贡献，业务可借鉴点有限，核心价值在于提供理解SFT遗忘的新视角。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：SFT与RFT都会造成灾难性遗忘，但实验观察表明SFT遗忘更严重，即使教师演示语义完全正确。已有解释多从数据分布或优化角度出发，缺少对更新动态的细粒度分析。

方法关键点：在分类任务中，同一语义类别下不同token表达同一答案但风格不同。作者采用可解的线性-softmax策略，将更新精确分解为语义分量和风格分量。在共同策略与提示下，SFT与RFT的语义更新平行，但风格动态不同：从无类内风格偏好的策略出发，RFT的精确策略梯度保持对称性，而SFT在非均匀教师下沿非零任务均值产生离轴风格漂移。基于该漂移，在总体更新且从完美拟合checkpoint出发的显式条件下，可建立分离结果。

关键结果：SFT的语义遗忘在有限训练区间内存在严格正下界，而RFT保持零语义误差。任务序列上的仿真实验支持理论预测。
