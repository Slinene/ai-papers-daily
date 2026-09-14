---
title: 'MAxBench: A Multinomial Concept Recovery Benchmark'
title_zh: MAxBench：多类别概念恢复基准
authors:
- Divya Appapogu
- Freya Behrens
- Yonatan Belinkov
- Aaron Mueller
affiliations:
- Boston University
- Technion – Israel Institute of Technology
- Harvard University
arxiv_id: '2609.13072'
url: https://arxiv.org/abs/2609.13072
pdf_url: https://arxiv.org/pdf/2609.13072
published: '2026-09-11'
collected: '2026-09-14'
category: Eval
direction: 可解释性 · 多类别概念表示评估
tags:
- interpretability
- concept representation
- steering
- evaluation benchmark
- affine subspace
- multinomial concepts
one_liner: 提出几何无关的评估框架 MAxBench，比较 10 种方法，发现仿射子空间最优且优势源于偏移项
practical_value: '- 在需要控制多类别概念（如商品属性、兴趣标签）的生成式推荐或 Agent 中，仿射子空间表示（线性方向 + 非零偏移）比纯线性方向更可靠；若自行训练类别方向，应学习
  offset 而非只学 basis，可显著提升召回和可控性。

  - MAxBench 的采样评估方式（从表示中采样而非直接测量距离）可迁移到评估不同表示学习方法（如 LoRA、adapter、prompt 等）对多类别属性的操控效果，避免几何假设过强。

  - 论文发现 no method consistently beats prompting，提示在业务中做可控生成时，先用 prompt 基线验证概念可操控性，再决定是否需要更复杂的
  internal steering。

  - 本文属可解释性方向，对电商/搜索推荐直接业务价值有限，但若涉及模型内容安全/风格控制/属性操控，可参考其评估思路。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

## 动机
可解释性研究常聚焦二元概念（如拒绝），单一激活方向即可实现 steering。但 ANIMALS、COUNTRIES 等概念包含多个子类，表示几何搜索空间远大于二元情况，不清楚哪种几何结构最适合，什么恢复方法最有效。

## 方法
提出 MAxBench，一个几何无关的评估框架，通过从恢复的概念表示中采样来评估多类别概念表示。比较 10 种定位方法，覆盖 5 种几何类型（rank-one、线性子空间、仿射子空间、流形等），在 6 个概念和 4 个模型上系统评估。

## 关键结果
- 仿射子空间比 rank-one 或线性子空间 steer 更可靠，召回率更高；
- 该优势主要来自非零偏移，而非基向量选择；
- 流形 steering 在适用时与最佳方法相当；
- 无方法在一致性上超越 prompting，与二元概念发现一致。

这些发现表明可解释性研究和元评估需要扩展到结构更多样的概念。
