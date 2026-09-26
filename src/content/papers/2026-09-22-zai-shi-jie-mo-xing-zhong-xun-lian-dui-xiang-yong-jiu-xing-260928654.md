---
title: Training Object Permanence in World Models
title_zh: 在世界模型中训练对象永久性
authors:
- Haotian Zhang
- Fengyuan Yu
- Dezhi Luo
- Haoran Sun
- Zehong Zhao
- Qingying Gao
- Yihan Li
- Siyuan An
- Huayi Qin
- Yilan Zhang
affiliations:
- University of Southern California
- Carnegie Mellon University
- University of Michigan
- Johns Hopkins University
- University of California, San Diego
arxiv_id: '2609.28654'
url: https://arxiv.org/abs/2609.28654
pdf_url: https://arxiv.org/pdf/2609.28654
published: '2026-09-22'
collected: '2026-09-26'
category: Multimodal
direction: 视频世界模型 · 对象永久性推理
tags:
- Object Permanence
- Video Generation
- World Models
- Procedural Data
- Elo Evaluation
- Physical Reasoning
one_liner: 构建 150 类认知任务 Blender 数据生成器，产出 1.5M 视频训练集并微调 16B 模型，在对象永久性盲测中 continuation
  类第一
practical_value: '- 借鉴程序化生成数据的思路：把核心认知/业务结构固定（如用户意图、商品属性关系），随机化干扰因子（视角、光照、渲染参数）批量合成训练样本，用于提升多模态模型对核心特征的鲁棒性，类似电商商品图/视频的合成增强。

  - 构建小规模但高针对性的任务族 + 专门微调：用 150 类认知任务、每类 10k 样本的紧凑数据即可在特定物理推理能力上超过大模型，可用于快速补齐商品视频生成、3D
  试穿等模型的物理合理性短板。

  - 盲测 Elo 评估范式：对多个生成模型输出做匿名成对比较再计算 Elo，比单指标分数更接近人类感知排序，适合评估广告文案、商品描述或推荐理由生成质量。

  - 发布权重和训练栈的做法可参考：如果要复现或继续微调，公开训练栈和权重能降低多模态模型训练成本，团队内也可沉淀类似工具。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：对象永久性与固体性是人类核心认知先验。视频生成模型作为当前世界模型的主要形式，已开始展现推理能力，但尚不清楚它们是否具备对象永久性，以及能否通过核心认知启发数据集进行训练。

**方法**：构建 WROP（World Reasoning with Object Permanence）数据基础设施，包含 150 个手工设计的认知科学任务，划分为 6 个认知类别。使用 Blender 生成器随机化速度、光照、相机角度等干扰参数，同时保持任务的核心认知结构，每任务生成 10,000+ 样本。最终发布 1.5M 样本训练集和 300 题考试。评估 14 个视频模型：3 个 reference-to-video、7 个 edit、4 个 continuation，其中包括 16B 微调模型 PWM-WROP。采用盲测成对 Elo 评分。

**关键结果**：PWM-WROP 在 continuation 模型中排名第一，整体排名第三，仅次于两个 reference-to-video 模型之间的统计平局。数据、考试、模型答案、分数、权重及 AWS Trainium2 原生 PyTorch 训练栈均已公开。
