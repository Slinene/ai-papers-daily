---
title: Measuring the Gap Between Human and LLM Research Ideas
title_zh: 衡量人类与LLM研究想法之间的差距
authors:
- Ziyu Chen
- Yilun Zhao
- Arman Cohan
affiliations:
- Yale University
- University of Chicago
arxiv_id: '2607.01233'
url: https://arxiv.org/abs/2607.01233
pdf_url: https://arxiv.org/pdf/2607.01233
published: '2026-06-30'
collected: '2026-07-07'
category: Eval
direction: LLM生成式评估与品味分布偏差
tags:
- LLM ideation
- research taste
- distribution gap
- evaluation
- taxonomy
one_liner: 通过研究品味分类法，量化LLM生成的研究想法在分布上与人类存在系统性偏差
practical_value: '- 可借鉴其双轴分类法，对推荐系统生成的广告文案、搜索建议或解释性文本进行「机会模式×贡献范式」的分布评估，检验是否过度集中于某些低多样性模式

  - 在评估LLM推荐的创意（如推送文案、商品卖点生成）时，可仿照其逆向工程人类偏好分布的方法，构建参照集并度量生成结果与人工创意的品味偏移

  - 论文的提示工程思路（从相关论文中提取背景、要求生成新想法）可迁移至多路召回策略的生成：给定用户历史行为序列作为“先前工作”，让LLM生成下一个兴趣点，作为候选召回

  - 研究本身主要面向学术创意评估，与电商推荐直接关联较弱，但其中“分布差距”的概念可泛化为推荐结果多样性或探索性的衡量指标'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM越来越多用于研究想法生成，但现有评测仅针对单点的新颖性、可行性或专家偏好，缺乏对人类与LLM整体品味差异的刻画。本研究旨在量化二者在「研究品味」分布上的差距。  
**方法**：从高质量人类论文出发，每篇论文逆向工程出一小组密切相关的先前工作作为背景知识，然后让LLM基于这些工作的标题与摘要生成新想法。引入双轴分类法：从「机会模式」（如何识别研究空白）和「研究范式」（如何构建贡献）两个维度标注每个想法。通过对比人类论文的真实引用分布与LLM生成想法的分布，量化研究品味差距。  
**关键结果**：在多个LLM上均观察到一致的分布偏差——LLM想法过度集中于「桥接式机会」和「综合方法」，而人类引用分布更广泛，涵盖更多样的空白构建与贡献类型。强LLM虽能产出合理想法，但范围系统性地窄于且偏离人类研究品味。
