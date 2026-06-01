---
title: Consolidating Rewarded Perturbations for LLM Post-Training
title_zh: 通过合并奖励扰动实现LLM后训练
authors:
- Zheyu Zhang
- Shuo Yang
- Gjergji Kasneci
affiliations:
- Technical University of Munich
- Munich Center for Machine Learning
arxiv_id: '2605.31494'
url: https://arxiv.org/abs/2605.31494
pdf_url: https://arxiv.org/pdf/2605.31494
published: '2026-05-29'
collected: '2026-06-01'
category: Training
direction: LLM后训练 · 权重空间搜索与合并
tags:
- Rewarded Perturbations
- Model Merging
- Post-Training
- Low-Rank Structure
- Gradient-Free
one_liner: 在权重空间随机采样扰动后，通过兼容性感知加权合并为一个可部署模型，避免推理时多模型投票
practical_value: '- 直接可用在电商文案生成、对话Agent等有明确奖励信号（如转化率、用户评分）的LLM后训练中：只需采样少量随机扰动，用少量支持集奖励打分，即可通过CoRP合并成一个高质量模型，完全省去梯度计算，适合算力受限的业务场景。

  - 合并策略中的兼容性感知重权重（alignment与orthogonal dispersion）可迁移到模型融合场景：当合并多个由同一基座微调得到的推荐模型或Agent时，可先构造奖励加权方向，再根据各模型与该方向的对齐度及正交散度赋权，以压制互斥结构。

  - 提出的分半验证门控（held-out validation gate）可用于任何基于采样的模型更新过程，能自动放弃不可靠候选、减少退化，对线上模型迭代的稳定性很重要。

  - 发现奖励扰动在低秩子空间存在可复现结构，这为用轻量级LoRA适配代替全量微调提供了依据，可尝试仅在奖励群体主方向所在的低秩子空间内更新参数，降低部署成本。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：现有LLM后训练方法（PPO/GRPO等）依赖梯度和大量采样，RandOpt虽通过权重空间随机扰动和推理时集成免去梯度，但需K个前向推理（K≈50）且难以用于自由生成任务。核心问题是：能否将扰动群体合并为一个可部署模型？本文通过分半诊断发现，多个模型-任务对上奖励扰动存在可复现的低秩结构，但简单的奖励加权平均往往失败，因为扰动间存在兼容性问题。

**方法关键点**：
- **两阶段合并**：第一遍按奖励权重选出精英扰动方向；第二遍计算每个扰动与该方向的对齐度（alignment）和正交散度（orthogonal dispersion），将奖励与兼容性得分结合得到最终权重，归一化后得到单一更新方向。
- **验证门控**：将支持集分成构建、验证、探针三部分，候选更新须在验证集上获得正向增益且置信下界>0才能被采纳，否则放弃更新，防止退化。
- **迭代搜索**：采纳更新后，以新模型为中心再次采样扰动，协方差由历史奖励群体的方向调整，继续合并，形成逐步提升的链式更新。

**关键实验**：在5个模型（0.5B到8B，Qwen2.5/OLMo3/Llama3.1）和5个任务（数学推理、编程、创意写作）上，CoRP平均提升基座8.1分，仅用RandOpt十分之一的扰动预算（500 vs 5000）和一次推理，超过RandOpt K=1 6.5分，并恢复K=50多数投票集成一半以上的增益。PPO/GRPO在部分设置下仍最优，但CoRP以无梯度、低推理成本具备竞争力。分解显示增益不仅来自格式修正，也包含真实推理修复。
