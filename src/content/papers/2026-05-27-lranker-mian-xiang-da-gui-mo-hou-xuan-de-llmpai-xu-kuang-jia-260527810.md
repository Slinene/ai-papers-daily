---
title: 'LRanker: LLM Ranker for Massive Candidates'
title_zh: LRanker：面向大规模候选的LLM排序框架
authors:
- Tao Feng
- Zijie Lei
- Zhigang Hua
- Yan Xie
- Shuang Yang
- Ge Liu
- Jiaxuan You
affiliations:
- University of Illinois Urbana-Champaign
- Meta Monetization AI
arxiv_id: '2605.27810'
url: https://arxiv.org/abs/2605.27810
pdf_url: https://arxiv.org/pdf/2605.27810
published: '2026-05-27'
collected: '2026-05-28'
category: RecSys
direction: LLM驱动的超大规模候选排序
tags:
- LLM Ranker
- K-means Clustering
- Test-time Scaling
- Embedding-based Ranking
- LoRA
one_liner: 通过聚合候选全局信息和多嵌入集成，使LLM排序扩展到百万级候选并大幅提升效果
practical_value: '- **全局候选信息注入**：利用K-means对候选嵌入聚类，将质心通过可学习投影器注入LLM作为软提示，使查询表示条件于全局候选分布，适合电商/推荐中候选集巨大的场景，可提升粗排/精排的相关性。

  - **图测试时缩放**：在推理时迭代分区候选集、保留高分段、重新计算查询嵌入并平均集成，以多视角增强排序鲁棒性；该方法轻量、可插拔，能与现有嵌入排序模型结合，用于线上打分增强。

  - **训练鲁棒性强化**：训练时随机分区采样不同候选子集计算损失，使查询表示对不同候选规模不敏感，适合动态候选池或A/B测试环境。

  - **LoRA高效微调**：只对注意力层和FFN添加低秩适配，保持LLM基础能力的同时快速适应排序任务，便于在已有基座模型上构建推荐/搜索排序器。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有LLM排序受限于上下文长度和计算成本，无法处理百万级候选的真实场景，且多忽略全局候选信息。需要一种能显式建模全局候选分布且支持大规模推理的框架。

**方法关键点**：
- **候选聚合编码器**：离线对候选嵌入做K-means聚类，将质心通过MLP投影器注入LLM prompt的占位符，作为全局候选信息软提示。
- **LLM解码器**：基于融合提示生成查询嵌入（平均所有query token和<eos>的隐藏状态），候选嵌入同理，内积计算相关性分数。
- **图测试时缩放**：推理时迭代式分区候选集，每轮用当前查询嵌入保留top项，为各分区重新计算查询嵌入并平均更新，最后集成所有轮次的得分排序，提升鲁棒性。
- **训练技巧**：随机分区采样不同候选子集计算InfoNCE损失，使查询表示对不同候选规模鲁棒；使用LoRA微调LLM（仅更新注意力和FFN的低秩适配层）。

**关键结果**：
- RBench-Small（推荐/路由，候选20）：相对提升超30%（Rec-Music 37%，Routing-Balance 31%）。
- RBench-Large（推荐/检索，候选数千～数万）：MRR提升3–9%，在ESCI商品搜索上提升9%+。
- RBench-Ultra（服装推荐，候选680万）：相对提升20–30%。
- 消融：移除全局信息、测试时集成或LoRA训练均导致性能下降，验证各组件的必要性。
