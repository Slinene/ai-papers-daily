---
title: 'AtomRec: Evolving Atomic Memory for Agentic Recommendation'
title_zh: 原子化演化记忆驱动的智能体推荐系统
authors:
- Peiyu Hu
- Weihai Lu
- Siying Gu
- Zhuodong Liu
- Zhaokai Luo
- Yuean Niu
- Zhiyong Wang
- Jia Wang
affiliations:
- Xi'an Jiaotong-Liverpool University
- Xiaohongshu
- Peking University
- East China Normal University
- Beijing Jiaotong University
arxiv_id: '2609.04882'
url: https://arxiv.org/abs/2609.04882
pdf_url: https://arxiv.org/pdf/2609.04882
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agentic 推荐中的记忆演化与证据检索
tags:
- Agent Memory
- LLM
- Recommender Systems
- Collaborative Filtering
- Memory Evolution
- Evidence Retrieval
one_liner: 用结构化原子记忆与语义链接替代粗粒度摘要，实现可解释证据路径检索的 agentic 推荐
practical_value: '- 将用户记忆拆成结构化原子单元（content/keywords/tags/context/embedding/links），而不是单一长摘要。电商场景可对用户兴趣建立粒度更细的原子标签（如品类+价格带+风格+最近意图），方便选择性更新和检索，避免新行为覆盖旧偏好。

  - 用 LLM 对近邻记忆做语义关系建模（如偏好转移、互补、跨域迁移），构建可解释的协作链接，而不仅是 embedding 相似度。推荐召回或重排时，可沿链路检索多跳证据路径，提升排序可解释性和准确性。

  - 记忆演化采用字段级更新，保留原始时间戳，用相似度阈值控制演化保守度（论文选 τ_evo=0.7）。此做法可异步离线执行，线上只做检索与重排，控制时延；对偏好漂移较大的用户增益更明显，适合电商中兴趣变化快的场景。

  - 成本上，原子构建、链接、演化可缓存和批量处理，线上额外开销有限（每千次交互成本约 $2.95，略高于 MemRec 的 $2.65）。实际部署可用更轻量的模型做记忆代理，平衡成本与效果。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有 LLM 驱动的推荐智能体通常把用户/物品信息压缩成粗粒度摘要，并用标量协作边连接，导致细粒度偏好阶段丢失，检索时只能得到孤立邻居摘要，缺乏可解释的证据路径。用户偏好是多个随时间演化的痕迹（如稳定兴趣、近期意图、属性偏好），需要更细粒度且可重组的记忆表示。

**方法关键点**
- **原子协作记忆构建**：将用户和物品记忆表示为结构化原子笔记，字段包括内容、时间戳、关键词、语义标签、上下文描述、稠密嵌入和链接 ID。多字段互补视角使记忆可检索、可解释、可选择性修订。
- **语义协作链接构建**：对每个新记忆，用 embedding 相似度检索 top-k 近邻，再由 LLM 分析语义关系（共享话题、偏好转移、意图演进等），生成具有关系描述的可解释链接，而非数值边权重。
- **动态记忆演化**：新交互触发对相关历史记忆的字段级更新（相似度 > τ_evo 或已在链接内），保留原始时间戳，仅修改关键词、标签、上下文和链接，使记忆图随行为变化重组。
- **上下文感知协作检索**：推荐时先根据当前指令和近期交互检索种子记忆，再沿语义链接扩展 1-2 跳得到子图，LLM 综合提取证据路径，最后基于用户记忆、协作证据和候选物品记忆进行排序。

**关键结果**
在 Amazon Books、Goodreads、MovieTV、Yelp 四个指令增强基准上，ATOMREC 全面超越传统、LLM 和记忆增强基线，相比最强基线平均相对提升约 8.5%。在 Books 上 H@3 达到 0.7462，比 MemRec 提升 9.96%。消融显示移除原子记忆、语义链接、演化或链接检索均导致性能下降。偏好漂移分析中，高漂移用户相对增益达 +13.9%，验证了演化记忆对兴趣变化的适应性。

**最值得记住的一句话**：让推荐记忆可重组，而不是仅仅更详细。
