---
title: 'LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers'
title_zh: 循环 Transformer 的亚 1 位 KV 缓存量化 LoopVQ
authors:
- Minsoo Cheong
- Sungjoo Yoo
affiliations:
- Seoul National University
arxiv_id: '2611.05304'
url: https://arxiv.org/abs/2611.05304
pdf_url: https://arxiv.org/pdf/2611.05304
published: '2026-11-03'
collected: '2026-11-05'
category: LLM
direction: KV cache 量化 · 循环 Transformer
tags:
- KV Cache Quantization
- Vector Quantization
- Looped Transformers
- Inference Optimization
- SGLang
one_liner: 针对循环 Transformer 提出联合多循环步通道的 KV 缓存向量量化，0.5 位下超越现有方法，吞吐提升最高 6.1 倍
practical_value: '- 若业务中使用循环/共享层 Transformer 架构（如深度递归 LLM），可借鉴 LoopVQ 沿循环轴联合量化 KV
  cache，利用步间冗余大幅压缩内存；即使未用循环架构，其敏感度差异观察也提示可以对不同层/步采用差异化量化位宽。

  - 微调 codebook 匹配全精度模型输出，比直接聚类更有效，此校准思想可迁移到 embedding 压缩、语义 ID 量化或生成式推荐的 item 表示量化中。

  - 在 SGLang 中的实现显示，0.5 bit KV cache 量化在 32K 上下文下几乎将解码延迟减半、峰值吞吐提升 4.3～6.1 倍，证明低位量化是长上下文
  LLM 推理降本增效的关键，电商/广告场景处理用户长期行为序列或长商品描述时可直接受益。

  - LoopVQ 与现有标准 LLM KV cache 量化方法正交且可与 TaSQ 结合，说明可组合多种压缩技术进一步压低位宽至 0.25 bit，适合高并发生成式推荐/Agent
  服务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：循环 Transformer 通过循环步复用参数降低参数内存，但 KV cache 仍随循环步线性增长成为主要内存瓶颈。作者观察到循环模型 KV cache 沿循环轴高度冗余，且不同循环步对量化敏感度差异显著。

**方法关键点**：提出 LoopVQ，联合编码多个循环步的 channels 进行向量量化，并微调 codebooks 使其匹配全精度模型输出，而不是简单聚类；该方法与现有标准 LLM 的 KV cache 量化方法正交，可结合 TaSQ 进一步压缩。

**关键结果数字**：在 Ouro 和 Huginn 循环模型上，0.5 bits per element 下，LoopVQ 在通用、长链推理和长上下文检索任务上优于现有标准 LLM 的 KV cache 向量量化方法；与 TaSQ 结合后在 0.25 bits 仍保持大部分 BF16 精度。在 SGLang 实现中，32K 上下文解码延迟接近减半，峰值吞吐在 1.4B 和 2.6B Ouro 模型上分别提升 4.3 倍和 6.1 倍。
