---
title: 'Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence'
title_zh: 平衡 LoRA：消除参数不变性加速收敛
authors:
- Valérie Castin
- Kimia Nadjahi
- Pierre Ablin
- Gabriel Peyré
affiliations:
- École Normale Supérieure PSL
- CNRS
- Apple
arxiv_id: '2605.31484'
url: https://arxiv.org/abs/2605.31484
pdf_url: https://arxiv.org/pdf/2605.31484
published: '2026-05-29'
collected: '2026-06-01'
category: Training
direction: LoRA 优化 · 平衡投影
tags:
- LoRA
- Convergence
- Conditioning
- Balanced
- PEFT
one_liner: 提出 BaLoRA，通过投影到平衡流形改善 LoRA 条件数，实现更快收敛且几乎无额外开销。
practical_value: '- 在生成式推荐或 Agent 微调中，用 BaLoRA 替代标准 LoRA：每步优化后加一次极分解+SVD 投影（复杂度 O((a+b)r²)），收敛更快且不增加显存。

  - 高秩微调场景（如复杂多模态推荐、大规模 Agent 模型）下，BaLoRA 在高 rank（64、128）优势显著，可避免条件数恶化。

  - BaLoRA 对学习率和初始化缩放更鲁棒，降低超参搜索成本，适合业务中快速迭代。

  - 投影保持乘积 AB 不变，无伤融入现有 LoRA 流水线，可即插即用。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LoRA 微调时多对低秩因子可产生同一适配器，但不同因子对应的 Hessian 条件数差异很大，导致收敛速率不稳定。已有工作未揭示平衡条件与最优条件数的理论联系。本文证明平衡的适配器（A⊤A = BB⊤）使损失 landscape 条件数最小，收敛最快。

**方法关键点**：
- 理论：分析一层线性及深度非线性网络下 LoRA 的 Hessian 谱，证明平衡最小化器达到最优条件数，条件数由权重矩阵的奇异值或谱间隙决定。
- BaLoRA：每次优化器步骤后，将 (A,B) 投影到超平衡流形 H = { (U S^{1/2}, S^{1/2} V) }。投影 P 利用极分解与 SVD，保持乘积 AB 不变，计算量仅 O((a+b)r²)。
- 内在几何解释：用梯度下降时，BaLoRA 等价于在秩 r 矩阵流形上的 Bures 度量黎曼梯度下降，有优美的几何结构。
- 与 AdamW 结合即为实用 BaLoRA，兼容各种初始化。

**关键结果**：
- 合成数据：1 层/2 层线性网络优化，BaLoRA 先慢后快，最终收敛远快于 LoRA。
- 大模型微调：在 Llama-3.2-3B 和 Qwen-2.5-3B 上，跨 Wikitext、Alpaca、CodeFeedback 等多个数据集，BaLoRA 测试损失一致优于 LoRA，与 RefLoRA、DoRA 等持平或更优，尤其 rank=64/128 时优势明显。
- 显存：相比 LoRA 几乎无额外开销。
- 鲁棒性：对学习率和初始化缩放不敏感，超参选择更宽松。

**一句话**：BaLoRA 以零成本投影消除 LoRA 的参数不变性引发的条件数恶化，实现更快更稳的微调，特别适合高秩适配。
