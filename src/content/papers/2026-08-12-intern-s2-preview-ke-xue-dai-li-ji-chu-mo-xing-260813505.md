---
title: 'Intern-S2-Preview: Scientific Agentic Foundation Model'
title_zh: Intern-S2-Preview：科学代理基础模型
authors:
- Lei Bai
- Jiaqi Cao
- Chiyu Chen
- Guanzhou Chen
- Kai Chen
- Guangran Cheng
- Erfei Cui
- Xuanlang Dai
- Shengyuan Ding
- Shangheng Du
affiliations:
- Shanghai AI Laboratory
arxiv_id: '2608.13505'
url: https://arxiv.org/abs/2608.13505
pdf_url: https://arxiv.org/pdf/2608.13505
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: 科学代理基础模型 · RL与多模态训练
tags:
- Scientific Agent
- RL
- Multimodal
- Time Series
- Memory Decoder
- Foundation Model
one_liner: 构建科学多模态代理基础模型，融合强化学习训练与时间序列预测，支持长程科学任务
practical_value: '- **RL训练效率技巧可迁移至Agent策略优化**：partial rollout with off-policy correction
  和 adaptive length regularization 能降低长轨迹任务的训练成本，适合对话式推荐、搜索交互等场景的在线策略学习。

  - **online speculative decoding** 可加速线上Agent服务推理，降低延迟，在推荐解释生成、实时对话等场景有直接工程价值。

  - **Memory Decoder（4B）作为冻结大模型上的轻量适配层**，能快速注入垂直领域知识（如电商商品知识、广告文案规范），无需微调397B主干，规避大模型频繁更新风险，适合业务侧低成本定制。

  - **时间序列预测模块**扩展长序列理解到数值预测，可借鉴用于电商流量/销量预测、广告预算分配等业务时序任务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：科学发现需要AI系统能理解异构多模态证据、与科学工具交互、并维持长任务流程，现有通用模型难以覆盖这类复杂需求。

**方法关键点**：
- 从科学多模态预训练开始，数据包括渲染科学文档、图文交错数据与科学语料。
- 统一后训练流水线：监督微调（SFT）、可扩展多任务强化学习（RL）、黑盒/白盒代理强化学习（agentic RL）、以及在线蒸馏（on-policy distillation）。
- 引入多项工程优化：partial rollout with off-policy correction（部分展开+离策略校正）、自适应长度正则（adaptive length regularization）、在线投机解码（online speculative decoding）、鲁棒多任务优化、trace-aware experience assembly（轨迹感知经验组装）。
- 架构上，397B主干扩展时间序列建模能力（从长序列理解到数值预测），同时研究独立的Memory Decoder（4B）作为记忆增强路径，可在不修改冻结397B主干的情况下快速进行科学领域专业化。

**关键结果**：
- 在科学、多模态、代理、通用基准上取得竞争性或领先成绩。
- 时间序列模块提升SciTS科学信号理解与预测表现。
- 独立Intern-MemDec-4B扩展将Biology-Instructions平均分从56.92提升至60.32，且无需微调397B主干。
