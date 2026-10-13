---
title: On the Design Space of Continuous Diffusion Language Models
title_zh: 连续扩散语言模型的设计空间研究
authors:
- Oscar Davis
- Daan Roos
- Alice Bizeul
- Amitis Shidani
- Victor Turrisi
- Louis Béthune
- Pierre Ablin
- Marco Cuturi
affiliations:
- Apple
- University of Oxford
- University of Amsterdam
arxiv_id: '2610.13834'
url: https://arxiv.org/abs/2610.13834
pdf_url: https://arxiv.org/pdf/2610.13834
published: '2026-10-09'
collected: '2026-10-13'
category: Training
direction: 连续扩散语言模型训练设计
tags:
- Continuous Diffusion
- Language Models
- Self-Conditioning
- Embedding Geometry
- Text Generation
- Diffusion Models
one_liner: 揭示自条件与嵌入几何机制，提出 DoubleCat 和 SemiCat 显著提升连续扩散语言模型文本生成性能
practical_value: '- 在推荐/搜索场景中用连续扩散语言模型生成 query、文案或 push 消息时，优先关注 self-conditioning
  和 embedding geometry 两个训练杠杆；DoubleCat 无需额外前向即可修正 train/inference mismatch，适合低延迟在线生成。

  - SemiCat 引入 discrete reveals 后，在标准超参下即可达到离散扩散性能，且 tuned sampler 可显著提升精度；这套方法迁移成本低，适合资源有限的业务快速落地文本生成模块。

  - 嵌入几何的结论表明交叉熵驱动的 embedding 解码错误率已接近 one-hot，实际部署时不必过度设计嵌入空间，可以节省算力和存储。

  - 混合 corruption 过程和异步噪声调度的探索为广告文案、商品标题等可控文本生成提供了新的调参方向，值得在业务数据上做小规模验证。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：连续扩散语言模型（CDLMs）具备加速采样和可控生成潜力，但训练关键杠杆（如自条件、嵌入几何）理解不足，阻碍其性能对齐离散扩散。

方法关键点：
- 发现 self-conditioning 通过暴露模型于推理类似状态修正训练/推理不匹配，这些状态在训练中罕见。
- 提出 DoubleCat：两层 interpolant，无需额外前向传播即可获得自条件增益，在 TinyGSM 上精度提升三倍以上。
- 进一步引入 discrete reveals 得到 SemiCat，直接缓解 token identifiability 问题（大范数高斯主导 token 难以识别）。
- 分析嵌入空间：交叉熵驱动 embedding 向解码错误率接近 one-hot 的几何收敛。
- 额外探索混合 corruption 过程和同步/异步噪声调度。

关键结果：SemiCat 在 TinyGSM 上达到 49.94% 精度（标准训练超参+调优采样器），与离散扩散持平；在 1.7B 规模，SemiCat 在 6 个 likelihood 评估中 4 个超过离散扩散，并在无条件生成上超越 one-hot flows。
