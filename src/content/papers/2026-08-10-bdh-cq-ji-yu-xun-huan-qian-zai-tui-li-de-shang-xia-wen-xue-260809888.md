---
title: 'BDH-CQ: In-Context Learning with Recurrent Latent Reasoning'
title_zh: BDH-CQ：基于循环潜在推理的上下文学习模型
authors:
- Björn Engdahl
- Adrian Kosowski
- Jan Chorowski
- Zuzanna Stamirowska
- Przemysław Uznański
- Junlin Jiang
- Rohan Phadke
- Remigiusz Kinas
- Richard Zhong
affiliations:
- Pathway
- Bielik AI
- New York University
arxiv_id: '2608.09888'
url: https://arxiv.org/abs/2608.09888
pdf_url: https://arxiv.org/pdf/2608.09888
published: '2026-08-10'
collected: '2026-08-13'
category: Reasoning
direction: 潜在空间循环推理 · 低成本高效推理
tags:
- latent reasoning
- in-context learning
- recurrent memory
- ARC-AGI-1
- cost efficiency
one_liner: BDH-CQ 以循环潜在推理避免逐 token 中间推理，150M 参数在 ARC-AGI-1 达 29.5% pass@2，成本 $0.0007/任务
practical_value: '- 小型循环潜在推理模块可替代显式 CoT，用于商品属性抽取、query 意图分类等高频轻量任务，降低 tokens 费用与延迟，适合线上部署。

  - 循环记忆持续更新机制可借鉴到实时用户行为序列建模，如点击流增量处理，避免每次重算完整序列，但需验证长程依赖捕捉能力。

  - 评估模型时引入成本-精度帕累托分析，在 Agent 工作流中为简单任务配置低成本潜在推理模型，复杂决策再调用大模型，优化整体 ROI。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：现有 CoT 推理将计算与串行叙述耦合，中间状态必须通过离散词汇表投影、自回归生成并再次消费，导致 token 消耗、延迟和推理成本快速增长。潜在推理允许在连续隐藏状态中反复计算，只解码最终答案。
方法关键点：BDH-CQ 结合 in-context learning 与 recurrent latent reasoning；推理时输入持续更新循环记忆，模型在高维潜在空间迭代计算，不口头化中间步骤；并通过受控 ARC-like 干预分析模型从演示中学到什么、转换应用一致性及困难概念。
关键结果：150M 参数配置在 ARC-AGI-1 上达到 29.5% pass@2，单任务推理成本仅 $0.0007，突破此前成本-精度帕累托前沿，成为成本效率新 SOTA。
