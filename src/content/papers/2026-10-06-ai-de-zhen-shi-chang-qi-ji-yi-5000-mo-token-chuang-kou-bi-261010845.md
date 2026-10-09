---
title: 'Real Long-Term Memory for AI: A 50-Million-Token Window That Is Faster and
  Cheaper Than Recompute'
title_zh: AI 的真实长期记忆：5000 万 token 窗口，比重算更快更省
authors:
- Sietse Schelpe
affiliations:
- Corbenic AI
arxiv_id: '2610.10845'
url: https://arxiv.org/abs/2610.10845
pdf_url: https://arxiv.org/pdf/2610.10845
published: '2026-10-06'
collected: '2026-10-09'
category: LLM
direction: LLM 推理 · KV 卸载长期记忆
tags:
- KV cache
- long-term memory
- offloading
- LLM serving
- sliding-window attention
- energy efficiency
one_liner: 将 KV state 加密落盘并按需恢复，实现 50M token 零重算长期记忆，恢复比重算快 2.8–4.3 倍、省 8.8–12.3 倍
  GPU 能耗
practical_value: '- 在电商/广告/推荐 Agent 中，若大量 prompt 反复包含同一用户历史、商品序列或政策知识，可把已处理 prefix
  的 KV 状态落盘复用，而不是每次 RAG re-read：单 block 恢复比重算快 2.8–4.3×，能耗降 8.8–12.3×，且 TTFT 不随历史深度增长，适合长
  session 个性化。

  - 对含敏感 PII 的长期用户记忆，可用 AES-256-GCM 加密 KV store 作为组织级 durable memory；字节精确恢复避免文本重读和潜在泄露，同时小模型/大模型共享同一存储，日常请求用小模型，复杂问题用大模型读取同一个
  memory。

  - 评测长期上下文时，采用盲摄入 + needle/decoys + negative control + 存储审计的防作弊协议，避免仅靠前缀缓存命中或 keyword
  match 假阳性；业务侧做 A/B 时可借鉴分离「状态恢复命中率」和「模型回答准确率」两个指标。

  - 注意：方案依赖 local NVMe 和 sliding-window attention 的低 KV footprint（Gemma 4 12B 仅 36.4
  KiB/token），对 full-attention 模型需评估存储成本；当前只做单块 restore，不扩大单次 attention 窗口，也不做 learned
  retrieval。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：Transformer 只能注意 context window 内的 tokens，serving 每次请求都重建 KV cache，导致长期历史反复支付 prefill 成本。该工作将已计算的 KV state 加密持久化到本地 NVMe，按需恢复，使模型拥有跨 50M token 的长期记忆，而不是临时 cache。

方法关键点：
- galahad-kv 把每 ~16k tokens 的 KV state 写入 AES-256-GCM 加密磁盘；restore 时把存储 block graft 回 forward pass，不重新计算 tokens。
- 基于 Gemma 4 的 sliding-window attention，12B KV footprint 为 36.4 KiB/token，31B FP8 为 134 KiB/token；50M tokens 分别占 1.86 TB / 6.25 TB。
- vLLM connector 管理 moving window：一个 block 常驻 GPU，其余落盘，VRAM 恒定；不同模型可共享同一 durable store。
- 防作弊协议：运行时 mutator 替换实体防预训练污染；盲摄入防 query lookahead；每 block 植入 needle 与 same-format decoys；审计磁盘 header 与 KV footprint；negative control 检查幻觉。

关键实验（50M tokens = 3,125 blocks × 16k，H100 + vLLM）：
- 100/100 深度 0–49.49M tokens 均从加密 store 零重算恢复；12B recall 82/100，31B 98/100，均 0 幻觉；negative control 0/20 伪造。
- restore vs recompute：12B 中位数 0.266s/59J vs 0.760s/521J，即 2.8× 加速、8.8× 节能；31B 0.347s/80J vs 1.475s/976J，即 4.25× 加速、12.3× 节能；TTFT 不随深度增长。
- deposit 吞吐：12B 20,839 tok/s，31B 10,700 tok/s；整个 50M token 流期间 VRAM 保持平坦。

局限：不是更宽的 attention 窗口，也不包含 learned retrieval；只测量单 block restore。

> 最值得记住：存储 KV state 而非文本，把已见过的内容从“每次重读”变成“一次读、之后恢复状态”，是 LLM 具备 durable long-term memory 的关键。
