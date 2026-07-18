---
title: 'Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models'
title_zh: 划分、提示、聚合：语言模型的统计自洽性
authors:
- Patrik Wolf
- Thomas Kleine Buening
- Andreas Krause
- Celestine Mendler-Dünner
affiliations:
- Max Planck Institute for Intelligent Systems, Tübingen, Germany
- ETH Zürich
- ELLIS Institute, Tübingen
- Tübingen AI Center
arxiv_id: '2607.15277'
url: https://arxiv.org/abs/2607.15277
pdf_url: https://arxiv.org/pdf/2607.15277
published: '2026-07-15'
collected: '2026-07-18'
category: Eval
direction: LLM概率校准与统计自洽性评估
tags:
- Statistical Self-Consistency
- LLM Evaluation
- In-Context Learning
- Probabilistic Inference
- Macro Fallacy
one_liner: 揭示LLM在上下文条件推断中普遍违反全概率公式，提出无参考的统计自洽性评估准则
practical_value: '- 在电商/广告人群预测中，用LLM直接估计总体指标（如点击率、购买概率）可能不准，可改用树形属性划分（年龄、性别、消费层级），分别询问细粒度子群体概率，再按真实分布加权聚合，往往比总体提示更贴近真实数据。

  - 构建推荐Agent的推理模块时，可加入自洽性检查：对同一用户群按不同维度划分（如兴趣标签、行为序列），要求LLM给出条件概率，然后验算聚合后是否满足全概率公式；不一致的地方可作为潜在偏差或知识盲区定位。

  - 论文提出的无参考评估方法（Partition-Prompt-Aggregate）可直接用于检测推荐解释或用户画像生成中的群体偏见，无需人工标注，只需设计合理的树状划分schema即可量化LLM的统计自洽性。

  - 实验发现的“宏观谬误”提示：使用LLM做粗粒度决策（如全局策略生成）时，可先查询细粒度子场景估计再汇总，可能提升决策质量，例如在广告预算分配中先按渠道、人群细分询问效果再聚合。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：将上下文学习解释为条件推断时，LLM的输出应满足基本的概率恒等式，尤其是全概率公式——任意有效划分下，条件概率在先验加权后应还原总体边际分布。然而实际模型是否满足这种统计自洽性尚不明确。

**方法**：论文构建了一个划分-提示-聚合（Partition, Prompt, Aggregate）评估框架。用二叉决策树将总体递归分割为越来越细的子群体，用自然语言描述子群体并提示LLM估计目标条件概率，再将所有子群估计按先验权重聚合回总体估计，比较不同粒度划分下的聚合结果以及与直接总体估计的一致性。同时在多种任务（选举预测、职业收入估计等）和前沿模型（GPT-4、Claude等）上实验，并深入分析角色提示（persona prompting）下的宏观谬误。

**关键结果**：
1. 所有测试模型普遍违反自洽性：不同划分粒度得到的聚合估计显著不一致，且与直接总体估计差异大。
2. 发现“宏观谬误”：从更细粒度子群响应重建的聚合估计，往往比直接总体估计更接近人类参考数据，说明模型存储了相关的子群体知识，但未能可靠地向上聚合。
3. 通过隐式提示（implicit prompting）可部分恢复自洽性，但无法根本消除偏差。
4. 统计自洽性被确立为一种无需参考答案的评估LLM的准则，可反映模型知识的一致性和可靠性。
