---
title: 'MICE to Meet You: From Re-ranking Only to End-to-End Retrieval'
title_zh: MICE 与你相见：从仅重排到端到端检索
authors:
- Victor Morand
- Yuxuan Zong
- Mathias Vast
- Josiane Mothe
- Benjamin Piwowarski
affiliations:
- Sorbonne Université
- CNRS
- ISIR
- Sinequa by ChapsVision
- Univ. Toulouse
arxiv_id: '2610.31932'
url: https://arxiv.org/abs/2610.31932
pdf_url: https://arxiv.org/pdf/2610.31932
published: '2026-10-22'
collected: '2026-10-26'
category: Other
direction: 神经检索 · 端到端 Late-interaction
tags:
- Neural Retrieval
- Late Interaction
- PLAID
- Cross-Encoder
- MICE
- Efficiency-Effectiveness
one_liner: 首个基于 MICE 的端到端检索管线 MICE-P，用 PLAID 索引文档 token 表示，在保持 cross-encoder 效果的同时达到
  late-interaction 吞吐量
practical_value: '- 在商品/广告搜索中，可参照 MICE-P 将昂贵的 cross-encoder 级重排模型改造为端到端召回：离线预计算文档/商品侧上下文
  token 表示并用 PLAID 类索引存储，线上仅做轻量 token 交互，保持效果同时大幅降低计算开销。

  - 借鉴 Ettin Family 的公平对比框架：在自己的模型评测中，确保不同架构训练数据、优化器、步数等保持一致，避免因训练配置差异导致结论不可靠。

  - 若已有重排模型表现优异但推理慢，可探索为其增加文档侧预计算与索引模块，转化为召回或第一阶段检索，减少多级 pipeline 的延迟。

  - MICE-P 证明存在一种新的效率-效果权衡区间：在部分场景下，不必牺牲 cross-encoder 精度即可获得接近 late-interaction 的吞吐，适用于对精度敏感且有一定计算预算的电商搜索/推荐入口。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：神经检索中，late-interaction 模型（如 ColBERT）通过预计算文档 token 表示实现高效索引和检索，但交互机制（MaxSim）相对简单，效果弱于 cross-encoder；cross-encoder 效果好但推理成本高。MICE 作为重排架构尝试结合两者优势，但缺少文档表示存储方案。

**方法关键点**：提出 MICE-P，首个基于 MICE 的端到端检索管线。利用 PLAID 索引 MICE 的上下文文档 token 表示，支持候选生成与检索，使 MICE 从仅重排扩展到端到端。通过在 Ettin Family 下训练可比模型进行受控对比，确保公平性。

**关键结果**：MICE-P 形成一类新的检索架构，其效率-效果权衡独特：在保持 cross-encoder 级别效果的同时，吞吐量达到 late-interaction 检索模型水平。
