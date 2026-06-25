---
title: 'Training for the Model You Return: Improving Optimization for Iterate-Averaged
  Language Models'
title_zh: 优化迭代平均语言模型：面向返回模型的训练改进
authors:
- Kwok Chun Au
- Adam Block
affiliations:
- Columbia University
arxiv_id: '2606.25086'
url: https://arxiv.org/abs/2606.25086
pdf_url: https://arxiv.org/pdf/2606.25086
published: '2026-06-23'
collected: '2026-06-25'
category: Training
direction: 迭代平均感知的自适应优化器设计
tags:
- PACE
- exponential moving average
- AdamW
- LM fine-tuning
- pretraining
- optimization
one_liner: 提出PACE优化器，通过将在线权重拉向指数移动平均，提升最终返回的EMA模型性能
practical_value: '- **直接替换AdamW**：PACE是一个即插即用的AdamW封装，仅增加两个额外超参数（控制强度和削波系数），在SFT和预训练场景下对学习率、衰减策略等设定鲁棒，可以快速验证于自己的LLM微调流水线。

  - **配合EMA评估提升生成式推荐模型效果**：在生成式推荐（如Semantic ID生成）或对话Agent的LLM微调时，常返回EMA模型作为最终发布模型。PACE主动让优化过程适应EMA，有望获得更好的泛化表现。

  - **稳定训练，放宽学习率调参约束**：论文显示PACE允许使用更高学习率或更有限的学习率衰减，从而可能减少调参开销并加速收敛，适合需要快速迭代的业务场景（如大促期间的模型更新）。

  - **关注优化器与模型平均的协同**：无论使用EMA还是Polyak平均，此工作提醒我们可以针对返回的平均形式反向设计优化器，这是一种可迁移到其他平均策略（如SWA）的设计思路。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：现代LM流程常返回训练迭代的指数移动平均（EMA）而非最终迭代本身，但优化器并未针对这一返回形式进行设计。核心问题是如何修改训练以提升最终返回的平均模型性能。

**方法关键点**：
- 将针对迭代平均的优化器设计形式化为最优控制问题，在连续时间随机二次模型中求解最小化返回平均误差的控制策略。
- 提出PACE（Pulling Average with Clipped Estimate），一个轻量的AdamW封装：在每步更新中，将当前权重向EMA方向拉动，拉动强度 per-coordinate 且经裁剪，避免过大干预。
- 理论上证明PACE在随机凸优化中保持标准收敛速率，并在二次情形下可严格减小EMA估计的极限平方误差，改善幅度在某些实例上可任意大。

**关键结果**：
- 在1-2B参数LM的监督微调（SFT）和GPT-2规模模型在FineWeb上的预训练中，PACE相较AdamW和EMA-evaluated AdamW，在多种学习率、衰减策略及超参数下均取得更优性能。
- 展现出对超参数的强鲁棒性，允许使用更高学习率或更有限的衰减，并保持训练稳定性。
