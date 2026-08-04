---
title: 'SPEAR: Selection-aware Personalized End-to-end Adaptive Rewriting and Retrieval
  for Community Search'
title_zh: 'SPEAR: 社区搜索中端到端自适应改写与检索的防短路框架'
authors:
- Wenbin Wu
- Yuzhong Wu
- Yufan Xu
- Kuan Fang
- Xing Xu
- Cheng Ye
- Xiaobin Hu
affiliations:
- National University of Singapore
- Shanghai Dewu Information Group Co., Ltd.
arxiv_id: '2608.01738'
url: https://arxiv.org/abs/2608.01738
pdf_url: https://arxiv.org/pdf/2608.01738
published: '2026-08-03'
collected: '2026-08-04'
category: QueryRec
direction: 端到端查询改写与检索联合优化
tags:
- Query Reformulation
- Dense Retrieval
- End-to-End
- Multi-Objective
- Personalization
- E-commerce Search
one_liner: 通过梯度隔离双嵌入、乘性门控和动态选择器，解决改写-检索错位与通用词主导效应，点击召回@10提升99.5%
practical_value: '- 在多路召回改写系统中，可用乘法门控替代加法路径评分（如 Softplus 保证非负后加权），强制改写贡献需同时满足高置信与高
  item 相关，直接消除高频通用词的分数膨胀问题。

  - 若模型同时服务召回和排序任务，采用双嵌入分支 + stop-gradient 隔离梯度，保护召回语义不被 CTR 优化扭曲，工程上仅需增加少量投影 MLP，易于部署。

  - 动态生成样本级的 scale/bias 参数（由用户和 query 表征共同决定），使改写权重与匹配分数能随请求自适应校准，比固定超参更具个性化性。

  - 离线评估改写模型时，可同时关注 Exposure Recall、Click Recall 和 Semantic Similarity 三个指标，分别衡量检索覆盖、点击恢复和意图保真，避免单一语义相似度的片面性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机** 工业界搜索系统常将查询改写与检索分开优化，前者追求语义相似，后者优化点击，导致改写虽合理但未必有助于检索。直接移植推荐领域的端到端路径架构（PDN）到搜索时，会出现“通用词主导效应”：模型偏好高频泛词（如“手机壳”），依靠高选择置信度获得高分，却偏离原查询意图。

**方法**
- **双嵌入梯度隔离**：为召回和排序分支设计独立投影层，并在 CTR 损失到召回参数上使用 stop-gradient，防止排序信号侵蚀召回语义结构。
- **乘性门控聚合**：改写路径最终得分 = Σ (改写权重 × item 相关性)，其中相关性经 Softplus 保证非负，从而高权重但低相关性的改写贡献极低，根治通用词捷径。
- **动态改写选择器**：基于用户和原始查询生成改写分布权重，同时输出样本级 scale 和 bias 用于 item 匹配分数校准，使改写偏好和相关性调节随请求动态适配。
- 训练时主损失为 CTR 的二元交叉熵，辅助损失为召回分支的 InfoNCE 对齐损失。

**结果**
- 离线 100K 会话测试：相比生产基线，语义相似度@10 提升 18.2%，点击召回@10 提升 99.5%，曝光召回@10 提升 110.2%。
- 在线 A/B 测试：QVCTR +0.259%，阅读深度 +0.733%，且人工评估满意度 DCG 提升 0.67pp，坏例率下降。
- 系统已于 2025 年在得物社区搜索全量上线。
