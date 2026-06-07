---
title: In-Context Multiple Instance Learning
title_zh: 上下文多示例学习
authors:
- Alexander Möllers
- Marvin Sextro
- Julius Hense
- Gabriel Dernbach
- Klaus-Robert Müller
affiliations:
- Berlin Institute for the Foundations of Learning and Data
- Technische Universität Berlin
- Aignostics
- Charité – Universitätsmedizin Berlin
- Max-Planck Institute for Informatics
arxiv_id: '2606.06458'
url: https://arxiv.org/abs/2606.06458
pdf_url: https://arxiv.org/pdf/2606.06458
published: '2026-06-04'
collected: '2026-06-07'
category: Training
direction: 多示例学习 · 上下文预训练
tags:
- Multiple Instance Learning
- In-Context Learning
- Perceiver
- Synthetic Data
- Few-Shot
one_liner: 合成数据预训练Perceiver上下文学习器，单次前向传播实现少标签MIL分类，平均性能超越专训基线
practical_value: '- 电商推荐中可将用户行为序列视为袋，利用少量已标记袋（如购买）进行多示例弱监督，识别关键行为物品

  - 上下文学习范式可实现推理时仅提供少量示例即适应新推荐任务，免去逐任务微调，适合多场景快速上线

  - 合成数据预训练策略可迁移至推荐冷启动：生成合成用户会话数据预训练排序模型，增强小样本下的归纳偏置

  - Perceiver 架构可高效处理任意长度用户行为序列，无需截断或填充，适合推荐系统长序列建模'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：多示例学习（MIL）在病理、遥感等领域依赖包级标签，但现实标注严重不足，少量标记包下现有模型易过拟合或归纳偏置不匹配，任务特定训练无法泛化。

**方法**：提出在多种合成MIL数据生成器上预训练一个基于Perceiver架构的上下文学习器，使其能从少量标记包中提取任务信息，并在一次前向传播中完成新包分类，推理阶段无需梯度更新。多种生成器提供互补的归纳偏置，混合预训练继承各自优势。

**结果**：在12个MIL基准数据集上，混合生成器预训练的模型取得最佳平均性能，超越需任务特定训练的监督基线，验证了少量标签下上下文学习的有效性与泛化能力。
