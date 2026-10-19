---
title: 'FuTransformer: FP8 prefill and INT4 decode for Llama-style inference on Hopper'
title_zh: FuTransformer：面向 Hopper 的 Llama 式推理 FP8 Prefill 与 INT4 Decode
authors:
- Wei Wang
arxiv_id: '2610.23796'
url: https://arxiv.org/abs/2610.23796
pdf_url: https://arxiv.org/pdf/2610.23796
published: '2026-10-16'
collected: '2026-10-19'
category: LLM
direction: LLM 推理 GPU Kernel 与量化优化
tags:
- FP8
- INT4
- KV cache quantization
- CUDA kernel
- Transformer inference
- Hopper
one_liner: 在 H100 上实现 Llama 风格 Transformer 推理 CUDA kernel，prefill 用 FP8，decode 用 INT4
  权重和旋转 INT4 KV cache，单步解码从 8.1ms 降至 2.8ms
practical_value: '- 在线推荐/Agent 系统中 LLM 推理延迟敏感，可借鉴其 INT4 decode 方案：权重 INT4 + KV cache
  INT4，在 H100 上 batch=1 的 Llama-3.1-8B 单步从 8.1ms 降到 2.8ms，适合低延迟实时交互。

  - 将量化权重和 keys 直接按 Tensor Core fragment layout 存储，避免生成完整中间 tile，减少显存读写和 kernel 复杂度；这项工程优化可复用到线上
  embedding lookup 或 attention 模块的低精度部署。

  - 使用 block-diagonal Hadamard 旋转抑制异常通道对 KV cache 量化误差的影响（旋转后 cache 量化仅增加 0.20 PPL），对用户行为序列、长历史
  cache 的压缩存储有参考价值。

  - 把固定 RMSNorm gain 折叠进权重、FP8 输出直接写入并采用 delayed scaling，合并多个独立 kernel 为 GEMM+epilogue，减少
  kernel 启动和中间结果搬运，适用于实时特征服务中的算子融合。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：Transformer 推理的 prefill 和 decode 瓶颈不同。prefill 复用权重，受矩阵乘和 activation 搬运主导；decode 单 token 复用有限，受权重和 KV-cache 读取主导。现有推理 kernel 未充分针对这两个阶段分别量化优化。

**方法**：提出 FUTRANSFORMER，基于 CODA 的 GEMM+epilogue 思想实现 Llama 风格 block。prefill 采用 FP8，直接写 FP8 输出并用 delayed scaling，支持无 padding prefill，将固定 RMSNorm gain 折叠进权重。decode 使用 INT4 投影权重与 INT4 KV cache，权重和 keys 均按 Tensor Core fragment layout 存储，内核直接反量化到 MMA 操作数，无需完整中间 tile。采用 block-diagonal Hadamard 变换降低 cache 量化对 outlier channel 的敏感性。

**结果**：在单张 H100 上，prefill 比编译 PyTorch FP8 快 1.48x，达到 1.29 PFLOP/s；FP8 推理路径比 BF16 CODA 快 2.02–2.18x。在 8B/70B 形状、batch 1–32 下，INT4 decode 比对应最快的 PyTorch block 快 1.3–2.4x，比自身 FP8 路径快 31–51%。完整 Llama-3.1-8B 单步 decode 2.8ms，对比编译 transformers 实现 8.1ms。INT4 权重路径使 WikiText-2 困惑度从 6.24 升至 7.23（round-to-nearest）或 6.99（GPTQ），旋转 INT4 cache 再加 0.20；内核与量化参考一致性在 0.001 PPL 内。
