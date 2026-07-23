---
title: 'SLPO: Scaling Latent Reasoning via a Surrogate Policy'
title_zh: SLPO：通过替代策略优化实现潜在推理的扩展
authors:
- Runyang You
- Zhiyuan Liu
- Yongqi Li
- Wenjie Li
affiliations:
- The Hong Kong Polytechnic University
- Sichuan University
arxiv_id: '2607.19691'
url: https://arxiv.org/abs/2607.19691
pdf_url: https://arxiv.org/pdf/2607.19691
published: '2026-07-21'
collected: '2026-07-23'
category: Reasoning
direction: 强化学习 · 潜在推理 · 测试时扩展
tags:
- latent reasoning
- reinforcement learning
- test-time scaling
- surrogate policy
- outcome-reward RL
- Chain-of-Thought
one_liner: 提出替代潜在策略优化（SLPO），用经验密度和自适应停止将结果奖励RL引入潜在推理，实现测试时扩展
practical_value: '- **潜在计算可用于推荐Agent的推理加速**：在对话推荐或商品解释生成中，用连续向量代替显式CoT token，可大幅降低服务端推理成本，SLPO的RL训练方式可直接优化这种潜在表示。

  - **替代密度思想可借鉴到无似然生成场景的信用分配**：当推荐系统的生成模块（如生成式检索）的中间状态不可微时，可构造经验替代分布来分配轨迹级奖励，实现端到端优化。

  - **自适应停止头可动态控制推荐Agent的思考深度**：根据用户查询的复杂程度（如长尾商品推荐 vs. 热门商品），动态分配潜在计算步数，平衡效果与延迟，这与搜索/推荐中的动态路由需求一致。

  - **RL+潜在推理的范式可迁移到多步推荐策略优化**：例如在多轮对话推荐中，将隐式状态更新建模为潜在轨迹，用最终转化信号作为奖励进行RL训练，实现推荐策略的自适应优化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：显式思维链（CoT）推理虽可通过结果奖励RL实现测试时扩展，但每一步都需解码为离散token，成本高昂。潜在推理将中间计算维持在连续向量空间，步数更少且效果匹配显式CoT，但现有方法主要基于模仿学习，缺乏RL优化，因为潜在轨迹无逐步似然和自适应停止接口，无法利用结果奖励进行扩展。

**方法关键点**：提出SLPO（替代潜在策略优化），包含两个核心设计：1) 经验替代策略密度：在潜在转移上构建一个替代分布（如基于历史轨迹的核密度估计），用于轨迹级信用分配，使REINFORCE式梯度估计可行；2) 正确性监督的停止头：用结果正确性信号训练一个二分类停止预测器，在RL训练中自动细化为可变视界的自适应停止策略，动态分配潜在步数。

**关键结果**：在连续思考和软思考两种潜在推理范式下，SLPO显著提升并行采样时的Pass@k指标，并能在困难实例上分配更长的潜在计算，同时确定性解码的准确率更高，验证了潜在测试时扩展的有效性。
