---
title: Optimizing Visual Generative Models via Distribution-wise Rewards
title_zh: 通过分布级奖励优化视觉生成模型
authors:
- Ruihang Li
- Mengde Xu
- Shuyang Gu
- Leigang Qu
- Fuli Feng
- Han Hu
- Wenjie Wang
affiliations:
- University of Science and Technology of China
- Shanghai Innovation Institute
- Hunyuan Frontier Lab, Tencent
- National University of Singapore
arxiv_id: '2607.02291'
url: https://arxiv.org/abs/2607.02291
pdf_url: https://arxiv.org/pdf/2607.02291
published: '2026-07-01'
collected: '2026-07-04'
category: Training
direction: 分布级奖励与RL微调
tags:
- Distribution-wise Reward
- Reward Hacking
- Mode Collapse
- Reinforcement Learning
- Model Merging
- FID
one_liner: 用分布级奖励替代逐样本奖励以缓解奖励黑客和模式崩塌，并提子集替换策略与RL优化模型合并系数
practical_value: '- 生成式推荐常因逐样本奖励导致多样性坍塌（如仅生成头部商品），可借鉴**分布级奖励**：在 batch 级别设计奖励，衡量生成结果与真实用户行为分布的匹配（如类目覆盖率、长尾占比），抑制奖励黑客。

  - **子集替换策略**：在大规模候选集评估时，可动态更新一小部分样本（如 5%）来近似真实分布奖励，降低在线计算开销，适用于推荐模型中的常驻评估集或在线 RL
  的 reward normalization。

  - **RL 优化模型合并系数**：对于多目标融合（如点击率、转化率、多样性）的推荐模型，可学习后验合并系数以平衡各奖励项，缓解训练-推理不一致，尤其适合 LoRA
  合并或多专家集成。

  - 分布对齐视角可迁移到**推荐策略的多样性控制**：将用户交互分布视为真实分布，通过分布奖励直接优化生成策略的宏观统计属性，避免微观过拟合。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视觉生成模型的 RL 微调普遍使用逐样本奖励（如 aesthetic score），会诱发奖励黑客——模型生成高分但缺乏多样性的样本，甚至出现视觉假象。本质是单样本奖励无法约束整体分布，导致模式崩塌。

**方法**：
1. **分布级奖励**：不再对单张图像打分，而是比较一批生成样本与真实数据的分布差异（如 FID 的近似），以此作为奖励信号，迫使模型维持整体多样性。
2. **子集替换策略**：为降低分布奖励的计算量，仅将生成参考集中的一小部分（如 10%）替换为新样本，旧样本保留，从而快速更新分布估计，提供有效训练信号。
3. **RL 优化模型合并系数**：引入 SDE 的 RL 训练会造成训练-推理不一致，故在后验阶段用 RL 学习不同模型（如基础模型与微调模型）的合并权重，减轻该问题。

**结果**：在 SiT 和 EDM2 上，FID-50K 分别从 8.30 降至 5.77、3.74 降至 3.52，同时视觉质量与多样性均得到提升。
