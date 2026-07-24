---
title: Predictive Divergence Masks for LLM RL
title_zh: 预测散度掩码：LLM 强化学习的信任域方向优化
authors:
- Xiangxin Zhou
- Jiarui Yao
- Penghui Qi
- Bowen Ping
- Jiaqi Tang
- Haonan Wang
- Tianyu Pang
affiliations:
- Tencent Hunyuan
- UIUC
- NUS
arxiv_id: '2607.10848'
url: https://arxiv.org/abs/2607.10848
pdf_url: https://arxiv.org/pdf/2607.10848
published: '2026-07-11'
collected: '2026-07-24'
category: Training
direction: LLM 强化学习 · 信任域方向准则
tags:
- LLM RL
- PPO
- Predictive Divergence Mask
- Trust Region
- Top-K Estimation
- Off-policy
one_liner: 提出预测散度掩码替代 PPO 比率方向测试，用散度变化预测决定是否屏蔽 token
practical_value: '- 在推荐/Agent 的 RL 策略训练中，PPO 原有的 ratio 方向屏蔽可能导致错误保留会使散度增大的更新，改用散度方向预测可提升离线更新的稳定性与效率。

  - 当策略输出为 top-K 候选时（如推荐列表生成、对话动作筛选），论文的两种轻量级 top-K 估计器可直接嵌入，无需完整分布即可计算散度变化方向。

  - 预测散度掩码的闭式解计算开销低，适合大规模线上 RL 训练时的 token 级动态屏蔽，降低训练-推理分布漂移风险。

  - 该方法对模型规模与精度设置鲁棒，可以无缝集成到现有 PPO/DPPO 训练框架中，改善 reward hacking 并提升最终策略质量。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM RL 常用信任域掩码稳定离线更新，PPO 使用采样 token 重要性比率同时判断“接近性”（策略移动过多）和“方向”（更新是否拉大分布差异）。近期 DPPO 改用散度衡量接近性，但方向准则仍沿用比率。作者发现该比率方向与散度变化方向经常不一致，导致错误屏蔽。

**方法**：提出**预测散度掩码**，直接预测下一步策略梯度更新会增加还是减少行为策略与训练策略间的同一定义散度。针对 LLM 的离散 softmax 策略给出了方向预测的闭式解。考虑到生产环境仅暴露 top-K 词汇分布，进一步开发两种轻量级 top-K 估计器：基于 top-K 重归一化与基于重要性采样近似。

**关键结果**：分析表明散度方向预测与散度实际变化的一致性显著优于采样比率，在多个模型规模和精度配置下 RL 训练效果均有提升，验证了预测散度掩码的实用性与鲁棒性。
