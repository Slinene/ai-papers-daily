---
title: Continual Learning Mechanisms Compose for Long-Horizon Memorization
title_zh: 持续学习机制组合实现长期记忆
authors:
- Zheyuan Zhang
- Alvin Zhang
- Daniel Khashabi
- Tianmin Shu
affiliations:
- Johns Hopkins University
arxiv_id: '2609.06986'
url: https://arxiv.org/abs/2609.06986
pdf_url: https://arxiv.org/pdf/2609.06986
published: '2026-09-06'
collected: '2026-09-17'
category: Training
direction: 持续学习机制组合与长期记忆
tags:
- Continual Learning
- LoRA
- Catastrophic Forgetting
- Memorization
- Fine-tuning
one_liner: 组合数据/函数/权重 anchor 与 merged LoRA 将 100 任务顺序微调平均保留率从 1.2% 提升至 34.9%
practical_value: '- 模型需要持续更新商品目录或用户行为时，可采用 **merged LoRA** 为每个新任务/新领域分配独立低秩矩阵，避免直接覆盖全量参数，再定期合并或推理时加权组合，减少灾难性遗忘。

  - 借鉴 **data anchor**：在每次更新时混入少量历史代表样本（或合成回放），即使无法保存完整旧数据，也能显著提升长期保留率；对电商场景可保存高价值/长尾样本的小型
  memory buffer。

  - 多种机制存在超加性交互，尤其 data anchor + merged LoRA。工程实现上不要单独评估单一策略，应组合验证，并使用 factorial 实验量化主效应与交互作用。

  - 任务级 successive halving 搜索设计空间成本可控，适合在业务中快速筛选持续学习策略组合，再投入完整训练。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
语言模型需要随时间不断学习新信息并留存于参数中，但顺序微调会导致灾难性遗忘。论文定义 long-horizon memorization：在 100 个 QA 任务上持续 SFT，推理时不提供旧样本和任务 ID，检验模型长期记忆能力。  

**方法关键点**  
提出两个设计维度组合现有持续学习机制：① **data/function/weight anchors** 指定每次更新要保留何种先验信息；② **low-rank allocation rules** 决定连续更新存放在哪些低秩子空间。通过 task-level successive halving 搜索组合空间，并用 factorial experiment 测量个体与交互效应。最佳配置将三种 anchors（数据回放、函数正则、权重约束）与 merged LoRA 结合：每个任务使用独立 LoRA 矩阵，推理时合并所有矩阵，避免新任务覆盖旧知识。  

**关键结果数字**  
在三个独立构造的 100 任务数据集上，最佳方法均进入前三；平均最终保留率从 naive 顺序微调的 **1.2%** 提升至 **34.9%**，**28 倍**改进。其中 data anchor 和 merged LoRA 贡献最大，且在三个数据集上均呈现超加性交互，说明组合互补机制远优于任何单一机制。
