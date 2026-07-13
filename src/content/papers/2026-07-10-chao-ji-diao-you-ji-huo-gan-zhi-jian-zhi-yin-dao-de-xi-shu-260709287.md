---
title: 'Super-Tuning: From Activation-Aware Pruning to Sparse Fine-Tuning'
title_zh: 超级调优：激活感知剪枝引导的稀疏微调
authors:
- Ivan Ilin
- Philip Zmushko
- Peter Richtárik
affiliations:
- KAUST
arxiv_id: '2607.09287'
url: https://arxiv.org/abs/2607.09287
pdf_url: https://arxiv.org/pdf/2607.09287
published: '2026-07-10'
collected: '2026-07-13'
category: Training
direction: 稀疏参数高效微调 · 激活感知
tags:
- Sparse Fine-Tuning
- PEFT
- LoRA
- Activation-Aware Pruning
- Wanda
- LLM Adaptation
one_liner: 复用剪枝中的激活感知重要性分数来固定稀疏可训练参数，提出Super和Supra实现高效微调
practical_value: '- 在电商搜索/推荐中微调LLM（如查询理解、文案生成）时，可用Super根据少量校准数据确定关键权重子集，降低80%以上可训练参数仍保持性能。

  - Supra混合LoRA与稀疏更新，通过预算分割规则灵活平衡低秩与稀疏分量，适合在资源受限的线上服务中部署。

  - 使用Wanda-style激活加权重要性（权重与输入激活乘积）作为稀疏选择标准，比纯幅值更关注任务相关特征，可用于快速适配新品类或活动。

  - 该方法的支持集固定性使得不同任务可共享相同的稀疏mask，只需切换可训练值，实现多任务间存储高效切换。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**
全参数微调大模型（LLM）计算和存储开销大，参数高效微调（PEFT）方法如LoRA通过低秩适配器限制更新量，但未显式利用参数重要性信息。剪枝领域已发展出有效的参数重要性评估方法（如Wanda激活感知评分），这些信号可能帮助选择最需更新的权重。

**方法**
提出Super，使用一次前向校准计算Wanda-style重要性分数（权重×输入激活范数），据此选择固定比例的权重作为可训练稀疏支持，其余冻结。进一步提出Supra，将稀疏更新与LoRA结合：将总可训练参数预算分为两部分，一部分用于稀疏支持，另一部分用于低秩适配器，通过简单规则分配，保持总参数量与纯LoRA或纯Super相当。训练时仅更新选定稀疏权重和低秩矩阵。

**结果**
在Math17K算术任务上，对Llama-3.2-1B和8B模型，Super/Supra在多个预算配置下取得最高平均准确率，优于纯LoRA和全量微调。实验还发现，使用低重要性分数（而非高重要性）的支持有时同样有效，表明剪枝启发的排序可为PEFT提供鲁棒且高效的固定支持结构，尤其与低秩适配器结合时效果突出。
