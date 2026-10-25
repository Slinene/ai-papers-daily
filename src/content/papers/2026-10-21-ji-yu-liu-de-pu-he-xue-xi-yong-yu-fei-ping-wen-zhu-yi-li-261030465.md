---
title: Flow-based Spectral Kernel Learning for Nonstationary Attention
title_zh: 基于流的谱核学习用于非平稳注意力
authors:
- Zi Yang
- Ying Li
- Alejandro Lancho
- Darío C. Larese
- Pablo M. Olmos
- Michael Minyi Zhang
affiliations:
- The University of Hong Kong
- National University of Singapore
- Universidad Carlos III de Madrid
arxiv_id: '2610.30465'
url: https://arxiv.org/abs/2610.30465
pdf_url: https://arxiv.org/pdf/2610.30465
published: '2026-10-21'
collected: '2026-10-25'
category: LLM
direction: 注意力核学习 · 线性注意力
tags:
- Kernelized Attention
- Normalizing Flows
- Linear Attention
- Nonstationary Kernel
- Parameter Efficient
- Transformer
one_liner: FSKA 用归一化流学习非平稳注意力核，移除 QK 投影并固定正交 V 投影，减少参数 40-47% 且保持线性注意力
practical_value: '- 在电商用户行为序列 Transformer 中可替换标准 softmax 注意力为 FSKA：线性注意力内存扩展适合处理长点击/购买序列，避免截断，尤其适合用户长期兴趣建模。

  - 投影参数减少 40-47% 的思路可直接用于压缩 CTR/CVR 或 Agent 策略网络的 Transformer 层：移除 query/key 投影、使用固定正交
  value 投影，能降低参数量和过拟合风险，适合中小规模业务数据。

  - 可学习的非平稳核比固定 softmax/RBF 更灵活，可适应行为序列中时间间隔、事件类型等异构 token 交互；其谱密度正则化方式可迁移到其他基于内积的匹配或聚合层。

  - 注意论文聚焦通用序列建模，在推荐/广告数据上的效果需自行验证；更偏组件级参考而非端到端推荐算法。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**  
现有核化注意力多依赖固定或平稳核，难以适应复杂 token 交互；标准 softmax 注意力参数多、序列长度受限。需要一种可学习、可扩展且参数高效的注意力核。

**方法关键点**  
提出 FSKA（flow-based spectral kernel attention）：从谱密度学习角度构建核化注意力，用归一化流参数化二元谱密度，学习非平稳核；该设计兼容线性注意力计算，保持内存随序列长度线性扩展。进一步发现强表达力的核学习可以简化注意力结构：移除 query-key 投影，使用固定正交 value 投影，从而大幅减少可训练参数。

**关键结果**  
在分类、消融和扩展性分析中，FSKA 性能与现有注意力机制有竞争力或更优；投影相关可训练参数减少约 40%–47%，同时保持线性注意力内存扩展。
