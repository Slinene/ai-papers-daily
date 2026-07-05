---
title: Self-Gating Attention for Efficient Time Series Forecasting
title_zh: 自门控注意力：高效时间序列预测
authors:
- Dezheng Wang
- Tong Chen
- Wei Yuan
- Congyan Chen
- Shihua Li
- Hongzhi Yin
arxiv_id: '2607.02344'
url: https://arxiv.org/abs/2607.02344
pdf_url: https://arxiv.org/pdf/2607.02344
published: '2026-07-02'
collected: '2026-07-05'
category: Other
direction: 高效注意力机制 · 时序预测
tags:
- Self-Gating Attention
- Linear Complexity
- Time Series Forecasting
- Efficient Transformer
- Plug-and-Play
- Deployment-Oriented
one_liner: 提出即插即用的自门控注意力，以线性复杂度维持预测性能，避免冗余注意力计算。
practical_value: '- 在推荐系统的用户行为序列建模中，可直接替换标准自注意力，省略 query/key 投影，显著降低长序列的计算和内存开销，适合高并发在线推理。

  - 共享注意力矩阵 + 轻量残差的设计，可应对行为序列中常见的重复模式（如周期性、固定套路），对电商场景的点击序列预测有直接迁移价值。

  - 即插即用特性允许快速集成到现有 Transformer 推荐模型（如 SASRec、BERT4Rec）中，仅需微小改动即可获得推理加速。

  - 在边缘设备或资源受限推理环境下，SGA 能保持竞争力性能，适合部署在移动端推荐、实时出价等延迟敏感系统。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：标准自注意力在长历史窗口下的二次复杂度，严重制约了时间序列预测模型在资源受限或高吞吐工业系统中的部署。通过定性与定量分析，论文发现时间序列预测的注意力图常包含大量跨时间步的冗余模式，源于许多真实序列的重复周期和稳定时间相关性。

**方法**：提出 **Self-Gating Attention (SGA)**，一个即插即用的注意力模块。它用**共享可学习矩阵**捕获共性的注意力模式，同时叠加一个**输入依赖的轻量残差**来适应序列特异性。该设计完全绕过了 query 和 key 的投影计算，将注意力分数的计算复杂度降为 **线性时间与线性评分矩阵内存**（相对回溯窗口长度）。SGA 可无缝集成到多种预测骨干网络中。

**结果**：在电力、金融、天气、医疗等9个公开真实数据集上，SGA 与标准自注意力及多种轻量注意力变体（如 ProbSparse, Informer 等）对比，在保持有竞争力的预测精度的同时，**显著提升了推理效率**，提供了面向部署的有效基准。
