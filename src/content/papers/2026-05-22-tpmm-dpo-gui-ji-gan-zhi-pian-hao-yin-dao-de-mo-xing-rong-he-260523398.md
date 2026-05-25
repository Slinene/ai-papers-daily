---
title: 'TPMM-DPO: Trajectory-aware Preference-guided Model Merging for Iterative Direct
  Preference Optimization'
title_zh: TPMM-DPO：轨迹感知偏好引导的模型融合用于迭代直接偏好优化
authors:
- Lingling Fu
- Yongfu Xu
affiliations:
- Guangxi University
arxiv_id: '2605.23398'
url: https://arxiv.org/abs/2605.23398
pdf_url: https://arxiv.org/pdf/2605.23398
published: '2026-05-22'
collected: '2026-05-25'
category: Training
direction: 迭代 DPO 训练稳定性优化
tags:
- DPO
- model merging
- iterative alignment
- training stability
- trajectory
- noise robustness
one_liner: 提出轨迹感知模型融合方法，用学习到的融合权重整合迭代 DPO 过程中的历史模型，构建更稳定的参考模型，有效抑制噪声累积和性能退化。
practical_value: '- **迭代偏好对齐的稳定训练**：在电商对话、推荐理由生成等用到迭代 DPO 的场景，直接用上一轮模型作为参考可能引入噪声累积。可借鉴
  TPMM-DPO，保留历史模型轨迹，通过可学习融合权重动态构建参考模型，提升训练稳健性。

  - **模型融合权重学习**：相比简单平均，学习到的融合权重能更好地抑制噪声，可应用于其他需要集成多代策略模型的场景（如 Agent 多轮自我改进）。

  - **偏好数据抗噪**：当偏好标注存在噪声（如人工标注不一致、自动收集的反馈），该方法能减轻过拟合和性能波动，适合电商 UGC 环境下的大规模偏好数据训练。

  - **工程实现简单**：融合模块即插即用，一般是在线合并模型参数，无需额外训练奖励模型，可直接插入现有 DPO pipeline。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**【动机】**
迭代 DPO 将前一轮的策略模型直接用作下轮的参考模型，导致偏好数据噪声和参考模型误差逐步累积，引发后期过优化、性能震荡和泛化下降。

**【方法要点】**
提出 TPMM-DPO，将迭代 DPO 过程中产生的历史策略模型序列视为一条优化轨迹，通过可学习的融合权重自适应地整合多个中间模型，构造更平滑、稳健的参考模型。融合权重由偏好信号引导，训练时联合优化，避免简单依赖单一旧模型。

**【关键结果】**
- 标准迭代 DPO 在训练中后期常出现生成质量退化，TPMM-DPO 在域内和域外评估上均获得更高的胜率和奖励分数，且性能持续提升。
- 消融实验表明，可学习权重融合比简单平均更能缓解噪声引起的后期性能衰减。
- 方法在多种偏好噪声条件下表现出更强的鲁棒性。
