---
title: 'Beyond Parallel Sampling: Diverse Query Initialization for Agentic Search'
title_zh: 超越并行采样：智能搜索代理的多样化查询初始化
authors:
- Sidhaarth Murali
- João Coelho
- Jingjie Ning
- João Magalhães
- Bruno Martins
- Chenyan Xiong
affiliations:
- Carnegie Mellon University
- Instituto Superior Técnico
- INESC-ID
- NOVA LINCS
- NOVA School of Science and Technology
arxiv_id: '2606.17209'
url: https://arxiv.org/abs/2606.17209
pdf_url: https://arxiv.org/pdf/2606.17209
published: '2026-06-15'
collected: '2026-06-17'
category: Agent
direction: Agent 搜索 · 查询多样化
tags:
- agentic search
- parallel sampling
- query diversity
- test-time scaling
- MMR
- multi-hop QA
one_liner: 提出训练无关的首轮查询多样化方法 DivInit，通过 MMR 从生成池中选择多样性查询，解决并行搜索代理的锚定坍缩问题。
practical_value: '- 在 Agent 搜索或对话式购物助手中，首轮生成的查询多样性对后续检索路径影响巨大；可将多路独立生成改为单次生成候选池 +
  MMR 选择，避免锚定坍缩，提升并行采样的有效性。

  - 方法无需训练、即插即用，只需修改推理时的首轮查询生成逻辑，且总 LLM 调用次数从 kT 降至 1+k(T-1)，在中小模型上可降低延迟和成本。

  - 消融表明首轮多样性已足够维持轨迹分离，后续轮次无需额外干预，简化工程实现。

  - 对于电商搜索中的 Agent 多轮交互，可主动设计首轮查询覆盖不同维度（品牌、价格、功能等），提高最终找到满意商品或信息的概率。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
agent 搜索中通过并行采样扩大推理宽度（breadth scaling）时，往往出现收益递减。本文发现，多个并行轨迹的首轮查询常常高度相似，导致检索到的文档高度重叠，后续推理锚定在同一条路径上，形成**锚定坍缩（anchor collapse）**。这种冗余浪费了计算资源，限制了并行采样的上限。因此，需要一种机制在轨迹开始时就保证查询的多样性，让不同轨迹探索不同的检索空间。

## 方法关键点
- **DivInit**：训练无关的干预，仅在首轮做一次查询多样性选择。
- 首轮用一个 LLM 调用以高温度生成 n > k 个候选查询（n=16, k=4）；
- 使用最大边际相关性（MMR）从候选池中选出多样性最大的 k 个查询，MMR 仅基于查询间的 Jaccard 距离（λ=0），不额外偏向原问题相似度；
- 后续轨迹完全沿用原 Agent 搜索循环，不改动。
- 计算量：将 k 次首轮 LLM 调用合并为一次，总调用从 kT 降至 1 + k(T−1)。

## 关键结果
在 5 个开源模型（Qwen3-1.7B/4B/8B, Gemma3-4B/12B）和 8 个基准（多跳 QA: HotpotQA, MuSiQue, 2Wiki, Bamboogle, FRAMES；开放 web 推理: GAIA, HLE, WebWalker）上，DivInit 在匹配计算量下**一致优于标准并行采样**：
- 多跳 QA 平均提升 5–7 个 pass@4 百分点；
- 增益随模型规模增大而上升，1.7B 模型仅 2.8 点提升，8B 达 7.4 点，表明有小模型容量门槛；
- 提高采样温度不能替代显式多样性选择，DivInit 在 τ=1.0 已超过标准采样的最佳温度配置；
- 消融：将多样性选择延伸到后续轮次几乎没有额外收益，首轮锚定效应是关键；
- 使用 AggAgent 聚合后，pass@1 同样提升，说明多样性增益可传递到最终单答案精度。

**核心启示**：首轮查询是 agent 搜索轨迹的锚点，主动引入多样性可有效防止轨迹坍缩，且实现简单、无需训练。
