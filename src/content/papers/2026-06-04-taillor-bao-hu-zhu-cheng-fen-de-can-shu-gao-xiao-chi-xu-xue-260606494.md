---
title: 'TailLoR: Protecting Principal Components in Parameter-Efficient Continual
  Learning'
title_zh: TailLoR：保护主成分的参数高效持续学习
authors:
- Marius Dragoi
- Ioana Pintilie
- Alexandra Dragomir
- Antonio Barbalau
- Florin Brad
affiliations:
- Bitdefender, Romania
arxiv_id: '2606.06494'
url: https://arxiv.org/abs/2606.06494
pdf_url: https://arxiv.org/pdf/2606.06494
published: '2026-06-04'
collected: '2026-06-05'
category: Training
direction: 参数高效持续学习 · 谱分解
tags:
- TailLoR
- LoRA
- Spectral Decomposition
- Continual Learning
- PEFT
- Interference
one_liner: 通过软谱惩罚将低秩适应引导至长尾奇异方向，缓解持续学习中的干扰与遗忘
practical_value: '- 在电商推荐模型的持续更新中，用TailLoR替代标准LoRA，可将新任务对历史知识的干扰从主成分转移到长尾维度，有效缓解灾难性遗忘。

  - 可直接将预训练权重的奇异基冻结为参考系，仅学习对奇异值矩阵的低秩更新，参数效率极高，适合部署于频繁迭代的推荐Agent。

  - 软谱惩罚项可单独作为正则化技巧，融入现有LoRA微调流水线，强制模型利用未充分优化的长尾表示，提升多任务顺序学习能力。

  - 该方法天然适配多域推荐场景（如不同商品类目），允许逐个域顺序学习而无需重训练所有数据，降低工程成本。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有低秩适应方法（如LoRA）在持续学习场景中，不同任务间的更新方向往往在主导奇异空间重叠，导致严重干扰与灾难性遗忘，尤其当模型需要顺序适应多个下游任务时。

**方法**：提出TailLoR，将预训练权重的奇异基U和V作为固定参考框架，只对奇异值矩阵学习低秩更新，极大减少可训练参数量。同时引入一种软谱惩罚项，它会根据奇异值的大小自适应地抑制沿主导奇异方向的更新，将微调引导到灵活性高但通常未充分利用的长尾奇异坐标上，从而保护主成分不被新任务覆盖。

**结果**：在多个持续学习基准上，TailLoR相比标准LoRA和基于谱分解的变体，显著降低了不同任务间的干扰，提升了旧任务遗忘与新任务学习之间的平衡，并且在参数效率上更具优势。
