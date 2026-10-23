---
title: 'Lychee: Certified Screening of Inverted Lists for High-Recall Vector Search'
title_zh: Lychee：高召回向量搜索的倒排列表认证筛选
authors:
- Dongfang Zhao
affiliations:
- University of Washington, Tacoma School of Engineering and Technology
arxiv_id: '2610.30697'
url: https://arxiv.org/abs/2610.30697
pdf_url: https://arxiv.org/pdf/2610.30697
published: '2026-10-22'
collected: '2026-10-23'
category: Other
direction: 高性能向量检索 · GPU 倒排索引
tags:
- Vector Search
- Inverted Index
- GPU
- High Recall
- Certified Screening
one_liner: Lychee 在 GPU 倒排索引上通过 certified screening 跳过大部分向量读取，实现高召回向量搜索加速
practical_value: '- 在电商/推荐的高召回向量召回场景（如风控、相似商品去重、内容安全）中，可在现有 IVF/倒排索引上增加基于 anchor 的
  certified lower bound 预筛，用 GPU tensor cores 做数值比对，避免读取全精度向量，显著降低显存带宽压力；可参考其证明框架，确保不损失召回。

  - 若业务使用 cuVS / Faiss IVF-Flat，可借鉴 Lychee 的筛选顺序：先按 bound 递增处理候选，快速排除大部分不相关向量，只对少数候选计算精确距离；尤其适合
  probe 数较大、追求 0.999+ recall 的场景，吞吐不再与 probe 数量成反比。

  - 多 GPU 扩展方案对亿级/十亿级商品 embedding 库有参考价值：通过分片和跨 GPU 合并，可在 4 卡上达到十亿向量 0.9999 recall
  的工程可行性。

  - 对使用量化/图索引但需要高召回的业务，该方法的“certified exact top-k of probed lists”特性可替代部分重排，避免全量 rerank，平衡精度与延迟。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：高召回（0.999-0.9999）向量检索在风控、人脸、医学等场景不能漏掉真实邻居；近似索引无法报告丢失的查询，倒排索引探测更多列表能提高召回，但吞吐随探测列表数反比下降，因为需要读取并全精度打分每个探测向量。图索引在高召回上饱和，量化列表仍需用全向量重排。

方法关键点：Lychee 将倒排列表探测后，在 GPU tensor cores 上用来自同列表 anchors 的 certified lower bound 进行筛选，判断绝大多数探测向量不可能进入 top k，从而不读取向量；仅对少数幸存者计算精确距离，并按 certified bound 递增顺序处理。证明返回 probed lists 的精确 top k，即 IVF 全精度搜索结果，同时每次查询只读取数百个全向量，与探测列表数无关。

关键结果：在 11 个数据集（1M 到 1B 向量）和 10 个 GPU/CPU baseline 上，在最多 100M 向量数据集、200 个探测列表等召回条件下，Lychee 比 cuVS 的 IVF-Flat 快 9.7 到 117 倍；Deep-100M 上 recall 0.9997 时快 65 倍（1000 探测列表）；达到 CAGRA 和 HNSW 无法达到的 recall；在 >10M 向量上比 certified exclusion 精确搜索快 5-18 倍；4 GPU 上十亿向量 recall 0.9999，比 IVF-Flat 快 44.5 倍。
