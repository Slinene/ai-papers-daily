---
title: Scaling Automatic Research Agents via World Models
title_zh: 用世界模型扩展自动研究智能体训练
authors:
- Xiyuan Yang
- Sheikh Sarwar
- Jingru Cheng
- Zhan Shi
- Duanshun Li
- Huiyuan Chen
- Haiyang Zhang
- Xing Fan
- Chenlei Guo
- Jingrui He
affiliations:
- University of Illinois Urbana-Champaign
- Amazon
arxiv_id: '2608.12564'
url: https://arxiv.org/abs/2608.12564
pdf_url: https://arxiv.org/pdf/2608.12564
published: '2026-08-28'
collected: '2026-09-11'
category: Agent
direction: 智能体 RL 训练效率优化
tags:
- World Model
- RL
- AutoResearch Agent
- Post-training
- Debiasing
- Variance Reduction
one_liner: 用世界模型替代真实环境执行，消除 AutoResearch RL 训练瓶颈，并引入去偏与降噪提升稳定性
practical_value: '- 面向 Agent 后训练 RL：当环境交互成本远高于生成成本时，可训练一个世界模型替代真实环境执行，缓解训练吞吐瓶颈；在电商场景可模拟用户点击、搜索反馈等环境动态。

  - 世界模型奖励存在偏差和噪声时，可借鉴 Online Debiasing 维护偏差估计并修正奖励，结合 Inverse-Variance Denoising
  对高方差样本降权，提升 RL 训练稳定性。

  - 小模型智能体后训练：用世界模型蒸馏环境反馈，可在有限算力下让 4B/9B 智能体逼近甚至超过更大开源模型，适合业务侧轻量级 Agent 部署。

  - 该方法在 embodied VLA 策略上也有效，说明世界模型 RL 的分离生成与执行成本的思路具有跨任务迁移潜力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：AutoResearch 智能体通过 RL 后训练能够独立完成方案实现、实验执行和结果迭代。但训练轨迹中，agent 生成部分可通过批处理共享算力，而环境执行部分需要独占沙箱和真实机器时间，两者扩展方式不对称，导致环境执行成为训练成本瓶颈。

**方法关键点**：提出 World Model RL (WMRL)，用可学习世界模型替代真实环境执行，消除该瓶颈。针对世界模型奖励可能受偏差和噪声污染的问题，设计 Online Debiasing 和 Inverse-Variance Denoising 两个缓解机制：前者在线估计并修正奖励偏差，后者根据奖励方差对样本加权以抑制噪声。理论证明两种机制均严格改善收敛保证。

**关键结果**：WMRL 在多个任务和不同智能体规模上将训练加速 3–4 倍，同时性能超过标准 RL 基线。后训练的 4B 和 9B 智能体在 held-out 基准上超过 48B 和 120B 的开源权重智能体。此外，WMRL 可迁移到 embodied VLA 策略后训练，验证方法通用性。
