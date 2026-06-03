---
title: 'MARS: Multi-rate Aggregation of Recency Signals for Sequential Recommendation
  across Sparse and Dense Regimes'
title_zh: MARS：多速率时间感知聚合用于稀疏与密集序列推荐
authors:
- Zhenyu Yu
- Shuigeng Zhou
affiliations:
- 复旦大学计算机科学技术学院
arxiv_id: '2606.03718'
url: https://arxiv.org/abs/2606.03718
pdf_url: https://arxiv.org/pdf/2606.03718
published: '2026-06-02'
collected: '2026-06-03'
category: RecSys
direction: 序列推荐 · 多尺度时间建模
tags:
- Multi-rate aggregation
- Temporal dynamics
- Sequential recommendation
- Transformer
- Mamba
- Data density adaptation
one_liner: 提出编码器无关的多速率指数衰减聚合算子，根据数据密度自动选择Transformer/Mamba骨干，显著提升序列推荐。
practical_value: '- **解耦时间聚合与序列编码**：可将 MARS 作为轻量级后处理模块插入现有排序模型，仅O(LdK)开销，无需改动编码器，适合业务快速迭代。

  - **多速率衰减头与自适应门控**：用户条件调制和JSD多样性正则防止多头坍塌，捕捉多尺度兴趣（如短时爆发 vs 长期偏好），尤其适用于电商中长短周期混合的场景。

  - **数据密度驱动的骨干选择**：根据平均序列长度自动选用Transformer（稀疏）或Mamba（密集），避免单一骨干的边际收益递减，推荐系统可依此策略分场景部署。

  - **分组评估揭示收益来源**：长历史用户从多速率机制受益最大（Yelp上+29.7%），业务上可针对性对高活跃用户启用该模块，平衡性能与成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
用户行为呈现多时间尺度（分钟级会话突发到数月长期兴趣），现有序列推荐模型（Transformer基于位置编码，Mamba依赖固定衰减）均将多尺度结构压缩进单一机制，难以同时刻画细粒度局部模式和长期趋势。作者将时间感知聚合从序列编码器中解耦，提出MARS——编码器无关的多速率指数衰减算子，实时时间戳作为显式输入，生成K个不同时间尺度的摘要，并通过上下文自适应门控融合，还原真实数据生成过程中的多尺度时间结构。

**方法关键点**
- **多速率衰减聚合**：每个头学习不同的指数衰减率和温度，对编码器输出进行软性加权，得到K个时间尺度摘要。衰减率通过用户序列表示条件调制，实现个性化时间感知。
- **JSD多样性正则**：强制不同头关注不同时段，防止所有头坍缩为单一速率，理论保证在Hawkes过程生成数据下可识别真实衰减率。
- **上下文自适应门控**：门控网络基于最近交互时间、物品嵌入、编码器尾状态动态融合K个摘要，残差连接保留原有信号。
- **双骨干框架**：稀疏数据（平均序列长度<50，如Amazon、Yelp）采用MARS-T（Transformer），密集数据（ML-1M）采用MARS-M（Mamba），由数据集统计量自动选择。

**关键结果**
在5个公开数据集（Beauty、Sports、Games、ML-1M、Yelp）上对比10个基线，MARS在所有数据集上取得最高HR@10：稀疏数据上平均相对增益+19.7%（Games上+36.2%），密集ML-1M上HR@10超SIGMA 3.2%且MFLOPs减少42%。消融实验表明，多头衰减在稀疏长历史用户上贡献最大，JSD正则提升鲁棒性。效率分析显示，MARS-T参数仅比SASRec多2%，推理速度优于SIGMA和BERT4Rec。
