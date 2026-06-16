---
title: 'Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn
  LLM Serving'
title_zh: 解锁非均匀KV缓存压缩以高效支持多轮LLM服务
authors:
- Hyungmin Kim
- Minsoo Kim
- Hongseok Kim
- Jungwook Choi
affiliations:
- Hanyang University
- Rebellions
arxiv_id: '2606.06302'
url: https://arxiv.org/abs/2606.06302
pdf_url: https://arxiv.org/pdf/2606.06302
published: '2026-06-14'
collected: '2026-06-16'
category: LLM
direction: LLM服务 · 非均匀KV缓存压缩
tags:
- KV Cache Compression
- Multi-turn LLM
- Non-uniform Compression
- Serving Efficiency
- Memory Management
- vLLM
one_liner: 提出Tangram框架，通过静态预算预留、粗糙分页和提前负载均衡，使非均匀KV压缩在多轮LLM服务中可达最高2.6倍吞吐提升
practical_value: '- 多轮对话推荐 / Agent 场景中，KV 缓存膨胀是吞吐瓶颈，非均匀头级压缩精度保持更好，Tangram 展示了如何通过离线校准头的保留模式并静态规划调度，避免运行时碎片回收开销，对自研推理引擎有直接参考价值。

  - 可借鉴“预算预留”：请求调度时预先固定每头压缩后内存大小，消除 prefill 阶段的页面回收（原占 25% prefill 时间），减少延迟抖动，适合对延迟敏感的在线服务。

  - “粗糙分页”将预算相近的头分入独立页表，将内部碎片转化为可回收内存，提升显存利用率，利于在有限显存下支撑更长对话历史。

  - “提前负载均衡”离线计算 GPU 分区，彻底消除 decode 步中 15-20% 的动态重规划开销，这一思想可迁移到需要 GPU 并行推理的推荐模型部署中。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多轮 LLM 服务中，对话历史累积导致 KV 缓存急剧膨胀，内存成为吞吐瓶颈。非均匀 KV 压缩（不同注意力头分配不同预算）虽精度更优，但现有推理框架要求头长度一致，导致：1) 碎片化使得释放的内存无法利用，2) 需回收散乱页面消耗 25% prefill 时间，3) GPU 负载偏斜使 decode 延迟增加 1.7 倍且每步重规划占 15-20% 时间。

**方法**：观察到头的重要度排序具有输入不变性且每头保留比例范围窄，可从 50 个样本离线校准。Tangram 据此将动态处理转为静态规划：1) **预算预留**（Scheduling 时固定每头压缩后内存，消除回收）；2) **粗糙分页**（预算相似的头归入独立页表，碎片化为可回收内存）；3) **提前负载均衡**（预计算 GPU 分区，无运行时重规划）。在 vLLM 上实现，作为现有非均匀压缩方法的无感底座。

**结果**：精度与原有方法持平，端到端吞吐比全 KV 基线提升最高 2.6 倍，prefill 回收开销降为零，decode 延迟恢复正常，彻底消除每步重规划耗时。
