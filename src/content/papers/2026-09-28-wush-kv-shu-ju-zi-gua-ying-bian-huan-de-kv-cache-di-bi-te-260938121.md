---
title: 'WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms'
title_zh: WUSH-KV：数据自适应变换的 KV Cache 低比特量化
authors:
- Jiale Chen
- Vage Egiazarian
- Eldar Kurtić
- Torsten Hoefler
- Dan Alistarh
affiliations:
- Institute of Science and Technology Austria (ISTA)
- ETH Zürich
- Red Hat AI
arxiv_id: '2609.38121'
url: https://arxiv.org/abs/2609.38121
pdf_url: https://arxiv.org/pdf/2609.38121
published: '2026-09-28'
collected: '2026-10-01'
category: LLM
direction: LLM 推理优化 · KV Cache 量化
tags:
- KV Cache
- Quantization
- WUSH
- LLM Inference
- Data-Adaptive Transform
- SGLang
one_liner: 用 WUSH 数据自适应可逆变换对 KV cache 做低比特量化，2-bit 下 Qwen3-8B 全面优于 OSCAR
practical_value: '- 对需要长上下文/高并发 LLM 服务的推荐与 Agent 系统，KV cache 内存是主要瓶颈。可借鉴将可逆变换与量化解耦：校准阶段按每个
  head 的 Gram 矩阵（缓存张量自身统计）+ Hessian（下游消费者敏感度）构建变换，允许非正交各向异性缩放，比固定 Hadamard/随机旋转在 2-bit
  下显著降低误差。类似思路可用于用户/物品 embedding 缓存或特征存储的低比特压缩，关键是 Hessian 选下游任务对扰动的敏感度。

  - 值侧变换可在离线折叠进权重（V→WV、WO），在线零额外开销；键侧变换因 RoPE 无法折叠，放在 RoPE 之后，每新增 token 只多做一次 d×d
  矩阵乘。工程上优先折叠 value 侧，key 侧用固定在线 transform，避免逐位置补偿。

  - 保留 sink token 和最近 token 的 FP16 窗口（例如 sink=64, recent=256）并用批量量化 flush（chunk 8/16）可在大幅降低平均位宽时保护长上下文和生成质量；该策略与具体量化器无关，可直接迁移。

  - 校准只需 128 条序列、一次完成，跨 bitwidth 复用；量化器可选 QuEST 或 OSCAR-style percentile-clipped affine，证明
  WUSH 与 QuEST 搭配接近最优。在 SGLang 中集成时，可沿用 OSCAR 的 cache 管理策略，不必为 WUSH 重新调参。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM 推理中 KV cache 随上下文长度和 batch size 线性增长，长上下文推理的内存/带宽成为瓶颈。低比特量化是直接手段，但 aggressive quantization 会引入显著误差，影响 attention scores 和输出。已有工作如 KVQuant、KIVI 侧重量化器设计；QuaRot、SpinQuant、OSCAR 等用固定或正交变换做坐标重分布，但正交变换无法做各向异性缩放，难以同时考虑缓存张量自身分布和下游 sensitivity。

**方法关键点**
- WUSH-KV 把 WUSH 的乘积感知变换迁移到 KV cache：对每个 KV head，用校准数据分别构建 key 和 value 的可逆变换。key 变换的 Hessian 来自消费它的 query heads（∑ Q Q^T），value 变换的 Hessian 来自输出投影块（∑ W_O W_O^T），Gram 矩阵来自 key/value 自身。
- 变换构造：T = Wush(M,H)，通过 Cholesky + 特征分解得到闭式解，非正交，允许各向异性缩放；scale 保持 Frobenius 范数。
- 值侧变换折叠进模型权重（WV←WV T_V^T, WO←T_V^{-T}WO），在线零开销；键侧变换放在 RMSNorm 和 RoPE 之后，每新 token/query 做一次 d×d 矩阵乘，避免 pre-RoPE 放置导致的位置相关补偿。
- 量化器与变换解耦：理论部分用 QuEST INT，证明在 additive rounding noise 和 clipping 条件下，WUSH 在 sensitivity-balanced 变换中 near-optimal；端到端集成 SGLang 时使用 OSCAR-style percentile-clipped affine quantizer。
- 保留 full-precision sink + recent 窗口（sink=64/recent=256，flush chunk=8），逐批量化，兼顾缓存精度与长上下文。

**关键实验**
- 消融在 Qwen3-8B 36 个注意力模块、128 条 FineWeb-Edu 校准、32 条评估（长度 1024），2-bit 下 WUSH 的 geometric-mean module-output error 为 0.208，OSCAR 0.309，Hadamard 0.325；3/4-bit 也普遍更低。
- WikiText-2 PPL：Qwen3-8B 全精度基线 9.72；2-bit WUSH 10.51，OSCAR 13.74；4/3/2-bit 均最低。
- 下游 2-bit 任务：Qwen3-4B-Thinking、8B、32B 在 AIME 2025、MATH-500、GPQA Diamond、LiveCodeBench v6；8B 上 WUSH-KV 四个 benchmark 全部高于 OSCAR（AIME 46.7 vs 34.4，MATH 92.9 vs 89.3，GPQA 54.5 vs 52.9，LiveCodeBench 35.2 vs 20.4）；4B 和 32B 大多 competitive，LiveCodeBench 8B/32B 大幅提升。
- 校准成本：Qwen3-8B 在 L40S 上约 12 分钟、峰值 39 GiB，一次校准跨 bitwidth 复用。

**最值得记住的一句话**
KV cache 量化的关键不只是量化器，更在于为每个 head 选择数据自适应、非正交的可逆变换，使缓存张量坐标在量化前与下游敏感度对齐。
