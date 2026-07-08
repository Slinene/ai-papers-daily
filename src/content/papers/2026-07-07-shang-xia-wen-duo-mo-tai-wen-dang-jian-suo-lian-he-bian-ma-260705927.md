---
title: 'CMDR: Contextual Multimodal Document Retrieval'
title_zh: 上下文多模态文档检索：联合编码+对比学习
authors:
- Ryota Tanaka
- Taku Hasegawa
- Kyosuke Nishida
affiliations:
- NTT Human Informatics Laboratories, NTT, Inc., Tokyo, Japan
arxiv_id: '2607.05927'
url: https://arxiv.org/abs/2607.05927
pdf_url: https://arxiv.org/pdf/2607.05927
published: '2026-07-07'
collected: '2026-07-08'
category: Multimodal
direction: 多模态检索 · 上下文文档嵌入
tags:
- Multimodal Retrieval
- Document Context
- Contrastive Learning
- Embedding
- RAG
one_liner: 提出首个要求跨页上下文建模的多模态文档检索基准与嵌入框架CMDR-Embed，结合CMCL对比学习显著提升跨页查询性能
practical_value: '- **商品详情页跨图检索**：可借鉴联合编码多页/多图的上下文嵌入思路，处理商品描述分布在多张细节图或PDF说明书中的场景，提升需要综合多图信息的查询召回率。

  - **多模态对比学习训练 trick**：CMCL平衡上下文建模与页面区分性的损失设计，可直接用于训练电商多模态检索模型，尤其适合“店铺主页多图组合匹配用户风格查询”等任务。

  - **RAG 中的多模态文档检索增强**：在电商客服或搜索总结系统里，用CMDR-Embed替换现有文档嵌入，能让检索到的页面片段保留更完整的上下文，提高生成答案的事实一致性。

  - **构建检索基准的方法论**：可参照CMDR-Bench设计面向业务的跨页/跨图上下文检索评测集，衡量排序模型对“浏览型查询”（如“适合搭配这个包的上衣”）的上下文理解能力。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有多模态文档检索基准仅评测简单字面或语义匹配，方法独立编码单页，无法处理需要跨页信息聚合的查询（例如“比较第3页和第7页的数据”），缺失对文档上下文的建模。为此，论文提出新的任务CMDR和基准CMDR-Bench，强制要求利用文档级别的上下文信息。

**方法关键点**：提出CMDR-Embed框架——将多页作为序列联合输入Transformer编码器，显式捕获跨页上下文，再从共享上下文表示中提取每个页面的嵌入向量；而非传统方案独立编码各页。训练采用CMCL（上下文多模态对比学习）损失，在正负样本对中平衡页面级判别能力和上下文建模能力，使嵌入既保留全局上下文又区分不同页面。

**结果**：在CMDR-Bench上，CMDR-Embed显著优于所有非上下文嵌入基线，证明了上下文感知多模态嵌入对提升文档检索效果的关键价值。
