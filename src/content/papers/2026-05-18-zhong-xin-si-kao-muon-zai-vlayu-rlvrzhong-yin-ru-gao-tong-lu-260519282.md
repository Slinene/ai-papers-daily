---
title: 'Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies
  for VLA and RLVR'
title_zh: 重新思考Muon：在VLA与RLVR中引入高通滤波解决频谱失效
authors:
- Chongyu Fan
- Gaowen Liu
- Mingyi Hong
- Ramana Rao Kompella
- Sijia Liu
affiliations:
- Michigan State University
- Cisco
- University of Minnesota
- IBM Research
arxiv_id: '2605.19282'
url: https://arxiv.org/abs/2605.19282
pdf_url: https://arxiv.org/pdf/2605.19282
published: '2026-05-18'
collected: '2026-05-25'
category: Training
direction: 训练优化器设计：高通频谱滤波
tags:
- optimizer
- Muon
- spectral whitening
- VLA
- RLVR
- high-pass NS
one_liner: 提出Pion优化器，用高通频谱滤波替代Muon的均匀白化，解决VLA低秩噪声放大和RLVR不稳定问题
practical_value: '- 在电商推荐模型的**RLHF/RLVR微调**中，若使用类似Muon的优化器，需警惕低信噪比梯度导致崩溃，可改用Pion或保守选择AdamW。

  - 多任务或多头推荐模型中，**per-head独立更新**（通过reshape实现）能保留不同商品类目或用户群体的头部特异性，避免均匀白化破坏已学的差异性。

  - 在梯度噪声大、存在低秩组件的场景（如冷启动、稀疏特征），**高通滤波**思路可直接用于动量或梯度修正，抑制尾部方向噪声。

  - 预训练有效的优化器（如Muon）在微调/RL阶段可能失效，需根据梯度频谱特性做适配，Pion为这种迁移提供了低成本替换方案。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Muon通过牛顿-舒尔茨迭代将动量矩阵奇异值推向1（频谱白化），在LLM预训练中超越AdamW，但在**VLA（视觉-语言-动作）训练**中，动作模块梯度低秩，白化会放大噪声尾方向；在**RLVR（强化学习可验证奖励）**中，低信噪比梯度且需保持注意力头预训练差异化，白化导致不稳定甚至输出塌缩为零。

**方法**：提出Pion，将均匀白化替换为**两阶段“提升+抑制”高通NS迭代**：将主导奇异值固定在1附近，噪声尾成分压制到0，滤波强度可调。同时支持**per-head模式**，通过reshape在注意力头间独立更新，无额外开销，保留预训练异构性。

**结果**：在LIBERO VLA训练中，1500步后VLA-Adapter达到100%成功率，超越Muon (97.0%) 和AdamW (32.2%)；真实机器人抓放任务表现更优。RLVR后训练（Qwen3-1.7B/4B, GRPO/GMPO）中，MATH和GSM8K上Pion优于AdamW，而Muon梯度归零失败。Pion可作为Muon的直接替换，保持计算效率。
