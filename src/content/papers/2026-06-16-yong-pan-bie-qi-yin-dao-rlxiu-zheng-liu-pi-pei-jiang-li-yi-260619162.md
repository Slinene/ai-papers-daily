---
title: 'The Reward Was in Your Data All Along: Correcting Flow Matching with Discriminator-Guided
  RL'
title_zh: 用判别器引导RL修正流匹配：奖励已在数据中
authors:
- Nicolas Beltran-Velez
- Felix Friedrich
- Zhang Xiaofeng
- Reyhane Askari-Hemmat
- Xiaochuang Han
- Adriana Romero-Soriano
- Michal Drozdzal
affiliations:
- FAIR at Meta
- Columbia University
- Mila – Québec AI Institute
- McGill University
- Université de Montréal
arxiv_id: '2606.19162'
url: https://arxiv.org/abs/2606.19162
pdf_url: https://arxiv.org/pdf/2606.19162
published: '2026-06-16'
collected: '2026-06-19'
category: Training
direction: 生成式模型 · 判别器引导RL
tags:
- Flow Matching
- Discriminator-Guided RL
- FID Reduction
- KL-Regularized RL
- Preference-Free Reward
one_liner: 在预训练表示空间训练判别器，以其logit为奖励进行KL正则化RL，无需人类偏好即可大幅提升生成质量
practical_value: '- **生成式推荐的质量后处理**：可将类似思路用于提升生成式推荐模型（如生成item语义ID）的样本质量：利用预训练的用户/物品表示空间训练判别器，以判别器logit为奖励，通过KL正则化RL微调模型，无需人工偏好标注。

  - **离线奖励构建**：在推荐Agent或策略优化中，可以用判别器估计生成样本与真实数据的对数似然比，作为保真度奖励，避免昂贵的人类偏好收集，尤其适用于冷启动场景。

  - **与偏好优化的协同**：DRL后训练得到的模型能作为更好的初始点，再结合少量偏好反馈进行多目标RL，可获得更优的保真度-偏好帕累托前沿，可直接套用到推荐系统的多目标对齐（如新颖性、相关性）中。

  - **表示空间选择**：效仿其使用预训练表示空间（并非原始像素）作为判别器输入，推荐系统中可选用预训练的通用协同过滤嵌入或CLIP多模态空间，使奖励更聚焦语义相关性而非表面统计。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：流匹配模型的训练损失（速度场/得分场的ℓ2回归）与推理时的视觉语义质量存在结构不匹配，导致即使加了引导也需偏好RL来补救。但人类偏好昂贵且混杂主观性。本文发现：若有一个与数据分布对齐的奖赏，无需人工即可恢复真实感。

方法：提出判别器引导RL（DRL）。在固定预训练表征空间（如DINOv3、CLIP）上训练二分类判别器区分真实数据与基模型样本，其未归一化logit近似数据与模型分布的对数似然比，是使模型逼近真实分布的最优奖赏。以该logit为奖励，对基模型进行KL正则化RL微调（带预训练表征空间的REPA辅助），限制模型偏离太远并稳定训练。整个过程无需任何人类偏好或CFG。

结果：在SiT、JiT、REPA、RAE等骨干上，DRL将无CFG的FID大幅降低（SiT: 9.38→2.62），DINOv3语义FD从88.2降至19.3，均显著优于基模型和随机权重判别器基线。同时提升人类偏好奖赏，并与后续偏好RL相容，获得更好的保真度-偏好帕累托前沿，减少过饱和、过亮等低级伪影。
