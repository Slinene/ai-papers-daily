---
title: Dissecting GPU Utilization for LLM Inference on Nvidia Hopper
title_zh: 剖析 Nvidia Hopper 上 LLM 推理的 GPU 利用率
authors:
- Mohammad Siavashi
- Gerald Q. Maguire
- Dejan Kostic
- Marco Chiesa
affiliations:
- KTH Royal Institute of Technology, Stockholm, Sweden
arxiv_id: '2609.12923'
url: https://arxiv.org/abs/2609.12923
pdf_url: https://arxiv.org/pdf/2609.12923
published: '2026-09-11'
collected: '2026-09-14'
category: LLM
direction: LLM 推理 GPU 性能剖析
tags:
- LLM inference
- GPU utilization
- NVIDIA Hopper
- GMMA
- profiling
- decode
one_liner: 用八个 NCU 计数器视图替代单一 SM 利用率，分解 Hopper 上 LLM 推理 decode 阶段利用率低的机制
practical_value: '- 部署 LLM 服务（如搜索推荐中的对话/Agent）时，不要只依赖 SM utilization 判断 GPU 是否饱和，应结合
  fragment fill、occupancy、stall cycles 等多个 NCU counter 做性能归因，避免误导性扩容决策。

  - decode 阶段小 batch 是主要瓶颈：Hopper GMMA 固定 64 行片段，实际 batch 远小于 64 时有效计算占比极低。可尝试 continuous
  batching 或 sequence packing 提高 fragment 填充率，但需与延迟约束权衡。

  - 论文提出的 counter-validated 视图方法可复用：从 Nsight Compute 原始报告定义 8 个视图，把性能问题映射到具体 kernel
  角色（QKV 投影、attention、MoE expert 等），适用于自建推理引擎或调优 vLLM。

  - 生成式推荐/Agent 场景常混合长序列与多请求，需区分 cold prefill 与 warm prefill 的 kernel 选择差异，分场景建立性能基准以指导
  batch size 和序列长度配置。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：单一 SM utilization 百分比会让 LLM 推理负载看起来计算饱和，却掩盖实际有用工作的比例。问题在 decode 阶段尤为严重——每个请求只产生一个新 token，稠密投影 GEMM 变成小行矩阵乘法；Hopper 的 bfloat16 GMMA 路径以固定 64 行矩阵片段执行，小 batch decode 只能填充片段的一小部分。

**方法关键点**：在 H100 NVL 上使用 vLLM + FlashAttention-3 + cuBLASLt，对 cold prefill、warm prefill、decode 三个阶段进行 profiling，并扫描序列长度与 batch size。用八个 counter-validated 视图替代传统单一利用率，每个视图绑定一个 NCU counter 或显式公式，分别对应 fragment fill、occupancy limits、stall signatures、wave quantization、kernel selection 等机制，覆盖四个生产模型和六种 per-layer kernel 角色。

**关键结果**：八个视图将利用率缺口映射到具体机制，揭示小 batch decode 时 GMMA fragment 填充率低是主要损耗来源；不同 kernel 角色（如 attention、GEMM）表现出不同的瓶颈特征；单一利用率无法区分真实矩阵乘吞吐与伪饱和。
