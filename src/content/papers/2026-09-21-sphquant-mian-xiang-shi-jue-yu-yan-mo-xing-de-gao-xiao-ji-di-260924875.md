---
title: 'SPHQuant: Efficient extreme low bit weight quantization for Vision-Language
  Models'
title_zh: SPHQuant：面向视觉语言模型的高效极低比特权重量化
authors:
- Kewei Zhang
- Zheng Chen
- Haotong Qin
- Yulun Zhang
affiliations:
- Shanghai Jiao Tong University
- The Hong Kong Polytechnic University
arxiv_id: '2609.24875'
url: https://arxiv.org/abs/2609.24875
pdf_url: https://arxiv.org/pdf/2609.24875
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: VLM 极低比特权重量化
tags:
- Weight Quantization
- Low-bit
- VLM
- PTQ
- Outlier
- GEMV
one_liner: 提出旋转无关的球面权重量化框架，通过分解8D权重向量分离异常值，实现2-3比特下精度匹配与30.3%解码吞吐提升
practical_value: '- 将权重按向量维度（如8D）分解为坐标符号、半径、正单位方向，并单独给半径分配更高精度，可迁移到LLM骨干的极低比特量化，降低异常值影响而不引入旋转的额外开销。

  - 方向码本采用角度参数化并微调来保持单位球约束，可以借鉴到生成式推荐的Semantic ID码本优化或embedding量化，提升低比特表示能力。

  - 自定义GEMV kernel：保持方向码本小到可放进共享内存，同时高效打包半径位，对自回归解码的memory-bound场景有实际加速效果，可参考用于部署推荐/Agent中的自回归LLM推理服务。

  - 旋转无关方法在2-3bit能与旋转方法精度相当，说明在追求低延迟、低内存的边缘部署时，优先避免旋转开销是可行路线，对端侧Agent或实时推荐推理有借鉴价值。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：VLMs正成为下一代基础模型，但大语言骨干导致内存占用高、自回归解码memory-bound，边缘部署困难。权重仅后训练量化（PTQ）是实用方案，但在2-3比特下，旋转无关方法受异常值影响精度差，旋转方法则带来额外运行时开销。

**方法关键点**：提出SPHQuant，一个旋转无关的球面权重量化框架。将每个8D权重向量分解为坐标符号、半径和正单位方向：半径隔离异常值幅度，方向有界且统计正则。基于此，给半径分配额外精度以缓解异常值带来的精度损失；使用紧凑的正方向码本，并通过角度参数化微调码本以保持单位球约束。还设计了硬件友好的GEMV kernel，使方向码本足够小以支持共享内存查找，同时高效打包半径位。

**关键结果**：实验表明SPHQuant在极低比特下与最先进量化方法精度相当，同时在RTX A6000上解码吞吐比QTIP提升30.3%。
