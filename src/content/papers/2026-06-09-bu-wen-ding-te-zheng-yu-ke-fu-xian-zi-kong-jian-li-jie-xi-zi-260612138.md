---
title: 'Unstable Features, Reproducible Subspaces: Understanding Seed Dependence in
  Sparse Autoencoders'
title_zh: 不稳定特征与可复现子空间：理解稀疏自编码器的种子依赖性
authors:
- Gleb Gerasimov
- Timofei Rusalev
- Nikita Balagansky
- Daniil Laptev
- Vadim Kurochkin
- Daniil Gavrilov
affiliations:
- T-Tech
arxiv_id: '2606.12138'
url: https://arxiv.org/abs/2606.12138
pdf_url: https://arxiv.org/pdf/2606.12138
published: '2026-06-09'
collected: '2026-06-17'
category: Training
direction: SAE训练稳定性 · 低秩子空间
tags:
- SAE
- feature stability
- seed dependence
- interpretability
- low-rank subspaces
one_liner: 提出可扩展的特征稳定性度量，揭示稳定特征主导功能信号，不稳定特征集中于可复现的低秩子空间
practical_value: '- 若在电商推荐中采用 SAE 抽取可解释特征，应优先信任稳定性高的特征，它们对重建和下游预测贡献更大，不稳定特征多为表面形式触发，实际效果弱。

  - 对于不同随机种子下特征不一致的问题，可通过跨种子合并独特特征构建更稳定的 SAE，同时保持解释方差，这一 trick 可直接用于生产中的可解释性模块。

  - 不稳定特征虽单个不可复现，但整体驻留于可复现的低秩子空间，说明可对激活空间施加低秩约束来增强特征的可辨识性，为模型设计提供几何视角。

  - 该稳定性评估方法可扩展，适用于不同模型层和字典大小，可快速筛选可靠特征，减少线上实验的种子敏感波动。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：SAE 被广泛用于解释神经网络表征，但其学到的特征在不同训练种子下可能差异很大，这威胁到可解释性的可靠性。需要一种方法量化单个特征的跨种子可复现性，并深入理解不稳定特征的本质。
**方法**：作者提出特征稳定性指标——为每个 SAE 特征估计在独立训练中再次出现的概率，通过大规模实验覆盖不同种子、模型、层、字典大小及 SAE 变体。他们分析稳定与不稳定特征在重建能力、预测重要性、激活统计和自动解释方面的不对称性，并利用几何分析发现不稳定特征集中于可复现的低秩子空间。通过受控合成模型验证了：即使真实特征是低秩的，SAE 也只能在子空间层面恢复，单个隐式特征不可辨识。最后，他们通过跨种子合并独特特征来构建更稳定的 SAE。
**关键结果**：稳定特征承载了绝大部分重建和预测相关信号，不稳定特征边际影响弱，且多由低频表面形式触发。几何上，不稳定特征虽然个体不可复现，但整体散布在可复现的低秩子空间中，暗示种子依赖性源于基的模糊而非纯粹噪声。合并跨种子特征后的 SAE 在保持解释方差的同时显著提升稳定性。
