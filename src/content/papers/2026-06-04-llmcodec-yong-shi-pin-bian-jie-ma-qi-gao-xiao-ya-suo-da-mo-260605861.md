---
title: 'LLMCodec: Adapting Video Codecs for Efficient Weight Compression of Large
  Language Models'
title_zh: 'LLMCodec: 用视频编解码器高效压缩大模型权重'
authors:
- Rui Wang
- Yan Zhao
- Li Song
- Zhengxue Cheng
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2606.05861'
url: https://arxiv.org/abs/2606.05861
pdf_url: https://arxiv.org/pdf/2606.05861
published: '2026-06-04'
collected: '2026-06-08'
category: Training
direction: 模型压缩 · 仿射量化与视频编码
tags:
- LLM Compression
- Video Codec
- Quantization
- Affine Transform
- VVC
one_liner: 将视频编解码器VVC/H.266与仿射量化结合，无需微调即可高压缩LLM权重，显著降低困惑度并提升下游精度
practical_value: '- 权重压缩方法可直接用于电商推荐模型部署，在边缘设备或带宽受限场景下降低模型体积和传输成本

  - 视频编解码器对矩阵数据的结构化压缩思路可迁移到推荐系统Embedding表的压缩，利用现有硬件编解码加速

  - 无需校准数据或微调的压缩流程适合在线学习场景，模型更新后无需重新校准即可快速压缩发布

  - 2-bit极限压缩下仍保持较低困惑度，为Agent场景中的轻量化LLM本地部署提供新的压缩方案'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：大语言模型规模急剧增长，存储、传输与部署成本高昂。现有量化压缩方法通常依赖校准数据或微调，对不同张量类型泛化性有限。

**方法**：提出LLMCodec，将模型权重矩阵视为视频帧，利用仿射变换将权重值映射到视频编解码器的动态范围，再通过VVC/H.266等视频编码进行压缩。该方法无需任何微调或校准数据，天然适配矩阵结构化数据，并能借助高度优化的现成编解码器实现高效压缩。

**结果**：在LLaMA-3-8B模型上，2-bit精度下，LLMCodec相比现有方法将困惑度降低超过1.5倍，下游任务准确率提升21%。实验涵盖了多种视频编解码器与编码配置，验证了方法的鲁棒性与通用性。
