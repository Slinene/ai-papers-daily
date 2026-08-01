---
title: Capturing Token Tendencies for Training-Free Token Pruning in Multimodal Large
  Language Models
title_zh: 面向多模态大模型的趋势感知训练自由视觉Token剪枝
authors:
- Jie Ma
- Zhike Qiu
- Jie Gao
- Jiayi Ji
- Qian Chen
- Xiaoshuai Sun
- Rongrong Ji
affiliations:
- Xiamen University
- Xiamen Ocean Vocational College
- Sino-Russian Research Center for Digital Economy
arxiv_id: '2607.28341'
url: https://arxiv.org/abs/2607.28341
pdf_url: https://arxiv.org/pdf/2607.28341
published: '2026-07-30'
collected: '2026-08-01'
category: Multimodal
direction: 多模态LLM高效推理 · Token动态剪枝
tags:
- Token Pruning
- Multimodal LLM
- Attention Momentum
- Training-Free
- Late-Blooming Tokens
- Dynamic Rectification
one_liner: 通过捕捉注意力流动量实现动态可逆的视觉Token剪枝，避免“晚期绽放”关键token被过早丢弃
practical_value: '- 在多模态Agent或电商内容理解中，处理商品图片、视频时可采用注意力动量追踪，识别并保留初始被低估但深层关键的视觉token，避免误剪，提升下游任务精度。

  - 训练自由特性可直接集成到现有多模态LLM推荐或对话系统，无需重新训练，降低部署成本；超过77.8%的token缩减可显著加速推理，支撑实时交互。

  - 可逆剪枝设计为复杂场景（如用户拍摄的模糊、遮挡商品图）提供容错，动态修正机制可适配其他模态的token筛选，如文本序列中后期关键token的保留。

  - 方法不依赖额外模型结构，适合在电商搜索、广告生成等流量密集型场景中快速实验并上线，作为通用的效率优化插件。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有多模态LLM的视觉token剪枝方法依赖静态即时启发式，不可逆地过滤token，忽略了层次结构中token重要性随层动态变化的特性，导致深层推理所需的“晚期绽放”token被浅层过早丢弃，损害性能。

**方法关键点**：提出趋势感知剪枝（Trend-aware Pruning），将剪枝建模为时序轨迹预测问题。不再依赖单层孤立得分，而是捕捉注意力流动量（momentum），构建动态修正机制，选择性重新激活那些初始被低估但语义重要性逐步上升的token，实现可逆剪枝。

**关键结果**：在多种多模态任务上，视觉token减少超过77.8%，最终层仅保留约23个token，仍保持有竞争力的性能，取得效率与性能的优越平衡。
