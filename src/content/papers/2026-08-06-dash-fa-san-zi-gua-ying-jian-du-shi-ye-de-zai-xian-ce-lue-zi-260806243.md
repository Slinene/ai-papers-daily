---
title: 'DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation
  of Reasoning Models'
title_zh: DASH：发散自适应监督视野的在线策略自蒸馏
authors:
- ZhiYan Hou
- Xinyu Tang
- Hongyan An
- Jianjin Zhang
- Weizhen Wang
- Yunyun Han
- Gengsheng Li
- Xiangzhao Hao
- Haiyun Guo
- Wenbin Hu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- EverMind
- Shanda Group
- University of Chinese Academy of Sciences
- Wuhan AI Research
arxiv_id: '2608.06243'
url: https://arxiv.org/abs/2608.06243
pdf_url: https://arxiv.org/pdf/2608.06243
published: '2026-08-06'
collected: '2026-08-08'
category: Training
direction: 蒸馏训练 · 推理优化
tags:
- On-Policy Self-Distillation
- RLVR
- Token-Level Supervision
- Adaptive Gating
- Mathematical Reasoning
- LLM
one_liner: 提出DASH，根据局部发散与序列均值的差异自适应调整token级蒸馏权重，提升推理模型在线策略自蒸馏效果
practical_value: '- 在推荐/广告场景的生成式模型训练中（如Semantic ID生成），若采用教师-学生在线蒸馏，可引入 DASH 的自适应门控机制，根据生成过程中每个token的偏差程度动态调整蒸馏损失权重，避免对所有token同等对待。

  - 该方法不增加额外前向计算，仅复用已有的教师和学生分布，工程实现成本低，适合在已有OPSD流程中快速叠加。

  - 对于使用RLVR训练推荐Agent的场景，可将 DASH 作为token级奖励塑形的一种手段，结合 KL 散度权重自适应调整，平衡探索与利用。

  - 核心 trick：构建局部发散与全局均值的 gap 作为门控信号，可通过 simple 的递归聚合实现，无需复杂时序模块，易于部署。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：在线策略自蒸馏（OPSD）通过在学生探索到的前缀上询问教师模型，提供稠密的token级分布监督，缓解RLVR中奖励稀疏问题。但标准OPSD对所有时间步的局部发散赋予相同系数，忽略了自回归生成中发散历史的时序上下文：相同的发散幅度可能跟随不同的历史轨迹，反映不同的师生分布偏离演化，固定权重无法区分。

**方法**：提出发散自适应监督视野（DASH）。计算每个token的局部蒸馏信号（如KL散度）与序列均值的差值，将其通过一个可学习的门控函数映射为自适应传播门；然后使用这些门进行反向多步加权聚合，生成该位置最终的自适应蒸馏权重。这样，在发散剧烈或变化快的区域自动获得更高或更低监督强度。

**结果**：在 GSM8K、MATH 等三个数学推理基准上，使用三种规模模型（7B、13B、33B）实验，DASH 在全部设置下均优于匹配的普通 OPSD rerun，且无需额外教师或学生前向传播，计算开销极小。
