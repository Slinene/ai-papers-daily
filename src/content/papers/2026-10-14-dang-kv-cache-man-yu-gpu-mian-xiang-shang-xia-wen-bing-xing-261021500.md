---
title: 'When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel
  Prefill'
title_zh: 当 KV Cache 慢于 GPU：面向上下文并行预填充扩展远程 KV 层
authors:
- Muhammad Ibrahim
affiliations:
- Multiverse Computing
arxiv_id: '2610.21500'
url: https://arxiv.org/abs/2610.21500
pdf_url: https://arxiv.org/pdf/2610.21500
published: '2026-10-14'
collected: '2026-10-17'
category: LLM
direction: LLM serving · 远程 KV 层性能优化
tags:
- KV cache
- remote tier
- context parallelism
- LLM serving
- prefill optimization
- LMCache
one_liner: 用成本模型解释远程 KV 命中何时不如重算，并通过分片、按 rank 分区和异步加载把 p99 从 83.32s 降至 0.67s
practical_value: '- 部署远程 KV cache 前先用成本模型估算：带宽需超过 sR（本例 2.53 GB/s），且存在固定 per-hit 开销
  T0≈0.33s，短于 ~17k token 的 prompt 命中根本不如 recompute；电商/Agent 的 long-context 服务中可用于决定启用远程缓存的阈值。

  - 远程 KV 层按 PCP rank 分片、一个 server per rank 无协调，能将 GET 带宽提升 6.3 倍；可复用该思路给多卡并行推理服务，避免所有
  rank 读写同一实例导致瓶颈。

  - 将远程 KV 加载改为异步，能避免同步加载造成 GPU 空转、队列不稳；实测 p99 从 83.32s 降到 0.67s，对实时推荐/搜索的 LLM 在线服务很有参考价值。

  - 修复客户端 bug 对稳定性影响大；如果接入 LMCache 等库，注意 unbounded stall 问题，及时同步 upstream 补丁。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：长上下文 LLM 服务中重用 KV cache 是降低 prefill 成本的常见手段，但远程 KV 层可能反而拖慢请求。论文在 GLM-5.3（FP8 MoE + MLA）8×B300 节点上启用 LMCache + Valkey 远程层后，TTFT 中位数不变，但 16k token p99 从 3.96s 恶化到 17.3s。

**方法关键点**：回放生产流发现远程命中耗时 0.88s vs 重算 0.31s，同步加载让队列不稳。提出两项成本模型：带宽需大于 2.53 GB/s 才值得用远程层；固定 per-hit 开销 0.33s 使得 <17k token 的 prompt 命中无法优于重算。据模型优化：① 将 MLA KV 存储按 PCP rank 分片，证明最小 over-ranks 查找返回最长缓存前缀且不会破坏集合通信同步；② 远程层按 rank 分区，每 rank 一个 server 实例，无协调，GET 带宽提升 6.3×至 10.76 GB/s；③ 对分片存储加异步加载；④ 修复三个导致无限停等的客户端 bug。

**关键结果**：在 98.5% prompt token 来自远程层的命中密集流上，p99 从 83.32s 降至 0.67s；分片存储使 prefill 吞吐提升 14%，配合上游 kernel fix 提升 34%。所有改动已提交上游 LMCache。
