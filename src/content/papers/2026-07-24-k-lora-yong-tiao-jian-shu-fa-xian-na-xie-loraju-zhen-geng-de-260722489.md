---
title: '\k{appa}-LoRA: Condition Numbers Reveal Which LoRA Matrices Worth Updating'
title_zh: κ-LoRA：用条件数发现哪些LoRA矩阵更值得更新
authors:
- Jianghui Wang
- Silong Yong
- Francesco Orabona
- Marco Canini
- Katia P. Sycara
- Yaqi Xie
affiliations:
- King Abdullah University of Science and Technology
- Carnegie Mellon University
arxiv_id: '2607.22489'
url: https://arxiv.org/abs/2607.22489
pdf_url: https://arxiv.org/pdf/2607.22489
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: 高效微调 · 条件数驱动的选择性LoRA
tags:
- LoRA
- condition number
- efficient fine-tuning
- spectral analysis
- model compression
one_liner: 基于权重矩阵的条件数选择性更新LoRA参数，在匹配标准LoRA精度的同时减少约一半的参数量和16.2%的训练时间
practical_value: '- **选择性微调的思路可直接用于推荐模型部署**：在电商/广告推荐系统中，通常需对多个任务（CTR、CVR）或场景进行LLM微调，κ-LoRA表明不必更新所有权重矩阵，仅更新条件数大的50%矩阵即可保持效果，节省边缘端/实时更新的算力与内存。

  - **条件数作为矩阵重要性的度量可嵌入自动化微调流程**：条件数计算轻量，可在微调前快速评估各层权重的重要性，为模型裁剪、量化或稀疏更新提供依据，适用于在线学习的资源分配。

  - **谱重平衡的思想可迁移到特征交互层或嵌入表更新**：推荐模型中存在大量嵌入矩阵和交互矩阵，可类比用条件数识别哪些特征空间尚未充分学习，选择性进行微调或重训，提升资源利用率。

  - **对于Agent中多模型微调的场景，κ-LoRA能有效降低联合微调成本**：多Agent系统往往需对多个LLM进行适配，κ-LoRA的稀疏化更新策略可让不同Agent共享基座模型，仅更新各自相关的关键矩阵，减少显存和通信开销。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LoRA虽然广泛用于高效微调，但仍统一更新所有权重矩阵，即使许多矩阵对任务适应贡献微小。在大规模模型和资源受限场景（如边缘部署）中，不必要的更新带来计算和内存浪费。本工作首次发现LoRA矩阵的条件数（最大与最小奇异值之比）能指示其更新价值：条件数小的矩阵已方向平衡，贡献有限；条件数大的矩阵包含未充分发展的方向，驱动了大部分性能提升。

**方法**：提出κ-LoRA，仅对条件数最大的前50%权重矩阵进行低秩更新。具体而言，对预训练模型各层的权重矩阵计算条件数，按降序选择top-half的矩阵绑定LoRA适配器，其余矩阵冻结。训练中这些矩阵的条件数持续下降，表明方法通过针对性谱重平衡达到高效适应，而非纯粹的参数选择。

**关键结果**：在多项基准（自然语言理解、生成、视觉任务）上，κ-LoRA用标准LoRA一半的可训练参数，匹配甚至略优于标准LoRA的精度，平均减少训练时间16.2%，内存成本降低4.5%。分析表明选定矩阵的条件数在训练中单调递减，验证了谱重平衡假设。
