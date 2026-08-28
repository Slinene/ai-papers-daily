---
title: Boosting LLM Exploration via Weak-Model Guidance in RLVR
title_zh: 弱模型引导提升 RLVR 中 LLM 探索
authors:
- Xingyu Shen
- Huishuai Zhang
- Peng Li
- Yinchun Wang
- Dongyan Zhao
affiliations:
- Wangxuan Institute of Computer Technology, Peking University
- National Engineering Research Center of New Electronic Publishing Technologies
arxiv_id: '2608.27420'
url: https://arxiv.org/abs/2608.27420
pdf_url: https://arxiv.org/pdf/2608.27420
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: LLM 强化学习 · 探索增强
tags:
- RLVR
- entropy collapse
- exploration
- LLM reasoning
- pass@k
- weak model guidance
one_liner: 用弱模型生成部分推理前缀，强制主模型续写陌生路径，缓解 RLVR 熵坍塌并提升 pass@k
practical_value: '- 在搜索/推荐场景用 RLVR 微调 LLM（如 query 改写、商品文案生成、可验证奖励排序决策）时，可引入弱模型前缀：用轻量模型生成部分推理或候选文本，由主模型续写，以提升生成多样性，适合需要多个候选解的生成式推荐与
  Agent 决策。

  - 对 pass@k 有要求的生成管道（多路 query 建议、多候选推荐解释），熵保持比单条平均奖励更重要；该方法无需额外 SFT 或复杂奖励设计，可直接复用现有粗排/轻量模型，工程成本低，作为训练阶段的即插即用探索增强。

  - 多模型协同（粗排-精排、teacher-student、Agent 层级）可借鉴跨模型扰动思路：刻意用弱模型产生分布不一致的前缀，让强模型适应陌生输入，提高策略鲁棒性；需注意差异过大可能引入噪声，应调节前缀长度或来源模型。

  - 若 RLVR 奖励可验证（点击、转化等），可设计外部前缀机制，避免主策略在高奖励模板上过拟合，扩大覆盖的推理路径。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RLVR 能显著提升 LLM 推理能力，但训练中策略熵往往快速下降，导致推理路径覆盖变窄，大 k 下的 pass@k 反而退化。现有缓解熵崩溃的工作多聚焦算法正则化，跨模型非参数扰动被忽视。

**方法关键点**：不再只依赖目标模型自身内部探索，而是强制其基于一个较小、较弱语言模型生成的部分推理轨迹（“外部前缀”）进行续写。这些前缀与目标模型分布存在差异，能打破其对熟悉路径的过度自信，鼓励探索不同的推理分支。此外，经验性地分析了前缀分布差异对 RLVR 探索动态的影响机制。整个过程无需额外 SFT、复杂奖励设计或复杂提示。

**关键结果**：在多个数学基准上，该方法一致优于 vanilla RLVR；随着 k 增大，性能增益愈发明显，表明推理覆盖得到显著扩展，同时有效缓解了熵坍塌。
