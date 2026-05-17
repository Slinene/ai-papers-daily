---
title: 'TabPFN-3: Technical Report'
title_zh: 'TabPFN-3: 大规模表格基础模型的速度与性能突破'
authors:
- Léo Grinsztajn
- Klemens Flöge
- Oscar Key
- Felix Birkel
- Philipp Jund
- Brendan Roof
- Mihir Manium
- Shi Bin
- Hoo
- Magnus Bühler
affiliations:
- Prior Labs
arxiv_id: '2605.13986'
url: https://arxiv.org/abs/2605.13986
pdf_url: https://arxiv.org/pdf/2605.13986
published: '2026-05-13'
collected: '2026-05-17'
category: RecSys
direction: 表格基础模型规模化与推理加速
tags:
- tabular foundation model
- test-time compute scaling
- KV cache
- synthetic data
- AutoML
- scalability
one_liner: 基于合成数据预训练的表格基础模型，通过测试时计算扩展和工程优化，在多种表格任务上超越调优集成方法，速度提升20倍
practical_value: '- 合成数据预训练范式可迁移至电商推荐特征工程：不依赖真实标签，用先验生成大量多样化表格数据训练基础模型，冷启动场景潜力大。

  - 测试时计算扩展（Thinking模式）思路可借鉴至推荐模型推理阶段：对复杂样本动态分配更多前向次数或集成，以可控计算成本换取显著效果提升，适合高价值决策场景。

  - 工程优化直接复用：通过缩减KV缓存和row-chunking支持百万行数据单卡推断，可应对推荐系统海量用户-物品交互数据。

  - SHAP值计算加速120倍：若业务需用SHAP进行模型可解释性分析，可参考其KV缓存复用策略，大幅降低线上或离线归因耗时。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：表格数据预测是工业与科学的核心，但现有模型难以兼顾大规模数据下的高性能与低延迟。TabPFN-3旨在打破这一瓶颈，将基础模型能力扩展至千万行级，并融入时间序列、关系数据等多模态。

**方法关键点**：
- 仅用合成数据预训练，完全避免对真实标注的依赖。
- 引入测试时计算扩展（Thinking模式），通过增加推理计算量大幅提升困难样本表现。
- 工程上精简KV缓存，配合行分块（row-chunking），实现在单张H100 GPU上高效处理百万行数据。
- 统一架构适配分类、回归、时序预测、关系预测和表格-文本混合任务。

**关键结果**：
- 在标准表格基准TabArena上，单次前向传播即超越所有调优和集成基线，占据性能/速度帕累托前沿。
- API版本TabPFN-3-Plus (Thinking) 相对非TabPFN模型Elo提升超200点，最大数据子集上领先420点，比AutoGluon 1.5 extreme快10倍以上。
- 在RelBenchV1和TabSTAR上分别取得关系数据和表格-文本数据SOTA。
- 专用时序版本TabPFN-TS-3在fev-bench排名第二；SHAP值计算加速120倍。
- 推理速度比TabPFN-2.5快20倍。
