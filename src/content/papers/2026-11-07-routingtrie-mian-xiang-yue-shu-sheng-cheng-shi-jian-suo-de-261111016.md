---
title: 'RoutingTrie: Metadata Routing for Constrained Generative Retrieval'
title_zh: RoutingTrie：面向约束生成式检索的元数据路由
authors:
- Darshan Fofadiya
- Yang Liu
- Shuying Sun
- Kyumin Park
- Juhana Kangaspunta
affiliations:
- Shopify
arxiv_id: '2611.11016'
url: https://arxiv.org/abs/2611.11016
pdf_url: https://arxiv.org/pdf/2611.11016
published: '2026-11-07'
collected: '2026-11-10'
category: GenRec
direction: 生成式推荐 · 元数据约束解码
tags:
- Generative Retrieval
- Semantic ID
- Metadata Filtering
- Beam Search
- Trie
- Efficient Inference
one_liner: 在生成式检索的 SID 解码中前置元数据约束，用 Dense Bitset 和 Sparse List 索引对候选边做 mask，避免 beam
  容量浪费在后过滤候选上
practical_value: '- **把 metadata 约束前置到 trie-constrained beam search 的 mask 生成**：生成式推荐/检索上线时，不要把过滤放在候选项解析之后。按
  SID 前缀边计算 eligible mask，在 beam selection 前过滤，能显著提升命中率（本文 Hit@100 提升 28.6pp）。

  - **按字段基数与值密度选择索引**：低基数高密度字段（如国家、库存状态）用 Dense Bitset，利用 distinct row 去重和 O(1) 位测试；高基数稀疏字段（如
  shop_id 几百万）用 Sparse List，只存实际值并二分查找。可直接套用文中的内存选择公式快速决策。

  - **GPU 上把 probe + Boolean mask 合并为单个 Triton kernel**：本实验表明 GPU probe 延迟对 beam width
  从 8 到 256 只增加 3%~7%，远低于 CPU。将 metadata 检查与 mask 生成融合，减少 kernel launch overhead，适合低延迟线上服务。

  - **低基数 bitset 可原位 patch，适合频繁更新的业务字段**：在 ShopTrie 中更新 0.01% 叶子元数据，紧凑字段耗时约 0.08~0.09s，而高基数
  Sparse List 要 6~19s。库存状态、可售国家等变化频繁的字段优先用 Dense Bitset，高基数稀疏字段考虑批量更新或增量结构。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生产级生成式检索（GR）必须同时满足相关性和 metadata 约束（如国家、店铺、库存）。传统做法是先完整生成 SID 再后过滤：被丢弃的候选浪费了模型计算和有限 beam 容量，甚至可能因 beam 被无效前缀占满而漏掉 eligible item。

**方法关键点**
RoutingTrie 在同一棵 SID trie 上为每个 metadata field 建独立索引，解码时对当前 beam 前缀的所有候选 child edge 做 probe，合并成 mask 后再进行 beam selection。
- **Dense Bitset**：面向低基数高密度字段，将每个 edge 可达的值集合存成 bitset，并通过 distinct row 去重；probe 只需两次数组访问和一次位测试，O(1)。
- **Sparse List**：面向高基数低密度字段，采用 CSR 风格 offset + value array，每个 edge 只存实际出现的值并排序，probe 用 lower_bound 二分查找，O(log s)。
- 给出内存成本选择公式：当 `I > 2(D/E)⌈M/64⌉ − 1 − 2/E` 时 Dense Bitset 更省，否则 Sparse List 更优；row sharing（D/E）越低，Dense Bitset 越有优势。
- 支持 AND/OR/NOT 布尔请求，但 mask 只是路由优化，最终仍需对 resolved item 做原始谓词检查。

**关键结果**
ShopTrie 合成 benchmark 包含 338M trie edges、8 个字段，基数从 2 到约 190 万。共享 trie + 所有 metadata 索引总 resident memory 为 10.91 GiB。GPU 上八个字段的总 probe latency 均值仅 0.075~0.087 ms，显著低于 CPU。生产重放（23,167 个历史购买 session，14B 模型，beam width 100）中，RoutingTrie 将 item-level Hit@100 从 67.5% 提升到 96.1%（+28.6pp），而请求中位延迟仅增加 1.1ms（27.1→28.2ms）。低基数 bitset 字段支持原位快速更新，0.01% 叶子变更耗时约 0.08s，而高基数 Sparse List 要 6~19s。

**最值得记住的一句话**
把 metadata mask 融入 trie-constrained beam search 的前向过程，才能让生成式检索的 beam 容量真正服务于 eligible items，而不是被后过滤的候选白白消耗。
