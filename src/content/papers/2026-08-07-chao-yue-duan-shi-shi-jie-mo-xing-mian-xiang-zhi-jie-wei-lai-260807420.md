---
title: 'Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future
  Prediction'
title_zh: 超越短视世界模型：面向直接未来预测的长时域端到端训练
authors:
- Xinyi Li
- Zaishuo Xia
- Chenjie Hao
- Yubei Chen
affiliations:
- University of California, Davis
arxiv_id: '2608.07420'
url: https://arxiv.org/abs/2608.07420
pdf_url: https://arxiv.org/pdf/2608.07420
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: 世界模型长时域训练范式
tags:
- world model
- end-to-end training
- long-horizon prediction
- endpoint objective
- non-recursive architecture
one_liner: 提出直接预测终端状态的训练范式，避免递归误差累积，显著提升长时域预测精度
practical_value: '- **长序列动作效果评估**：在电商广告序列投放或对话式推荐中，可通过直接优化最终转化/满意度目标的训练方式，替代单步奖励预测的误差累积，提升长期效果的预估精度。

  - **Planning 与 Agent 决策**：方法可直接用于生成式 Agent 的多步规划，将动作序列编码为单一嵌入后预测终点状态，避免自回归展开的推理不稳定性和高昂计算成本。

  - **轨迹级别的损失设计**：在用户行为序列建模（如 session-based 推荐）中，可以借鉴端点回归的思想，直接优化对最后交互 item 的预测，而非每一步的
  next-item 预测，可能提升高价值末尾行为的召回。

  - **非递归架构设计**：DPWM 的并行化动作序列编码模式（如 Transformer 或卷积）可直接迁移到广告序列生成模型中，将整段预算分配计划压缩为平面表示，一次性预测最终效果，加速在线求解。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有世界模型普遍通过局部少步预测目标训练，部署时递归展开预测长时域未来，导致局部误差放大、梯度传播不稳定，且训练时对所有转移等权对待，忽略不同转移对终点的差异影响。作者认为长时域精度应通过直接优化端点预测目标实现。

**方法关键点**：
- 提出 **Direct Prediction World Model (DPWM)**，一种非递归架构：将任意长度的动作序列压缩为单一嵌入，单次前向传播直接预测终止时刻的观测。
- 训练目标为端到端的终点预测误差，梯度无需通过递归展开反向传播，避免了长时域训练的不稳定性。
- 实验表明，在连续控制和像素环境中，DPWM 的长时域端点预测性能显著优于递归 baseline，且视界越长优势越大。
- 进一步将递归模型用相同端点目标重新训练时，同样获得相似提升，表明训练目标而非网络形式是长时域预测性能的关键。

**关键结果**：
- 在 DMControl 视觉任务上，预测视界 100 步时，DPWM 的终点观测预测误差较递归基线（RSSM）降低约 40%。
- 将 RSSM 改用端点回归目标训练后，其性能接近 DPWM，差距从差距显著缩小至~5% 以内。
- 消融显示，训练时直接考虑终点信号相比仅用单步/多步局部损失，长期效果提升幅度最大。
