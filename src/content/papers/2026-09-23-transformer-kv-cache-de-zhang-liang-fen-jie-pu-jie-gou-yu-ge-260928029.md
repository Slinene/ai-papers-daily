---
title: 'Tensor Decomposition of Transformer Key-Value Caches: Spectral Structure and
  Format Comparison'
title_zh: Transformer KV Cache 的张量分解：谱结构与格式对比
authors:
- Rahul Krishnan
- Volker Schulz
affiliations:
- Universität Trier
arxiv_id: '2609.28029'
url: https://arxiv.org/abs/2609.28029
pdf_url: https://arxiv.org/pdf/2609.28029
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM KV cache 张量分解压缩
tags:
- KV cache
- tensor decomposition
- Tucker
- low-rank approximation
- RoPE
- inference
one_liner: 对 KV cache 四阶张量做谱测量，在 2-5× 压缩下 Tucker 重构误差最低，head/layer 近满秩不可压
practical_value: '- 工业 LLM serving 做 KV cache 压缩时，可优先用 2D/SVD 压 key；value 需保留 4 维结构，用
  Tucker 且不压 head/layer 轴，同存储下误差更低。

  - 压缩预算不要均匀给四个轴：head 和 layer 近满秩，强行压缩收益极低且伤精度；预算应集中在 token 与 feature 轴。

  - RoPE 后 key 的可压缩性下降 41%-64%，若做 prefill 缓存或分阶段压缩，尽量在 RoPE 前对 key 做低秩/缓存，或对 post-RoPE
  key 分配更高 rank。

  - value 的错误地板比 key 高，在电商/Agent 长上下文场景做混合 KV cache 管理时，value 应给更高存储比例或更保守压缩。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：KV cache 成为长上下文、大 batch 推理的瓶颈，但压缩格式选择缺少谱结构指导。

**方法关键点**：将 KV cache 视为 head×token×feature×layer 四阶张量；在 Mistral-7B-v0.3 和 LLaMA-2-13B 上测四种 mode unfolding 的奇异值谱，比较 Tucker、CP、tensor train、t-SVD 在 2×-5× 压缩比下的重建误差，并对比 2D 展开基线；提出 mode-pinning 定理，从谱上判断满秩保护。

**关键结果**：token/feature 轴低秩明显，尤其 key；head/layer 轴近满秩，难以压缩。Tucker 在所有压缩比下重建误差最低，因为它能保留满秩 mode。2D 方法对 key 误差更低，但四向 Tucker 对 value 误差更低。value 误差地板高于 key；post-RoPE key 的可压缩性比 pre-RoPE 下降 41%-64%。
