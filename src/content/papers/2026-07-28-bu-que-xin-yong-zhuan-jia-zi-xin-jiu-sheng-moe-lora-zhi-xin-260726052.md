---
title: 'Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts
  LoRA'
title_zh: 不确信用专家，自信就省：MoE-LoRA 置信度自适应路由
authors:
- Tom Saliencro
- Rohan Desai
- Priya Nair
- Maya Lindqvist
- Daniel Whitmore
affiliations:
- University of California, Irvine
- University of Washington
arxiv_id: '2607.26052'
url: https://arxiv.org/abs/2607.26052
pdf_url: https://arxiv.org/pdf/2607.26052
published: '2026-07-28'
collected: '2026-07-29'
category: Training
direction: MoE-LoRA 置信度自适应路由
tags:
- MoE
- LoRA
- Adaptive Routing
- Uncertainty Estimation
- Budget Thermostat
- Nucleus Filtering
one_liner: 利用路由器分布作为 token 置信度信号，动态分配专家数量，在匹配预算下提升 MoE-LoRA 性能
practical_value: '- 在电商推荐模型的 LoRA/MoE-LoRA 微调中，可直接用路由器分布替代额外置信度模块，实现 token/representation
  的动态专家分配，节省推理成本。

  - 推荐系统在线服务的 PEFT 适配：设置预算恒温器（budget thermostat）自动校准阈值，使平均激活专家数恒定，便于工程实现尾部延迟控制。

  - 对用户/物品 Embedding 的 MoE 计算，可借鉴“分歧扩展”机制：当激活专家输出不一致时追加专家，提升困难样本质量。

  - OOD 检测可复用相同的置信度与分歧信号，无需额外模型，为推荐系统的安全性、时效性监控提供低成本方案。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：固定 top-k 的 MoE-LoRA 对所有 token 平均分配专家，导致简单 token 算力过剩、困难 token 算力不足。观察到路由器的输出分布本身已携带 token 难度信号：峰值尖锐意味着模型自信，分布平坦表示模型拿不准。

**方法**：提出 CARE（Confidence-Adaptive Routing of Experts），采用 nucleus 式路由：按路由器权重降序激活专家，直到累积概率超过阈值。若已激活专家间输出分歧大，则追加少量专家。通过一个“预算恒温器”动态调整阈值，使平均激活专家数精确匹配目标预算。该方案无需额外参数，单次前向推理即可完成。

**结果**：在 Llama-3.1-8B、Qwen2.5-7B 及多个常识、数学、代码、知识任务上，与计算量匹配的固定 k 相比，CARE 取得更好性能；甚至仅使用更少专家（激活量减少 12%）即可达到 k=4 基准线的表现。同一置信度与分歧信号还能提升 OOD 检测，超过最大 softmax 概率、熵及多趟推理等代理指标。
