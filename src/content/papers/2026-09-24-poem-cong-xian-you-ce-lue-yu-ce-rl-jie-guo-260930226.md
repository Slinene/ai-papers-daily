---
title: 'PoEM: Predicting RL Outcomes from Existing Policies'
title_zh: PoEM：从现有策略预测 RL 结果
authors:
- Kimia Hamidieh
- Giannis Daras
- Antonio Torralba
affiliations:
- MIT CSAIL
arxiv_id: '2609.30226'
url: https://arxiv.org/abs/2609.30226
pdf_url: https://arxiv.org/pdf/2609.30226
published: '2026-09-24'
collected: '2026-09-25'
category: Training
direction: RL 后训练策略组合预测
tags:
- RLHF
- policy composition
- post-training
- reward interpolation
- LoRA
one_liner: 提出 PoEM 框架，用已后训练策略的线性组合预测新奖励下的 RL 策略，无需再次运行 RL
practical_value: '- 在推荐/搜索的 LLM 后训练中，可维护多个单奖励 LoRA adapters（如相关性、点击、多样性），用 PoEM 组合近似新奖励策略，避免每次改奖励都重新
  RL；可利用 reward outputs 快速估计混合权重。

  - 若业务需要在线调整多个目标权重（如 GMV vs 用户体验），可离线训练几个 base 策略，线上通过线性组合 log-policy 动态合成，降低训练与维护成本。

  - 注意假设：奖励线性组合成立或 log-policy 低秩；在推荐场景中需验证多目标 reward 组合是否满足，若不满足可作为初始化再微调。

  - 工程实现可借鉴：用已有 adapter 的 logits/策略输出和 reward 值做最小二乘估计权重，无需额外梯度更新。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：基础模型后训练 RL 昂贵且不稳定，奖励函数改变或多奖励组合时需从头运行 RL。希望给定新奖励函数，直接用已后训练策略预测 RL 结果，避免重复训练。

**方法关键点**：
- 理论观察：若新奖励是已有奖励的线性组合，则新策略在 log 空间是已有 log-policy 的线性组合。
- 经验观察：即使奖励不线性相关，不同奖励下的 log-policies 通常张成近似低秩子空间。
- 权重估计：组合系数可仅通过 reward 输出或 basis policy 在样本上的输出估计，无需梯度更新。
- 算法：输入一组单奖励后训练模型和一个新奖励函数，输出近似目标 RL 策略。

**关键结果**：在合成与真实奖励上验证，覆盖文本和图像模态，证明 PoEM 可以在不运行额外 RL 的情况下逼近目标策略。
