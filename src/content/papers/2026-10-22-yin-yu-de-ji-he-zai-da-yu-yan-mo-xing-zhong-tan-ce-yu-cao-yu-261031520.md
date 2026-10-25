---
title: 'The Geometry of Metaphor: Probing and Steering Metaphor Representations in
  Large Language Models'
title_zh: 隐喻的几何：在大语言模型中探测与操控隐喻表征
authors:
- Shihui Li
- Mette Andersen
- Martha Lewis
affiliations:
- Institute for Logic, Language, and Computation, University of Amsterdam
arxiv_id: '2610.31520'
url: https://arxiv.org/abs/2610.31520
pdf_url: https://arxiv.org/pdf/2610.31520
published: '2026-10-22'
collected: '2026-10-25'
category: LLM
direction: LLM可解释性与表征操控
tags:
- mechanistic interpretability
- metaphor
- representation steering
- causal subspace
- LLM
one_liner: 用机制可解释性定位多规模LLM中的隐喻因果子空间，并实现对分类与生成任务隐喻性的操控
practical_value: '- 在电商/广告文案生成中，可借鉴“概念方向”表征工程：定位“创意/隐喻/促销/正式”等风格的因果方向，通过激活空间 steer
  控制文案风格，无需微调大模型。

  - 用 probing 先行定位模型内部可操控子空间，再做 causal intervention 验证，成本低，适合快速验证 LLM 是否存在某种可调的风格维度。

  - 可迁移到搜索推荐 query 改写、push 文案：按场景调节隐喻度/创意度，例如信息流标题更含蓄有吸引力，搜索广告关键词更直白匹配意图。

  - 该工作主要是学术贡献，业务直接应用需自行构建风格标签、验证集和离线评测，但方法框架可复用。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：隐喻在人类语言中普遍存在，是创意与概念形成的基础；理解 LLM 如何表征隐喻、能否控制输出隐喻程度，对自然语言生成有理论与实用价值。

方法：使用机制可解释性技术，在覆盖不同架构与规模的多个 LLM 中定位与隐喻相关的因果子空间（causal subspace）；通过因果干预对内部表征进行 steering，并在分类与生成两类任务上验证，覆盖不同词性。

关键结果：在分类任务上，能够操控模型对隐喻性判断的输出；在生成任务上，也能调节生成文本的隐喻程度。这表明隐喻方向可被定位并作为“旋钮”控制文本风格。论文未披露具体准确率数值，但在多模型上验证了方法的通用性。
