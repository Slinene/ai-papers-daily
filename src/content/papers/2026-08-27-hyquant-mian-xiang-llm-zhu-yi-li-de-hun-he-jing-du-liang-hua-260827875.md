---
title: 'HyQuant: Hybrid-Precision Quantization for LLM Attention'
title_zh: HyQuant：面向 LLM 注意力的混合精度量化框架
authors:
- Jiatong Ding
- Bingxin Xing
- Yu Zhang
- Dian Ding
- Xiaodong Yi
- Xianbin Ouyang
- Feihu Zhou
- Kun Zhang
- Zhenyu Guo
- Hao Pan
affiliations:
- Shanghai Jiao Tong University
- Xi’an Jiaotong University
- Tencent Penglai Lab
- Xiamen University
arxiv_id: '2608.27875'
url: https://arxiv.org/abs/2608.27875
pdf_url: https://arxiv.org/pdf/2608.27875
published: '2026-08-27'
collected: '2026-09-11'
category: LLM
direction: LLM 长上下文推理 · 混合精度量化
tags:
- LLM
- Quantization
- KV Cache
- Attention
- Long Context
- Inference
one_liner: 保留 vertical-line token 与局部窗口全精度、其余 KV 低比特，实现长上下文推理的近无损量化加速
practical_value: '- 长上下文/Agent 场景做 KV cache 量化时，不要全局等精度：按列注意力质量选择 top-5% vertical-line
  token + 最近 W=128 窗口保留 FP16/BF16，其余 4-bit，可在 LongBench/GSM8K 上接近全精度；该模式可直接迁移到电商导购
  Agent 的长期对话历史、RAG 长 prompt 缓存。

  - 工程实现上，把 dequantize 融合进 attention kernel 的 online softmax 扫描，避免先材料化全精度 KV；在 H100
  上 32K 前缀 decode kernel 相对 FA2 达 3.58×、端到端 1.17×；对广告/搜索的 LLM serving 能降低显存带宽压力，显存不足时也可以跑更大
  batch。

  - Vertical-line 识别只需累加 attention 概率列和，额外 runtime 约 3-5%；用 tail-query proxy 且每 64
  tokens 更新，避免逐 token 全局打分，可作为轻量重要性评估器与稀疏/eviction 策略配合。

  - 局限：短上下文收益有限，且未在 coding/agentic 任务评估；接入长提示或 long CoT 前应先在自家任务验证 vertical-line 稳定性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：长上下文 CoT 推理使 Prefill 计算密集、Decode KV 带宽瓶颈突出；低比特量化可降本，但 attention 对误差敏感，uniform token-wise 量化忽视注意力分布高度不均，少量高注意力位置主导误差。

**方法关键**：
- 观察到 Qwen3-8B/Gemma/Llama 等 attention heatmap 存在 persistent vertical line，top-1% key position 覆盖 47-59% attention mass，top-5% + local window W=128 覆盖超 80%。
- HyQuant 将 key 分成 K_VL ∪ K_Win ∪ K_Q，按累计列注意力分数 S(k)=Σ_t a_{t,k} 选 top-ρ（≈5%）非 window prefix 作 vertical-line tokens，与最近 W=128 window 保留 FP16/BF16，其余 K/V 量化到 4-bit。
- Prefill：一个 fused FlashAttention-like online softmax 算子，融合低比特 GEMM 与全精度 vertical/window 路径；Decode：KV cache 混合存储，dequantization 在 attention kernel 内部执行，不材料化全精度 cache；新增 token 先进 staging buffer，降低重算开销。
- Vertical-line 识别用 tail-query proxy 轻量更新，每 64 tokens 做一次矩阵乘并求和，额外 runtime 约为 3-5%。

**关键实验**：
- 在 Qwen3-8B/32B、Llama-3.1-8B、GLM-4-9B 上的 LongBench、GSM8K、MATH500 评测中，K4V4 top-5% 平均接近或超过 FA2，优于 KIVI/KVTuner/SageAttention；LongBench avg: Qwen3-8B FA2 44.59→HyQuant 45.04，Qwen3-32B 48.61→48.46，GSM8K 96.52 vs FA2 95.88。
- Decode kernel latency：1K prefix 1.32×、32K prefix 3.58× speedup vs FA2；端到端 decode 1.04-1.17×；batch 32 场景下 HyQuant 未 OOM，而其他 KV 量化方法 OOM。
- 消融显示 vertical-line + window 组合 MSE 最低，top-k 提高可提精度但增加全精度 KV 预算。

**最值得记住的一句话**：低比特量化不应按 token uniform 分配精度，保留 <5% 的高列注意力 token 与最近局部队列即可让 K4V4 逼近全精度，同时获得长上下文 decode 的显著带宽收益。
