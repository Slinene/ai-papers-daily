---
title: Subspace Inference Enables Efficient Active Reward Learning from Preferences
title_zh: 子空间推断让偏好主动奖励学习更高效
authors:
- Yutai Zhou
- Erdem Bıyık
affiliations:
- University of Southern California
arxiv_id: '2609.04066'
url: https://arxiv.org/abs/2609.04066
pdf_url: https://arxiv.org/pdf/2609.04066
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: 主动偏好学习 · 贝叶斯滤波
tags:
- RLHF
- Active Learning
- Bayesian Deep Learning
- Extended Kalman Filter
- Preference Learning
one_liner: 用低维子空间扩展卡尔曼滤波追踪奖励模型不确定性，以更少偏好标注训出高质量奖励模型
practical_value: '- 可将“低维参数子空间 + EKF”的在线不确定性量化方案迁移到推荐/搜索的用户反馈场景：例如对排序策略、创意文案或 prompt
  偏好做主动对比采样，只维护子空间后验，避免对大模型全参数做后验推断，显著降低在线更新成本。

  - 采集函数基于参数采样高效计算，可复用信息增益/BALD 等主动学习指标，在电商标注预算有限时用于选择最有信息量的偏好对，减少人工评估次数。

  - 方法给出的不确定性校准更好，适合用在带探索的在线决策（如 bandit 或 RLHF 策略）中，降低过度自信带来的推荐风险。

  - 可增量接入现有 RLHF/偏好优化流程，若团队使用 LLM-as-a-judge 或偏好奖励模型，可考虑用子空间 EKF 在线更新 reward model，替代全量微调。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
RLHF 学习奖励模型通常需要大量人类偏好标注，主动学习能减少标注成本，但前提是能可靠地估计奖励模型的不确定性；对大型神经网络做全参数后验推断在计算上不可行，因此难以扩展到实际 RLHF 流程。

**方法关键点**  
PreferenceEKF 将主动偏好学习建模为序列贝叶斯滤波问题：在低维参数子空间内使用扩展卡尔曼滤波（EKF）进行序列推断，随着新的偏好查询到达持续更新奖励模型后验；再通过从子空间后验采样网络参数，高效计算主动学习采集函数，选择最有信息量的样本。该方法避免了全参数后验推断的高昂代价，同时保持可扩展的采样能力。

**关键结果**  
在 D4RL 与 V-D4RL 基准上，PreferenceEKF 相比其他 Bayesian deep learning 方法在样本效率、运行时间、可扩展性和不确定性校准方面均表现更好；学习到的奖励模型用于离线强化学习策略时也取得有竞争力的表现，验证了可扩展贝叶斯方法在偏好奖励建模中的潜力。
