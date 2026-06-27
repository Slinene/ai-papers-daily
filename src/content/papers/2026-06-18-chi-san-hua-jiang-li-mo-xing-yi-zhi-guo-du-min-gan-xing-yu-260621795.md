---
title: Discretizing Reward Models
title_zh: 离散化奖励模型：抑制过度敏感性与奖励黑客
authors:
- Vijay Viswanathan
- Shiqi Wang
- Devamanyu Hazarika
- Chirag Nagpal
- Tongshuang Wu
- Graham Neubig
- Yuning Mao
affiliations:
- Carnegie Mellon University
- Meta Superintelligence Labs
arxiv_id: '2606.21795'
url: https://arxiv.org/abs/2606.21795
pdf_url: https://arxiv.org/pdf/2606.21795
published: '2026-06-18'
collected: '2026-06-27'
category: Training
direction: 奖励模型离散化与RL训练优化
tags:
- Reward Model
- Oversensitivity
- Monte Carlo Dropout
- Discretization
- RLHF
- Reward Hacking
one_liner: 用蒙特卡洛dropout将连续奖励离散化，减少奖励模型的过度敏感性，改善RL策略质量
practical_value: '- 训练推荐对话Agent的RLHF流程中，连续奖励模型易对相似回答给出不同分，导致策略过度优化，可借鉴离散化方法，用少量聚类标签代替原始分数，抑制奖励黑客。

  - 工程实现极简：无需重训奖励模型，仅对现有模型注入Monte Carlo dropout，通过多次采样聚类得到离散奖励标签（如高/中/低），可直接插入现有RL训练管线。

  - 评估奖励模型时，除准确率外建议关注“判别能力”与“特异性”（特异性高=过度敏感低），这两项指标更贴近下游策略效果，对挑选或调试奖励模型有直接指导意义。

  - 在生成式推荐（如直接生成物品ID或描述）中，若用奖励模型作为生成质量信号，离散化可稳定训练、减少模式坍塌，尤其适用于用GRPO等RL算法优化推荐生成的场景。'
score: 6
source: huggingface-daily
depth: abstract
---

连续奖励模型虽然能捕捉回复的细微差异，但普遍存在**过度敏感**问题：对同等质量的回复给出明显不同的分数，这一缺陷在理论上可证明（完美奖励模型仍可能高度敏感），在实践中则引发奖励黑客和策略恶化。

为解决此问题，论文提出一种**免训练**的离散化算法：对任意神经奖励模型施加Monte Carlo dropout，多次采样得到同一样本的多个分数，再聚类形成离散奖励标签（如{优,良,差}）。理论保证存在一种离散化，能在仅牺牲极小的判别能力下显著降低过度敏感性。

在控制实验和真实RL场景（如指令遵循、偏好对齐）中，使用离散化奖励指导策略训练，相比原始连续奖励，**奖励黑客行为减少**，最终策略质量更高。该方法无需修改模型结构或重新训练，可直接嵌入现有RLHF流程。
