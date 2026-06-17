---
title: 'On the Memorization Behavior of LLMs in Generative Recommendation: Observations,
  Implications, and Training Strategies'
title_zh: LLM 在生成式推荐中的一跳记忆行为分析与缓解策略 IIRG
authors:
- Sunwoo Kim
- Sunkyung Lee
- Clark Mingxuan Ju
- Donald Loveland
- Bhuvesh Kumar
- Kijung Shin
- Neil Shah
- Liam Collins
affiliations:
- KAIST
- Sungkyunkwan University
- Snap Inc.
arxiv_id: '2606.17276'
url: https://arxiv.org/abs/2606.17276
pdf_url: https://arxiv.org/pdf/2606.17276
published: '2026-06-15'
collected: '2026-06-17'
category: GenRec
direction: 生成式推荐 · 记忆行为与训练策略
tags:
- LLM Memorization
- Generative Recommendation
- One-hop Memorization
- Item-Item Relations
- Auxiliary Training
- Semantic ID
one_liner: 发现 LLM 生成式推荐强依赖一跳记忆，性能增益集中于此类用户，提出 IIRG 利用协同与语义邻居生成任务促进物品关系学习，显著提升非记忆受益用户表现
practical_value: '- **诊断一跳记忆倾向**：在生成式推荐模型评估中，可计算 top-K 推荐中来自训练集一跳转移邻居的比例，识别模型是否过度依赖表面模式，尤其对于
  LLM-based 模型。

  - **构造协同邻居与语义邻居作为辅助任务**：对于电商或内容推荐，可以基于多跳共现（时间窗口内的 co-purchase）构建协同邻居，基于文本嵌入相似度构建语义邻居，作为
  LLM 微调时的额外生成目标，显式注入物品关系知识。

  - **区分用户群体进行收益分析**：按测试目标物品是否在一跳候选集中，划分“记忆受益用户”与“非记忆受益用户”，分别观察指标，驱动粗排/精排策略差异化设计。

  - **适用于多种 ID 形式**：IIRG 同时兼容 TID 和 SID，可在现有 Semantic ID 或 Term ID 的生成式推荐框架上直接叠加，无需改变
  ID 生成 pipeline，工程改造成本低。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 被广泛用于生成式推荐，预期利用预训练知识提升泛化。但 LLM 天然存在记忆倾向，可能导致模型过度依赖训练集中简单的一跳转移（用户序列中连续出现过的物品对），而非学习深层物品关系。本文首次量化了这一现象：与非 LLM 模型 TIGER 相比，LLM 推荐中来自一跳记忆的比例显著更高；且 LLM 相对于 TIGER 的 Recall 提升几乎全部来自测试目标存在于一跳候选集的用户（记忆受益用户），对剩余用户增益甚微。

**方法关键点**：
- **一跳记忆度量**：对每个用户构建一跳候选集（训练集中所有输入物品的直接后继，取 top-50 最频繁），计算模型 top-5 推荐落入该集合的比例。
- **用户分组**：按目标物品是否在一跳候选集中，分为记忆受益/非受益两组，观察性能增益分布。
- **IIRG（Item-Item Relation Generation）训练策略**：在标准 next-item prediction 基础上，增加两个辅助生成任务——对于每个物品，生成其协同邻居（基于多跳共现频率，窗口长度 W）和语义邻居（基于文本嵌入余弦相似度 top-N）。损失函数联合优化 next-item 预测、协同邻居生成、语义邻居生成三项。
- **ID 无关性**：支持 SID 和 TID，仅利用物品文本描述构建邻居，不依赖特定 ID 结构。

**关键结果**：
- 在 Amazon Sports/Toys/Beauty 三个数据集上，IIRG 相比纯 next-item 预测的 LLM（Naive）Recall@5 平均提升 21%。
- 对非记忆受益用户，IIRG 带来约 40% 的 Recall@5 相对提升（vs. 记忆受益用户约 16% 提升），成功缓解记忆偏见。
- 与 17 个基线（包括 P5, ReAT, LC-Rec, PLUM, GRLM 等）相比，IIRG 在所有数据集上取得最优。
- 消融实验证实协同邻居与语义邻居两类任务缺一不可，随机邻居替代方案效果显著下降。

**核心洞察**：LLM 生成式推荐并非真正“理解”物品关系，而是严重复用训练序列中的简单转移模式；通过显式建模多跳共现和语义相似性，可以引导模型学习更有价值的推荐信号。
