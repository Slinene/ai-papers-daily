---
title: 'NetCause: Counterfactual Learning for Root Cause Analysis in Large-Scale Networks'
title_zh: 基于反事实学习的大规模网络根因分析框架
authors:
- Fabien Chraim
- Jian Zhang
- Dominik Janzing
- Xiang Song
- Christos Faloutsos
- John Evans
affiliations:
- Amazon Web Services
arxiv_id: '2606.13543'
url: https://arxiv.org/abs/2606.13543
pdf_url: https://arxiv.org/pdf/2606.13543
published: '2026-06-11'
collected: '2026-06-14'
category: Other
direction: 网络运维 · 反事实因果推断
tags:
- root cause analysis
- counterfactual learning
- graph neural networks
- self-supervised learning
- network management
one_liner: 将网络事件建模为图时序过程，通过反事实仿真自监督学习因果排序，根因准确率提升16.1%
practical_value: '- 推荐系统故障根因定位：可将物料/链路故障传播建模为图网络，用反事实仿真排序根因，替代人工规则排查。

  - Agent 联合诊断：多智能体协作场景下，借鉴图时序模型捕捉跨服务依赖，定位宕机或延迟瓶颈。

  - 因果推断工程化：使用自监督预训练 + 小样本专家标注微调，适合线上系统冷启动与成本控制。

  - 轻量级推理：训练耗时但线上推断仅需秒级 GPU，可在推荐召回链路实时嵌入根因分析模块。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：云网络故障传播跨物理与逻辑拓扑，传统根因分析依赖静态规则或相关性启发式，难以在动态环境中区分因果与偶发共现。

**方法**：NetCause 将网络事件建模为图时序过程，利用自监督学习捕捉故障传播模式，再通过反事实仿真生成根因假设的因果效应，输出可解释的根因排序。训练时从生产网络数月事件中抽取超1500个事件自监督，评估时用31个专家标注事例，与规则基线对比。

**结果**：在运维决策最相关的排序头部，准确率较启发式基线提升16.1%，且推理仅需秒级GPU计算，满足实时诊断需求。
