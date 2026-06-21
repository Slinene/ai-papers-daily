---
title: 'When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic
  Vector Retrieval Systems'
title_zh: 当全局门控即足够：各向异性向量检索中的入时枢纽控制
authors:
- Prashant Kumar Pathak
- Tarun Kumar Sharma
arxiv_id: '2606.19692'
url: https://arxiv.org/abs/2606.19692
pdf_url: https://arxiv.org/pdf/2606.19692
published: '2026-06-18'
collected: '2026-06-21'
category: RAG
direction: RAG 安全 · 入时枢纽门控
tags:
- hubness
- adversarial retrieval
- admission control
- global gating
- anisotropy
- HNSW
one_liner: 在文档入库时用全局哨兵查询门控检测并隔离枢纽向量，无需周期性全库重扫，实现高召回低误报。
practical_value: '- 向量召回系统中引入轻量级入库门控：用一组固定哨兵查询计算新物品的 kNN 倾向，若频繁出现则视作枢纽并隔离/降权，避免少数物品主导召回分布，提升多样性与防攻击能力。

  - 无需周期性全库重扫：门控阈值可增量维护，插入成本与索引大小无关，适合频繁更新的电商商品库或内容池，只在摄入时增加约 3% 延迟。

  - 简单全局门控足够：实验表明 per-topic 门控在各向异性空间中无统计显著增益，因此用单一全局阈值即可达到强防御效果，工程实现成本低。

  - 结合业务规则处理自然热品：热门商品可能是天然枢纽（如爆款），可额外利用 provenance（如商品来源、类目）做白名单或分级处置，避免误伤正常高热物品。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：向量检索中的 hubness 现象（少数点成为大量查询的最近邻）构成 RAG 下毒攻击面——注入一个文档可污染大量无关请求。现有防御依赖周期性反向 kNN 扫描，存在暴露窗口且全库重扫开销大。

**方法**：提出入时控制，在文档插入索引前用一组防御方哨兵查询对其评分，使用全局门控（global gate）判别枢纽并隔离。将新文档的最近邻哨兵占比与全局分布比较，基于分位数阈值决策。阈值通过指数滑动窗口增量维护，无需全库重扫，插入成本与语料规模无关。在 100k 文档语料、5 种编码器（MiniLM、BGE、GTE、E5 等）、攻击查询与哨兵分离的设置下评估。

**结果**：全局门控在嵌入空间攻击上达到 recall 1.0（有效工作点 ≥0.92），AUROC≈1.0，通用文档误报率约 1%；对 HotFlip 梯度攻击平均 recall 0.91±0.07。与周期性反向 kNN 检测器匹配且优于仅靠 provenance 的基线。per-topic 门控无显著增益，因各向异性空间里局部与全局可见性正相关。在 HNSW 近似索引上摄入延迟增加约 3.1%，检索评分在 10^6 向量以内保持平坦，仅 1.2% 决策翻转且无不涉及攻击。自然枢纽可通过 provenance 补充处理。
