---
title: 'PACE: A Unified Condense-and-Extract Paradigm for Fast VLM Inference'
title_zh: PACE：统一的压缩-提取范式加速视觉语言模型推理
authors:
- Junjie Liu
- Shengyuan Ye
- Xu Chen
affiliations:
- Sun Yat-sen University
- Power Dispatch Control Center, Guangdong Power Grid Co., Ltd.
- Shenzhen Loop Area Institute
arxiv_id: '2608.27206'
url: https://arxiv.org/abs/2608.27206
pdf_url: https://arxiv.org/pdf/2608.27206
published: '2026-08-27'
collected: '2026-08-29'
category: Multimodal
direction: VLM推理加速 · token压缩
tags:
- VLM
- Inference Acceleration
- Visual Token Pruning
- Training-Free
- Multimodal
one_liner: 训练无关的VLM推理加速框架，通过像素自适应压缩和动态双注意力提取，仅用10%视觉token保留93.8%性能，TTFT加速3.1倍
practical_value: '- 电商商品图像理解：对大规模商品图进行VLM推理（如属性提取、图文一致性校验）时，可借鉴APC在编码前评估像素信息密度，对背景简单或冗余区域降采样，降低视觉编码器计算量，显著缩短首token延迟，适合实时性要求高的在线服务。

  - 多模态Agent在搜索/推荐中的应用：当Agent需要理解用户上传图片或商品图来辅助推荐时，DDAE融合视觉编码器内部信号和LLM语义信号，可在严格token预算下保留关键视觉细节（如商品logo、纹理），避免性能损失，提升交互响应速度。

  - 训练无关、即插即用的设计便于快速集成到现有VLM服务，无需微调即可部署，适合频繁迭代的线上系统；10%视觉token保留93.8%性能、3.1倍TTFT加速的结论可作为token预算设定的参考基准。

  - 架构上，将压缩前置到编码器之前、提取后置到LLM之前，形成两级优化，这种“先压缩后提取”的范式可以启发多模态推荐中其他模态（如视频帧、音频）的token优化，在保持性能的同时降低整体推理成本。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：VLM推理成本随视觉token数量激增；现有视觉token剪枝方法多在后视觉编码器阶段，未优化编码阶段延迟；且在严格token预算下难以同时保留全局上下文和细节。

**方法关键点**：提出PACE，训练无关的统一压缩-提取范式。Condense阶段，自适应像素压缩器（APC）在编码前评估视觉信息密度，自适应下采样冗余区域，减少编码器计算，保留全局上下文和关键视觉线索。Extract阶段，动态双注意力提取器（DDAE）融合视觉编码器内部信号和LLM语义信号，选择性保留视觉token，保护任务关键细节。两级优化分别加速视觉编码器和LLM。

**关键结果数字**：集成到Qwen2.5-VL-7B，仅用10%视觉token，保留93.8%原始性能，TTFT加速3.1倍。
