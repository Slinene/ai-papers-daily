---
title: 'SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend
  SuperPOD'
title_zh: SLAI T-Rex：在昇腾超节点上对DeepSeek-V4家族进行全参数后训练
authors:
- Dongfang Li
- Xiaodong Luo
- Ruoyu Sun
- Xuhui Chen
- Linyuan Qiu
- Jian Meng
- Zhengxuan Lu
- Yiting Wang
- Yucheng Xie
- Tao Guo
affiliations:
- Shenzhen Loop Area Institute
arxiv_id: '2607.20145'
url: https://arxiv.org/abs/2607.20145
pdf_url: https://arxiv.org/pdf/2607.20145
published: '2026-07-21'
collected: '2026-07-23'
category: Training
direction: 万亿参数MoE全参数训练优化
tags:
- MoE
- Distributed Training
- Ascend NPU
- MFU
- Domain Specialization
- Operations Research
one_liner: 在昇腾NPU超节点上实现万亿参数MoE模型全参数后训练，达34.22% MFU，并构建运筹优化领域专用模型
practical_value: '- 大规模MoE分布式训练优化经验可迁移到推荐模型训练：模型并行+流水线并行组合、计算与通信重叠编排、低层核函数优化等技巧，能直接提升推荐大模型训练效率与MFU

  - 领域数据构建管线：结合收集资源和求解器验证的合成数据，可用于构建电商搜索/广告/Agent场景下带强逻辑验证的微调数据集，例如用业务规则引擎验证生成式推荐结果的合理性

  - 全参数后训练相比LoRA等轻量微调能更深层地注入领域知识，适合需要强结构化推理的任务（如广告策略生成、复杂购物决策Agent），在算力资源允许时值得尝试

  - 昇腾NPU上的全栈优化实践表明，从并行策略到算子级别的适配可带来明显加速，对国产化推荐系统基础设施的选型与调优有参考意义'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：万亿参数MoE模型的全参数后训练面临内存压力、通信开销与内核执行效率等系统挑战，且现有方案多基于GPU集群，缺乏在昇腾NPU上的端到端实践。本文以DeepSeek-V4家族为对象，探索在昇腾SuperPOD上的高效训练范式，并进一步将优化后的基础设施用于运筹优化（OR）领域模型构建。

**方法**：提出分层优化框架SLAI T-Rex，涵盖模型并行策略、计算-通信编排、底层算子优化，使系统MFU达34.22%，相对开源基线提升2.93倍。在此基础上，构建OR领域持续预训练（CPT）与监督微调（SFT）流程，收集领域资源并结合求解器验证的合成文档，形成覆盖4类任务、3种问题表示的10K高质量SFT样本，用DeepSeek-V4-Flash进行领域特化。

**结果**：特化模型在零样本Pass@1上平均达71.81%，优于GPT-5.4-Mini（+3.98pp）和基础模型（+11.27pp）。CPT为模型植入可迁移的OR建模先验，提升面向求解器的可行性和结构等价性，完成从Infra优化到领域特化的全栈验证。
