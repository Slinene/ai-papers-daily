---
title: Trust Region Policy Distillation
title_zh: 信任区域策略蒸馏
authors:
- Zhengpeng Xie
- Li Lyna Zhang
- Zeke Xie
- Mao Yang
affiliations:
- Hong Kong University of Science and Technology (Guangzhou)
- Microsoft
- Xingyun Zhili
arxiv_id: '2607.04751'
url: https://arxiv.org/abs/2607.04751
pdf_url: https://arxiv.org/pdf/2607.04751
published: '2026-07-05'
collected: '2026-07-13'
category: Training
direction: 信任区域蒸馏训练范式
tags:
- Policy Distillation
- Trust Region
- Training Stability
- On-Policy
- LLM Reasoning
one_liner: 动态构建近端教师将在线策略蒸馏转化为稳定训练，理论保证梯度方差控制且零额外开销
practical_value: '- 推荐系统的强化学习训练（如对话推荐）可借鉴：用当前学生策略与目标教师策略的**移动平均**构造近端教师，替代固定教师监督，缓解梯度方差，提升训练稳定性，无需额外推理开销。

  - 蒸馏时引入**信任区域约束**，避免学生一次性追随强教师导致的剧烈更新，相当于在策略空间上做平滑，可防止训练崩溃。

  - 理论部分提供**单调改进界**，在电商/广告场景中对风险敏感的策略优化（如出价策略、排序策略）有直接指导意义，确保迭代更新不会损害累积收益。

  - 零额外计算量的特点适合工业级大规模在线蒸馏，可参考其**动态混合系数**的简单实现，快速落地到现有 teacher-student 框架。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：在线策略蒸馏（OPD）通过外部固定教师提供 token‑级信号，但训练不稳定、梯度方差高，不利于 LLM 后训练。

**方法关键点**：提出信任区域策略蒸馏（TOP‑D），每次迭代**动态构建一个近端教师**——它是当前学生策略与目标教师策略的加权混合，权重由 KL 散度约束决定。学生从该近端教师学习，更新被限制在信任区域内，从而抑制方差。理论上证明了梯度方差有界，并给出**全局收敛分析和单调改进界**，形式化保证训练稳定可靠。

**关键结果**：在数学推理基准 AIME 上，基于 Qwen3‑8B‑Base 学生和 30B 教师，TOP‑D 显著超越 OPD 和基线 RLVR。AIME24 avg@32 准确率：TOP‑D 50.42 vs OPD 24.58；AIME25：34.06 vs 23.33；AIME26：44.06 vs 25.42。训练曲线显示方差大幅降低，且方法**不引入任何额外计算开销**。
