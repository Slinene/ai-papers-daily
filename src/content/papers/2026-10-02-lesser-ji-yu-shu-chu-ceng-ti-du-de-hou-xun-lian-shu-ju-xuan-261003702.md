---
title: 'LESSER: Post-Training Data Selection with Output-Layer Gradients'
title_zh: LESSER：基于输出层梯度的后训练数据选择
authors:
- Lyuxin David Zhang
- Eric Wong
- Surbhi Goel
- Anton Xue
affiliations:
- University of Pennsylvania
- University of Texas at Austin
arxiv_id: '2610.03702'
url: https://arxiv.org/abs/2610.03702
pdf_url: https://arxiv.org/pdf/2610.03702
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 训练数据选择 · 输出层梯度近似
tags:
- Data Selection
- Gradient-based
- Post-training
- LLM
- Output-layer Gradients
- Efficient Training
one_liner: 用输出层梯度近似全参数梯度进行数据选择，降低特征提取FLOP 9.7倍/3倍且保持下游性能
practical_value: '- 在 LLM 微调数据筛选中，只提取输出层梯度作为样本特征，避免全参数反向传播，数据选择成本大幅下降；适用于电商搜索/推荐场景下的
  LLM 微调、指令数据清洗。

  - 工程实现上只需 hook 模型最后一层，兼容现有 gradient-based 选择方法（如 LESS），可作为 drop-in wrapper 快速迁移，无需改变训练流程。

  - 即使单个样本的梯度排序与全梯度存在差异，选出的 batch 梯度仍然对齐，因此批量训练效果稳定；可以在大规模候选池中做粗筛或迭代选择。

  - 对 RLHF/DPO 等后训练数据筛选，输出层梯度可替代全梯度做相似度排序，尤其适合计算资源受限的团队进行高质量样本挑选。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：后训练数据选择对 LLM 下游性能影响显著，基于梯度的选择方法通过样本梯度与验证集梯度对齐度排序，但全参数梯度需要对每个样本做昂贵反向传播，候选池大时不可行。

**方法关键点**：发现输出层梯度足以有效进行数据选择，且只需更便宜的前向传播。实现为 LESSER，一个 drop-in wrapper，提取输出层梯度特征替代全梯度特征，接入现有选择方法（如 LESS）。输出层梯度可通过前向计算得到，避免全参数反向传播。

**关键结果**：在 SFT 和 RL benchmarks 上，LESSER 将特征提取 FLOP 分别降低 9.7× 和 3.0×，同时在下游任务性能上追踪全梯度方法。即使输出层梯度与全梯度对单个样本排序不同，它们选择的 batch 梯度仍保持对齐，支持批量训练的有效性。
