---
title: How Model Growth, Recursion, and Boundary Operators Influence Scaling Exponents
title_zh: 模型增长、递归与边界算子如何影响 scaling 指数
authors:
- Zixi Chen
- Akshay Vegesna
- Samip Dahal
- Andrew Gordon Wilson
affiliations:
- New York University
- Q Labs
arxiv_id: '2609.19107'
url: https://arxiv.org/abs/2609.19107
pdf_url: https://arxiv.org/pdf/2609.19107
published: '2026-09-16'
collected: '2026-09-17'
category: Training
direction: 模型架构与训练效率 scaling 分析
tags:
- Scaling Laws
- Looped Transformers
- Recursive Depth
- Model Growth
- Compute Efficiency
- Boundary Operator
one_liner: 发现架构干预可改变预训练 scaling 指数，循环深度带来计算效率随规模递增的指数级收益
practical_value: '- 在算力受限的推荐/广告大模型训练中，可尝试循环深度（looped transformer）实现参数共享下的模型增长：训练时逐步增加循环次数，比单纯堆叠层更省显存，且计算效率随规模提升。

  - 边界算子（boundary operator）对 vanilla transformer 即插即用，仅通过归一化并注入前一个 block 就能获得递增的计算效率增益，适合作为轻量级改进直接迁移到现有架构。

  - 数据受限、多 epoch 场景下，循环深度有正则化效果，推荐在用户行为序列等重复训练数据上优先增加循环次数而非扩大模型宽度。

  - 核心结论：架构干预可以改变 scaling 指数，意味着不再只依赖增大模型和数据，通过设计递归或注入结构可能获得指数级收益，值得在排序/召回大模型预训练中探索。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：scaling laws 通常认为架构改动只影响常数，难以改变指数。本文探索架构干预能否修改预训练 scaling 指数，从而获得随计算量递增的效率提升。

**方法关键点**：以 looped transformer 为锚点，将递归深度（recursive depth）作为模型增长手段：训练时增加循环次数，可共享权重或不共享。同时提出边界算子（boundary operator），在 vanilla transformer 中归一化并注入前一个 block，以低成本增加有效深度。通过计算深度（computational depth）视角分析：给定预算，提升 transformer 可用深度可带来随规模递增的效率收益。

**关键结果**：7.4B 的模型增长架构在 CORE 上匹配 GPT-3 13B 性能，计算量约少 20 倍，且效率增益随规模扩大；边界算子也能带来递增的计算效率增益，但幅度较小。在数据受限多 epoch 场景下，标准 looping 有正则化效果，计算最优是随规模增加循环次数。
