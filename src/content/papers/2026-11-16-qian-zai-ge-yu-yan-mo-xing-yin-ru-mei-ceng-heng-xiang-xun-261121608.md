---
title: Latent Lattice Language Models
title_zh: 潜在格语言模型：引入每层横向循环隐状态
authors:
- Shivam Duggal
- Zongze Wu
- William T. Freeman
- Antonio Torralba
- Richard Zhang
- Eli Shechtman
affiliations:
- MIT CSAIL
- Adobe
arxiv_id: '2611.21608'
url: https://arxiv.org/abs/2611.21608
pdf_url: https://arxiv.org/pdf/2611.21608
published: '2026-11-16'
collected: '2026-11-17'
category: LLM
direction: Transformer 架构改进 · 横向循环隐状态
tags:
- Latent Lattice
- Transformer
- SSM
- Residual Stream
- Perplexity
- Architecture
one_liner: 在 Transformer 中增加沿时间循环的每层横向隐状态流，直接调制注意力、KV cache 和 MLP，降低困惑度
practical_value: '- 自研 LLM 或做大规模预训练时，可将 Lattice 作为 Transformer 的扩展模块，在长序列生成（如商品描述、推荐理由）中通过增加水平循环状态提升表达能力，参数开销可控（406M
  模型仅小幅增加）。

  - 若团队已在做多路架构改进，可参考论文结论：Lattice 与 hyper-connections、input residuals 等残差流增强可叠加，组合后困惑度进一步降至
  13.61，说明不同改进能互补。

  - 推荐系统中用户行为序列建模可借鉴“横向 persistent state”思路：在 Transformer 编码器中加入跨时间步共享的 latent，捕获长期兴趣，比纯
  SSM 或纯 Attention 更灵活。

  - 直接业务应用需重新训练，适合有预训练资源的团队；若只是微调开源模型或调用 API，可关注后续是否开源权重，目前主要是架构研究贡献。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：标准 Transformer 每层只有一个垂直残差流 latent，同时承担读取记忆、注意力、MLP 等多项任务，计算状态有限。已有改进如更深层、循环层或残差连接增强，但未系统利用每层持久状态。

**方法关键点**：提出 Lattice of Latents，在每层引入一组水平 latent streams，沿时间步循环更新，与垂直残差流并行。这些 latent 不是像 SSM 那样仅作内部记忆，而是直接参与垂直流的注意力计算、KV cache 写入、MLP 计算和解码。相当于为模型增加一组持久计算状态，扩展计算容量而不加深网络或增加 token 数。

**关键结果**：在 20B FineWeb-Edu tokens 上，406M 参数 Lattice 模型验证困惑度从 15.41（参数匹配 Transformer）降至 14.40；与 hyper-connections 和 input residuals 叠加后进一步降至 13.61。在 Gated DeltaNet、Mamba-2、Triadic GDN、GDN-Mamba-2 等混合架构上，每个 native state size 下均提升，Lattice-GDN 和 Lattice-Triadic-GDN 甚至超过 4 倍 native state 的纯基线。结论：持久 per-layer state 是扩展语言模型计算的互补轴。
