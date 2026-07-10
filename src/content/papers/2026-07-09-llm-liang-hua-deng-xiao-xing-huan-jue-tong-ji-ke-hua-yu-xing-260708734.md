---
title: 'The Illusion of Equivalency: Statistical Characterization of Quantization
  Effects in LLMs'
title_zh: LLM 量化等效性幻觉：统计刻画与行为分歧度量
authors:
- Baha Rababah
- Cuneyt Gurcan Akcora
- Carson K. Leung
affiliations:
- University of Manitoba
- Red River College Polytechnic
- University of Central Florida
arxiv_id: '2607.08734'
url: https://arxiv.org/abs/2607.08734
pdf_url: https://arxiv.org/pdf/2607.08734
published: '2026-07-09'
collected: '2026-07-10'
category: Training
direction: 量化效应分析 · 行为分歧度量
tags:
- quantization
- correctness agreement
- attention analysis
- behavioral divergence
- LLM evaluation
one_liner: 提出 correctness agreement 指标揭示量化导致的行为分歧，发现 query/key 投影对量化更敏感
practical_value: '**可以在推荐/搜索系统中这样借鉴：**

  - 部署量化推荐模型（如 LLM-based ranker）时，不能只监控离线 AUC/GAUC，应引入 correctness agreement 这类行为指标，防止量化后模型对同一批样本给出迥异的精排序结果，却因整体指标持平而被忽略。

  - 研究发现 query 和 key 投影层比 value/output 投影对量化更敏感；在混合精度量化策略里，可优先保留这几层为高精度（如 INT8 甚至
  FP16），降低推荐模型推理成本的同时，守住 query–item 匹配的稳定性。

  - 低比特（≤4-bit）存在非线性断点，业务落地时建议以 8-bit 作为安全起始点，逐步尝试 6/4-bit，并逐层分析 attention 分布的 KL
  散度，避免直接跳进极低精度带来的冷启动召回崩溃。

  - correctness agreement 不依赖绝对准确率，可作为生成式推荐（如 Semantic ID 生成）的评估指标：量化后生成 item 序列与全精度模型的一致性，比困惑度更能反映线上效果。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机：** 当前 LLM 量化评估几乎完全依赖困惑度和任务准确率，这些指标无法反映模型决策层面的行为变化。在资源受限场景部署推荐、搜索模型时，量化带来的隐蔽行为分歧可能导致不可预期的线上效果抖动。

**方法关键点：**
- 提出 **correctness agreement**：度量基模型与量化变体在正确预测样本上的重叠率，与绝对准确率解耦。
- 将量化视作注意力权重的结构算子，逐层统计权重分布的扭曲程度（如 KL 散度）以及 query/key/value/output 投影矩阵的敏感度差异。
- 实测参数涵盖 8-bit 至 2-bit 多方案、多模型，寻找量化引起行为分歧的临界比特位宽。

**关键结果：**
- 即使准确率看似保持，中度量化（如 4-bit）已产生显著行为分歧，形成“等效性幻觉”。
- query 和 key 投影对量化噪声最敏感，value 和 output 投影相对鲁棒。
- 低比特位宽（≤4-bit）出现非线性断点，模型行为急剧偏离全精度基线。
这些发现主张在部署量化模型时采用行为层面的评估，而不仅是传统性能指标。
