---
title: Contextual Correction of Parallel Draftsfor Speculative Decoding
title_zh: 并行草稿上下文校正用于投机解码
authors:
- Roy Eisenstadt
- Harel Lidar
- Tal Gonen
- Omer Luxembourg
- Itamar Zimerman
- Lior Wolf
- Eli David
- Ilan Naiman
arxiv_id: '2610.12570'
url: https://arxiv.org/abs/2610.12570
pdf_url: https://arxiv.org/pdf/2610.12570
published: '2026-10-07'
collected: '2026-10-13'
category: LLM
direction: LLM 推理加速 · 投机解码
tags:
- Speculative Decoding
- Drafting
- Contextual Correction
- LLM Inference
- Parallel Decoding
- Diffusion Drafter
one_liner: DCOCO通过并行上下文评分恢复并行草稿块内依赖，在多种解码设置下取得最高吞吐，最高6.6倍加速
practical_value: '- 若在线上用 LLM 做搜索 query 生成、商品文案、Agent 对话等文本生成服务，可引入投机解码降低首 token 延迟，DCOCO
  的并行上下文校正比顺序校正更适合高并发请求，实测 4–32 并发下提升 6–23%。

  - DCOCO 在保留 drafter 并行性的前提下，通过轻量 scorer 恢复块内 token 依赖；类似思路可用于生成式推荐的 beam search
  / 候选生成，在保持并行推理的同时加入相邻候选的相容性打分，避免完全独立采样导致的低质量序列。

  - 部署时要关注 drafter 与 verifier 的 KV cache 管理，DCOCO 的候选打分机制只增加很小开销，适合与 continuous batching
  / vLLM 等 serving 框架结合。

  - 顺序校正（如逐个用上下文修正）在高并发下可能因为 kernel launch 开销反而退化，选择并行打分方案更稳。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：diffusion-based drafter 能在并行预测多个未来 token 的同时保持强预测能力，但同一 draft block 内的 token 预测时看不到前面 draft token 的真实身份，丢失了块内依赖，限制了接受率。需要一种不牺牲并行性又能恢复依赖的机制。

**方法关键点**：DCOCO（DFlash Contextual Corrector）不为每个位置只保留 top-1 token，而是保留多个候选 token，然后并行评估相邻位置候选间的上下文兼容性，据此进行上下文感知的 token 选择。该机制以极低额外开销恢复块内依赖，且保持并行 drafting。

**结果**：在 4 个 verifier backbones、10 个 benchmarks 上，DCOCO 在所有评估配置（greedy、stochastic、含/不含 extended reasoning）中均取得最高平均吞吐，相对 vanilla decoding 加速最高 6.6×。并发 serving 场景下，4–32 个并发请求时 DCOCO 比最强竞争方法高 6–23%，而顺序校正方法在该负载下甚至低于未校正的 DFlash。
