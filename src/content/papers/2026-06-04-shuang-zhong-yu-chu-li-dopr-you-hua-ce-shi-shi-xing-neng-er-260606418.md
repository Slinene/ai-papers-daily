---
title: 'Double Preconditioning (DoPr): Optimization for Test-Time Performance, not
  Validation Loss'
title_zh: 双重预处理（DoPr）：优化测试时性能而非验证损失
authors:
- Thomas T. Zhang
- Alok Shah
- Yifei Zhang
- Vincent Zhang
- Nikolai Matni
- Max Simchowitz
affiliations:
- University of Pennsylvania
- Carnegie Mellon University
- Amazon FAR
arxiv_id: '2606.06418'
url: https://arxiv.org/abs/2606.06418
pdf_url: https://arxiv.org/pdf/2606.06418
published: '2026-06-04'
collected: '2026-06-05'
category: Training
direction: 训练优化 · 测试时反馈
tags:
- Double Preconditioning
- Test-Time Feedback
- Activation Preconditioning
- Optimization
- Autoregressive Models
one_liner: 提出双重预处理（DoPr）结合梯度与激活预处理，提升自回归等测试时反馈场景下的下游性能，且不一定改善验证损失。
practical_value: '- 在自回归生成、多步推理等测试时反馈场景中，可直接将 DoPr 作为即插即用的训练方案，减少误差累积，提升下游任务成功率。

  - 对于电商 Agent 的规划、工具调用等需要多步 rollout 的任务，DoPr 提供了一种不依赖昂贵 RL 微调的轻量优化思路。

  - 激活预处理（AP）强调层间特征学习的均匀性，这可以迁移到推荐模型中，潜在地改善特征交互与泛化，尤其在 generation-based RecSys 中值得尝试。

  - 验证损失与下游指标脱钩的发现提醒：在评估生成式推荐或多步 Agent 时，不能仅追求单步预测损失，应直接观测 rollout 质量或任务完成率。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  \n许多深度学习的训练使用单步预测损失（如交叉熵、L2回归），但部署时需沿模型自身预测进行多步 rollout（如自回归语言模型、流生成、策略学习）。这导致训练/验证损失与下游指标（生成质量、任务成功率）之间的差距随任务长度放大，即测试时反馈(TTF)现象。现有工作从数据、架构、目标设计等角度缓解这种训练-测试偏移，本文首次将**优化算法**作为新的设计维度，提出双重预处理(DoPr)。  \n\n**方法关键点**  \nDoPr 在标准的梯度预处理（如 Adam、Muon）之前，对每一层的梯度施加**激活感知的预处理（AP）**，借鉴了 KFAC 等二阶优化思想。AP 通过正则化层间特征学习的“均匀性”，抑制某些维度过早过拟合或欠学习，从而降低 rollout 时的误差累积。该方法实现为 drop-in 组件，只需在反向传播后对梯度做一次额外的线性变换即可接入现有优化器。  \n\n**关键结果**  \n在多个 TTF 密集的任务上（语言建模、流生成、机器人策略学习），DoPr 显著提升了测试时性能（如任务成功率、生成困惑度），且这些提升**并不总伴随验证损失的改善**。例如，在自回归语言建模中，DoPr 使长序列生成的困惑度下降超 10%，但验证集上的交叉熵几乎不变。这挑战了仅凭验证损失选择模型的常规做法，提示需要针对 rollout 指标进行模型评估。
