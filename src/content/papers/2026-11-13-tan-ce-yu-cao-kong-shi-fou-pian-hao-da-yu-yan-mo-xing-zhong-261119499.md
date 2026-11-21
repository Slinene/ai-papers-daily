---
title: Do Probing and Steering Favor the Same Directions Within and Across Language
  Models?
title_zh: 探测与操控是否偏好大语言模型中的同一方向？
authors:
- Afshin Sadeghi
- Daniel Becker
affiliations:
- Fraunhofer IAIS, Sankt-Augustin, Germany
arxiv_id: '2611.19499'
url: https://arxiv.org/abs/2611.19499
pdf_url: https://arxiv.org/pdf/2611.19499
published: '2026-11-13'
collected: '2026-11-21'
category: LLM
direction: LLM 表征工程与可解释性
tags:
- probing
- steering
- representation engineering
- model transfer
- truthfulness
- sentiment
one_liner: 发现LLM中最佳探针方向不等于最佳操控方向，操控更偏好均值差，跨模型迁移二者表现不同
practical_value: '- 若要在广告文案、客服Agent等场景用 hidden state 方向控制 LLM 的情感、合规或拒答行为，不要直接复用线性探针得到的“概念方向”；探针方向擅长检测，但操控效果通常不是最优，应优先使用均值差方向或做小范围方向扫描。

  - 从开源模型或其它模型迁移可解释方向时，要分开评估：探针方向经简单线性映射即可保留81–91%检测性能，但 steering 向量迁移会明显损失操控效果，需在目标模型上重校准，而非直接复用。

  - 在电商Agent/客服模型中做“不确定时弃答/转人工”干预时，可尝试在 hidden state 加“unknown”方向；它能让模型自身不确定的错误弃答率提升18–44个百分点，但对自信错误几乎无效，适合与置信度分层机制配合，而不是全局强制。

  - 比较方向效果时，应在固定 side-effect 预算下进行统一扫描，避免只关注目标增益而忽略生成长度、相关性等副作用，这种评估方式可直接照搬到业务里的可控生成实验。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM hidden state 中的一个方向既可用于探测概念是否存在，也可用于操控模型朝该概念生成。此前工作常直接复用探针方向做 steering，但检测最好的方向未必是改变行为最好的方向。

**方法关键点**：在3个不同家族的指令微调模型上，构造从协方差调整判别方向到均值差的单参数方向族；在固定副作用预算下，对 truthfulness 和 sentiment 分别评估 probing 准确率与 additive steering 效果；并做跨层扫描、匹配文本实验、旋转算子对照，以及跨模型线性映射迁移。

**关键结果**：在59/60层-模型-概念组合中，最佳探针与最佳操控方向分离，操控一致偏好更接近均值差的方向。sentiment 中，中间方向可比均值差强27–56%，但该增益随文本匹配、层和算子变化而不稳定。跨模型迁移后，探针保留81–91%的 above-chance 检测性能，而转移的均值差 steering 效果在11/12模型对中保留更少。PopQA 应用上，向“unknown”方向 steering 使不确定错误弃答提升18–44个百分点，自信错误仅提升2–5个百分点，且很少纠正原本可答对的错误。
