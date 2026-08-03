---
title: 'The Parts Are Greater Than the Sum: Automated Task Sequencing for Efficient
  Training of Multi-Policy LLMs'
title_zh: 自动任务排序实现多策略 LLM 高效训练
authors:
- Jiajia Tang
- Sizhe Yuen
- Francisco Gomez Medina
- Yali Du
- Adam Sobey
affiliations:
- The Alan Turing Institute
- University of Southampton
- King’s College London
arxiv_id: '2607.29601'
url: https://arxiv.org/abs/2607.29601
pdf_url: https://arxiv.org/pdf/2607.29601
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: 参数高效微调 · 任务分组与排序
tags:
- PEFT
- LoRA
- Task Sequencing
- Multi-Policy
- Catastrophic Forgetting
- QLoRA
one_liner: 提出自动化任务分组与排序框架，用独立 QLoRA 解耦优化路径，在固定参数预算下提升异构任务微调性能
practical_value: '- **多任务微调的任务组织**：面对电商搜索、推荐等异构任务（如语义相关性、点击率预估、不良内容检测），可借鉴任务分组与排序策略，将相容任务归入同一适配路径，减少梯度干扰和灾难性遗忘。

  - **多 LoRA 替代单一大适配器**：使用多个小型 QLoRA 替代一个共享适配器，每个策略只服务一组相容任务，既控制总参数量又提升表达能力，适合需同时维护多个小模型的业务场景（如多国、多站点推荐）。

  - **自动化任务路径组织**：在固定参数预算下，通过自动分组和排序决定适配器分配，避免人工经验试错，该流程可直接迁移到 Agent 工具调用或意图识别等多能力微调中。

  - **工程实现简洁**：每个任务组对应一个 QLoRA 模块，推理时按路由加载，与 LoRA 生态兼容，便于在已有 PEFT 框架上扩展，适合快速实验和部署。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有 PEFT 方法用单一共享 LoRA 适配所有下游任务，当任务序列异构时，共享优化空间会产生梯度干扰，导致正向迁移差、灾难性遗忘。增加适配器容量或组合多个适配器仍依赖同一优化路径，未根本解决冲突。

**方法**：提出优化路径组织框架，将任务自动分组并排序，为每组相容任务分配独立的 QLoRA 适配策略，形成“多策略 PEFT”。具体包括：① 构建任务间迁移性矩阵；② 基于谱聚类自动分组，最大化组内相容性；③ 对组内任务按迁移增益动态排序，保证正向迁移；④ 每个组使用独立 QLoRA 训练，总参数量固定。

**结果**：在 TRACE 多任务基准上，从单策略 PEFT 到多策略 PEFT 性能持续提升，所提自动多策略框架在相同可训参数量下取得 44.78 最佳平均分。分析表明，解耦优化路径比单纯扩大适配器容量更有效，且任务分组与排序策略对最终性能贡献显著。
