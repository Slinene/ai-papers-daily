---
title: 'A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter
  Merging (MaLoRA)'
title_zh: LoRA 的边际视角：抗灾难性遗忘与适配器合并（MaLoRA）
authors:
- Ziqing Xu
- Hancheng Min
- Lachlan Ewen MacDonald
- Salma Tarmoun
- Enrique Mallada
- Weijie Su
- Rene Vidal
affiliations:
- University of Pennsylvania
- Shanghai Jiao Tong University
- Johns Hopkins University
arxiv_id: '2611.14397'
url: https://arxiv.org/abs/2611.14397
pdf_url: https://arxiv.org/pdf/2611.14397
published: '2026-11-10'
collected: '2026-11-12'
category: Training
direction: LoRA 理论基础与适配器合并
tags:
- LoRA
- Adapter Merging
- Margin Theory
- Catastrophic Forgetting
- Multi-task Learning
- PEFT
one_liner: 用 margin 理论分析 LoRA，揭示正则化权衡并导出无需训练的适配器合并规则 MaLoRA
practical_value: '- **多场景 LoRA 合并上线**：电商推荐中常为首页、搜索、详情等场景分别微调 LoRA，MaLoRA 给出基于 margin
  的封闭式最优加权系数，无需额外训练或验证集，可直接合并多个场景适配器为单一模型，降低在线推理的模型切换与资源成本。

  - **调节正则化强度平衡新旧知识**：理论显示 LoRA 的 ℓ2 正则化参数精确控制遗忘与适应之间的 margin trade-off。在实际微调推荐模型时，可通过增大正则化/权重衰减来保留预训练知识，防止新活动数据覆盖旧行为模式。

  - **多租户/联邦场景的隐私友好合并**：不同商家或垂直行业独立训练 LoRA 后，无需共享原始数据即可合并为全局模型，MaLoRA 的免训练公式比现有基于权重平均的方法更稳定，适合快速迭代多租户模型。

  - **持续学习中的增量适配器合并**：当业务数据按时间分片增量训练时，可将各时间窗的 LoRA 适配器按 MaLoRA 系数合并，替代完全重训，有效缓解灾难性遗忘，同时保持对新趋势的适应。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
LoRA 已成为大模型参数高效微调的事实标准，但在实际部署中观察到两个关键性质：对灾难性遗忘的鲁棒性，以及独立训练的适配器可以合并为一个在多任务上表现良好的模型。这些性质对持续学习和多任务学习至关重要，但一直缺乏严格的理论解释。  

**方法关键点**  
论文在近正交任务设定和多分类线性模型下，结合 ℓ2 正则化分析 LoRA 的最优适配器。在正则化参数的中间区域，最优适配器与微调数据的最大间隔（max-margin）解对齐。基于这一表征，推导出预训练数据与微调数据上间隔的闭式表达式，揭示正则化参数精确控制保留与适应之间的权衡。进一步分析适配器合并：证明合并模型在每个任务上取得正间隔，并导出使任务间间隔平衡、在并集上最大化间隔的最优混合系数。由此提出一种完全免训练的合并规则 MaLoRA，仅凭各适配器的 margin 信息即可计算最优加权。  

**关键结果数字**  
在现代视觉和语言分类任务上验证，MaLoRA 与多种适配器合并基线相比，匹配或超越其性能，且无需额外训练、验证集或超参数搜索。
