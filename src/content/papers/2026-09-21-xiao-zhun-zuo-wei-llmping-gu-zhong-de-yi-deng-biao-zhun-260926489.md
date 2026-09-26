---
title: Calibration as a First-Class Criterion in LLM Evaluation
title_zh: 校准作为LLM评估中的一等标准
authors:
- Mario Sanz-Guerrero
- Katharina von der Wense
affiliations:
- Johannes Gutenberg University Mainz
- University of Colorado Boulder
arxiv_id: '2609.26489'
url: https://arxiv.org/abs/2609.26489
pdf_url: https://arxiv.org/pdf/2609.26489
published: '2026-09-21'
collected: '2026-09-26'
category: Eval
direction: LLM评估 · 置信度校准
tags:
- calibration
- LLM evaluation
- confidence estimation
- trustworthy AI
- LLM-as-a-judge
one_liner: 主张将置信度校准纳入LLM评估核心，指出当前未采用导致部署与研究风险
practical_value: '- 在业务中使用LLM做自动评估（LLM-as-a-judge）、合成数据生成或主动学习时，先验证模型置信度校准，否则会放大错误。例如生成搜索query或推荐文案时，模型给出的置信度可能过度自信，需要校准后再用于下游决策。

  - 在离线评估benchmark中，除AUC、NDCG、准确率等性能指标外，同时报告校准分数（如ECE），成本极低，因为已有置信度和正确标签可直接计算。

  - 对于开放式生成场景（如生成商品文案、推荐query），定义置信度和正确性困难，可探索一致性采样、自评估等方式获取近似置信度，并定期校准。

  - 部署Agent自动决策时，对LLM输出置信度做校准或后处理，避免过度自信导致的错误动作，尤其在无人监督的自动化流程中。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM从研究原型变为广泛部署工具，置信度成为用户和自动代理判断正确性的唯一信号，但主流评估忽视校准，导致过度自信错误在部署中造成实际伤害，并在研究管道中影响LLM-as-a-judge、合成数据生成、主动学习等依赖置信度的方法。

**方法关键点**：标准校准指标（如ECE）只需置信度分数与正确性判断两个输入，多数现有基准已提供两者，因此可零成本报告校准分数；开放式生成中定义置信度和正确性仍是开放挑战。

**结果**：本文为立场论文，无实验数据；核心呼吁是每个NLP子领域将性能指标与校准分数配对，把校准作为模型基本属性。
