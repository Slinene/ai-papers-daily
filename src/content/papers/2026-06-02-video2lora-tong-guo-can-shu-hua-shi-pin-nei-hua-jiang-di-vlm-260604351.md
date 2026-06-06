---
title: 'Video2LoRA: Parametric Video Internalization for Vision-Language Models'
title_zh: Video2LoRA：通过参数化视频内化降低 VLM 推理成本
authors:
- Manan Suri
- Sarvesh Baskar
- Dinesh Manocha
affiliations:
- University of Maryland, College Park
arxiv_id: '2606.04351'
url: https://arxiv.org/abs/2606.04351
pdf_url: https://arxiv.org/pdf/2606.04351
published: '2026-06-02'
collected: '2026-06-06'
category: Multimodal
direction: 视觉语言模型 · 视频压缩内化
tags:
- Video Understanding
- LoRA
- Hypernetwork
- VLM
- Inference Efficiency
- Parameter Generation
one_liner: 用超网络从视频直接预测 LoRA 权重，查询时零视觉 token，保持性能的同时大幅降低延迟和吞吐成本
practical_value: '- 对于电商商品视频、直播切片等需要反复问答的场景，将视频内化为 LoRA 权重后，后续查询完全省去视频帧编码，可实现 6~80
  倍的首 token 延迟降低和 1500 倍的视觉 token 负载缩减，适用于对同一内容多次交互的 Agent 或推荐解释链路。

  - 超网络预测 LoRA 权重的思路可迁移到其他多模态输入的快速适配：如图集、商品描述集合等，用一次前向生成一个适配器，替代传统微调，快速构建个性化模型。

  - 发现不重叠视频段独立生成的 LoRA 可在秩空间直接相加组合，这为长视频（如长时直播回放）的分块处理提供了可能，可在电商视频理解中用于处理超长商品讲解或直播内容。

  - 单次前向生成适配器的架构设计（感知器超网络读取冻结 VLM 中间层特征）可作为“模型即存储”的参考，当业务需要反复访问同一批多媒体内容时，可将内容压缩为轻量权重，减少对上下文窗口的依赖。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：VLM 处理视频成本极高，每帧产生数百视觉 token，推理耗时与帧数、查询次数线性增长，超出上下文窗口后输出退化。现有方案无法在保持视频忠实度的前提下显著压缩查询时的视觉 token 负载。

方法：提出 Video2LoRA，一种参数化视频内化方法。用一个小型感知器超网络，在冻结的 VLM 逐层编码视频时，读取各层的中间表示，直接预测出一组 LoRA 适配器的权重。训练时使用视频摘要和字幕任务，预测出的 LoRA 加载到同一 VLM 后，仅通过文本查询（无任何视觉 token）即可生成答案。

结果：在 5 个字幕基准和 7/8 个视频问答基准上，Video2LoRA 与传统的带视频帧上下文推理相比，性能统计等价且非劣。模型仅用 12 帧 384px 训练，却能稳定处理高达 1024 帧、1024px 的视频，而直接上下文推理在此条件下常失效。回答阶段视觉 token 数降低最高 1500 倍，首 token 延迟缩短 6–80 倍，且输出保持视频忠实。此外，发现不重叠视频段独立生成的适配器可在秩空间相加，支持长视频的分块内化。
