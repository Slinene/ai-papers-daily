---
title: 'Chorus: Shared N-gram Embeddings with Layer-wise Adaptation'
title_zh: Chorus：共享 N-gram 嵌入的逐层自适应机制
authors:
- Stephen Chung
- Wenyu Du
affiliations:
- DualverseAI
arxiv_id: '2611.23386'
url: https://arxiv.org/abs/2611.23386
pdf_url: https://arxiv.org/pdf/2611.23386
published: '2026-11-16'
collected: '2026-11-20'
category: LLM
direction: 高效 n-gram 嵌入表参数共享与层自适应
tags:
- n-gram embeddings
- parameter sharing
- layer-wise adaptation
- memory-efficient training
- language model scaling
one_liner: 用共享 n-gram 表加逐层自适应投影，在表参数减少 87% 下匹配或超越现有方法
practical_value: '- 当推荐/搜索模型中多层需使用同一组 ID、行为序列或 query n-gram 嵌入时，可改为共享基础表 + 每层轻量投影
  + 由 hidden state 生成逐分量缩放因子，既大幅压缩嵌入表内存，又保留层间差异，适合多塔 Transformer 或序列建模。

  - 大型 ID embedding 表训练时优化器状态（如 AdamW 的 m/v）是主要内存瓶颈，Ember 这类内存高效优化器能节省 99% 以上表优化器内存且不损效果，可直接用于
  item、behavior hash embedding 训练，降低 GPU 成本。

  - 哈希 n-gram 嵌入表与计算解耦，每一步只查很少行，却能显著提升模型容量；在电商行为序列、搜索 query 分词上引入 hash-based n-gram
  特征，可捕捉局部共现模式，几乎不增加推理延迟。

  - 利用当前 hidden state 动态调整共享嵌入的缩放与投影，是一种轻量的层特异性机制，可用于多任务/多场景共享底层特征，减少为每个任务维护独立大嵌入表的需求。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：n-gram embedding 表能以极小计算代价为语言模型增加容量，但现有设计要么每层独立持表、内存过大且无法跨层复用知识，要么单表共享导致所有层嵌入相同、缺乏层偏好，实际效果差。如何在保持容量和层自适应的同时显著压缩表内存？

**方法关键点**：Chorus 用一组共享 n-gram 表服务整个网络，每层以自己的方式读取：先根据当前 hidden state 计算逐分量缩放因子，对精炼后的嵌入做 rescale，再经过该层专属投影层得到最终向量。通过这种轻量层适配，共享表既能跨层复用知识，又能表达层间偏好。

**关键结果**：Chorus 仅用 1.2B 表参数，预测文本质量超过 FactorEngram 和 DeepSeek Engram 用 9.6B 参数的水平，相当于表大小减少 87%；在 20M 到 9.6B 参数范围内，所有对比设置中均优于 Engram、TN-gram 和 FactorEngram。结合 Ember 优化器，相较 AdamW 节省 99.2% 的表优化器内存，且训练性能不下降。
