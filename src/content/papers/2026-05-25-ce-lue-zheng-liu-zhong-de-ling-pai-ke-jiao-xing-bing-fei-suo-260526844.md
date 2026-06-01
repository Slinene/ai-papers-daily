---
title: 'Not All Disagreement Is Learnable: Token Teachability in On-Policy Distillation'
title_zh: 策略蒸馏中的令牌可教性：并非所有分歧都可学习
authors:
- Yuanyi Wang
- Su Lu
- Yanggan Gu
- Pengkai Wang
- Yifan Yang
- Zhaoyi Yan
- Congkai Xie
- Jianmin Wu
- Hongxia Yang
affiliations:
- The Hong Kong Polytechnic University
- InfiX.ai
arxiv_id: '2605.26844'
url: https://arxiv.org/abs/2605.26844
pdf_url: https://arxiv.org/pdf/2605.26844
published: '2026-05-25'
collected: '2026-06-01'
category: Training
direction: LLM 训练 · 策略蒸馏令牌选择优化
tags:
- On-Policy Distillation
- Token Teachability
- Selective Distillation
- Knowledge Distillation
- LLM Training
one_liner: 提出令牌可教性区分可学习与不可兼容的分歧，TA-OPD 仅保留 5% 高可教性令牌蒸馏即可超越全令牌训练
practical_value: '- **蒸馏效率与效果提升**：当在电商场景中蒸馏LLM用于商品描述、推荐理由或Agent对话时，可借鉴TA-OPD仅对“可教性”高的token位置施加蒸馏，避免低效甚至有害的监督信号，实验仅用5%令牌即超越全令牌蒸馏，显著节省计算。

  - **无需额外模型**：TA-OPD仅利用教师和学生logits计算局部兼容性，无需奖励模型或验证器，易于集成到现有蒸馏流程（如生成式推荐中的语义ID生成器蒸馏）。

  - **信号质量重新审视**：揭示了原始KL散度作为学习价值代理的缺陷，提示在设计蒸馏损失时，应优先关注教师分布与学生top-K候选重叠高的token，而非简单加权高分歧位置，这对多智能体策略迁移中避免灾难性遗忘有参考价值。

  - **算法轻量化**：可教性计算简单，能在训练时动态筛选token，为推荐系统或Agent中频繁更新的小模型提供了一种低成本、高性能的在线蒸馏策略。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：策略蒸馏（OPD）通过教师分布监督学生自回归生成的每个token，但现有选择性方法多基于高熵或高KL散度筛选token，假设分歧大的位置更重要。本文质疑这一假设，探究哪些教师信号真正可被学生学习。

**方法**：通过固定上下文的诊断实验，度量同一上下文下教师-学生KL散度的降低程度，发现原始KL分歧会混叠两类信号：一是**可学习分歧**，即教师分配了校正质量到学生的top-K候选中；二是**不可兼容分歧**，即教师分布与学生当前支持集几乎无重叠。据此定义**令牌可教性**为教师分布在学生top-K候选上的累积概率，即局部兼容性。提出**TA-OPD**，只对高可教性的token位置施加OPD损失，无需额外模型。

**结果**：在Qwen2.5和Qwen3的多组师生实验中，TA-OPD仅保留5%的令牌，常超越全令牌OPD，并优于基于熵或KL散度的选择基线。结论：选择性蒸馏应关注信号的可学习性，而非单纯显著性。
