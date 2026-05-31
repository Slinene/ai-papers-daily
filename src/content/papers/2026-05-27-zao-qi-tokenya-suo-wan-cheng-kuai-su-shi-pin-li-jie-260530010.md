---
title: 'EarlyTom: Early Token Compression Completes Fast Video Understanding'
title_zh: 早期Token压缩完成快速视频理解
authors:
- Hesong Wang
- Xin Jin
- Lu Lu
- Chenhaowen Li
- Jian Chen
- Qiang Liu
- Huan Wang
affiliations:
- Zhejiang University
- Westlake University
- Alibaba Cloud Computing
arxiv_id: '2605.30010'
url: https://arxiv.org/abs/2605.30010
pdf_url: https://arxiv.org/pdf/2605.30010
published: '2026-05-27'
collected: '2026-05-31'
category: Multimodal
direction: 多模态视频理解效率优化 · Token压缩
tags:
- Token Compression
- Video Understanding
- Vision-LLM
- Training-free
- Efficiency
one_liner: 提出训练无关的视觉编码器内部早期token压缩框架EarlyTom，显著降低TTFT和计算量
practical_value: '- **视觉编码器内压缩可大幅降低首Token延迟**：在实时视频理解或推荐场景（如短视频内容分析、直播审核），可以直接借鉴EarlyTom的帧合并策略，在编码器中间层提前丢弃冗余帧，无需重新训练模型，即刻提升推理速度。

  - **解耦空间Token选择减少压缩偏差**：在生成式推荐（如基于视觉的个性化feed）中，对图像/视频帧的空间信息进行压缩时，采用独立于通道的选择方式（如空间注意力引导的token保留）可以避免重要细节丢失，保持推荐准确性。

  - **训练无关方法易于集成**：该方案不依赖额外训练，可直接插入现有Vision-LLM流水线，适合快速迭代的工业级系统，尤其在对延迟敏感的Agent或多智体交互中，能快速实现多模态模块的加速。

  - **对视频多模态系统的工程启示**：揭示了视觉编码器在端到端推理中的时间占比过高问题，从业者应优先优化编码器而非仅关注LLM部分，类似思路可用于电商场景中的商品视频理解、虚拟主播驱动等任务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Video-LLMs推理时，大量视觉token的处理成为瓶颈，现有压缩方法多在LLM预填充后期进行，但视觉编码器本身的计算延迟被忽视。本文通过剖析发现视觉编码器贡献了主要的首Token延迟（TTFT），因此探索在编码器内部进行早期token压缩。

**方法**：提出EarlyTom，一个完全训练无关的压缩框架。关键设计包括：（1）早期视觉token压缩：在视觉编码器的多层内部进行“帧合并”，通过计算相邻帧的相似度，动态融合冗余帧，从源头减少后续处理的token数量；（2）解耦空间token选择：对每帧内部的空间区域独立评估重要性，去除不重要的空间token，采用一种无偏的筛选策略，避免压缩带来的分布偏移。这些操作均无需梯度更新，可即插即用。

**结果**：在A100 GPU上测试LLaVA-OneVision-7B模型，EarlyTom将TTFT降低最多2.65倍，FLOPs减少61%，同时在四个主流视频理解基准（MVBench、EgoSchema、LongVideoBench、VideoMME）上保持与全token基线相当的准确率，实现了吞吐量和效率的显著提升。
