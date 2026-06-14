---
title: A Stationary (and Therefore Compatible) Representation is All You Need
title_zh: 平稳即兼容：基于d-Simplex固定分类器的表示学习
authors:
- Niccolò Biondi
- Federico Pernici
- Simone Ricci
- Alberto Del Bimbo
arxiv_id: '2606.12488'
url: https://arxiv.org/abs/2606.12488
pdf_url: https://arxiv.org/pdf/2606.12488
published: '2026-06-09'
collected: '2026-06-14'
category: Training
direction: 模型更新时兼容表示学习
tags:
- Compatible Learning
- Stationary Representation
- d-Simplex Classifier
- Contrastive Loss
- Lifelong Learning
- Retrieval
one_liner: 证明用d-Simplex固定分类器学到的平稳表示天然兼容旧模型，并结合对比损失捕获高阶依赖，无需重索引即可支持不间断检索。
practical_value: '- 电商/推荐系统向量索引更新痛点：模型迭代时通常需要全量重嵌物品，成本极高。本文证明固定d-Simplex分类器可使新旧嵌入分布对齐，实现无需重索引的直接兼容，大幅降低工程开销。

  - 训练技巧：采用固定原型（d-Simplex等角紧框架）作为分类器权重，结合交叉熵与对比损失的凸组合，既保持类别可分离性又强制旧模型兼容性，训练过程即满足兼容约束，可嵌入现有微调流程。

  - 在Agent多智体中，若各Agent维护独立向量记忆库，模型替换时使用该方案可保证记忆库嵌入不失效，避免重新编码历史数据，保障服务连续性。

  - 实验表明对比损失的加入能捕获高阶分布依赖，弥补纯交叉熵仅对齐一阶矩的不足，提示在类似表示对齐任务中可考虑矩差异损失与对比损失的协同。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：学习兼容表示对检索系统至关重要，模型更新后新旧特征若不兼容，需重处理图库中断服务。本文指出，使用d-Simplex固定分类器学到的平稳表示等价于形式化兼容定义。但仅用交叉熵损失会忽略高阶统计量，影响兼容性。

**方法**：提出将交叉熵损失与监督对比损失进行凸组合，在固定d-Simplex分类器下训练。交叉熵对齐一阶统计量，对比损失捕获高阶依赖，理论证明该组合等价于在兼容约束下的交叉熵学习。分类器原型采用等角紧框架（ETF），保证类间均匀分离。

**结果**：在持续微调与模型替换场景下，所提方法实现SOTA，且无需重处理图库即可无缝切换模型，检索性能在更新中持续提升。例如在CIFAR-100和ImageNet上，兼容性指标显著优于直接微调与现有兼容学习方法。
