---
title: 'MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning
  of Lightweight Time Series Forecasters'
title_zh: 元harness优化多智能体实现轻量时序预测器小样本训练
authors:
- ChengAo Shen
- Wenchao Yu
- Fangyu Wu
- Dongjin Song
- Hanghang Tong
- Dongsheng Luo
- Wei Cheng
- Haifeng Chen
- Jingchao Ni
affiliations:
- University of Houston
- NEC Labs
- University of Waterloo
- University of Connecticut
- University of Illinois at Urbana-Champaign
arxiv_id: '2608.23473'
url: https://arxiv.org/abs/2608.23473
pdf_url: https://arxiv.org/pdf/2608.23473
published: '2026-08-24'
collected: '2026-08-25'
category: MultiAgent
direction: 多智能体元优化 · 时间序列预测
tags:
- MultiAgent
- Time Series Forecasting
- Few-shot Learning
- LLM
- Data Generation
- Meta-Learning
one_liner: 用多智能体生成数据+元优化harness，从少量样本训练轻量时间序列预测器
practical_value: '- 数据稀缺或隐私敏感场景（如新商品冷启动、低频事件预测），可借鉴多智能体数据生成：用 LLM agent 从少量真实样本+文本上下文合成训练数据，再训练轻量模型，避免直接依赖大模型在线推理。

  - 将 LLM 定位为“离线工程师”而非在线预测器：在电商推荐中，可让 LLM 离线生成商品描述增强、用户兴趣特征或合成样本，训练轻量排序/CTR模型，保证线上低延迟和低成本。

  - 多智能体分工（数据生成、过滤、评估）提升合成数据质量，该模式可迁移到推荐系统的数据增强 pipeline，通过多个 agent 协作筛选高质量样本。

  - meta-harness 优化思想：把数据生成流程（prompt/工具调用）视为可学习对象，用元学习在多个任务上优化，使生成数据能最大程度提升下游模型效果，可类比推荐中的自动特征工程或数据增强策略搜索。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：时间序列预测正走向多模态与 agent 化，但基础模型在资源受限场景不经济，轻量预测器又通常依赖大量训练数据，难以用于数据稀缺、积累缓慢或隐私敏感的领域。因此需要解决轻量预测器的小样本学习问题。

**方法关键点**：构建 MetaCaster，一个元 harness 优化的多智能体框架。它不把 LLM 作为直接预测器，而是让多个智能体充当“工程师”，通过 agentic data generation 从少量示例和文本上下文自动生成训练数据，进而训练专门、可部署的轻量预测器。核心是 meta-harness 优化：对智能体的数据生成流程进行元级优化，确保生成的数据能够有效提升下游轻量预测器的性能。

**关键结果**：在 18 个数据集、23 种 SOTA 轻量预测器和 14 个基线方法上验证，MetaCaster 同时取得数据效率与计算效率，并保持高质量的时间序列预测性能。
