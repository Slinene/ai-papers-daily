---
title: Efficient Reasoning Training Does Not Always Harm CoT Faithfulness and Monitorability
title_zh: 高效推理训练不总损害 CoT 忠实度与可监控性
authors:
- Samuel Lewis-Lim
- Xingwei Tan
- Mario Sanger
- Zhixue Zhao
- Nikolaos Aletras
affiliations:
- School of Computer Science, University of Sheffield
- AstraZeneca
arxiv_id: '2610.03509'
url: https://arxiv.org/abs/2610.03509
pdf_url: https://arxiv.org/pdf/2610.03509
published: '2026-10-02'
collected: '2026-10-05'
category: Reasoning
direction: 推理训练 · CoT 忠实度与监控性
tags:
- CoT faithfulness
- monitorability
- efficient reasoning
- length pressure
- LLM fine-tuning
- reasoning
one_liner: 系统评估三种长度压力训练方法，发现压缩 CoT 会降低忠实度但监控性较鲁棒
practical_value: '- 在电商/搜索推荐 Agent 中，若为降低推理成本对 CoT 做长度压缩（如固定 token 预算或长度奖励），不要只看任务准确率；需补充评估
  CoT 忠实度与模型一致性，否则可能引入“解释不可信”风险，影响事后归因和策略审计。

  - 若 CoT 主要用于监控（例如检测输入扰动、prompt 注入或特征变化是否改变推荐结果），短 CoT 仍能保留较好的可监控性，可以继续将压缩后的 CoT
  作为低成本的线上异常信号，而不必强依赖长推理。

  - 方法借鉴：长度压力机制选择上，倾向使用组相对长度奖励而非全局固定预算，并在训练后同时报告忠实度和一致性指标；对于需要向用户展示推理过程或解释推荐理由的场景，应谨慎压缩，或对关键路径保留更长
  CoT。

  - 可在业务中用干预实验评估可监控性：改变用户历史、商品属性或上下文特征，观察压缩后的 CoT 是否仍能暴露输出变化，用于决定哪些链路可以启用短推理。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：CoT 推理能提供可检查的解释，但推理成本高。高效训练通过压缩 token 数来降低成本，却可能让模型跳过关键步骤，使 CoT 不再忠实反映决策。由于不同效率方法施加长度压力的方式不同，忠实度受任务影响也不同，现有研究缺乏系统理解。

**方法关键点**：对多种模型进行微调，采用三种不同的长度压力方法：固定生成预算（fixed generation budget）、逐样本长度目标（per-example length target）、组相对长度奖励（group-relative length reward）。评估两个维度：CoT 忠实度（CoT 是否反映模型在相关输入上的决策）和可监控性（当输入干预改变输出时，CoT 是否能暴露这一变化）。

**关键结果**：高效推理训练对忠实度和可监控性的影响不同。忠实度在大多数设置下下降，主要原因是训练后模型的一致性降低；而可监控性更为鲁棒，即使 CoT 大幅缩短，模型仍能体现输入干预对答案的影响。
