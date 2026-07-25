---
title: Statistical Inference for Rank Allocation in Low-Rank Adaptation
title_zh: 基于统计推断的LoRA秩分配方法
authors:
- Yihang Gao
- Vincent Y. F. Tan
arxiv_id: '2607.20205'
url: https://arxiv.org/abs/2607.20205
pdf_url: https://arxiv.org/pdf/2607.20205
published: '2026-07-22'
collected: '2026-07-25'
category: Training
direction: 参数高效微调 · 统计推断
tags:
- LoRA
- Statistical Inference
- Rank Allocation
- PEFT
- Hypothesis Testing
- Asymptotic Normality
one_liner: 将秩分配视为假设检验问题，利用p值驱动剪枝，实现更稳定的参数预算分配
practical_value: '- 在推荐或对话模型用LoRA微调时，可用统计检验代替基于梯度的启发式重要性分数，自动决定各层/模块的秩分配，避免人工调参与欠佳分配。

  - 该方法为每个可学习的低秩组件提供明确的p值，可直接设定显著性阈值进行剪枝，适合在资源受限的在线服务中动态调节模型容量。

  - 基于优化器轨迹的渐近正态理论（覆盖AdamW等常用优化器）为下游应用中的梯度统计量提供了可靠分布假设，可用于构建更准确的早期停止或在线不确定性估计。

  - 统计检验驱动的分配规则对超参数不敏感，经验诊断表明其稳定性优于AdaLoRA等灵敏度方法，在电商搜索/推荐模型的持续微调场景中能减少重复调参成本。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：LoRA 微调时，不同模块和层对下游任务的贡献不均，在固定参数预算下合理分配各组件秩至关重要。现有自适应秩方法依赖梯度灵敏度或不确定性构造重要性分数，缺乏清晰的统计解释与不确定性量化。

**方法**：将 LoRA 的秩分配形式化为统计假设检验问题。为每个 LoRA 组件构建检验统计量，利用随机优化器轨迹的渐近正态性（文中为 AdamW 等常见优化器建立了中心极限定理）推导出统计量的渐近分布，从而估计 p 值。在给定秩预算下，保留统计证据最强的组件，剪除 p 值最大的（即贡献不显著的）组件，实现基于统计推断的自动化分配。整个过程无需预定义重要性阈值，提供了显式的不确定性度量。

**结果**：在 DeBERTaV3-base、BART-Large、Qwen2.5-7B 上执行 NLU、NLG、QA 任务的 LoRA 微调。在匹配秩预算下，StatLoRA 性能与原始 LoRA、AdaLoRA、IGU-LoRA 相当或更优；敏感性分析和经验诊断证实分配规则的稳定性，并通过实验验证了组件得分渐近正态分布的理论。
