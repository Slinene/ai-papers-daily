---
title: Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific
  Parametric Absorption
title_zh: 面向内存高效自回归视频生成的实例特定参数吸收方法
authors:
- Xiaomeng Fu
- Jia Li
- Yiming Hu
- Yong Wang
- Hayden Kwok-Hay So
- Jiao Dai
- Xiangxiang Chu
- Jizhong Han
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- The University of Hong Kong
- AMAP, Alibaba Group
arxiv_id: '2607.00712'
url: https://arxiv.org/abs/2607.00712
pdf_url: https://arxiv.org/pdf/2607.00712
published: '2026-07-01'
collected: '2026-07-05'
category: Other
direction: 自回归生成 · 参数化KV缓存压缩
tags:
- KV Cache
- Autoregressive Generation
- Video Generation
- Memory Efficiency
- Parametric Absorption
- Instance-Specific
one_liner: ISPA首次将KV缓存压缩从丢弃转变为实例级参数蒸馏，在视频生成中实现50%缓存缩减且质量无损
practical_value: '- 在推荐系统的长序列Transformer或生成式推荐模型中，可借鉴ISPA将部分层转为局部注意力，并通过最小二乘将历史缓存吸收到权重中，节省推理内存。

  - 预热阶段监测全注意力和局部注意力的输出差异来确定转换点，可用于Agent对话历史压缩，动态决定何时将旧上下文编码进模型参数。

  - 闭式解的权重调制无需重新训练，适合在线推理时实时进行缓存压缩，可直接集成到现有KVCache管理的工程框架中。

  - 对于电商场景的实时生成（如商品描述、直播推流），用ISPA减少视频/文本自回归生成的KV缓存，提升吞吐。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：自回归视频生成模型推理时，KV缓存随帧数线性增长，导致内存溢出和吞吐下降。常见做法是丢弃冗余token，但会破坏长程依赖，引起时间闪烁和身份丢失。亟需一种既能压缩缓存又不损失时序一致性的方法。

**方法**：提出实例特定参数吸收（ISPA），将缓存压缩从丢弃转向蒸馏。核心是让一部分层从全注意力（F-Layers）转为局部注意力（L-Layers），并通过吸收历史上下文到模型权重来补偿丢失的信息。具体流程：在短预热阶段，持续监测F-Layer与L-Layer的输出差异。在差异稳定后的转换点，利用历史累加的注意力状态构建闭式最小二乘问题，求出针对当前实例的权重调制矩阵，将其注入层后，该层即可仅依赖局部注意力，历史缓存被隐含进权重。此调制仅需一次前向计算，无迭代。

**结果**：在1.3B到14B参数的多架构视频生成模型上，ISPA可移除高达50%的KV缓存，视觉质量接近无损，且无闪烁或身份丢失，同时推理速度提升。
