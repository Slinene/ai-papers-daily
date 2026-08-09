---
title: A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications
  in AI Governance
title_zh: 训练后适应技术的六维分类法及其AI治理应用
authors:
- Fardin Afdideh
- Fernando Seoane
- Farhad Abtahi
affiliations:
- Karolinska Institutet
- Karolinska University Hospital
- University of Borås
- KTH Royal Institute of Technology
arxiv_id: '2608.06246'
url: https://arxiv.org/abs/2608.06246
pdf_url: https://arxiv.org/pdf/2608.06246
published: '2026-08-06'
collected: '2026-08-09'
category: Training
direction: 训练后适应技术分类与治理
tags:
- Post-Training Adaptation
- Taxonomy
- Fine-tuning
- RAG
- Model Governance
one_liner: 提出统一六维分类法，区分微调、RAG等训练后适应技术，支持模型变更治理
practical_value: '- 模型迭代治理：可借鉴其六维分类（机制、目标、数据需求、持久性、结构范围、模型类型）建立模型变更日志，便于在推荐系统频繁微调、RAG更新等场景下合规审计。

  - 适应技术选择：通过持久性维度区分一次性微调与持续推理时适应（如RAG、动态提示），指导电商搜索/推荐系统在候选生成、重排序阶段的工程架构选型。

  - 技术栈梳理：论文梳理的继承、取代、混合等关系可帮助团队理清模型更新技术栈，避免重复或冲突。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：训练后适应技术（微调、RAG、模型编辑、遗忘等）碎片化严重，缺乏统一描述框架，难以比较方法或追踪模型变更。
**方法**：提出一个六维分类法，维度包括机制（如参数更新、检索增强、提示）、目标（性能提升、对齐、遗忘）、数据需求、持久性（一次性 vs. 持续）、结构范围（层/模块级）和模型类型（传统ML到多模态LLM）。分类法清晰区分了微调、RAG、提示等易混淆概念，并绘制了技术间的继承、替代、混合和分层堆叠关系。
**结果**：提供了一套统一词汇，可直接用于技术文档、模型变更追踪和AI治理分析。论文指出当前评估、可复现性、持续推理时适应、遗忘、多模态适应等开放挑战。
