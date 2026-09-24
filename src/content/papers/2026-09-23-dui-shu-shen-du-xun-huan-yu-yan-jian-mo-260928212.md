---
title: Log-Depth Recurrent Language Modeling
title_zh: 对数深度循环语言建模
authors:
- Yiqin Wang
- Nuri Cingillioglu
- Charles Pert
affiliations:
- Imperial College London
arxiv_id: '2609.28212'
url: https://arxiv.org/abs/2609.28212
pdf_url: https://arxiv.org/pdf/2609.28212
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: 对数深度循环架构替代 Transformer
tags:
- log-depth
- recurrent
- language-modeling
- length-extrapolation
- autoregressive
- balanced-tree
one_liner: 扩展平衡树递归算子至自回归预测，实现对数深度与线性复杂度的语言建模，长度外推稳健
practical_value: '- 用户长期行为序列建模可借鉴：电商/广告场景中用户历史长度大，Transformer 二次注意力成本高；对数深度递归算子提供线性复杂度且并行训练，适合作为长序列编码器候选。

  - 所有前缀表示可高效计算：推荐系统常用用户历史前缀做序列预测，该方法避免逐位置重复计算，适合 next-item/next-query 训练效率优化。

  - 长度外推稳健：线上序列长度波动大，位置编码失效常见；可考虑引入树结构或对数深度归纳偏置，缓解长度外推问题。

  - 该工作目前性能仅接近 ALiBi Transformer，仍属初步研究，落地需在业务序列模型上验证收益，不宜直接替换。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：Transformer 虽可并行训练，但计算深度固定、注意力复杂度随序列长度二次增长；传统循环模型深度线性但无法并行。需要同时具备对数深度、线性复杂度且可并行的语言建模架构。

方法关键点：将平衡树递归算子从序列编码扩展到自回归预测。通过对前缀序列构造平衡树并在树上执行关联性偏置的 up-sweep 操作，所有位置的前缀表示可在对数深度内并行计算，整体计算复杂度为线性。模型称为 Log-Depth Recurrent Units 的自回归版本。

关键结果：在语言建模任务上，该模型表现出稳健的长度外推能力，性能接近基于 ALiBi 的 Transformer。尽管尚未超越 Transformer，但展示了作为替代架构的潜力，并初步刻画了这一模型类的性质。
