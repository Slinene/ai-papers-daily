---
title: 'Induction in Both Directions: A Mechanistic Analysis of In-Context Learning
  in Masked Diffusion Language Models'
title_zh: 掩码扩散语言模型的双向归纳电路与隐式时间步分析
authors:
- Andy Catruna
- Emilian Radoi
affiliations:
- National University of Science and Technology POLITEHNICA Bucharest
arxiv_id: '2607.15893'
url: https://arxiv.org/abs/2607.15893
pdf_url: https://arxiv.org/pdf/2607.15893
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: 扩散语言模型机制分析 · 上下文学习
tags:
- In-Context Learning
- Diffusion Language Models
- Induction Heads
- Mechanistic Interpretability
- Bidirectional Circuit
- Masked Diffusion
one_liner: 发现扩散语言模型用双向归纳电路实现上下文学习，且以全局掩码比例作隐式时间步
practical_value: '- 对于电商搜索中的序列建模，可借鉴双向上下文访问的思路：在允许未来信息的场景（如离线重排）下，利用扩散模型隐式地融合下文，提升对用户意图的推断准确性。

  - 隐式时间步的发现提示：在设计扩散式推荐或生成式检索时，可以省略显式时间步嵌入，让模型从噪声比例中自学习去噪进度，简化工程实现。

  - 归纳电路的分析方法（激活修补、因果追踪）可以迁移到推荐模型的解释性工作中，例如定位关键注意力头，帮助 debug 召回结果中的主观偏差。

  - 当仅左上下文可用时，DLM 的 induction 能力并不优于自回归模型，因此若线上真实场景只能获取左侧历史行为，盲目切换生成范式未必带来增益，需根据上下文可获取性选择架构。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：自回归 Transformer 的上下文学习机制已有较多研究，但扩散语言模型（DLM）的内部工作方式尚不清晰。本文聚焦于 induction（一种通过重复上下文复制后续 token 的上下文学习模式），探究掩码扩散模型如何实现该能力，并对比自回归模型。

方法：使用相同架构的仅注意力自回归模型和吸收掩码 DLM，通过激活修补（activation patching）和注意力模式分析等机理可解释性工具，定位参与 induction 的注意力头，并验证电路行为的因果性。

关键结果：DLM 学习到一套方向对称的双向归纳电路——「邻域头」将前一个/下一个 token 信息写入残差流，「归纳头」据此匹配掩码位置与源位置，并复制答案 token。当上下文仅左侧可见时，DLM 的 induction 性能并不优于 AR 模型；但当掩码两侧均可见时，DLM 显著更强，表明其优势源于双向上下文访问，而非更强的单向机制。此外，作者首次发现 DLM 在无显式时间步嵌入的条件下，利用全局掩码 token 的比例作为隐式时间步信号，为扩散生成过程提供进度信息。
