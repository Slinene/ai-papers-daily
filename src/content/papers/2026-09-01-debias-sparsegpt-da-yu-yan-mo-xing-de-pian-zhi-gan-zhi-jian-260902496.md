---
title: 'Debias-SparseGPT: Bias-Aware Pruning for Large Language Models'
title_zh: Debias-SparseGPT：大语言模型的偏置感知剪枝
authors:
- Irina Proskurina
- Guillaume Metzler
- Antoine Gourru
- Julien Velcin
affiliations:
- Laboratoire Hubert Curien, UMR CNRS 5516
- Université Claude Bernard Lyon 1
- Université Lumière Lyon 2, ERIC
- École Centrale de Lyon, LIRIS, CNRS UMR 5205
arxiv_id: '2609.02496'
url: https://arxiv.org/abs/2609.02496
pdf_url: https://arxiv.org/pdf/2609.02496
published: '2026-09-01'
collected: '2026-09-05'
category: Training
direction: LLM 压缩与公平性 · 偏置感知剪枝
tags:
- LLM
- Pruning
- Bias Mitigation
- SparseGPT
- Fairness
- Post-training
one_liner: 在 SparseGPT 剪枝中引入基于对比输入的二阶去偏正则项，显著降低剪枝引起的偏置放大，同时保持模型质量
practical_value: '- 在电商/推荐场景部署压缩后 LLM（如生成商品文案、用户评论回复）时，SparseGPT 等剪枝可能放大对特定用户群体（性别、年龄
  persona）的偏见。可借鉴 Debias-SparseGPT 的思路：在剪枝校准阶段加入对比敏感属性的输入对，并加入二阶正则项，在几乎不损失困惑度/准确率的情况下降低公平性风险。

  - 校准集的选择直接影响剪枝后模型质量：在强结构化剪枝（如 2:4）下，应优先选择长上下文、内容丰富的样本，而非随机短样本。提示我们在为推荐场景 LM 做压缩时，校准数据应覆盖业务中典型的长尾、复杂情境，以提高泛化和公平性。

  - 若业务中需用压缩后 LLM 做个性化推荐或广告文案生成，可在离线评估时加入 fairness 指标（如不同性别/年龄群体输出差异），并将 Debias-SparseGPT
  作为模型压缩 pipeline 的一部分，避免上线后因 persona 提示产生明显偏好。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 剪枝压缩虽能提升推理效率，但已有研究表明 SparseGPT 等权重稀疏化方法会放大模型内在偏见，输出随 prompt 中 persona 提示显著变化。需要一种在剪枝过程中保持公平性的方法。

**方法关键点**：提出 Debias-SparseGPT，一种后训练剪枝方法。在 SparseGPT 剪枝目标中引入 representational debiasing 正则项，该正则项基于二阶统计量，定义在一组人口统计学对比输入上（如不同性别/种族 persona）。通过在剪枝优化过程中最小化敏感方向的表征差异，引导剪枝后的模型在表征层面减少对不同群体的偏见。整体框架保持 SparseGPT 的计算效率，只需额外准备对比校准样本。

**关键结果**：在多个生成式 LLM 上验证，在 25%、50% 非结构化稀疏和 2:4 结构化稀疏设置下，与 SparseGPT 相比，Debias-SparseGPT 一致降低了剪枝引入的偏置，同时保持模型困惑度和零样本准确率基本不变。在最严格的 2:4 结构化剪枝中，使用长上下文、内容丰富的校准样本扩展后，下游性能和公平性进一步提升。总体实现了 bias-performance 权衡的改善，且不牺牲稀疏模型的推理效率。
