---
title: 'How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization'
title_zh: 混合专家模型缩放：从μP到最大尺度稳定性参数化
authors:
- Leena Chennuru Vankadara
- Moritz Haas
- Luke Hayward
- Sebastian Bordt
- Alessandro Breccia
affiliations:
- University College London
- Amazon
- University of Tübingen
arxiv_id: '2605.14200'
url: https://arxiv.org/abs/2605.14200
pdf_url: https://arxiv.org/pdf/2605.14200
published: '2026-05-13'
collected: '2026-05-15'
category: Training
tags:
- MoE
- Scaling Laws
- μP
- MSSP
- DMFT
- Training Dynamics
one_liner: 提出最大化尺度稳定性参数化 (MSSP) 解决 MoE 联合缩放时的动态退化问题，恢复学习率迁移和单调性能增益
score: 10
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：大规模语言模型普遍采用混合专家 (MoE) 架构，但如何联合缩放嵌入宽度 N、专家宽度 Ne、专家数量 M、活跃专家数 K 及深度 L 的超参数一直缺乏原则性指导。现有最大更新参数化 (μP) 在密集网络中有效，却在 MoE 的多种联合缩放模式下失效，导致性能不随规模单调上升、学习率无法迁移。

**方法关键点**：
- 定义三种缩放模式：(I) N,Ne→∞ 且 M,K 固定；(II) N,M,K→∞ 且 Ne 固定；(III) N,Ne,M,K 全比例缩放。
- 推导各模式的 μP 并诊断其失败根源：跨专家聚合中，中心极限定理 (CLT) 和大数定律 (LLN) 行为失衡，使得某些项随规模衰减或发散，破坏特征学习动态。
- 提出**最大尺度稳定性 (MSSP)** 原则：要求前向、后向及聚合的所有分解项（初始、有效、传播）均保持 Θ(1)。据此给出修正参数化：
  - Regime II：将专家输出初始化方差从 1/Ne 放大至 M/Ne；
  - Regime III：在初始化时共享专家权重；
  - Regime I：路由器零初始化。
- 利用动态平均场理论 (DMFT) 验证 MSSP 的极限动态良好定义，其中 Regime III 呈现独特的四层条件平均场层次。

**关键实验**：
- 在 TinyImageNet 上训练 MLP MoE：μP 下 Regime II/III 损失随规模恶化，MSSP 恢复单调下降；例如 Regime II 采用 SGD 时，MSSP 训练损失随宽度单调改善，而 μP 相反。
- 训练 GPT MoE (Transformer) 至宽度 2048 或 2.5B 参数：MSSP 实现最优学习率跨宽度迁移，μP 则发生明显偏移。
- 坐标检查证实 MSSP 下所有关键量始终保持 Θ(1)，μP 中初始消失项引发级联尺度依赖。

**一句话**：MoE 缩放需要超越 μP 的最大尺度稳定性，通过针对不同缩放模式的结构化修正，才能真正实现可预测的性能提升和超参数迁移。
