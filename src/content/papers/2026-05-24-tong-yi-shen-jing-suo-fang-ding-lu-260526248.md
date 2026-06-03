---
title: Unified Neural Scaling Laws
title_zh: 统一神经缩放定律
authors:
- Ethan Caballero
- Priyank Jaini
- David Krueger
- Irina Rish
affiliations:
- Mila
- University of Montreal
- Google DeepMind
arxiv_id: '2605.26248'
url: https://arxiv.org/abs/2605.26248
pdf_url: https://arxiv.org/pdf/2605.26248
published: '2026-05-24'
collected: '2026-06-03'
category: Training
direction: 神经网络多维度联合缩放行为建模
tags:
- Scaling Laws
- Neural Scaling
- Predictive Modeling
- Large-scale Training
- Functional Form
one_liner: 提出统一函数形式UNSL，同时建模多维度（参数、数据、计算、推理步骤等）下的缩放行为，预测更准确
practical_value: '- 在多变量（数据量、模型大小、训练步数等）同时调整时，可用UNSL拟合scaling law，比单维度拟合更准确，帮助在有限预算下选择最优配置。

  - 在生成式推荐或LLM训练中，可基于小规模实验结果预测大模型性能，提前决定是否扩大规模，避免不必要投入。

  - 函数形式纳入了推理步骤数，可用于分析推理成本与性能的权衡，指导Agent或查询推荐系统在延迟约束下的部署决策。

  - 实际使用时需自行收集多维度实验数据拟合参数，并非预训练即用；主要贡献在于提供了一种更好的联合预测工具。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：训练顶级神经网络需要大量计算资源，准确预测不同规模的性能至关重要。现有缩放定律通常只考虑单一维度（如参数量或数据量），而实际业务中往往多个维度（参数量、数据量、训练步数、推理步数、超参数等）同时变化，单一维度预测不准，且小规模最优的方法在大规模可能失效。因此需要一种能够联合建模多维度变化的统一缩放定律。

**方法**：提出统一函数形式UNSL，将评估指标表示为多个维度光滑变换的乘积组合（包含幂律与交互项），覆盖参数量N、数据集大小D、训练步数S、推理步数I等。通过在不同架构（Transformer等）和任务（视觉、语言、数学、强化学习）上进行大量多维度联合测量，拟合函数参数，并与其他形式（如Kaplan等）对比预测准确度。

**结果**：在多个上游和下游任务上，UNSL的预测误差显著低于现有形式，能够更可靠地指导缩放决策，证明联合考虑多维度能有效提升预测精度。
