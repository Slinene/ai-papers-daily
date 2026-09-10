---
title: Difficulty-Adaptive Tree-Structured Policy Optimization for Expanding Reasoning
  Coverage in RLVR
title_zh: 难度自适应树结构策略优化以扩展RLVR中的推理覆盖
authors:
- Youngjun Yu
- Sanghwan Jang
- Hwanjo Yu
affiliations:
- Pohang University of Science and Technology (POSTECH)
arxiv_id: '2609.08650'
url: https://arxiv.org/abs/2609.08650
pdf_url: https://arxiv.org/pdf/2609.08650
published: '2026-09-07'
collected: '2026-09-10'
category: Training
direction: RLVR训练策略优化 · 树搜索
tags:
- RLVR
- Tree Search
- Pass@k
- Reasoning Coverage
- Policy Optimization
one_liner: 提出DATPO，通过难度自适应树搜索和句子熵引导分叉提升pass@k，增强测试时缩放能力
practical_value: '- 在对话式推荐或搜索Agent的多步决策训练中，可借鉴难度自适应采样：根据问题难度动态分配rollout深度/宽度，避免简单样本浪费算力，同时让困难样本获得更多探索机会，提升策略覆盖率。

  - 树搜索结构比并行采样更利于发现正确答案，可用于训练阶段的策略探索；结合句子级熵引导分叉（而非token级）能增强语义多样性，对生成推荐理由或搜索query改写等开放式生成任务有参考价值。

  - 引入sibling-diversity advantage term，显式鼓励同一父节点下不同分支的语义差异，可迁移到多臂老虎机或beam search解码中，用于生成多样化的商品文案、广告标题或推荐理由。

  - 该工作主要针对数学推理，业务场景直接迁移需谨慎，但RLVR训练中通过结构化探索扩大策略覆盖的思路，对需要长程推理的Agent（如多轮商品筛选、意图澄清）有启发性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR虽提升单样本准确率，但训练探索不足限制模型内在推理覆盖（pass@k），影响测试时缩放（如多数投票、MCTS）的上限。

**方法关键点**：
- 通过分析提出三条设计原则：难度自适应rollout不仅为效率，更能扩展pass@k；树搜索优于并行采样；句子熵引导分叉（而非token级）可克服局部化现象，最大化语义多样性。
- 提出DATPO，融合难度自适应树搜索与sibling-diversity advantage项，显式促进语义多样性。
- 在数学推理基准上验证。

**关键结果**：DATPO尤其在pass@k上显著优于基线，直接转化为更优的测试时缩放性能，表明训练阶段扩大推理覆盖能提升下游推理能力。
