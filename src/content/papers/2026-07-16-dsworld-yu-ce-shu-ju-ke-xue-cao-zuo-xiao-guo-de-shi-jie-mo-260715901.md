---
title: 'DSWorld: A Data Science World Model for Efficient Autonomous Agents'
title_zh: DSWorld：预测数据科学操作效果的世界模型框架
authors:
- Zherui Yang
- Fan Liu
- Hao Liu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2607.15901'
url: https://arxiv.org/abs/2607.15901
pdf_url: https://arxiv.org/pdf/2607.15901
published: '2026-07-16'
collected: '2026-07-20'
category: Agent
direction: 数据科学世界模型 · 代理训练加速
tags:
- world model
- reinforcement learning
- autonomous agents
- data science
- transition prediction
- cost-aware routing
one_liner: 提出数据科学世界模型预测操作结果，实现代理训练加速14倍、推理加速3-6倍
practical_value: '- **可复用的世界模型思路**：在搜索推荐系统的自动化调参或特征工程代理中，借鉴“低代价操作真执行，高代价操作用LLM模拟”的策略，用历史日志训练一个轻量过渡预测模型，减少线上实验成本。

  - **结构化状态表示**：将工作流状态（数据Schema、模型性能、资源消耗等）组织成结构化文本输入LLM，而非原始代码或日志，能稳定提升预测准确率，可直接用于推荐agent的状态管理。

  - **成本感知路由**：设定成本阈值，简单操作（如数据抽样、缺失值填充）直接执行，复杂操作（如模型训练）用世界模型模拟，可构建分级探索的AutoML代理，降低计算开销。

  - **反思式世界模型优化**：利用真实执行后的错误反馈更新世界模型，可将自动化A/B测试的模拟器与线上结果对齐，逐步提升模拟保真度，减少策略上线前的风险评估偏差。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有数据科学自主代理依赖昂贵的试错执行，例如反复跑模型训练，计算开销巨大。受视觉世界模型启发，希望构建能预测数据科学操作效果的世界模型，在真实执行前预判状态变化，从而加速代理训练和推理。

**方法**：提出DSWorld框架，核心是将数据科学环境建模为状态转移预测器。关键点：① 结构化状态构造——将工作流状态（数据概要、代码、错误信息、资源指标等）组织为类JSON结构输入LLM，而非原始长文本；② 成本感知路由——设定计算成本阈值，对于低成本操作（如数据预览）采用真实执行，高成本操作（如模型训练）则调用LLM-based模拟器预测结果；③ 轻量真实执行与模拟器结合，降低整体开销；④ 构建8K规模的状态转移轨迹数据集，并提出Reflective World Model Optimization (RWO) 算法：根据真实执行误差修正世界模型，使用强化学习微调LLM，提升预测准确率。

**结果**：在数据科学代理的RL训练中，DSWorld实现约14倍加速，搜索式推理加速3-6倍，同时保持性能持平；在过渡预测任务上，比最强LLM基线提升35.6%。
