---
title: A Hybrid Nested Harness for Decoupling Structure and Parameters in LLM-Driven
  Optimization
title_zh: LLM驱动的混合嵌套搜索：解耦结构与参数优化
authors:
- Víctor Gallego
affiliations:
- Komorebi AI Technologies
arxiv_id: '2608.08156'
url: https://arxiv.org/abs/2608.08156
pdf_url: https://arxiv.org/pdf/2608.08156
published: '2026-08-07'
collected: '2026-08-12'
category: LLM
direction: LLM驱动的结构-参数解耦优化
tags:
- LLM
- Hybrid Optimization
- CMA-ES
- Genetic Algorithm
- Structure–Parameter Decoupling
one_liner: 提出外层LLM生成结构草图、内层数值优化器调参的混合框架，在科学任务中大幅超越纯LLM搜索
practical_value: '- 在推荐系统的策略自动化设计中，可以用LLM生成召回/排序的规则结构（如if-else逻辑、模型组合方式），再用CMA-ES或贝叶斯优化微调其中的阈值、权重等参数，避免token浪费并提升性能

  - 对于Agent的行为策略优化，可让LLM提出高层次控制流草图，内层用数值优化器（如MCMC）搜索最优参数，减少试错成本

  - 在自动超参搜索场景，将LLM生成的训练脚本作为结构模板，内部超参（如学习率、dropout）交给梯度优化器，可结合LLM的先验知识与数值优化的高效性

  - 框架支持内外层柔性替换，业务中可根据实际算力与需求选择不同的LLM和优化器（例如用闭源LLM生成结构，开源轻量模型微调参数），具有很强的工程落地灵活性'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有的LLM驱动的演化算法让同一个语言模型同时优化程序的结构（如控制流、函数定义）和连续参数（如阈值、学习率）。LLM擅长结构探索，但处理数值参数时效率极低，在试错循环中浪费大量token和计算。

**方法**：论文提出混合嵌套搜索框架，将优化过程解耦为两层：外层LLM生成包含“数值空位”的代码结构草图，内层插入一个免梯度的数值优化器（如CMA-ES）或基于梯度的优化器，精准调整这些空位处的参数。外层和内层均可插拔，支持任意文本生成模型与零阶优化器、MCMC采样器等的组合。每次迭代，LLM基于评估反馈改进结构，参数优化器则负责在该结构下找到最佳参数配置。

**结果**：在三个科学领域（元优化器测试函数、代码策略设计、近似贝叶斯推断）中，混合优化器一致且显著地优于纯LLM搜索和纯数值优化基线，证明了结构-参数解耦的有效性。
