---
title: 'PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like
  Benchmarks'
title_zh: PAIChecker：检测类SWE-Bench基准中PR与Issue错位的多智能体系统
authors:
- Manyi Wang
- Junjielong Xu
- Pinjia He
affiliations:
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2607.28587'
url: https://arxiv.org/abs/2607.28587
pdf_url: https://arxiv.org/pdf/2607.28587
published: '2026-07-30'
collected: '2026-08-02'
category: MultiAgent
direction: 多智能体系统用于基准数据质量检测
tags:
- Multi-Agent System
- Benchmark Misalignment
- PR-Issue Alignment
- SWE-bench
- LLM Evaluation
one_liner: 提出多智能体系统PAIChecker，三阶段渐进式验证PR-Issue错位，准确率达92%
practical_value: '- 多智能体协作的**三阶段验证模式**（模式识别→交叉智能体合成标签→代码级验证）可迁移到搜索推荐的数据质检流程，例如检查Query与商品描述的语义一致性、广告文案合规性等。

  - **交叉智能体标签合成**利用多个LLM实例投票/辩论增强判断鲁棒性，类似Ensemble方法，可用于需要高可靠性的标注纠错、内容审核或A/B指标归因。

  - 结合**静态代码分析**的最终验证阶段，启发我们在RAG生成答案后增加确定性规则校验（如商品属性冲突检测），提升可信度。

  - 论文对基准错位的系统模式分析，提醒从业者在构建内部评测集时需检查黄金标准的隐性偏差，避免“垃圾进垃圾出”影响模型迭代方向。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：SWE-bench通过GitHub issue与PR配对构建LLM解决问题基准，但实际仓库维护复杂，配对常存在错位，威胁评测有效性。对SWE-bench Verified的分析发现**13.6%实例存在错位**，涵盖5种模式11种细粒度场景。

**方法**：提出PAIChecker，一个**多智能体检测系统**。采用三阶段设计：(1) **特定模式识别**：多智能体并行分析PR与Issue文本，识别已知错位模式；(2) **交叉智能体标签合成**：集成多个智能体判断，通过投票/辩论合成更可靠标签；(3) **代码级验证**：基于PR diff与issue描述进行确定性代码分析，最终确认错位。该设计兼顾发现能力与精确度。

**结果**：在SWE-Gym和SWE-bench Multilingual上，PAIChecker在GPT-4o、Claude 3.5 Sonnet等4种LLM后端下均获最佳性能，**二分类准确率最高达92.12%和91.67%**，召回率与F1均显著优于基线，并展现出跨语言泛化能力。
