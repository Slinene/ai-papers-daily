---
title: Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport
title_zh: 模型感知调度通过纤维最优传输改进生成
authors:
- Luyi Jia
- Boyan Zhang
- Yilun Liu
- Steffen Rulands
affiliations:
- Arnold-Sommerfeld-Center for Theoretical Physics, Ludwig-Maximilians-Universität
  München
- Institute of Informatics, Ludwig-Maximilians-Universität München
- Munich Center for Machine Learning
arxiv_id: '2609.11842'
url: https://arxiv.org/abs/2609.11842
pdf_url: https://arxiv.org/pdf/2609.11842
published: '2026-09-10'
collected: '2026-09-12'
category: Training
direction: 扩散/流匹配训练调度优化
tags:
- diffusion models
- flow matching
- optimal transport
- training schedule
- generative models
one_liner: 提出基于纤维最优传输的模型感知调度，显著提升扩散/流匹配生成效率，并发现可复用的风险模板
practical_value: '- 训练时间重分配思路可迁移到扩散式生成推荐：用早期 checkpoint 估计模型在不同噪声时间步的预测风险，将训练采样集中在高风险区域，提升
  item 表示生成质量或加速推理采样。

  - 归一化风险 profile 跨模型/设置的经验普适性表明，可以离线生成一个冻结的解析调度模板，在类似任务中直接复用，省去逐模型调参成本。

  - 模型感知调度把计算资源向预测困难处倾斜，与推荐中困难样本挖掘/课程学习思想一致，可结合业务指标设计风险函数，例如对高交互稀疏 item 的时间步加权。

  - 注意该工作面向图像生成，迁移到推荐需谨慎：需重新定义纤维上的 OT 成本（如 item embedding 距离），并适配召回/NDCG 等业务目标。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散和流匹配模型的信号/噪声系数调度对生成质量与采样效率至关重要。现有基于 kinetic action 的模型无关方法虽然能解释强基线，但忽略实际预测误差，导致采样步数分配不优。

**方法**：作者提出 fiberwise optimal transport 构造模型感知调度。在概率路径的固定时间和状态，所有兼容的信号/噪声分解构成仿射纤维；定义纤维预测风险为真实分解与预测器诱导分解之间的最优传输成本期望。将该风险与系数路径 kinetic action 结合，得到闭式最优时间分配。风险 profile 可由早期 baseline checkpoint 估计，无需完整训练。方法可扩展到一般线性预测目标。

**结果**：在 DDPM 和 flow matching 上，跨预测目标、训练配置、数据集和架构，模型感知调度一致优于强基线，例如 flow matching 在 CIFAR-10 上 16 次函数评估的 FID 相对降低 38.6%。进一步发现，不同模型/设置下的归一化纤维风险 profile 高度对齐，冻结解析模板即可保留大部分改进，并在较大的 conditional latent diffusion 和 2-RF 模型上得到验证。
