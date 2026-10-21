---
title: Large Flow Language Models
title_zh: 大规模流语言模型：连续流实现并行生成与自推测加速
authors:
- Arnav Chavan
- Chanhyuk Lee
- Udbhav Bamba
- Jaehoon Yoo
- Seunghoon Hong
- Aditi Raghunathan
- Jinwoo Kim
affiliations:
- UC Berkeley
- Amazon
- KAIST
- Carnegie Mellon University
arxiv_id: '2610.28559'
url: https://arxiv.org/abs/2610.28559
pdf_url: https://arxiv.org/pdf/2610.28559
published: '2026-10-19'
collected: '2026-10-21'
category: LLM
direction: 连续流语言模型 · 块并行解码加速
tags:
- flow language model
- parallel decoding
- self-speculative decoding
- multi-token prediction
- LLM training
- diffusion language model
one_liner: Lafa 8B 连续流语言模型用 <30B token 训练达到 AR 质量，并以自推测解码实现 2.54 倍吞吐
practical_value: '- 连续流语言模型可直接适配预训练 AR 模型，只用不到 30B token 训练即可达到匹配或更好的指令跟随/推理/编码质量，对业务中已有
  LLM 的低成本改造有参考价值；在搜索 query 生成、广告文案生成等高吞吐场景，可将 AR 模型转为流式并行解码。

  - 自推测解码方案用同一模型生成流式草稿并自回归验证，无需额外 draft 模型，相较 multi-token prediction 和离散扩散方法吞吐提升显著（2.54
  倍），可直接用于线上推理降本。

  - blockwise 流建模 + prefix caching + 块并行解码的组合可以作为工程参考：前缀因果注意力保证与 AR 的兼容性，块内双向异步流提升并行度，适合生成式推荐的
  prompt 长、重复前缀多的场景。

  - 流训练带来的 multi-token prediction 效应能保留甚至提升预训练 AR 能力，说明可以在业务微调阶段引入流训练做能力增强，而不只是推理加速。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：连续流语言模型支持并行生成、可控和加速，但十亿参数规模的构建技术仍不成熟；离散扩散的加速能力有限。

方法关键点：提出 Lafa，一种 blockwise 连续流语言模型。模型在前缀上使用因果注意力，在每个块内部使用双向、异步的流建模。这种设计支持从预训练 AR 模型高效适配，并在推理时利用前缀缓存和块级并行解码。训练规模覆盖 0.5B、7B、8B，训练 token 少于 30B，比已有扩散语言模型更数据高效。流训练还能蒸馏成一步或几步生成流映射。此外，利用流训练的多 token 预测效应，提出自推测解码：同一模型生成流草稿，再做自回归验证。

关键结果：在指令跟随、数学和编码任务上，Lafa 匹配或超越同量级 AR 模型；自推测解码在可比质量下达到 AR 模型 2.02–2.54 倍吞吐，优于 multi-token prediction 和离散扩散方法。
