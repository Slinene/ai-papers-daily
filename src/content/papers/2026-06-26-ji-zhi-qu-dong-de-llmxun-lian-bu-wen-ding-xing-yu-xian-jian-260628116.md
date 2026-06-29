---
title: Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability
title_zh: 机制驱动的LLM训练不稳定性预先检测监控器
authors:
- Ruixuan Huang
- Yipei Wang
- Wenyi Fang
- Hantao Huang
- Yifan Huang
- Ansheng You
- Zhenxing Zhang
- Shuai Wang
- Fan Wu
- Yang Zheng
affiliations:
- HKUST
- Huawei
arxiv_id: '2606.28116'
url: https://arxiv.org/abs/2606.28116
pdf_url: https://arxiv.org/pdf/2606.28116
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: LLM训练稳定性异常检测
tags:
- Training Stability
- Fault Detection
- Low-precision Attention
- MoE
- Monitoring
one_liner: 从注意力谱熵和MoE路由器内部信号提前数千步预警训练崩溃
practical_value: '- 若你的推荐系统使用低精度训练（如FP8），可监控注意力层的谱熵一阶项，在损失发散前数千步预警，避免资源浪费。

  - 对于采用MoE架构的生成式推荐模型，可借鉴论文中的路由器负载和专家选择分布指标，提前发现路由崩塌。

  - 训练大型模型时，不要只依赖loss和梯度范数，引入模块内部的结构化信号进行健康监测，提高训练效率。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：前沿LLM训练消耗巨大算力，稳定性故障损失昂贵。但数值或超参数故障已破坏训练动态后，loss和梯度范数可能仍正常数千步，导致发现延迟。

**方法**：提出机制驱动的监控思路，从关键模块功能角色推导最早可测异常信号。对低精度flash attention，计算QK双线性分解的谱熵，其一阶项在loss崩溃前出现异常。对MoE路由器，根据专家选择功能推导分布指标（如负载均衡度）。通过故障注入实验（低精度注意力误差、大学习率、组合故障）验证信号有效性。

**结果**：这些内部指标对不同故障给出不同签名，可在loss发散前数千步触发警报，实现预知检测，且比传统指标更早、更明确。
