---
title: 'Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning'
title_zh: 随机注意力：重新思考 KV 缓存淘汰以实现高效推理
authors:
- Heng Wang
- Jielin Qiu
- Wenting Zhao
- Cheng Qian
- Liangwei Yang
- Jiawei Han
- Heng Ji
- Silvio Savarese
- Shelby Heinecke
- Huan Wang
affiliations:
- Salesforce AI Research
- University of Illinois Urbana-Champaign
arxiv_id: '2609.03430'
url: https://arxiv.org/abs/2609.03430
pdf_url: https://arxiv.org/pdf/2609.03430
published: '2026-09-02'
collected: '2026-09-04'
category: LLM
direction: LLM 推理效率 · KV 缓存随机淘汰
tags:
- KV cache
- eviction
- random attention
- efficient inference
- LLM
- reasoning
one_liner: 提出 Random Attention，保留 prompt 并在各注意力头内随机淘汰 KV 缓存，匹配最强选择器同时吞吐提升 32-43%
practical_value: '- 在部署长上下文 LLM 服务（如电商 Agent 的多轮对话或长链推理）时，可将 KV cache 淘汰策略简化为“保留 prompt
  + 每头随机淘汰”，省去 token 重要性打分，降低额外计算和延迟，实现 32-43% 的推理吞吐提升。

  - 显式保护 prompt 是稳定性的关键：随机淘汰由于天然保留 prompt 而表现出与复杂选择器相当的性能，提示我们在设计缓存管理策略时应优先确保 prompt
  完整，而非依赖复杂重要性估计。

  - 推理轨迹在文本和注意力头两个层面存在冗余，因此随机抽样足以保留必要信息，这对长 CoT 生成场景尤其有借鉴：可放宽对精确 token 选择的假设，采用更轻量的随机策略。

  - 可作为强 baseline：在电商搜索推荐系统的 LLM 模块中，如果采用 KV 压缩，先测试随机淘汰，它实现简单、无需训练或计算分数，且能匹配最优方法。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：推理模型的长链思维（chain-of-thought）使 KV cache 成为严重内存瓶颈。现有 KV cache 压缩方法均遵循同一范式：对每个 token 打分，保留高分 token。

**方法关键点**：Random Attention 认为选择信号几乎无用，直接保留 prompt，并在每个注意力头内独立地均匀随机淘汰其他 token，完全无需计算任何分数。

**关键结果**：在四个模型（Qwen3-4B, Phi-4, Qwen3-14B, Qwen3-32B）和六个推理任务上，Random Attention 与最强先验淘汰器 TriAttention 匹配，同时在 vLLM 部署中吞吐提升 32-43%。控制实验揭示：1) prompt 是缓存中最脆弱的部分，选择器之间的大部分差距仅源于是否碰巧保留了 prompt；2) 推理轨迹通过两个层面冗余自我保护：文本层面模型会重述所需信息，跨注意力头层面各头保留自己的拷贝。因此一旦 prompt 安全，随机抽样足以保留足够副本，无需打分挑选。代码已开源。
