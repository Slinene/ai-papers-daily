---
title: 'LEV: Thinking Fast and Deep with Looped Decision Models'
title_zh: LEV：循环决策模型实现快速与深度思考
authors:
- Dingjie Song
- Zhiling Yan
- Yuxuan Zhang
- Lichao Sun
affiliations:
- Lehigh University
- University of British Columbia
- Vector Institute
arxiv_id: '2610.20951'
url: https://arxiv.org/abs/2610.20951
pdf_url: https://arxiv.org/pdf/2610.20951
published: '2026-10-13'
collected: '2026-10-19'
category: Reasoning
direction: 循环决策模型 · 自适应深度推理
tags:
- Looped Models
- Decision Models
- Adaptive Computation
- Efficient Inference
- Latency-Accuracy Tradeoff
one_liner: 提出 LEV，通过循环重跑层而非生成 token 实现自适应深度推理，在决策任务上以低计算开销提升准确率
practical_value: '- 在排序/CTR 预估模型中引入循环 Transformer 层，共享权重跑多步，让模型根据样本难度自适应停止，在线推理可节省
  15-24% 计算，准确率损失 <1 点，适合高 QPS 的广告精排场景。

  - 借鉴 LEV 的联合训练策略：对每个循环步骤都计算损失并回传，训练时模拟不同深度，使一个 checkpoint 支持任意推理深度，便于线上动态调整 latency-accuracy
  平衡点，无需部署多套模型。

  - 设计轻量 stopper 网络，利用未标注请求（如线上曝光日志）拟合停止阈值，避免人工标注难度，可直接迁移到推荐系统中做自适应 early exit，在低延迟约束下最大化效果。

  - 该工作表明循环层优于同延迟的稠密模型和级联模型（5.4-8.8 点提升），因此在资源受限的端侧或边缘推荐场景中，优先考虑循环架构而非简单加深或级联。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：传统决策模型（单次前向输出概率）像快思考，深度固定，对简单和困难问题投入相同计算；生成式推理能变深但 token 解码开销大。希望既保持决策模型的直接概率输出，又能按需加深推理。

**方法关键点**：LEV 基于预训练为循环的语言模型，改造为决策模型：每个循环步骤后读取选项，所有步骤联合训练，因此单一权重支持任意深度。无需生成 token，通过循环层实现“思考”。引入小型 stopper 网络，根据未标注请求拟合阈值，实现按需停止。

**关键结果**：在三个循环骨干上，准确率随深度增加而提升，主要在难题；JevBench 上 2.6B 模型深度 1 的 63.2% 提升到深度 4 的 76.2%。按需深度节省 15-24% 计算，准确率损失 <1 点。锁定测试集上，1.4B 和 3B 循环模型比同延迟的稠密模型和级联模型高 5.4-8.8 点。
