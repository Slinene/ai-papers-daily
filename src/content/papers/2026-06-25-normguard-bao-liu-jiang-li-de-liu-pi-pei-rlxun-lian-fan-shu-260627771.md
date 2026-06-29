---
title: 'NormGuard: Reward-Preserving Norm Constraints in Flow-Matching Reinforcement
  Learning'
title_zh: NormGuard：保留奖励的流匹配RL训练范数约束
authors:
- Tianlin Pan
- Lianyu Pang
- Cheng Da
- Huan Yang
- Changqian Yu
- Kun Gai
- Wenhan Luo
affiliations:
- The Hong Kong University of Science and Technology
- Kuaishou Technology
- University of Chinese Academy of Sciences
arxiv_id: '2606.27771'
url: https://arxiv.org/abs/2606.27771
pdf_url: https://arxiv.org/pdf/2606.27771
published: '2026-06-25'
collected: '2026-06-29'
category: Training
direction: 流匹配RL训练的范数正则化
tags:
- Flow Matching
- RL Fine-tuning
- Norm Regularization
- Reward Alignment
- Image Generation
one_liner: RL微调会导致流模型速度范数膨胀损害质量，提出训练时hinge惩罚有效抑制并保持奖励
practical_value: '- 在电商/推荐场景使用生成式模型（如流匹配生成item embedding或序列）进行RL微调时，可借鉴 NormGuard
  监控并约束输出速度范数，防止过度偏离参考模型导致质量崩塌。

  - 推理时归一化无效的结论提示：对于推荐系统的RL策略优化，单纯在推理阶段调整输出分布（如温度缩放）不足，需在训练时嵌入正则项。

  - hinge 惩罚设计简洁，可与任何 velocity-local base loss 加性组合，易于迁移到现有 RL 训练管线中（例如 DPO、NFT 的推荐版本）。

  - 范数膨胀作为质量退化的早期信号，可用于训练过程中实时监测，辅助自动早停或触发约束。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：RL 后训练虽提升流匹配生成器的奖励匹配度，却常损害视觉质量。作者发现三种 RL 方法（NFT、AWM、DPO）均导致每步速度范数‖v_θ‖相对参考膨胀 5%-15%，且与过锐、过饱和等失真相关。类似现象在 CFG 中可通过推理时重缩放缓解，但此处推理时归一化完全失效：因为范数膨胀已与模型权重协同适配，重缩放既不改善奖励也不恢复质量；进一步邻接敏感度分析表明，速度幅值重缩放不携带一致的一阶奖励信号，说明抑制范数膨胀不会移除与奖励相关的成分。因此，训练时干预是唯一有效策略。

**方法**：提出 NormGuard——一种 hinge 惩罚项，仅在‖v_θ‖超出参考范数‖v_ref‖时激活，直接加性组合到任意速度局部基础损失上，无需改动原损失函数。

**结果**：在两个基模型、三种后训练方法、两个奖励代理上，NormGuard 一致提升 MLLM 评判的图像质量与法医真实感，且保持奖励，增益在少步推理下进一步放大，排除早期停止的解释。代码已开源。
