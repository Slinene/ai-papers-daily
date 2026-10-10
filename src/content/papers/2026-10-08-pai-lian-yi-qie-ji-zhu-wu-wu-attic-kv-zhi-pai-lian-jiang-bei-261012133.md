---
title: 'Rehearse Everything, Remember Nothing: Attic-KV Rehearses What Will Be Read'
title_zh: 排练一切，记住无物：Attic-KV 只排练将被读取的内容
authors:
- Zhiyun Shi
affiliations:
- Nanyang Technological University
arxiv_id: '2610.12133'
url: https://arxiv.org/abs/2610.12133
pdf_url: https://arxiv.org/pdf/2610.12133
published: '2026-10-08'
collected: '2026-10-10'
category: LLM
direction: LLM 长上下文 KV 缓存压缩
tags:
- KV cache
- query-agnostic compression
- long-context LLM
- self-generated QA
- RAG
- serving
one_liner: 提出训练无关的 Attic-KV 排练策略，以自生成 QA 与内容自适应锚点取代全文重读，大幅提升极限压缩下的长上下文问答与缓存复用
practical_value: '- 电商商品详情、文档库做预计算 KV 缓存时，可用 LLM 对每个商品/文档生成“读者可能问的问题+原文引用答案”作为 rehearsal，再做
  3-5% 预算的 KV 淘汰；比全文重读更能保住属性、价格、政策等答案片段，且 5% keep ratio 可把缓存容量放大 20 倍。

  - 选择 rehearsal 长度不要固定比例，按内容稠密自适应：锚点数量=目标 keep ratio，再扩展到包含锚点的句子长度；商品参数表、FAQ、规格列表会被排练更多，营销
  prose 少排练，避免预算浪费。

  - 可直接替换现有 KVzip/KVgrad/RestoreKV 的 rehearsal，不改变 scoring、不重训；适合已有推理加速链路的团队，先用 KV2+Attic
  低成本验证，再决定是否引入 restore tokens。

  - 自生成 QA 放在离线/一次性路径，每个商品或文档只生成 6 个 Q&A（≤256 tokens），压缩耗时反而低于全文重读；适合大规模语料缓存、RAG 文档库与
  Agent 长对话记忆。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：许多 KV cache 需在前置未知 query 时一次性压缩，服务于 RAG 文档缓存、共享前缀和长对话记忆；只有 3-5% 的极限 keep ratio 才能显著放大缓存容量。现有 rehearsal scoring 主流重读整个上下文，但在紧预算下注意力撒在流畅 prose 上，答案所需 token 存活率仅略高于随机，导致得分崩坏。

**方法关键点**：Attic-KV 训练无关，只改 rehearsal，不改 scorer：
- 原则一：排练将被读取的内容。让模型自生成 6 个读者可能问的问题，并用原文引用作答，拼成 QA rehearsal。
- 原则二：排练尽可能多。以 KeyDiff 选锚点，锚点数量=keep ratio；再扩展到包含锚点的句子 token 数，使表格/事实密集块排练更多。
- 与 KV2、KVgrad、RestoreKV+ 直接组合，score 取 anchor rehearsal 与 QA rehearsal 的 max；支持原生 KV 或 restore tokens。

**关键结果**：Qwen3-8B RULER-4K 3% 预算：Attic 73.4 vs KVzip+ 31.5，差 41.9；5% 时 82.1 vs KV2 76.8、KVzip+ 58.6（无压缩 96.5）。Attic 在 RULER 与 LongBench 自然文本共 8 个 setting 中均为最好训练无关方法；插件到 KVgrad 最高 +17.1，RestoreKV+ 最高 +28.1。压缩一次回答多问的 LooGLE 上 RestoreKV+ +Attic 双指标最好，压缩耗时 126s vs KVzip+ 154.8s。

**最值得记住**：缓存保留它排练过的东西，所以压缩预算应投放给未来会被读出的答案片段，而不是全文。
