---
title: 'Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation'
title_zh: 探索式建模：解锁预训练第三维度与端到端生成
authors:
- Alexi Gladstone
- Heng Ji
- Yilun Du
affiliations:
- UIUC
- Harvard
arxiv_id: '2607.27372'
url: https://arxiv.org/abs/2607.27372
pdf_url: https://arxiv.org/pdf/2607.27372
published: '2026-07-28'
collected: '2026-07-31'
category: Multimodal
direction: 多模态生成 · 探索式预训练新范式
tags:
- Explorative Modeling
- End-to-End Generation
- Pretraining Axis
- Multimodal Generation
- Exploration Scaling
- Mode Coverage
one_liner: 提出探索式建模，在训练中探索多个候选生成并选择最佳匹配，将探索作为预训练新轴，提升多模态生成模型效率与性能
practical_value: '- **生成式推荐训练**：训练生成用户下一个物品（如 Semantic ID）时，对每个用户序列生成 K 个候选物品，选取与真实物品最匹配的进行训练，有效缓解多意图模糊问题，提升推荐多样性与准确性。

  - **长尾与冷启动覆盖**：探索式训练迫使模型关注多种模式，可帮助模型更好捕捉长尾物品，提升推荐新颖性和召回率。

  - **Agent 决策生成**：生成 Agent 行动方案时，生成多个候选动作，通过环境反馈选取最佳动作训练，提升策略鲁棒性和探索效率，适用于多臂老虎机、对话策略等场景。

  - **工程实现**：探索候选数量 K 可作为新的调优维度，在资源允许下加大 K 能稳定提升效果，且随着模型与数据规模扩大，收益愈加显著，是有效的 scaling
  策略。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有生成模型（自回归、扩散等）本质是多模态分布建模，但通常将生成过程分解为多步（如自回归逐 token 生成）以避免模糊预测，无法端到端训练。本工作提出探索式建模（Explorative Modeling），通过在训练循环中分解：对每个数据点生成 K 个候选预测，选择与真实数据最佳匹配的候选进行训练，使模型聚焦于某个模式而非模式平均。

**方法关键点**：Explorative Models (XMs) 将探索（K 的大小）作为除模型参数、数据量之外的第三预训练轴。训练时，模型为每个样本生成多个可能输出，根据重构误差或匹配度选择最佳预测，反向传播该预测的损失。这迫使模型学习产生更清晰的模式归属。该方法可应用于现有生成模型结构（如扩散模型、自回归模型），只需改变训练损失计算方式。

**关键结果**：在图像、视频、语言等跨模态任务上，增加探索量（K）单调提升性能。随着数据规模增大，收益从 7% 攀升至 36%；随模型规模增大，收益从 13% 升至 23%。探索显著提升效率：FLOP 效率 4.1 倍、样本效率 6.2 倍、参数效率 47%。在 ImageNet 上无引导时达到 1.43 FID，接近最优。此外，XMs 实现了端到端重构生成，在控制任务上以 16–256 倍更少推理步数匹配扩散模型。
