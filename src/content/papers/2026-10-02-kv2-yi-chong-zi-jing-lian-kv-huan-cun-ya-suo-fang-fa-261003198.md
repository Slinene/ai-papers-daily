---
title: 'KV$^2$: A Self-Refining KV Cache'
title_zh: KV²：一种自精炼 KV 缓存压缩方法
authors:
- Johannes Wesch
- Danni Liu
- Jan Niehues
affiliations:
- Karlsruhe Institute of Technology
arxiv_id: '2610.03198'
url: https://arxiv.org/abs/2610.03198
pdf_url: https://arxiv.org/pdf/2610.03198
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: LLM 推理 · KV cache 压缩
tags:
- KV cache
- long-context LLM
- query-agnostic compression
- selective reconstruction
- inference efficiency
one_liner: 用轻量代理选少量锚点做选择性重建，在 2% KV 预算下大幅优于 KVzip 等基线
practical_value: '- 对 Agent 长期记忆、用户历史、商品知识库等“一次缓存、多次 query”场景，优先用 query-agnostic 压缩；KV²
  两阶段思路可复制：先用便宜业务信号（如 key 相似度、商品/行为 embedding）挑锚点，再做局部 max-attention 打分，比全量重建省钱。

  - 可将 KV 预算压到 2%–5%，适合电商搜索/推荐的超长上下文（长用户序列、多商品文档），降低缓存显存和 decode 带宽；chunk size 4K
  是性价比甜点。

  - 默认单轮即可，别急着上多轮 self-refinement；只有在 proxy 很弱或 reconstruction 比例极小时才考虑 2–3 轮。

  - 落地注意：论文基于 kvpress 的 masking 实现未物理 compact，需配合 headwise 变长 attention、paged cache
  和重复 query 服务后端，才能把压缩阶段收益转成实际 decode 收益。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
长上下文 LLM 部署中 KV cache 决定显存与 decode 带宽；在“一次 prefill、多次 query”的可复用场景（如长期 Agent 上下文、长文档知识库）中，query-aware 压缩不可靠，query-agnostic 压缩成为关键。轻量 proxy（KeyDiff）便宜但不准，KVzip 全上下文重建准但太贵。

**方法关键点**
- 两阶段选择性重建：Stage1 用轻量 proxy 对每个 chunk 打分，选 top-ρ 的 token 作为重建 query；Stage2 只对这些 query 做 causal forward，让其 attend 全 cache，然后用 chunk 内每个位置被这些 query 关注的 max attention 作为 eviction score。
- 保留 sink tokens，chunk size 默认 4K，query 选择比例默认等于最终 KV 保留比例。
- 支持多轮 self-refinement：把上一轮 Stage2 分数当下一轮 proxy，但默认单轮已足够。

**关键结果**
在 RULER 16K、LongBench、NIAH、InfiniteBench 上验证 Llama-3.1-8B-Instruct 与 Qwen3-8B。RULER 16K 在 2% KV budget 下平均分比 next-best baseline 高 40+ 百分点；LongBench 2% budget 下 Llama 从 24.16 提到 33.59，Qwen 从 16.59 提到 32.97。压缩阶段 runtime 与 peak memory 均低于 KVzip，且在极端预算下优势更大。

**最值得记住的一句话**
可复用 KV cache 压缩不需要重建全上下文：用便宜 proxy 选少量锚点 query 做选择性重建，就能在 2% 级别预算下保住关键长上下文信号。
