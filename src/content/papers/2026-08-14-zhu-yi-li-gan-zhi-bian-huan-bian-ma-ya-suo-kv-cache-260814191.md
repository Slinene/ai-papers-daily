---
title: KV Cache Compression Through the Lens of Transform Coding
title_zh: 注意力感知变换编码压缩 KV Cache
authors:
- Hannah Laus
- Claudio Mayrink Verdun
- Hao Wang
- Flavio du Pin Calmon
- Felix Krahmer
affiliations:
- Technical University of Munich
- Technical University of Darmstadt
- MIT
- Harvard University
- Red Hat AI
arxiv_id: '2608.14191'
url: https://arxiv.org/abs/2608.14191
pdf_url: https://arxiv.org/pdf/2608.14191
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM 推理 · KV Cache 压缩
tags:
- KV cache compression
- transform coding
- reverse water-filling
- quantization
- long-context inference
one_liner: 用白化变换与反向注水按注意力输出失真分配 KV cache bit，5.8x 压缩下近无损
practical_value: '- 长上下文 LLM 推理服务里，KV cache 是大头成本；这套方法只需离线校准集做白化 + 全局 bit 分配，在线仅做
  per-token 标量量化，无额外训练，适合快速接入 vLLM/TensorRT-LLM 的量化路径。

  - 注意力感知权重可直接复用：key 通道用 q_c^2 加权，value 通道用 W_O 行范数加权；对重要通道多给 bit，尾部通道给 0 bit 等价低秩裁剪，比
  uniform precision 更稳，尤其适合商品描述、多轮会话历史、Agent memory 等长上下文场景。

  - 校准数据混合思路值得照搬：FineWeb 与 OpenR1-Math 各半，同时覆盖通用文本和推理链；电商场景可替换为商品描述/搜索会话/推理 trace
  混合，避免只在通用语料上过拟合。

  - 工程细节有复用价值：保留前 4 个 token 与最近 128 token 全精度，按 block 16 重量化；GQA 下按 head-group 做 token-wise
  max scaling；在更 aggressive 的 2-bit 预算下，attention-aware 分配相对 var-only 优势更明显，可做服务分层压缩。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：KV cache 在长上下文推理中成为主要内存瓶颈。现有量化方法大多最小化 cache 本身的重建误差，没有考虑量化噪声如何通过 softmax 注意力传播到最终输出。该工作把信号处理中的变换编码与反向注水引入 KV cache 压缩，直接最小化注意力输出失真。

**方法关键点**：
- 在白噪声量化假设下，推导出注意力输出失真分解为 key 项、value 项和高阶余项：key 通道按注意力权重平方 a_i^2、输出残差 ||v_iW_O - o||^2、query 分量 q_c^2 加权；value 通道按 a_i^2 与 W_O 行范数加权。
- 离线标定阶段：对 W_K/W_V 做 Cholesky 白化 + SVD，得到 A、B 因子，缓存变换后特征 HK/HV；从校准集统计通道方差和注意力感知权重；用全局反向注水解出 per-channel bit 分配。
- 在线推理：对每个 token/head-group 做 max 缩放 + 均匀标量量化；保留前 4 个 token 和最近 128 token 全精度，按 block 16 重量化。

**关键结果**：在 Llama-3.1-8B-Instruct 和 Qwen-2.5-7B-Instruct 上覆盖 LongBench、RULER、GSM8K、MMLU-Pro、MATH-500。5.82x 压缩下，AATC 在所有 benchmark 上与 FP16 统计不可区分；Qwen 上 RULER-32k 和 MMLU-math 分别超过最强量化 baseline 7.2 和 16.8 点；在 2-bit 更 aggressive 预算下，attention-aware 分配相对 var-only 的优势更明显。

**最值得记住的一句话**：先白化去相关，再按“注意力输出敏感度”而非缓存重建误差分配 bit，是长上下文 LLM 推理接近无损压缩的关键。
