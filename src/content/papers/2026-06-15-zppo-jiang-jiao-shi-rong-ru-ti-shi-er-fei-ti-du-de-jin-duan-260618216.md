---
title: 'Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients'
title_zh: ZPPO：将教师融入提示而非梯度的近端策略优化
authors:
- Byung-Kwan Lee
- Ximing Lu
- Shizhe Diao
- Minki Kang
- Saurav Muralidharan
- Karan Sapra
- Andrew Tao
- Pavlo Molchanov
- Yejin Choi
- Yu-Chiang Frank Wang
affiliations:
- NVIDIA
arxiv_id: '2606.18216'
url: https://arxiv.org/abs/2606.18216
pdf_url: https://arxiv.org/pdf/2606.18216
published: '2026-06-15'
collected: '2026-06-17'
category: Training
direction: 基于提示的教师引导强化学习训练
tags:
- ZPPO
- Knowledge Distillation
- Reinforcement Learning
- Prompt Engineering
- Small Model Training
- Vision-Language Models
one_liner: 在困难样本上，教师通过构造对比提示替代策略梯度注入，使学生模型摆脱蒸馏与GRPO的局限。
practical_value: '- **难例训练范式**：当RL训练的智能体（如对话推荐Agent）在稀疏奖励场景下持续失败时，可将更强模型或模拟器的正确答案作为对比提示注入，而非直接蒸馏logits或修改梯度，避免策略漂移。

  - **对比式提示构造**：借鉴BCQ和NCQ，将正确与错误响应匿名配对，让学生模型自行判别，可迁移至推荐系统候选列表的对比学习，提升模型对优劣结果的辨识力。

  - **动态困难样本重放**：采用基于准确率的提示重放缓冲区，让模型反复练习尚未掌握的困难例，直到毕业，有助于解决推荐场景中长尾物品或冷启动样本的训练不足问题。

  - **小模型增效**：最小学生规模（0.8B）时提升最显著，适合在边缘设备部署的轻量级推荐或意图识别模型，用ZPPO替代传统蒸馏以保持更强泛化能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：知识蒸馏让小模型强迫模仿大教师的最强模式，损害泛化；强化学习（GRPO）在困难样本上所有生成均失败（零优势），丢弃样本导致学习停滞，若直接注入教师响应又破坏on-policy假设，引起策略漂移。

**方法**：受维果茨基“最近发展区”启发，提出ZPPO，将教师置于提示而非策略梯度中。对困难问题构造两种提示：（1）Binary Candidate-included Question (BCQ) 将一条正确教师响应与一条错误学生响应匿名配对，让学生辨别正确选项；（2）Negative Candidate-included Question (NCQ) 汇总学生的错误生成，暴露共享失败模式。同时设计一个提示重放缓冲区，以FIFO维护困难问题，并重复出题直到该问题平均准确率达50%才“毕业”，使训练始终聚焦于学生当前可学会的最高难度区间。

**结果**：在Qwen3.5系列四个学生尺寸（0.8B-9B）上，以27B模型为教师，后训练为视觉-语言模型，于31个基准（16 VLM, 10 LLM, 5 Video）评估，ZPPO全面超越离线/在线蒸馏与GRPO，最小模型增益最大，验证了“教师进提示”在小模型训练中的有效性。
