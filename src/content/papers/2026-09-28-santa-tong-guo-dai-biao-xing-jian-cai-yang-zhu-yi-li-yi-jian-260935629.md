---
title: 'SANTA++: Sampling Attention through Representative Keys'
title_zh: SANTA++：通过代表性键采样注意力以减少 KV 读取
authors:
- Kyle Lee
- Christian Z. Pratt
- Ruoyu Fang
- Heekyung Lee
- Avinash Lohitsa
- Ryan Modafe
- Kerem Y. Camsari
affiliations:
- University of California, Santa Barbara
- Flucta
arxiv_id: '2609.35629'
url: https://arxiv.org/abs/2609.35629
pdf_url: https://arxiv.org/pdf/2609.35629
published: '2026-09-28'
collected: '2026-09-29'
category: LLM
direction: LLM 长上下文推理 · 稀疏注意力采样
tags:
- sparse attention
- KV cache
- importance sampling
- long-context LLM
- training-free
- FlashAttention
one_liner: 训练自由随机注意力方法，用代表性键路由团队采样，以 16%-22% KV 读取保留 94%-99% 精度
practical_value: '- 在需要长上下文 LLM 推理（如用户长期行为序列、商品详情、多轮对话历史）的服务中，采用“代表性键 + 团队采样”做 decode
  期稀疏 attention，可在 KV 读取降到 16%-25% 时仍保留接近 dense 的精度，适合降低在线推理成本。

  - prefill 后一次性用 k-means 或 contiguous 分块构建 parent groups，再在每个 parent 内选 actual-key
  representatives（首点最近均值，后续逐次最远点），decode 阶段固定复用；避免逐 token 全量扫描，尤其在 batch-one 长序列下成本低。

  - GQA 架构下，多个 query head 共享 KV head 的团队划分与代表键读取，但各 head 独立采样并保留自己的 inclusion correction，可进一步提升吞吐；与
  MLA 等压缩 KV 表示互补，已在 DeepSeek-V2-Lite 上验证仍有 token 稀疏性。

  - 实际部署注意：contiguous 分块可省去 k-means 预处理，虽然某些任务略降精度但访问更低；预算 S 是团队数而非 token 数，需要按团队大小和头间重叠重新估算实际
  KV 读取。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
长上下文解码时，attention 常集中在少量 token，但找出这些 token 仍需扫描所有 key；内存带宽受限时 KV cache 读取成为主要瓶颈。SANTA++ 在不全量扫描 key 的前提下，用代表性键做查询相关路由，让解码只读取少量团队，从而同时降低选择和评估的 KV 访问。

**方法关键点**  
- prefill 后对每层每 KV head 将 prompt key 分成 parent groups（k-means 或 contiguous）；每个 parent 内选最多 R 个实际 key 作为 representative，成员按最近欧氏距离加入团队。
- decode 时，对每个 query 只用每个团队的代表键计算路由分数（log n_g + q^T l_g / sqrt(d)），用 Gumbel-top-K 无放回采样 K 个团队；读取选中团队所有成员 KV 并计算精确 attention。
- 重要性采样校正：每个选中团队的 attention mass 和加权 value sum 除以条件 inclusion probability c_g = 1 - exp(-exp(phi_g - tau))，tau 是第 K+1 大扰动分数；保证未归一化和的无偏估计。
- 新生成 token 作为后缀精确评估；GQA 下共享团队划分和代表键读取，各 head 独立采样与校正。

**关键实验数字**  
Qwen2.5-7B-Instruct, 32K context：LongBench v2 以 16.68% KV reads 保留 dense SDPA 99.07% 分数；HELMET RAG 以 38.49% access 保留 98.00%；RULER 从 19.95% access 保留 91.07% 到 46.95% access 保留 98.54%。contiguous 分组免去 k-means，LongBench v2 在 15.27% access 达 96.88% 归一化分数，HELMET RAG 在 31.23% access 保留 97.56%。GPU Triton 实现：32K batch-one FP16，31 团队/头，attention 延迟从 107.33µs 降至 63.52µs，1.69× speedup vs Flash SDPA。

**最值得记住的一句话**  
用“实际键代表 + 团队采样 + inclusion probability 校正”可以在不重新训练的情况下，把长上下文注意力 KV 读取降到约 1/5 仍保持接近 dense 的精度。
