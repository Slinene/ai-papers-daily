---
title: Cache Engineering for Agents
title_zh: 面向智能体的 Cache Engineering：直接操控 KV Cache 以降低长程 Agent 成本
authors:
- Tianyu Fu
- Ruoxi Wang
- Zihan Min
- Zhongqi Ren
- Zhihao Li
- Tengxuan Liu
- Shengxu Mu
- Hanling Zhang
- Yu Wang
affiliations:
- Tsinghua University
- The Chinese University of Hong Kong
arxiv_id: '2610.28577'
url: https://arxiv.org/abs/2610.28577
pdf_url: https://arxiv.org/pdf/2610.28577
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent 长程执行 KV cache 直接操控与 serving 优化
tags:
- KV cache
- LLM agents
- serving system
- cache eviction
- position encoding
- context engineering
one_liner: 提出 cache engineering 让 Agent 通过 drop/repos 直接控制 KV cache，无需改轨迹或重算；AKV 服务系统实现
  27.7% 成本下降与 1.51x P95 延迟加速
practical_value: '- 在长程搜索/推荐 Agent 中，不要等上下文阈值触发全量 summary/trim；按消息角色和 recency 做 rolling
  drop 更划算。具体：保留所有 reasoning 与最近 N 轮 tool response 的 KV cache，丢弃更早的 tool response（如搜索结果、商品列表），可同时降低
  cost 并维持甚至提升精度。该策略已在 BCP/SWE 等 benchmark 上比 48K/96K summarization 平均成本降 21.9–27.7%，且分数更高。

  - 将 cache 操作从文本编辑中解耦：在 agent 网关中实现 stateless 接口，业务侧只需传完整 messages 和 drop/reposition
  指令，由服务端维护物理 cache 状态；这样不会破坏并发请求间的 cache 重用与隔离，也便于恢复被驱逐状态。可直接参考 AKV 的 extended radix
  tree + drop-aware eviction + segment-batch attention 设计，在内部推理服务上提供类似能力，降低 P95 延迟。

  - 把“缓存管理”作为 tool 暴露给 LLM，或在固定策略上用 recursive self-improvement 自动调参，可替代专家手工设计。对电商场景，可以让
  Agent 根据查询意图、候选商品相关性自主丢弃旧工具返回，平衡信息保留与成本；RSI 在论文中进一步比专家策略降本 7.1%。

  - 注意位置编码：长会话中即使 active token 减少，RoPE 绝对位置仍会耗尽；引入 repos 重置位置编码（旋转 key）可继续探索，不建议直接牺牲上下文信息。这一点对多轮搜索、翻页、跨页比较场景尤其重要。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM agent 处理长轨迹时，KV cache I/O 与存储成为主要成本，实验显示 KV cache reads 占 API 成本的 82.4%。传统 context engineering 通过 trim/summarize 修改历史，会破坏后续 KV cache 状态并触发 re-prefill；为控制重算成本又不得不大幅删减历史，导致 accuracy 下降。论文提出 cache engineering，直接在 active KV cache 上操作，保留文本历史不变，从而避免重算。

### 方法关键点
- 三个基础 cache 操作：append（正常添加 token KV）、drop（从未来 attention 中移除选中的 KV entries，已保留状态不变）、repos（调整 RoPE 位置编码并重置下个 token 位置）。
- 用 cache operation sequence 形式化历史：相同 token 前缀在不同操作顺序下会产生不同 KV 状态，prefix matching 不够。
- 配套 AKV serving system：提供 stateless 接口（请求带 messages + cache 操作指令），服务端内部通过 extended radix tree（加入 drop nodes 和 reposition nodes）追踪操作历史、drop-aware eviction 管理状态生命周期、segment-batch attention 在单次 prefill pass 中重建缺失状态，避免多次前向。
- 示例策略采用 tool-response rolling drop：保留所有 reasoning 和最近 12 轮 tool response 的 KV，旧 tool response 直接 drop，并在达到模型 summarization 阈值时 repos 重置位置。

### 关键结果
在 MiniMax-M2.7、GPT-OSS-120B、MiroThinker-1.7-Mini 三个 LLM 上，覆盖 BCP、GAIA-Text、SWE-Verified、xbench-DS 四个 agent benchmark。相比 conventional threshold-triggered summarization（Standard 96K/192K），平均 score 提高 1.7 分，平均 cost 降低 27.7%；相比 Text Engineering（48K），cost 降低 21.9%。AKV 相对于 Standard 在 peak throughput 设置下，P95 request latency 获得 1.51x speedup，output throughput 1.18x，input throughput 1.53x。Recursive self-improvement 进一步比专家策略降低 7.1% cost；把 cache 管理作为 tool 暴露给 LLM 也带来更高 pass rate。

> 最值得记住的一句话：直接在 KV cache 层做 drop/repos，无需改变文本轨迹或重算保留内容，就能同时提升 agent 精度并降低成本。
