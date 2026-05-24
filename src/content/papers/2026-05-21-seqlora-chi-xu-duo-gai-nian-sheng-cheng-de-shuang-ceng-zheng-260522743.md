---
title: 'SeqLoRA: Bilevel Orthogonal Adaptation for Continual Multi-Concept Generation'
title_zh: SeqLoRA：持续多概念生成的双层正交适配方法
authors:
- Javad Parsa
- Enis Simsar
- Amir Joudaki
- Thomas Hofmann
- André M. H. Teixeira
affiliations:
- Uppsala University
- ETH Zurich
arxiv_id: '2605.22743'
url: https://arxiv.org/abs/2605.22743
pdf_url: https://arxiv.org/pdf/2605.22743
published: '2026-05-21'
collected: '2026-05-24'
category: Multimodal
direction: 持续多概念扩散模型正交 LoRA 微调
tags:
- Continual Learning
- LoRA
- Text-to-Image Generation
- Multi-Concept
- Bilevel Optimization
- Catastrophic Forgetting
one_liner: 通过双层优化联合学习 LoRA 因子，在持续学习新概念时强制正交约束，最小化灾难性遗忘和组合干扰
practical_value: '- **持续多任务 LoRA 微调范式**：当需要在电商场景中不断引入新商品概念或新用户画像时，可借鉴 SeqLoRA 顺序微调而不遗忘旧知识，避免每次重新训练或复杂融合。

  - **双层优化稳定子空间**：底层更新 LoRA 基（A）保持跨任务共享，上层学习任务特定系数（B），并加入正交约束，适合推荐系统中多类目 Embedding
  的增量学习，减少特征干扰。

  - **正交正则化抗遗忘**：在 Agent 多技能训练中，强制新技能 LoRA 与旧技能正交，可防止技能间干扰，提升持续学习效果。

  - **残差能量最小化**：理论表明最小化残差干扰能量比冻结基方法更优，可迁移到序列推荐或多轮对话的状态更新中，通过正则化残差保持历史信息。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：参数高效的 LoRA 微调使个性化文生图成为可能，但顺序学习多个概念时，不同概念的 LoRA 权重会产生表示干扰，导致组合生成时身份丢失或属性混淆。现有方案要么依赖昂贵的后融合步骤，要么冻结适配子空间，牺牲模型容量。

**方法**：SeqLoRA 将多概念持续学习形式化为双层优化问题。底层优化 LoRA 矩阵 A（基）使其跨概念共享，并学习如何从数据中适应基；上层对每个新概念学习 LoRA 矩阵 B（系数），同时施加正交约束：新概念的 B 列须与之前所有概念的 B 列正交，并添加正则项最小化层内激活残差的能量，从理论上保证灾难性遗忘的高概率界。训练时，SeqLoRA 顺序微调，无需存储旧概念数据，仅通过正交投影和残差正则化维持旧知识。

**结果**：在包含 101 个概念的多概念生成基准上，SeqLoRA 显著提升身份保留度，属性干扰率降低。相比需要后融合的方法（如正交 LoRA 融合），SeqLoRA 在避免融合计算的同时，组合生成的 FID 和 CLIP 分数更优。理论分析也证明了算法的收敛性及残差能量最小化的优势。
