---
title: 'ACCT: Asymmetric Cross-LLM Context Transfer'
title_zh: 非对称跨 LLM 上下文迁移：KV 缓存跨模型复用
authors:
- Yuzhe Liu
- Haolin Tian
- Tonghan Wang
affiliations:
- Tsinghua University, Beijing, China
arxiv_id: '2610.42116'
url: https://arxiv.org/abs/2610.42116
pdf_url: https://arxiv.org/pdf/2610.42116
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: LLM 异构部署 · KV cache 跨模型迁移
tags:
- KV cache
- cross-model transfer
- sparse attention
- LLM serving
- context prefill
one_liner: 提出 ACCT，将源模型 KV 稀疏转换为目标模型可直接消费的状态，削减 75% KV 仍匹配原性能
practical_value: '- 在电商多模型/Agent 路由中，可以把共享长上下文（会话历史、商品详情、检索文档）先由低成本源模型做 prefill，再由同
  family 的大目标模型复用其 KV，省掉重复 prefill，适合动态路由频繁切换模型的在线服务。

  - 借鉴 Cartographer 的 query-relevant 稀疏化：对每层每个 KV head 分别选择与当前 query 相关的 context token，比全局
  Top-K 更精细；推荐系统里长用户行为序列或多模态商品上下文也可以按 query/候选 item 做非对称稀疏化，而不是固定截断。

  - Allocator 的“全局 KV 预算下逐层/逐 head 分配”思路可用于模型服务：给深层/浅层或不同 attention head 分配不同的缓存 token
  数，在 latency/cost 约束下最大化长上下文任务效果。

  - 工程实现上，Compiler 把不同 hidden size 的源 KV 映射到目标模型，意味着上下文计算与最终推理可解耦，适合 Agent 系统里同一上下文被多个异构模型消费的架构，能简化上下文缓存服务。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：真实 LLM 系统从单模型走向异构多模型动态路由，同一上下文在不同目标模型间被重复 prefill，带来显著计算开销。

**方法**：ACCT 面向同模型族不同规模模型，把源模型产生的 KV cache 转换为目标模型可直接消费的稀疏 KV。三个轻量组件：Cartographer 按目标层和 KV head 识别与 query 相关的 context token；Allocator 在全局 KV 预算下决定每个 target layer/head 保留多少 token；Compiler 将选中的源 KV 映射成目标稀疏 KV。目标模型无需重新处理原始 context。

**结果**：在 5 个通用能力 benchmark 和 6 个强上下文依赖任务上，KV cache 减少 75% 时，ACCT 性能达到或超过目标模型原始推理；约 19K token 上下文下，KV 转换比目标 prefill 快 6.5–21.2×。
