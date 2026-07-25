---
title: Context-weighted Discrete Flow Matching
title_zh: 上下文加权的离散流匹配
authors:
- Daniil Cherniavskii
- Daniel Severo
- Karen Ullrich
affiliations:
- University of Amsterdam
- Meta FAIR
arxiv_id: '2607.21427'
url: https://arxiv.org/abs/2607.21427
pdf_url: https://arxiv.org/pdf/2607.21427
published: '2026-07-23'
collected: '2026-07-25'
category: LLM
direction: 离散流匹配训练效率提升
tags:
- Discrete Flow Matching
- Context-Weighted Training
- Perplexity Reduction
- Text Generation
- CTMC
- Training Efficiency
one_liner: 通过局部上下文密度重加权训练损失与采样过程，将文本生成困惑度降低最高63%。
practical_value: '- 在生成推荐理由、广告文案、对话回复等文本时，不同位置的token预测难度差异大，可借鉴基于局部上下文密度的损失重加权，让模型聚焦高熵、低上下文密度的token，提升整体生成质量。

  - 上下文加权采样器几乎无额外计算开销，适合在线服务；同时保留任意顺序生成能力，可用于交互式推荐场景中动态调整输出顺序。

  - 对于语义ID生成、结构化描述生成等离散序列任务，可以事先估计上下文密度（例如用掩码语言模型得分），并在训练时对高难度位置加大梯度，减少训练集上易样本主导的偏置。

  - 该方法在匹配半自回归块扩散基线质量的同时保持灵活性，提示我们在设计生成式推荐模型时，不一定要牺牲灵活性来换取效率，可以通过简单的上下文感知策略兼得。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：离散流匹配（DFM）的标准因子化训练目标将不同难度的token等权混合：局部上下文充分的token预测明确，而缺少邻域上下文的token高度不确定。模型被大量容易token的信号主导，影响整体质量。文章实证表明，token预测的不确定性与它周围可用的局部上下文密度紧密相关。

**方法**：提出两种轻量级改进：（1）**上下文加权采样器**：修改底层连续时间马尔可夫链（CTMC），在采样速率中引入token特定的局部上下文信息，优先处理高上下文密度的token，改善生成顺序；（2）**缩放交叉熵损失**：根据每个token的上下文密度动态调整训练损失权重，对高不确定性的token赋予更大梯度，对低不确定性的token适当降权，从而平衡训练信号。

**关键结果**：在OpenWebText上，缩放交叉熵损失将生成困惑度降低最高63%；上下文加权采样器以可忽略的计算开销提升生成质量；整体方法在质量上与强半自回归块扩散基线相当，同时保持任意顺序生成的能力。
