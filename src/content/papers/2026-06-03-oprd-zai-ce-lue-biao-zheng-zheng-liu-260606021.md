---
title: 'OPRD: On-Policy Representation Distillation'
title_zh: OPRD：在策略表征蒸馏
authors:
- Shenzhi Yang
- Guangcheng Zhu
- Bowen Song
- Haobo Wang
- Mingxuan Xia
- Xing Zheng
- Yingfan Ma
- Zhongqi Chen
- Weiqiang Wang
- Gang Chen
affiliations:
- Zhejiang University
- Ant Group
arxiv_id: '2606.06021'
url: https://arxiv.org/abs/2606.06021
pdf_url: https://arxiv.org/pdf/2606.06021
published: '2026-06-03'
collected: '2026-06-05'
category: Training
direction: 策略蒸馏 · 表征对齐
tags:
- on-policy distillation
- representation alignment
- LLM
- post-training
- sample efficiency
one_liner: 将在策略蒸馏从输出空间提升到隐藏状态空间，消除采样方差并提供更丰富的结构化监督信号
practical_value: '- **用表征蒸馏替代输出空间KL**：在训练小模型（如电商客服、推荐解释）时，可直接对齐学生与教师中间层隐藏状态，绕过庞大的词表投影，消除采样方差，使训练更稳定，尤其适用于大词表（如中文150k+）场景。

  - **内存与速度优化**：OPRD loss在LM head之前计算，避免存储完整词表分数矩阵，训练速度快1.44倍，内存减少54%，适合资源受限的线上微调或频繁迭代。

  - **层间对齐可迁移到多模态或推荐模型**：方法不限于文本，可扩展到多模态表征蒸馏（如视觉-语言对齐），或用于推荐系统中用户/物品编码器的迁移学习，将复杂大模型知识压缩到轻量级线上模型。

  - **提供确定性、逐层结构监督**：相比输出蒸馏的稀疏奖励，表征蒸馏给出逐位置、逐层的稠密信号，利于捕捉细粒度语义，对于对话Agent的多轮一致性、推荐解释生成等任务可能更有效。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有在策略蒸馏（OPD）只在输出空间通过匹配下一词概率监督学生，存在两大局限：① 在大词表上基于采样的KL估计始终存在方差，训练后期梯度噪声占据主导；② 仅使用教师模型的概率输出，丢弃了所有中间隐藏状态，这些状态包含丰富的层间结构信息。

**方法**：提出OPRD，首次将在策略蒸馏提升到隐藏状态空间。在相同的在策略轨迹上，将学生与教师选定层的中间表示对齐，提供稠密的确定性监督，完全绕过LM head。理论上，OPRD消除了梯度估计的采样方差，并暴露了教师每层、每位置的额外结构信息，监督信号严格更丰富，且不增加额外推理成本。

**结果**：在三个竞赛级数学基准（AIME 2024, AIME 2025, AIMO）上，OPRD使学生-教师差距缩小至接近零，而输出空间OPD基线均停滞在教师水平以下。同时，OPRD训练速度快1.44倍，actor更新瞬态内存使用最多减少54%。
