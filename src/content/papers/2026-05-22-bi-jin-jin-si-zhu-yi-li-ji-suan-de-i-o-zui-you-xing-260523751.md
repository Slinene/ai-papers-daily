---
title: Approaching I/O-optimality for Approximate Attention
title_zh: 逼近近似注意力计算的 I/O 最优性
authors:
- Pál András Papp
- Aleksandros Sobczyk
- Anastasios Zouzias
affiliations:
- Huawei Technologies
arxiv_id: '2605.23751'
url: https://arxiv.org/abs/2605.23751
pdf_url: https://arxiv.org/pdf/2605.23751
published: '2026-05-22'
collected: '2026-05-25'
category: Training
direction: I/O 高效近似注意力计算
tags:
- Approximate Attention
- I-O Complexity
- FlashAttention
- Lower Bound
- LLM Training
one_liner: 将近似注意力与 I/O 高效算法结合，使数据传输量几乎线性于序列长度，逼近理论下界
practical_value: '- 在长序列场景（如电商用户行为序列或 Agent 长时间交互记忆）中，可参考其近似框架，用多项式展开或低秩分解替代精确 softmax，大幅减少显存访问与传输量。

  - 工程实现上，可将近似注意力与 tile 策略结合，在 GPU 共享内存有限的推理环境下获得比 FlashAttention 更低的 I/O 开销，适合边缘部署。

  - 论文提供 I/O 下界分析，可用来评估自研注意力近似方案的数据搬运效率是否接近最优，指导算法选型（例如多项式次数、分块大小）。

  - 对于生成式推荐中的语义 ID 序列建模，长上下文注意力是瓶颈，借鉴此近似方法有望在损失微小精度下换取显著的训练/推理速度提升。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有精确注意力实现（如 FlashAttention）虽然通过 tiling 避免完整注意力矩阵的物化，但其 I/O 复杂度仍与序列长度 n 呈二次相关，远高于仅需读取输入输出矩阵的平凡下界 Ω(nd)。当 n 极大时，数据搬运成为瓶颈。

**方法**：受 Alman & Song (NeurIPS 2023) 近似注意力框架启发，不显式计算 QK^T 矩阵，而是通过对 softmax 核进行多项式展开或低秩变换，将注意力计算分解为多次矩阵-向量乘法或小矩阵乘加操作。关键设计在于整个计算过程只处理大小为 d 的向量或低维中间结果，从而避开 n×n 量级的临时数据，使快慢存传输量几乎与 n 成线性关系。

**关键结果**：在大多数参数区域（n 较大，d ≪ n），I/O 成本为 Õ(nd)，仅比平凡下界多出对数因子，逼近理论最优。同时为各参数区证明匹配的下界，表明算法在 I/O 意义上接近无法再改进。
