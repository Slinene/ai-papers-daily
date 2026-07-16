---
title: Consensus as Privileged Context for Label-Free Self-Distillation
title_zh: 共识作为特权上下文实现无标签自蒸馏
authors:
- John Gkountouras
- Josip Jukić
- Ivan Titov
affiliations:
- ILLC, University of Amsterdam
- ILCC, University of Edinburgh
arxiv_id: '2607.13643'
url: https://arxiv.org/abs/2607.13643
pdf_url: https://arxiv.org/pdf/2607.13643
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 无标签自蒸馏 · 共识锚定
tags:
- Label-Free Self-Distillation
- Consensus Anchoring
- Majority Voting
- Test-Time Training
- Reasoning
- Self-Improvement
one_liner: 用多票共识充当特权上下文，将投票信号转化为逐token的密集监督，替代RL并接近带标签蒸馏
practical_value: '- 在无标注的推理场景（如电商搜索对话/商品理由生成）中，可通过采样多个回复、多数投票提取共识答案，将对应的高置信回复作为教师上下文进行自蒸馏，实现无黄金答案的模型提升

  - 采用JSD散度进行全词表分布蒸馏，比硬标签SFT保留更多信息，且能利用非共识rollout中的差异信号，适合处理模糊或长尾输出

  - 冻结教师快照，避免共享参数训练时迅速崩塌的问题，是低成本稳定蒸馏的关键工程技巧

  - 一次采样同时获得投票结果和蒸馏数据，训练仅一个epoch，在精度-计算量前沿上显著优于TTRL等RL方案，适合资源受限的线上业务快速迭代'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：大语言模型的推理能力提升通常依赖带可验证奖励的强化学习，但黄金答案难以获取。多票一致性（self-consistency）虽能无监督提升准确率，却常被压缩成标量伪奖励或仅用于答案筛选，丢失了达成共识的完整推理信息。本文研究如何将投票产生的共识答案作为“特权上下文”，通过自蒸馏将一致性信号转化为逐token的密集监督，实现无标签的高效自我改进。

**方法关键点**：
- **共识提取**：对每个无标签提示采样N条推理链路，提取多数答案，再从多数集中选出平均对数概率最高的链路作为共识解。
- **教师锚定**：冻结模型快照，将共识解作为额外上下文喂入教师，教师对每条学生采样逐位置计算下一token分布；教师不参与梯度更新。
- **全词表蒸馏**：最小化学生与教师分布间的Jensen-Shannon散度（对称有界，避免KL模式崩塌），覆盖所有采样链路，包括与共识不一致的链路。
- **轻量高效**：仅需一次生成（与推理时的self-consistency相同），单轮训练（一个epoch），无需奖励模型或重复采样，通过LoRA微调。

**关键实验**：
- **直推式测试时训练**：在AMC数学竞赛、AIME、GPQA科学等基准上，CANON提升pass@1最高达12个点，比无标签RL（TTRL等）高出约6点，计算量仅为其1/7，且接近带有黄金解的oracle蒸馏（AMC 76.5 vs 76.9）。
- **归纳迁移**：在不相交的AIME 2024上，AMC训练后的模型提升7个点；使用池化无标签数学集训练后，在AIME 2024上达到41.7，匹敌黄金奖励RL和黄金条件蒸馏。
- **超越纯概率集中**：多数投票准确率与pass@32均有提升，模型能解决之前32次采样从未解出的问题，增益集中在原模型置信度低但共识正确的困难样本上。
- **适用条件**：当基模型共识准确率高于单样本准确率且未饱和时收益最大；在已饱和或共识可靠性低的提示上增益有限甚至为负。

**一句话记忆**：用投票结果直接构造教师上下文进行全词表蒸馏，无标签、单轮训练就接近带标签教师的水平，且大幅优于同计算量的RL。
