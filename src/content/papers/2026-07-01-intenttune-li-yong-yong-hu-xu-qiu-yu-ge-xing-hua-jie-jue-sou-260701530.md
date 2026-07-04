---
title: 'IntentTune: Using user demand and personalization to resolve "unknown" query
  intents for e-commerce search'
title_zh: IntentTune：利用用户需求与个性化解决电商搜索中模糊查询意图未知问题
authors:
- Rachith Aiyappa
- Ishita Khan
- Chester Palen-Michel
- Jayanth Yetukuri
- Samarth Agrawal
- Mehran Elyasi
- Shuang Zhou
affiliations:
- eBay Inc., USA
arxiv_id: '2607.01530'
url: https://arxiv.org/abs/2607.01530
pdf_url: https://arxiv.org/pdf/2607.01530
published: '2026-07-01'
collected: '2026-07-04'
category: QueryRec
direction: 个性化查询意图解析
tags:
- Query Understanding
- Personalization
- Intent Inference
- LLM
- E-commerce Search
- User Behavior
one_liner: 通过融合用户历史查询等行为信号，用LLM推断模糊查询的性别、年龄、尺寸等意图，显著优于仅用总体需求或静态画像
practical_value: '- **意图推断模块设计**：当基线意图模型输出 “unspecified” 时，路由到 LLM 进行个性化推断。可参考 IntentTune
  架构，单独构建一个服务或模型，用近期高置信度用户查询（如性别置信度>0.8、年龄置信度>0.9）作为上下文，输出细化的性别、年龄、类目甚至尺寸意图，直接接入检索排序通路。

  - **用户信号选择**：历史查询行为远优于用户画像属性（如注册时填写的年龄、性别）和总体需求分布。实际系统中应优先利用短期搜索历史，提取其中意图明确的查询作为
  prompting 素材，而不是依赖静态标签。

  - **类目粒度优化**：对于模糊查询，先将类目预测模型给出的候选类目列表提供给 LLM，让 LLM 根据用户历史行为选择或收缩正确类目，可有效减少下游检索的候选空间，同时保持正确性，类似
  “后验类目精排” 思路。

  - **冷启动与冲突处理**：当历史查询不足时可回退到需求模式（利用类目预测模型最高置信度类目推断意图），但尺寸意图不适用此方法。多重信号冲突时，需要设计置信度投票或加权机制，避免直接采信单一来源。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商搜索中大量真实查询极度简短且模糊（如“boots”“shirt”），现有意图模型常将其标记为“未指定”，导致下游检索与排序效果恶化。用户固有的偏好（浏览历史、购买记录）蕴含丰富意图信号，但传统查询理解主要依赖查询文本，未有效利用这些个性化信息。

**方法关键点**：
- **框架设计**：IntentTune 在基线意图模型（BERT 分类器：性别、年龄、尺寸、类目）输出“unspecified”时被激活，提供两类解析模块。
  - **需求模块**：利用类目预测模型给出的最高置信度类目，从类目层级推断性别与年龄（不用于尺寸）。
  - **个性化模块**：采用内部 LLM，输入模糊查询、意图类别定义、以及用户上下文（画像属性或 1 个月内历史搜索查询），让 LLM 输出性别、年龄、尺寸和精炼类目。历史查询经过筛选，仅保留原意图模型高置信度（性别>0.8 或年龄>0.9）的查询。
- **数据构建**：从活跃用户中选取 30 个模糊查询与 30 名有丰富搜索行为的用户，组成 900 对 query-user 进行人工标注，覆盖性别、年龄、尺寸（允许多标签）和类目。

**关键结果**：
- 历史查询个性化在所有维度上远优于需求与画像方法：年龄加权 F1 0.816（需求 0.698）；性别加权 F1 0.726（需求 0.330）；尺寸加权 F1 0.853（仅历史查询可用）。
- 类目精炼上，个性化模块在 68.5% 的案例中将需求模型给出的多个候选类目正确缩减为单一类目。
- 用户动态行为信号（历史查询）的意图推理能力大幅领先于静态画像或全局需求分布，证明个性化查询理解是解决模糊查询的有效路径。
