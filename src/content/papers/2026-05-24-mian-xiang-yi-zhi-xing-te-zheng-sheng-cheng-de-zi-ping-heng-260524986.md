---
title: Self-Balancing Gradient Allocation for Heterogeneity-Aware Feature Generation
  in Click-Through Rate Prediction
title_zh: 面向异质性特征生成的自平衡梯度分配，用于CTR预测
authors:
- Moyu Zhang
- Yun Chen
- Yujun Jin
- Jinxin Hu
- Yu Zhang
- Xiaoyi Zeng
affiliations:
- Alibaba Group
arxiv_id: '2605.24986'
url: https://arxiv.org/abs/2605.24986
pdf_url: https://arxiv.org/pdf/2605.24986
published: '2026-05-24'
collected: '2026-05-26'
category: GenRec
direction: 生成式推荐 · 异质性特征生成 · 难度感知
tags:
- Generative CTR
- Discrete Diffusion
- Gradient Balancing
- Heterogeneity
- Self-Balancing Loss
- CTR Prediction
one_liner: 提出统一可学习难度信号，同时驱动自平衡损失和难度引导注意力，解决生成式CTR中不同字段重建难度不均衡问题。
practical_value: '- **自平衡损失加权**：将每个特征字段视为独立任务，借鉴多任务同方差不确定性加权，损失设为 `exp(-s)*loss +
  s/2`，无需手工调权，自动将更多梯度分配给高基数ID、序列等难重建字段，冷启动受益明显。

  - **难度引导注意力调制**：在HSTU去噪网络中，用 `exp(-s/2)` 缩放查询向量，抑制收敛后字段的注意力，增强困难字段的信息聚合，与损失加权使用同一
  `s` 信号，保持一致性。

  - **统一难度信号**：仅需学习每个字段一个标量 `s_i`，零额外超参数，与现有生成式预训练框架（如 DGenCTR）无缝集成，离线预训练开销极低。

  - **冷启动与长尾增益**：该方法对稀疏用户和长尾物品提升更大，生产环境中可针对这些分段部署，获得显著业务指标提升（在线 A/B 冷启动用户 CTR +9.2%）。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式 CTR 预训练通过重建全部特征字段提供密集监督，但现有方法对所有字段一视同仁，忽略了高基数 ID、稀疏类别、数值、序列字段之间的重建难度差异。简单字段（如低基数类别、数值）快速收敛，主导训练梯度，而信息量最丰富的高基数 ID 和序列字段长期欠拟合，导致下游 CTR 预测受损，尤其在冷启动和长尾场景下。

## 方法
- **统一难度信号**：为每个特征字段引入可学习的对数难度参数 `s_i`，联合去噪网络训练。
- **自平衡损失**：借鉴多任务不确定性加权，将每个字段视为独立任务，损失函数为 `L = sum_i [ exp(-s_i) * l_i + s_i/2 ]`。当字段重建损失 `l_i` 高时，权重 `exp(-s_i)` 自动增大，梯度向困难字段倾斜；平衡点 `exp(-s_i) = 1/(2l_i)` 稳定。
- **难度引导注意力**：在去噪网络的 HSTU 层中，用 `exp(-s_i/2)` 缩放查询向量 `q_i`，抑制已收敛字段的注意力输出，放大困难字段的跨字段信息流。缩放系数与损失权重共享 `s_i`，确保一致性。
- 框架基于离散扩散生成预训练，与 DGenCTR 的两阶段流程兼容。

## 实验
在 Criteo、Avazu、KDD12、Amazon（含序列）、工业数据集（68字段，513M样本）上评估。对比判别式（DeepFM、DCN、HSTU等）和生成式基线（GenCTR、DGenCTR、SGCTR）。HeteGenCTR 在所有数据集上 AUC 显著提升（工业数据集：0.7956→0.7974）。消融显示自平衡损失贡献最大，注意力调制提供额外增益。难度参数演化符合预期：ID与序列字段保持高权重。冷启动用户 AUC 提升 +0.0066（工业数据）。7天在线A/B测试：整体 CTR +4.7%，冷启动用户 +9.2%，99分位延迟增加 <0.5ms。

> 统一的可学习难度信号是解决生成式预训练中异质性重建不平衡的关键，它无需额外超参数，自动将训练容量分配给最难且最有用的字段。
