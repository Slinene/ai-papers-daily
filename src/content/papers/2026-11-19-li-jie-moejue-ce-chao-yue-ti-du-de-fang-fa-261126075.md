---
title: Understanding MoE Decisions Beyond Gradients
title_zh: 理解MoE决策：超越梯度的方法
authors:
- Zhen Xu
- Zitao Zhang
- Kevin Zhao
- Xuefeng Liu
affiliations:
- University of Chicago
- eBay
- University of Florida
arxiv_id: '2611.26075'
url: https://arxiv.org/abs/2611.26075
pdf_url: https://arxiv.org/pdf/2611.26075
published: '2026-11-19'
collected: '2026-11-21'
category: LLM
direction: LLM可解释性 · MoE干预效应
tags:
- MoE
- interpretability
- gradient-based attribution
- intervention
- LLM
one_liner: 提出结合专家输出与选择规则的预测器，显著降低MoE模型干预效应预测误差
practical_value: '- 对于使用MoE架构的LLM（如Qwen、Mixtral等）作为推荐/搜索排序或生成模块的团队，该预测器提供了一种无需重复前向传播的高效归因方法，可快速定位哪些专家对特定输出（如推荐理由生成）贡献最大。

  - 干预效应预测器利用专家输出和路由规则，避免了昂贵的高阶梯度计算，适合在线调试或A/B测试前评估模型组件替换的影响，降低实验成本。

  - 方法强调离散路由切换对输出的非线性影响，提示在分析动态路由推荐模型（如专家混合的召回或排序模型）时，不能仅依赖梯度，需结合路由决策本身进行归因。

  - 该思路可迁移至任何具有动态选择机制的模型（如多任务学习中的门控网络），用于更准确地预测结构修改对最终指标的影响。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：梯度归因方法在MoE语言模型中预测干预效应时存在系统性误差：替换某一专家会改变后续层的专家选择，这种离散切换造成答案分数跳变，局部导数无法捕捉。

**方法关键点**：提出一个新预测器，直接利用模型自身的专家输出和路由选择规则来估计因路由切换产生的额外效应，并将其叠加到二阶梯度预测上。该方法无需额外梯度计算，仅需前向传播中已有的专家输出和路由logits即可完成修正。

**结果**：在三个基准的问答任务上，相比使用梯度和二阶导数的多步基线，新方法在Qwen3.6上将答案分数变化预测误差降低60%，在Gemma4上降低47%，验证了显式建模路由切换对准确归因的必要性。
