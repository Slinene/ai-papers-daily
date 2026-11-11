---
title: 'A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference
  Resets'
title_zh: 后训练策略优化：覆盖坍缩与参考重置的理论
authors:
- Audrey Huang
- Nan Jiang
- Sham M. Kakade
- Sadhika Malladi
- Akshay Krishnamurthy
- Dylan J. Foster
arxiv_id: '2611.14467'
url: https://arxiv.org/abs/2611.14467
pdf_url: https://arxiv.org/pdf/2611.14467
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: LLM 后训练策略优化理论
tags:
- post-training
- PPO
- GRPO
- coverage collapse
- KL regularization
- policy optimization
one_liner: 证明参考重置可避免策略优化中的覆盖坍缩，使 PPO/GRPO 与平方损失法实现覆盖保持的全局收敛。
practical_value: '- 在推荐/广告文案生成用 GRPO/PPO 微调 LLM 时，若发现生成多样性骤降、只集中少数模板，很可能是 coverage
  collapse；不要只固定 KL 到 SFT 基模型，建议每隔若干步把 KL reference 重置为当前策略（APMD）。

  - APMD 允许使用更强的 KL 正则：每个子问题更平滑、更好解，同时重置参考不会牺牲全局最优；这比单纯调小 learning rate 或加大 batch
  更本质。可在训练不稳定时优先增加 KL 强度并配合 reference reset。

  - 对电商/Agent 场景中的黑盒 reward（点击、GMV、工具成功率），平方损失形式的策略优化（Kimi 式）隐式实现 reference reset，可作为实现更简单、更稳的替代方案，尤其适合稀疏
  reward 或低容错在线实验。

  - 若在 Agent 工具选择/会话式推荐中用 RL，可借鉴 coverage-preserving 概念：监控采样回放中成功/高 reward 轨迹的概率占比，避免策略过早收敛到次优工具序列。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 后训练中策略优化（PPO/GRPO）广泛使用，但缺乏覆盖保持的理论保证。作者研究如何以基模型对最优响应的覆盖度来控制样本与梯度复杂度。

方法：指出 REINFORCE 即使有精确梯度也会使最优响应概率坍缩到接近 0，且在固定基模型 KL 正则下仍会发生。提出 APMD 元算法：顺序求解多个 KL 正则化 RL 子问题，并把 KL 参考定期重置为最近策略；这样强正则使子问题更易解，参考重置保持全局收敛。

在预训练特征上的 softmax 线性策略族中，证明带显式 KL 与参考重置的 PPO/GRPO 变体、以及隐式实现该机制的平方损失算法（如 Kimi 训练方法）均具有覆盖保持性，首次获得全局收敛保证。

结果：样本与梯度步数由基模型的最优响应覆盖度定界，并揭示正则化强度、clipping 与目标函数选择对采样/优化成本的影响。
