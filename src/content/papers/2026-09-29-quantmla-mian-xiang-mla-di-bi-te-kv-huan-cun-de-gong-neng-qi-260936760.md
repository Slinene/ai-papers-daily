---
title: 'QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching'
title_zh: QuantMLA：面向 MLA 低比特 KV 缓存的功能对齐双路量化
authors:
- Zunhai Su
- Yuxuan Sun
- Jianchao Tan
- Tao Zhang
- Ruihan Hu
- Yuchen Xie
- Xunliang Cai
- Ngai Wong
affiliations:
- The University of Hong Kong
- Meituan LongCat Team
- South China University of Technology
- Harbin Institute of Technology
arxiv_id: '2609.36760'
url: https://arxiv.org/abs/2609.36760
pdf_url: https://arxiv.org/pdf/2609.36760
published: '2026-09-29'
collected: '2026-10-13'
category: LLM
direction: MLA KV 缓存低比特量化与推理加速
tags:
- MLA
- KV cache quantization
- INT4
- RoPE
- LLM serving
- function-aligned quantization
one_liner: 针对 MLA 的 content 与 RoPE 双缓存，提出路径专属可离线融合变换与功能对齐目标，实现首个联合 INT4 缓存且精度损失极小
practical_value: '- 部署 DeepSeek-V2/V3、Kimi、LongCat、GLM 等 MLA 架构模型做长上下文 RAG、Agent 记忆或搜索摘要时，可直接采用
  content INT4 / RoPE INT4，甚至 content INT2 / RoPE INT4，并配合首 4 个 sink token 和最近 128
  token 的 BF16 保护，获得 3.59× KV cache 压缩和 5.168× 吞吐提升，显著降低在线 serving 成本。

  - 不要把 MLA 不同缓存一视同仁：同一 cache NMSE 下，RoPE 路径造成的注意力输出失真比 content 路径高 1.94–6.86 倍。如果预算有限或需要先做部分量化，应优先保留
  RoPE key cache 更高精度，content cache 可以更激进压缩。

  - 量化训练时不要只用 cache reconstruction MSE：可借鉴其功能对齐思路——content 路径用 attention-output reconstruction，RoPE
  路径用 positional QK reconstruction；学到的 rotation/scale 可以完全融合进权重，online 无额外变换开销。

  - Sink/recent BF16 保护是低成本 trick：在统一 softmax 下按 token 选择 BF16 或 INT4，能有效保持长上下文检索和推理能力，同时减少
  preemption，适合直接复用到生产 serving 策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：MLA 通过共享 content latent 和 decoupled RoPE key 降低 KV cache，但缓存仍随上下文线性增长；现有方案主要把 content 量化到 FP8，RoPE key 保留 BF16，联合低比特量化缺乏理解。作者发现同样 cache 重构误差下，RoPE 路径造成的 attention 输出失真显著更大：6 个模型跨 4 个家族，RoPE/content 响应比从 1.94× 到 6.86×。这说明 cache reconstruction error 不是功能损失的可靠 proxy。

**方法关键点**：
- 建立双路有限误差路由：content 误差同时影响 attention matching 和 value aggregation，RoPE 误差只影响 positional QK logits；用 Jacobian/Rayleigh quotient 把放大效应分解为 operator sensitivity、error energy allocation 和方向耦合。
- 提出 QuantMLA：content 路径在正交 rotation + channel scaling 空间学习，目标为 attention-output reconstruction；RoPE 路径在 frequency-pair rotation + tied scaling 空间学习，目标为 positional QK reconstruction，并有输出失真上界。
- 学到的变换完全离线融合进 pre-RoPE 投影和 normalization，online 无额外变换开销。
- 原生低比特 MLA kernel 将 unpack/dequant 融合进 attention；cache 策略为首 4 个 sink token 和最末 128 token 保留 BF16。

**关键结果**：在 DeepSeek-V2-Lite、Moonlight-16B-A3B、LongCat-Flash-Lite、GLM-4.7-Flash 四个 MLA 家族上，C4R4 联合 INT4 下，DeepSeek-V2-Lite 十任务平均 66.54 vs BF16 66.80，Moonlight 73.44 vs 73.57；LongCat-Flash-Lite 7 任务平均 62.01 vs BF16 64.26，GLM-4.7-Flash 53.75 vs 55.32。C2R4 下仍显著超过 RTN/SmoothQuant/QuaRot。RULER S-NIAH-3 检索比最强量化 baseline 高 7.40 点。系统上 128K 时 3.59× 持久缓存压缩，cache-pressure 负载下 whole-job 输出吞吐是 BF16 的 5.168×，preemption 从 32 降到 0。

**最值得记住**：MLA 的 RoPE key cache 虽小，但每比特误差对输出影响远大于 content cache，压缩时应按功能路径而非 cache 大小分配精度。
