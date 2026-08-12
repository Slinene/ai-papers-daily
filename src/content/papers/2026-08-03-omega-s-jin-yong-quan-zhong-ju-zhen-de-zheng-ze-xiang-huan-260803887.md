---
title: 'Omega-S: A Functional Resilience Index for LLM Fine-Tuning'
title_zh: Omega-S：仅用权重矩阵的正则项缓解 LLM 微调遗忘
authors:
- Alberto Acedo
affiliations:
- Biome Makers Inc.
arxiv_id: '2608.03887'
url: https://arxiv.org/abs/2608.03887
pdf_url: https://arxiv.org/pdf/2608.03887
published: '2026-08-03'
collected: '2026-08-12'
category: Training
direction: LLM 持续学习防遗忘正则化
tags:
- Continual Learning
- Regularization
- LoRA
- Fine-tuning
- Catastrophic Forgetting
- Graph Topology
one_liner: 仅从权重矩阵计算拓扑正则项，无需旧任务数据或旧权重，使 LoRA 微调保留率从 62.9% 提升至 84.1%
practical_value: '- **轻量微调防遗忘**：在电商/搜索推荐模型进行领域微调时，可作为一个无数据依赖的正则项，避免基础能力衰退，只需在训练循环中添加三行代码，额外开销小于
  4%。

  - **简化实现路径**：论文揭示实际有效成分是节点度方差惩罚，业务中可直接实现该方差项，无需完整拓扑构建，降低工程复杂度。

  - **适配 LoRA 微调场景**：方法在 LoRA 微调下验证有效，适合当下主流的高效微调范式，可直接嵌入现有推荐模型微调流程，防止对新任务过拟合而丢失原推荐质量。

  - **基线对比价值**：提供了与 weight decay、EWC 的详细对比，若需在业务中引入持续学习正则，可优先尝试 Omega-S 简化版。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 在新数据上微调会灾难性遗忘先前能力，现有正则化方法（EWC、weight decay）或需存储旧权重/计算 Fisher 信息，或需旧任务数据。需要一种仅从当前权重就能计算的轻量惩罚项。

**方法**：Omega-S 将权重矩阵视为邻接图，以 Tr(A³) 为优化目标构建正则项，实际梯度分解为四项后，仅节点度方差项起主要作用（弹性系数 9×10⁻³，其他三项 ≤10⁻⁴）。惩罚项直接作用于权重矩阵，无需旧数据或旧权重副本，三行代码即可集成，计算开销 <4%。

**关键结果**：在 Llama-3-8B 上用 LoRA 从代码微调至散文，HumanEval 评估原始代码能力保留。Omega-S 在 10 个种子中 9 个优于无正则化，绝对 pass@1 从 0.173 提升至 0.238（相对提升 37.7%），保留率从 62.9% 升至 84.1%；10/10 种子胜调优 weight decay，8/10 种子胜调优 EWC。机制分析表明实际起作用的仅是节点度方差惩罚，且对比度保留变体反而降低保留。
