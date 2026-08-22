---
title: 'FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving'
title_zh: FlashPrefill V2：面向长上下文LLM服务的块稀疏预填充注意力
authors:
- Qihang Fan
- Huaibo Huang
- Zhiying Wu
- Bingning Wang
- Ran He
affiliations:
- MAIS & NLPR, CASIA
- UCAS
- WeChat, Tencent
arxiv_id: '2608.19758'
url: https://arxiv.org/abs/2608.19758
pdf_url: https://arxiv.org/pdf/2608.19758
published: '2026-08-20'
collected: '2026-08-22'
category: LLM
direction: 长上下文推理·块稀疏注意力优化
tags:
- Block-Sparse Attention
- Prefill Optimization
- KV Cache
- FP8 Inference
- Long-Context Serving
one_liner: 通过均值修正、FA3/4对齐内核与分页KV/连续批处理，将块稀疏预填充从原型推进到生产级，128K下最高加速47倍
practical_value: '- 用户长序列（如点击序列、会话历史）的预填充延迟是长上下文推荐/Agent系统的首要瓶颈，可借鉴块稀疏注意力：用均值修正项在极端稀疏下稳定精度，避免稀疏化后排序/检索效果明显下降。

  - PackGQA内存访问、warp specialization和pingpong pipelining的组合可直接指导自研稀疏attention kernel，尤其适合在H20等推理卡上部署FP8量化，显著降低长上下文服务成本。

  - 原生支持paged KV cache与continuous batching，说明稀疏注意力可作为现代推理框架（如SGLang）的backend无缝接入，适合在电商/搜索推荐在线服务中做透明替换，无需改动上层模型逻辑。

  - 如果业务中有大规模多轮对话或长文档预填充，可参考块稀疏阈值机制做动态跳块，并在FP8精度下验证效果，兼顾首token延迟与模型质量。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：长上下文LLM推理中，prefill阶段的注意力计算复杂度随序列长度二次增长，成为在线服务的主要瓶颈。此前工作FlashPrefill已用瞬时模式发现和最大动态阈值降低开销，但仍是算法原型，距离生产部署较远。

方法关键点：FlashPrefill V2从三方面走向实用：①引入均值修正项（mean correction term）抑制块稀疏注意力引入的近似误差，使极端稀疏下模型精度仍可接受；②重设计稀疏注意力算子，采用PackGQA内存访问、warp specialization和pingpong流水线，与FlashAttention-3/4实现完全对齐，并支持FP8推理；③原生支持paged KV cache和continuous batching，可直接作为SGLang等现代推理框架的注意力后端。

关键结果：在NVIDIA H20 GPU上评测，128K上下文长度下，FP8精度相对FlashAttention-2最高加速47.26倍，BF16精度相对FlashAttention-2最高加速27.19倍；FP8下相对FA3/4对齐的稠密基线仍加速30.49倍。
