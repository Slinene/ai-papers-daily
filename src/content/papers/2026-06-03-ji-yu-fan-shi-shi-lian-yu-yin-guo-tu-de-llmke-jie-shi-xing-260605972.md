---
title: LLM Explainability with Counterfactual Chains and Causal Graphs
title_zh: 基于反事实链与因果图的LLM可解释性方法
authors:
- Nirit Nussbaum-Hoffer
- Nitay Calderon
- Liat Ein-Dor
- Roi Reichart
affiliations:
- Technion
- IBM Research
arxiv_id: '2606.05972'
url: https://arxiv.org/abs/2606.05972
pdf_url: https://arxiv.org/pdf/2606.05972
published: '2026-06-03'
collected: '2026-06-09'
category: LLM
direction: LLM可解释性因果图构建
tags:
- LLM Explainability
- Causal Graphs
- Counterfactual Augmentation
- Concept-based Explanations
- MCMC
one_liner: 通过MCMC反事实增强从LLM预测中挖掘概念级因果图，实现透明推理
practical_value: '- 可直接用于电商评论情感分析等文本分类任务，抽取LLM决策所依赖的概念及其因果结构，辅助调试模型偏见（如发现“发货速度”是否被错误关联到负面情感）。

  - 反事实链增强方法能在标注数据稀疏时生成高信息量反事实样本，提升因果发现稳定性，适用于LLM-as-a-judge等需审计决策逻辑的场景。

  - 所构建的因果图可作为LLM代理的透明化中间层，帮助多智能体系统理解各Agent推理链路，优化协作协议。

  - 整体框架与模型无关，可快速迁移到产品分类、内容审核等业务中，为模型审计与合规提供概念级解释。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM推理过程不透明，其自由生成解释常不忠实，阻碍高风险决策采纳。现有因果图方法用于建模外部世界，本文转向建模LLM内部推理，为利益相关者提供概念级透明视图。

**方法**：提出四阶段框架。(1) **概念发现与映射**：给定LLM和文本分类示例，利用LLM自身发现区分类别的人类可解释概念，并将每个输入映射为LLM感知的概念状态（是否出现），形成稀疏观测数据。(2) **MCMC反事实增强**：针对观测样本稀少导致因果发现困难，引入一种受MCMC启发的链式反事实生成过程，通过从现有样本出发迭代替换概念状态并查询LLM逻辑一致性，扩展出大量高保真反事实数据。(3) **因果发现**：在增强数据集上运行σ-CG算法，学习概念间的稳定因果图。(4) **评估**：度量图对LLM预测的保真度及结构稳定性。

**实验**：在疾病诊断、情感分析、LLM-as-a-judge等3类任务、3个LLM（Llama-2、Mixtral等）上验证。结果表明，所学因果图能稳定捕获与LLM推理一致的有意义依赖；MCMC增强显著提升因果发现的收敛性和图结构的可解释性；图具有高预测保真度。方法为LLM概念级可解释性提供了基础。
