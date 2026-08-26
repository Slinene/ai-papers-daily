---
title: 'TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration'
title_zh: TileMix：面向 LLM 推理加速的 Tile 中心混合精度注意力
authors:
- Hanzhi Zhang
- Qiao Zhang
- Qinglei Cao
- Heng Fan
- Yan Huang
- Kewei Sha
- Yunhe Feng
affiliations:
- University of North Texas
- Saint Louis University
arxiv_id: '2608.17336'
url: https://arxiv.org/abs/2608.17336
pdf_url: https://arxiv.org/pdf/2608.17336
published: '2026-08-17'
collected: '2026-08-26'
category: LLM
direction: LLM 推理 · 混合精度注意力 kernel
tags:
- Mixed-Precision
- Attention Kernel
- LLM Inference
- Long Context
- FlashAttention
- INT8 Quantization
one_liner: 通过 tile 分组路由 FP16/INT8 注意力计算，在保留 dense 连接的同时加速长上下文 prefill 并恢复质量
practical_value: '- 长上下文 RAG / Agent memory / 多跳检索场景中，prefill 是延迟大头；可借鉴按 attention
  score tile 分组做混合精度（关键区域 FP16，其余 INT8），而不是整层 uniform INT8，能在质量和吞吐之间拿到更好 trade-off，且无需训练或改模型权重。

  - 路由模板可直接复用稀疏注意力的空间先验（local band / global / random / SpTrans / BigBird），但只决定精度路径、不删除
  token 交互；业务上可先用静态模板快速验证哪些位置对效果敏感，再考虑升级为自适应或 learnable 路由。

  - INT8 KV cache + per-block scale 能降低显存和 decode 成本，同时 V 保持 FP16 做 PV 更新，工程风险较低；如果使用
  FlashAttention-style serving，可参考其 shared online-softmax 状态与 bitmask constant-time
  查找的集成方式，支持 GQA 和 variable-length batching。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
长上下文 LLM prefill 中 dense self-attention 的 QK score 计算随序列长度平方增长，是推理瓶颈。现有 uniform 低精度如 INT8 会损失质量，稀疏注意力会改变 token 连接，而 IO-aware fused attention 通常只支持单一精度路径，缺少在 kernel 内部对 score tile 做空间精度调度的机制。

## 方法关键点
- TileMix 把 attention 矩阵分成硬件对齐的 score tiles，按 key-tile 维度分组，每组由一个 bit 决定走 FP16 或 INT8 路径；决策打包成 64-bit bitmask，inner loop 用 shift-and-mask 做 constant-time 查找。
- 引入 group factor g，让一个 bit 控制多个相邻 key tile，保持 metadata O(H_k*T_m)，支持长上下文。
- FP16 与 INT8 路径都更新同一个 online-softmax state；INT8 路用 blockwise absmax 量化，INT8 Tensor Core MMA + INT32 accumulation，rescale 后进入 FP16 的 shared running max/normalizer/output accumulator。
- 保持 dense token connectivity，不需要训练；支持 GQA、variable-length batching、INT8 KV cache；提供 band/global/row_rand/align_sparse/BigBird/SpTrans 等静态路由模板。

## 关键实验结果
- 质量：在 LongEval 和 LV-Eval 上，TileMix 相比 uniform INT8（One）一致恢复长上下文检索和 QA 质量，部分布局如 SpTrans 能达到或超过 FP16。
- 效率：A100 40GB 上 LLaMA 3.2 3B-Instruct，4k tokens 时 FlashAttention 14.33K tokens/s，TileMix SpTrans75 达 31.80K tokens/s（约 2.2x），也高于全 INT8 One 的 29.80K；8k 时 FlashAttention OOM，TileMix 仍可运行。
- 数值：mean absolute deviation 随 INT8 coverage 从 0% 的约 7e-5 增到 25% 的约 2e-3，提供可控精度-效率边界。

## 最值得记住的一句话
把精度路由下放到 attention score tile group，可以在不改变 dense 连接的情况下做 FP16/INT8 空间调度，实现长上下文 prefill 的可调质量-效率 frontier。
