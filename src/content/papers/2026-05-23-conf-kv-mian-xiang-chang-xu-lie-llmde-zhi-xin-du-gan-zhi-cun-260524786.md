---
title: 'CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for
  Long-Horizon LLM'
title_zh: CONF-KV：面向长序列LLM的置信度感知KV缓存淘汰与混合精度存储
authors:
- Yubo Li
- Yidi Miao
affiliations:
- Carnegie Mellon University
arxiv_id: '2605.24786'
url: https://arxiv.org/abs/2605.24786
pdf_url: https://arxiv.org/pdf/2605.24786
published: '2026-05-23'
collected: '2026-05-30'
category: LLM
direction: 长上下文LLM推理 · 置信度驱动KV缓存淘汰
tags:
- KV Cache
- Confidence-Aware
- Mixed-Precision
- Long-Horizon Inference
- Memory Management
one_liner: 利用模型生成时的置信度动态调整KV缓存预算，结合混合精度存储和分层金字塔预算，在低内存下保持长文本理解精度。
practical_value: '- 电商Agent等长对话/工具调用场景中，KV缓存迅速膨胀，可借鉴置信度感知淘汰策略：当模型对下一token预测不确定时保留更多历史，减少关键信息丢失；预测置信时激进剪枝，节省显存。

  - 混合精度存储（FP16/INT8）可有效压缩KV缓存，结合淘汰策略进一步降低内存占用，适合资源受限的在线服务部署。

  - 金字塔逐层预算分配（浅层保留较多token，深层保留较少）可平衡信息保留与计算开销，可结合具体模型结构调整各层预算比例。

  - 保护最近窗口（如固定最近若干token）保证局部连贯性，与置信度驱动预算结合，简单有效，可直接应用于现有Agent系统。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长序列LLM推理中KV缓存成为显存和注意力延迟的主要瓶颈。现有淘汰策略多依赖历史重要性或静态窗口，忽略了模型当前解码步骤的置信度这一实时信号。

**方法**：提出CONF-KV，将下一token分布转化为置信度分数，动态决定每步缓存预算——低置信时保留更多上下文，高置信时激进剪枝。预算内，token按累积注意力质量与近因的复合得分排序，同时保护一个最小最近窗口维持局部连贯。系统结合分块在线softmax注意力、混合FP16/INT8存储及金字塔逐层预算变体。

**结果**：在4个模型家族上生成4K长度，CONF-KV+INT8显存占用接近固定512-token滑动窗口，困惑度仅比完整KV高1.5-2.1。在32K Needle-in-a-Haystack测试中检索准确率达91.4%，远超滑动窗口的53.8%和H2O的80.6%。在VisualWebArena 75个任务上，CONF-KV以2.8倍更低峰值内存保留了95.3%的完整KV成功率。
