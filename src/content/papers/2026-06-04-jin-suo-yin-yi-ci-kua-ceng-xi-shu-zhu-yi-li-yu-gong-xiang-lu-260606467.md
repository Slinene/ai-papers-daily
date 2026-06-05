---
title: 'You Only Index Once: Cross-Layer Sparse Attention with Shared Routing'
title_zh: 仅索引一次：跨层稀疏注意力与共享路由
authors:
- Yutao Sun
- Yanqi Zhang
- Li Dong
- Jianyong Wang
- Furu Wei
affiliations:
- Microsoft Research
- Tsinghua University
arxiv_id: '2606.06467'
url: https://arxiv.org/abs/2606.06467
pdf_url: https://arxiv.org/pdf/2606.06467
published: '2026-06-04'
collected: '2026-06-05'
category: LLM
direction: 长上下文推理 · 稀疏注意力架构
tags:
- sparse attention
- cross-layer sharing
- KV cache
- long-context inference
- inference efficiency
one_liner: 在 KV 共享架构上复用路由索引，跨层共享 token 级 top-k 选择，以极低开销实现高精度稀疏注意力，大幅提升长上下文推理效率。
practical_value: '- **长上下文推理效率优化**：在电商搜索/推荐 Agent 中，需要处理大量历史对话或商品描述时，可借鉴 CLSA 的共享路由思路——使用
  YOCO 类架构共享 KV 缓存，并让不同层复用相同的 top-k 路由索引，极大降低 token 稀疏注意力的路由开销，实现接近 block 稀疏的速度却能保持
  token 级精度。

  - **工程实现 trick**：对于已使用 YOCO 或类似 KV 共享的 LLM 服务，只需额外实现一个跨层复用的 indexer，预填充时计算一次 token
  级 top-k，解码时各层直接读取该索引进行稀疏注意力，几乎不增加额外成本，即可将长上下文解码吞吐提升数倍。

  - **Agent 多轮交互场景**：当 Agent 需要在长多轮对话中维护完整上下文并频繁解码时，CLSA 能将 KV 缓存存储大幅减少（因子为数倍），并保持解码速度，同时质量几乎无损，适合部署在资源受限的在线服务中。

  - **生成式推荐中的长序列生成**：若用 LLM 生成个性化推荐理由或连贯的 item 序列，CLSA 可加速长序列的自回归解码，降低延迟，尤其适合对实时性要求高的推荐场景。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：长上下文 LLM 推理日益受限于解码效率，尤其是思维链等重推理场景。现有稀疏注意力存在效率-质量权衡：结构化块稀疏加速强但质量损失明显，token 级稀疏精度高但全缓存 top-k 路由开销大，端到端加速有限。

**方法关键点**：提出跨层稀疏注意力（CLSA），基于 YOCO 等 KV 共享架构。核心思想是将路由索引也跨层共享：单个索引器在预填充时计算 token 级 top-k 选择，生成的稀疏索引在多个解码层间复用。这样既保留了 token 稀疏的细粒度选择性，又通过平摊路由成本大幅降低开销。CLSA 同时缓解预填充、KV 缓存存储与长上下文解码三大瓶颈。

**关键结果**：在短文本和长文本基准上，CLSA 兼顾质量与效率。128K 上下文下，解码加速高达 7.6 倍，整体吞吐量提升 17.1 倍。相比稠密注意力，KV 缓存大幅减少，接近块稀疏的加速能力但保持了 token 级精度，为长上下文 LLM 提供了一种更完整的架构方案。
