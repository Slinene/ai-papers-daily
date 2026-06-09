---
title: 'Popcorn: A Configurable Benchmark for Visual Evidence in Multimodal Movie
  Recommendation'
title_zh: Popcorn：多模态电影推荐中视觉证据的可配置基准
authors:
- Ali Tourani
- Fatemeh Nazary
- Yashar Deldjoo
- Tommaso Di Noia
arxiv_id: '2606.09595'
url: https://arxiv.org/abs/2606.09595
pdf_url: https://arxiv.org/pdf/2606.09595
published: '2026-06-08'
collected: '2026-06-09'
category: RecSys
direction: 多模态推荐 · 视觉证据基准
tags:
- multimodal
- recommendation benchmark
- visual evidence
- vision-language model
- movie recommendation
one_liner: 构建可配置基准，系统比较电影推荐中预告片、全片和海报三种视觉源的效果差异
practical_value: '- **商品视觉源选择与评估**：在电商推荐中，商品主图、视频、直播切片等视觉源同样存在语义差异与成本权衡，可借鉴Popcorn的模态装配与融合配置思路，系统对比不同视觉源对排序、覆盖度和多样性的影响，避免盲目替换。

  - **利用VLM编码缩略图作为可扩展item特征**：实验表明，基于缩略图的VLM特征在保持强推荐效果的同时具备极高可扩展性，适合大规模商品库；可直接将商品主图/广告图经VLM编码为item
  embedding，作为冷启动或富媒体特征。

  - **融合策略与源不可互换的结论**：推荐中预告片和全片效果不可简单替代，融合策略（如late fusion vs. side information）会明显改变指标；业务中多视觉源融合时需实验验证最优组合，而非假定等价。

  - **LLM增强元数据与基准设计**：Popcorn将LLM生成的增强文本纳入统一配置，类似地为电商物品用LLM补充描述可提升内容信号；其“配置合约”统一拆分、评估的工程化思路可复用到内部推荐评测框架。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：电影是多模态作品，但现有推荐基准常依赖预告片、海报或元数据，忽略全片层面的消费级视觉证据。不同视觉源（全片、预告片、缩略图）在语义完整性、可获取性和计算成本上存在根本差异，缺乏系统比较基准。
**方法**：提出Popcorn基准，首次将全片和预告片的帧级嵌入（经由现代视觉模型编码）与MovieLens关联的缩略图特征对齐，并使用视觉语言模型（VLM）对缩略图进行深度编码。Popcorn通过单一配置合约统一模态装配、融合、数据划分、评估协议及LLM增强的文本元数据，确保公平对比。
**关键结论**：实验显示，利用VLM编码的缩略图特征能提供强且高度可扩展的item侧信号，在大规模场景下表现优异；而预告片与全片的对比表明视觉源不可随意互换——源选择和融合策略显著影响排序精度、覆盖度、多样性和校准度，其中校准度的差异尤为突出。基准框架已开源。
