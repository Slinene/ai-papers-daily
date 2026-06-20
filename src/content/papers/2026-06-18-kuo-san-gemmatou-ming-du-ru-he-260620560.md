---
title: How Transparent is DiffusionGemma?
title_zh: 扩散Gemma透明度如何？
authors:
- Joshua Engels
- Callum McDougall
- Bilal Chughtai
- Janos Kramar
- Senthoran Rajamanoharan
- Cindy Wu
- Arthur Conmy
- Asic Q Chen
- Jean Tarbouriech
- Min Ma
affiliations:
- Google DeepMind
arxiv_id: '2606.20560'
url: https://arxiv.org/abs/2606.20560
pdf_url: https://arxiv.org/pdf/2606.20560
published: '2026-06-18'
collected: '2026-06-20'
category: Reasoning
direction: 扩散模型透明度分析
tags:
- Text Diffusion
- Interpretability
- Transparency
- Monitorability
- LLM
- DiffusionGemma
one_liner: 通过token瓶颈使扩散LLM透明度媲美自回归模型，并揭示扩散特有推理现象
practical_value: '- 扩散模型中插入可解释token瓶颈（token bottleneck）可在不牺牲性能的前提下，使中间隐状态映射为可读token序列，显著降低不透明串行深度，可迁移至扩散式生成推荐（如物品序列生成）中实现可解释的中间步骤。

  - 扩散模型输出概率监控性（monitorability）与自回归模型相当，因此下游任务（如异常检测、置信度过滤、主动学习）对扩散生成结果的可干预性不受影响，实践中可放心复用自回归模型的监控方法。

  - 扩散模型可能出现非时序推理（non-chronological reasoning）和token涂抹（smearing）等现象，依赖生成顺序的可解释性不可靠，设计基于扩散的对话Agent或规划系统时应谨慎对待中间推理踪迹，考虑其他验证机制。

  - 算法透明度方面的退化提示，扩散模型内部可能执行复杂分布式算法，需警惕在安全敏感场景中仅靠输出概率不足以理解模型行为，建议结合额外探测手段。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

LLM推理透明度对于理解模型决策、缓解误用、调试异常行为至关重要。然而，扩散模型DiffusionGemma在连续潜空间中执行大量计算，这是否降低了它的透明度？本文将透明度分解为变量透明度（能否理解模型中间状态）与算法透明度（能否从中间状态重构推理过程）。初步测量显示，DiffusionGemma的不透明串行深度（即相邻可解释状态间的串行计算量）达到自回归Gemma 4的28.6倍。但通过在去噪步骤间插入可解释token瓶颈（将信息流映射为离散token），可以在不降低下游性能的前提下，将不透明串行深度降至仅1.1倍。算法透明度方面，扩散模型更加棘手：所有token预测在每一步都可能变化，使模型有能力在去噪过程中实施复杂的分布式算法。通过一系列可解释性案例研究，发现了扩散特有的现象：非时序推理、token与序列涂抹、中间上下文推理等。最后，评估了监控性（即模型输出对下游任务的有用性），发现DiffusionGemma与Gemma 4的监控性相当。这些结果表明，尽管扩散模型引入新的可解释性挑战，但通过适当设计（如token瓶颈）可实现与自回归模型相当的变量透明度，且监控能力不受损，而算法透明度仍需进一步研究。
