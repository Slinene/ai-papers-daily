---
title: Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training
title_zh: 运行时编排的二阶优化实现可扩展大模型训练
authors:
- Yishun Lu
- Junhao Zhang
- Zeyu Yang
- Wes Armour
affiliations:
- University of Oxford
arxiv_id: '2605.16184'
url: https://arxiv.org/abs/2605.16184
pdf_url: https://arxiv.org/pdf/2605.16184
published: '2026-05-15'
collected: '2026-05-18'
category: Training
direction: 二阶训练运行时优化
tags:
- second-order optimization
- runtime system
- asynchronous computing
- distributed training
- state offloading
- LLM training
one_liner: Asteria通过异步状态分布和有界陈旧同步，将二阶优化器高效应用于大模型训练
practical_value: '- **优化器状态卸载到主机**：将二阶优化器的大矩阵状态移至CPU内存或NVMe，GPU仅保留模型参数与梯度，大幅降低显存占用，使推荐/Agent模型中亦可尝试SOAP等二阶优化器以提升样本效率。

  - **异步逆平方根计算**：利用训练hook预准备影子状态，在主机端后台计算昂贵的矩阵逆平方根，GPU不用等待，适合大embedding矩阵等场景下将耗时的矩阵运算剥离出关键路径。

  - **有界陈旧同步协议**：分布式训练中设定同步频率上限，结合拓扑感知协调，在多个worker间减少通信开销的同时保障优化有效性，可直接在电商推荐模型的分布式训练中推广。

  - **存储分层与动态调度**：根据运行时内存压力，动态在GPU显存、CPU内存、NVMe间迁移优化器状态，应对内存受限环境，为部署大规模agent或生成式推荐模型的训练提供弹性资源管理思路。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：二阶优化器（如SOAP、Shampoo）能显著提升大模型训练的样本效率，但其庞大的矩阵状态和逆平方根计算导致极高的显存与同步开销，限制了实际应用。

**方法**：提出运行时系统Asteria，将二阶优化逻辑从GPU关键路径中解耦。首先，动态分布优化器状态到GPU显存、CPU内存和NVMe存储，根据内存压力分层放置。其次，利用训练hook提前准备影子状态，使逆平方根计算异步执行在主机端，GPU无需等待。分布式训练中，采用有界陈旧性协议，以拓扑感知方式协调各节点，限制同步频率，降低通信开销的同时保证优化质量。

**结果**：在单一GB10 GPU（128GB统一内存）上，Asteria成功支持1B参数模型的二阶训练；在多节点GH200集群上，7B模型训练中可见优化器开销降低，周期性延迟尖峰减少，壁钟时间下的收敛加速，且保持了SOAP和KL-Shampoo的优化效果。证明了通过运行时系统设计，而非仅简化优化器，可使二阶大模型训练具有实用性。
