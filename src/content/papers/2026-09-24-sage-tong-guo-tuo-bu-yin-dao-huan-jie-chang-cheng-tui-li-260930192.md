---
title: 'SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance'
title_zh: SAGE：通过拓扑引导缓解长程推理偏差
authors:
- Xinyue Zeng
- Jiawei Zhang
- Yujun Yan
- Dawei Zhou
affiliations:
- Virginia Tech
- University of Wisconsin Madison
- Dartmouth College
arxiv_id: '2609.30192'
url: https://arxiv.org/abs/2609.30192
pdf_url: https://arxiv.org/pdf/2609.30192
published: '2026-09-24'
collected: '2026-09-25'
category: Reasoning
direction: LLM 长程推理 · 拓扑结构引导
tags:
- Long-Horizon Reasoning
- Sparse Reward
- Topological Guidance
- Hyperbolic Embedding
- Algebraic Sparsification
- LLM
one_liner: 用代数稀疏化与双曲结构引导的SAGE框架，缓解长程推理的探索偏差与累积偏差，12基准7模型家族提升，AC问题8倍改善
practical_value: '- 在Agent多步规划（如导购Bot多轮需求澄清、商品筛选）中，候选步骤常局部合理但全局不可行；可借鉴代数稀疏化，对每步算子做结构约束投影/过滤，只保留可采纳分支，压缩搜索宽度、减少跳转幻觉。

  - 双曲结构引导可用到长流程状态表示：将多步决策的状态embedding从欧氏空间改为Poincaré/Lorentz双曲空间，能更自然编码层级与深度信息，为稀疏奖励过程提供稠密的深度连续信号。

  - 稀疏奖励场景不要只依赖最终结果做RL；可显式建模“局部可采纳性”作为过程监督/辅助reward，比如在召回→粗排→精排的多级funnel中为每阶段定义可采纳条件，缓解累积偏差。

  - 业务可借鉴点有限：SAGE偏符号/数学推理，开放域推荐对话中定义算子索引代数子空间成本较高，但结构先验与候选分层约束可直接用于受限Action空间的Agent决策。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**  
LLM 在长程推理中，当只有稀疏最终奖励时，容易受两种偏差影响：exploration bias 使模型偏向局部合理但全局不稳定的分支；compounding bias 使小的局部偏差随深度累积、压制稀有奖励。现有 outcome-based post-training 在数学和代码任务上有效，但长程、稀疏奖励下仍脆弱。

**方法关键点**  
作者先提出 Symbolic Closure Analysis (SCA)，刻画分支结构与稀疏奖励如何引入两种偏差，并作为设计结构先验的原则。基于此设计 SAGE 框架，注入两类结构引导：
- **Algebraic sparsification**：将局部可采纳的候选投影到算子索引的代数子空间，抑制虚假分支，缓解 exploration bias。
- **Hyperbolic structural guidance**：把推理状态嵌入负曲率双曲空间，提供稠密的深度方向信号，缓解 compounding bias。

**关键结果数字**  
在 12 个 benchmark、7 个模型家族上超越竞争基线；在开放真实长程任务 Andrews-Curtis 问题上最高获得 8 倍提升。代码已开源。
