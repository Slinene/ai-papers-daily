---
title: 'LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped
  Transformers'
title_zh: 'LoopCache: 加速长上下文Looped Transformer的自投机解码'
authors:
- Zizhuo Fu
- Haochen Huang
- Shengxuan Qiu
- Linye Wei
- Ziyu Tang
- Runsheng Wang
- Meng Li
affiliations:
- Peking University
arxiv_id: '2611.24301'
url: https://arxiv.org/abs/2611.24301
pdf_url: https://arxiv.org/pdf/2611.24301
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: LLM推理优化 · 自投机解码
tags:
- Looped Transformers
- Self-Speculative Decoding
- KV Cache
- Long-Context
- Inference Optimization
one_liner: 提出LoopCache框架，通过置信度引导动态草稿更新与循环KV缓存调度，大幅加速Looped Transformer长上下文自投机解码
practical_value: '- 自投机解码中，草稿更新不应固定于特定循环；可根据输出置信度动态修正草稿，避免浪费计算在过时轨迹上，提高接受率，可借鉴到长文本生成的推理加速场景。

  - 循环KV缓存调度策略将每步KV流量限制到单个循环，显著降低长上下文推理时的内存带宽压力，适合多轮对话、长文档摘要等对显存敏感的业务。

  - 选择性为少数浅层保留独立KV缓存，能以极小开销提升接受率，说明对不同层采用差异化缓存管理可有效平衡速度与精度。

  - 虽然Looped Transformers目前在推荐系统不常见，但相关推理加速技巧可迁移到任何采用递归或共享权重的LLM架构，如用于生成推荐解释或搜索摘要。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**  
Looped Transformers通过反复应用权重共享块获得大有效深度，但顺序循环执行导致推理慢。现有wave-style自投机方法（WFD、LoopSpec）存在两个限制：只在固定循环草稿，忽略中间预测变化导致计算浪费；批量处理不同循环的token需加载多份KV缓存，长上下文下内存流量剧增。

**方法关键点**  
LoopCache基于预测切换与输出置信度的相关性，引入置信度引导的动态草稿更新，在所有中间循环中实时修正草稿。同时，采用循环loop KV缓存调度，每步只访问单个循环的KV缓存，并在最近匹配周期批量token实现无损验证。此外，选择性为少数loop敏感浅层保留独立KV缓存，以极小开销提升接受率。

**关键结果**  
实验显示LoopCache平均比WFD加速10.25倍，比LoopSpec加速14.56倍，显著降低了长上下文推理延迟。
