---
title: 'E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models'
title_zh: E-MoE：面向非因子化扩散语言模型的增强型专家混合
authors:
- Arseny Ivanov
- Alexander Kolesov
- Alexander Korotin
- Ivan Oseledets
- Mikhail Goncharov
affiliations:
- Applied AI Institute, Moscow, Russia
arxiv_id: '2609.37533'
url: https://arxiv.org/abs/2609.37533
pdf_url: https://arxiv.org/pdf/2609.37533
published: '2026-09-28'
collected: '2026-10-03'
category: LLM
direction: 非因子化扩散语言模型 · MoE 路由
tags:
- Masked Diffusion Models
- Mixture-of-Experts
- Non-Factorized
- Language Modeling
- Few-step Generation
one_liner: 利用 MoE 路由决策作为离散共享隐变量，构建非因子化反向过程，在不增加激活参数下提升少步生成质量
practical_value: '- 若业务中存在**少步文本生成**需求（如创意文案、标题生成、query 补全、push 文案），E-MoE 可用 MoE 路由决策作为离散共享隐变量，比连续
  VAE latent 更不易 posterior collapse，且不增加激活参数，适合在线推理。

  - **非因子化建模思路可迁移**：在生成式推荐或 query 生成中，token 间常有强相关性（属性组合、标题模板、风格约束），可尝试将反向过程构造为多个因子化分布的
  mixture，通过轻量 MoE router 输出离散 latent 来捕获位置依赖。

  - **工程实现上**：共享路由决策不增加 active parameters，意味着在低 NFE 场景下推理时延可控；可在现有 MDLM 基础上仅替换反向建模方式，无需重新设计主干网络。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Masked diffusion models (MDMs) 的反向过程通常对位置做因子化，每个 token 独立 unmask，在少步生成时无法建模 token 间相关性，样本质量受限；连续高斯 latent 的 VAE 变体虽尝试捕获位置相关性，但易发生 posterior collapse，隐变量被忽略。

**方法关键点**：E-MoE 将 MoE 路由决策作为**离散共享 latent**，把反向过程构造为多个因子化分布的 mixture。该设计不增加激活参数，但通过共享离散变量捕获位置间依赖；训练上采用变分推断，避免连续 latent 的 collapse 问题。

**关键结果**：在合成多模态 benchmark、binarized MNIST 和 LM1B 上，E-MoE 均提升少步生成质量；LM1B 上，NFEs 1–16 范围内 generative perplexity 明显低于 factorized MDLM 和 continuous-latent VADD，且在 matched sample entropy 条件下保持优势。
