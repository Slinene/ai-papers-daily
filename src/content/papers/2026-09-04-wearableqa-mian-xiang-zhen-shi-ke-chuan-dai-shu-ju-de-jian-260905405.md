---
title: 'WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data'
title_zh: WearableQA：面向真实可穿戴数据的健康推理基准
authors:
- Ji Soo Lee
- Xilun Chen
- Pierce Chuang
- Ashish Shenoy
- Jason Wei
- Dohwan Ko
- Hyunwoo J. Kim
- Benoit Corda
affiliations:
- Meta
- KAIST
- Korea University
arxiv_id: '2609.05405'
url: https://arxiv.org/abs/2609.05405
pdf_url: https://arxiv.org/pdf/2609.05405
published: '2026-09-04'
collected: '2026-09-07'
category: Eval
direction: LLM 评估 · 健康时序推理
tags:
- WearableQA
- LLM Benchmark
- Health Reasoning
- Wearable Data
- Temporal Reasoning
- Multiple Choice
one_liner: 构建4084题真实可穿戴健康推理基准，覆盖16种题型，评估14个LLM准确率仅19.6%–72.9%
practical_value: '- 可迁移其「数据推理 vs 健康推理」的题型划分，用于评估推荐/电商场景中 LLM 对用户长期行为序列的推理：区分简单统计聚合（如近30天购买频次、复购率）与业务语义解释（如消费力迁移、流失风险），并设计单信号与跨信号交叉问题检验多域融合能力。

  - dual-grounding 框架值得复用：结合领域先验规则与统计显著模式生成多选题，可避免纯模板生成的表面线索，用于构建商品属性问答、用户画像推理评测集。

  - 保留真实数据分布（设备噪声、个体差异）的评测思路有借鉴意义：不要只用清洗后的聚合特征评测 LLM，应让模型接触原始事件序列和噪声，检验鲁棒性。

  - 直接业务借鉴有限，但对保险/健康电商、用户运营 Agent 等涉及可穿戴信号场景，提供了一套可落地的真实数据评测模板。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：可穿戴设备持续产生生理与行为信号，但现有基准很少评估 AI 能否对真实用户的长程穿戴记录进行推理。文章引入 WearableQA，填补这一空白。

**方法关键点**：
- 数据来自 200 名真实用户，每人最多 500 天每日测量，融合可穿戴时间序列、血液生物标志物与人口统计信息。
- 构建 4084 道 10 选项多选题，保留真实分布中的设备噪声与个体差异。
- 设计 16 种题型，沿两个轴划分：数据推理 vs 健康推理（统计计算 vs 生理解释）、单信号 vs 跨信号推理（单一信号 vs 多信号融合）。
- 采用 dual-grounding 框架：结合文献中的生理发现与统计验证的人群生理模式，确保问题可靠且可规模化生成。

**关键结果**：评估 14 个闭源与开源 LLM，准确率从 19.6% 到 72.9%，随机基线为 10%；多数模型低于 60%，表明该基准远未解决且能有效区分模型能力。
