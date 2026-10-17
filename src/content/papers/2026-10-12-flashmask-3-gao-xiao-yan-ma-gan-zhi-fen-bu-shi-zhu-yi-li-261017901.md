---
title: 'FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention'
title_zh: FlashMask-3：高效掩码感知分布式注意力
authors:
- Guoxia Wang
- Qianyue He
- Siming Wu
- Haoyang Xie
- Qiwen Bao
- Jinle Zeng
- Jiabin Yang
- Tian Wu
- Dianhai Yu
affiliations:
- Baidu Inc.
arxiv_id: '2610.17901'
url: https://arxiv.org/abs/2610.17901
pdf_url: https://arxiv.org/pdf/2610.17901
published: '2026-10-12'
collected: '2026-10-17'
category: Training
direction: 训练系统 · 掩码感知注意力
tags:
- FlashAttention
- Context Parallelism
- Sparse Attention
- Load Balancing
- Hopper Kernel
- Distributed Training
one_liner: 将列式稀疏掩码扩展至 Hopper 分布式注意力，实现零通信掩码本地化与负载均衡的长上下文训练加速
practical_value: '- 长序列行为建模或多文档检索中，采用列式稀疏掩码（column-wise sparse mask）编码 document/prefix-LM/sliding-window
  等结构化 attention，用 O(N) 边界向量替代 O(N^2) 显式掩码，kernel 跳过全掩码 tile，可大幅降低显存和计算，适合用户长期行为序列的
  Transformer 训练。

  - 分布式 context parallel 下，掩码边界向量仅需做 clip–shift–max 变换即得到 rank-local 掩码，零跨卡通信；在电商/搜索推荐的多机训练中可直接复用，避免
  mask 同步开销。

  - 对稀疏 mask 导致的负载不均，借鉴 Hierarchical Compute-Communication IPO：先 IPO 做 compute balance，再
  inter-node 交换降低 KV 通信量，最后 intra-node rebalance，在工程上可分层优化。

  - 通信重叠可使用 NVSHMEM 对称内存 + 一端 RDMA + mask 驱动的 chunk 剪枝，减少约 50% all-gather/reduce-scatter
  流量，提升 overlap 效率，适用于大规模分布式训练（如 LLM 驱动的搜索推荐）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：长上下文训练 LLM/多模态模型时，结构化 attention mask 与 context parallelism 结合后，mask 物化、调度与负载不均成为主要瓶颈。FlashMask 虽用列式稀疏掩码将存储降为 O(N)，但仅支持 Ampere，无 Hopper FA3 流水线和分布式能力。FlashMask-3 利用列式稀疏掩码“以 key 为索引、存储 query 轴边界”的不对称性，将每 rank 掩码本地化退化为对边界向量的元素级 clip–shift–max，零跨卡通信（Theorem 1），输出直接适配单 GPU kernel。

方法关键点：
- Hopper kernel：三 role warp specialization（KV Index Generator 扫描掩码分类 tile，KV Loader 用 TMA 加载有效块，MMA Consumer 执行 WGMMA），复用 FA3 异步流水线；配 preemptive persistent tile (PPT) 调度器处理不规则 mask 的长尾负载。
- 分布式扩展：HCC-IPO 负载均衡器（先 IPO compute balance，再 inter-node 交换降低 KV 流量，最后 intra-node rebalance）；mask-aware overlap 使用 NVSHMEM 对称缓冲、hierarchical all-gather（cross-node congruence groups + intra-node NVLink）、mask-driven 通信剪枝跳过全掩码 chunk，反向 multi-stage overlap 配 bitmask-AMO 同步。

关键结果：单 H100 GPU 上 12 种 mask、4K–128K，相比 FlashMask / FlexAttention / MagiAttention 提升 achieved TFLOPs 45–141% / 34–71% / 2–44%；CP 4–32、每卡 8K，吞吐比 Megatron-Core CP (ring/all-gather) 和 MagiAttention 分别高 1.80×–3.71× / 1.71×–2.92× / 1.09×–1.46×，overlap 效率 0.31–0.75；128 H100 GPU 上训练 118B-A14B MoE、128K 上下文，端到端吞吐提升 7.3%–11.0%，attention 部分快 24.5%–44.9%。

最值得记住的一句话：列式稀疏掩码的边界向量是天然的分布式接口，零通信 clip–shift–max 即可完成 rank-local mask 转换，与 Hopper 异步机制无缝结合。
