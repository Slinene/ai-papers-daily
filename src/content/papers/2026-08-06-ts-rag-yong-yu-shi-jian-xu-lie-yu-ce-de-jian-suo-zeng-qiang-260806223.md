---
title: 'TS-RAG: Retrieval Augmented Generation for Time Series Forecasting'
title_zh: TS-RAG：用于时间序列预测的检索增强生成
authors:
- Yixiong Xiao
- Congxi Xiao
- Jingbo Zhou
affiliations:
- Baidu, Inc.
arxiv_id: '2608.06223'
url: https://arxiv.org/abs/2608.06223
pdf_url: https://arxiv.org/pdf/2608.06223
published: '2026-08-06'
collected: '2026-08-08'
category: RAG
direction: 检索增强的时间序列预测
tags:
- time series forecasting
- retrieval augmented generation
- reference tokens
- transformer
- state-of-the-art
one_liner: 提出 TS-RAG，用参考令牌融合检索序列，提升时间序列预测精度
practical_value: '- 在电商销量、流量等时序预测中，可借鉴 TS-RAG 的检索增强思路，检索相似历史窗口并通过可学习的参考令牌融合，避免简单拼接带来的噪声。

  - 对于推荐系统的行为序列预测（如用户下一步动作），可检索相似用户序列作为参考，用融合机制增强模型对长尾或冷启动场景的预测能力。

  - 工程实现上，需预先对历史序列切片并计算表示向量，构建近似最近邻索引，在线推理时低延迟检索，同时注意定期更新索引。

  - 参考令牌设计与 Transformer 主干解耦，可灵活插入现有预测模型，无需大幅改动架构。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：RAG 在 NLP 中有效，但在时间序列预测中应用有限。现有时间序列模型参数量小、生成能力弱，直接拼接检索序列难以发挥作用。

**方法**：提出 TS-RAG，首先检索与输入序列最相似的历史子序列，然后引入一组可学习的参考令牌（reference tokens）。这些令牌在 Transformer 编码器中通过交叉注意力与检索序列交互，并将融合后的信息注入输入序列的表示，从而更鲁棒地捕捉时间动态。

**结果**：在多个真实世界预测基准（覆盖能源、交通、天气等领域）上，TS-RAG 一致超越现有最强模型（如 iTransformer、PatchTST），证明了检索增强在时序预测中的有效性。
