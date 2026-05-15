---
title: Efficient Generative Retrieval for E-commerce Search with Semantic Cluster
  IDs and Expert-Guided RL
title_zh: 基于语义聚类ID与专家引导RL的高效电商搜索生成式检索
authors:
- Jianbo Zhu
- Xing Fang
- Jing Wang
- Mingmin Jin
- Bokang Wang
- Guangxin Song
- Zhenyu Xie
- Junjie Bai
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2605.14434'
url: https://arxiv.org/abs/2605.14434
pdf_url: https://arxiv.org/pdf/2605.14434
published: '2026-05-14'
collected: '2026-05-15'
category: RecSys
tags:
- Generative Retrieval
- RecSys
- RQ-VAE
- RL
- E-commerce Search
- Semantic ID
one_liner: 提出语义聚类ID（CQ-SID）和专家引导GRPO，在电商搜索召回中大幅提升命中率并降低推理成本，在线GMV提升1.15%
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式检索试图用单一模型统一多级检索，但在工业电商搜索中面临三重挑战：商品库庞大且频繁更新、在线延迟严格、召回结果需与下游排序对齐。现有方法追求商品唯一ID，导致波束搜索计算量巨大，且稀疏奖励下强化学习容易坍缩。该工作将生成式检索定位为召回阶段的补充，而非端到端替代，重点关注效率与排序一致性。

**方法关键点**：
- **CQ-SID语义ID构建**：基于RQ-VAE，引入类别感知残差量化（首级码本强制对齐商品类目）和查询-商品双向对比学习（InfoNCE），使相似商品聚合成层次化语义簇，而非唯一ID。这种设计在不牺牲区分度的情况下大幅减少波束搜索复杂度。
- **渐进式查询-SID映射训练**：使用Qwen2.5-0.5B，分四个阶段逐步习得从商品标题、查询、个性化特征（用户画像+近期交互）到语义ID的生成能力，前三个阶段为监督微调，第四阶段用RL对齐排序信号。
- **EG-GRPO（专家引导GRPO）**：在GRPO的每个采样组中注入真实点击/曝光ID作为“专家样本”，利用组内优势归一化稳定策略梯度，克服标准GRPO在稀疏奖励下的模式集中与探索崩塌。

**关键结果**：离线实验中，CQ-SID相比标准RQ-VAE在相同波束尺寸下语义命中率提升最高26.76%，个性化命中率提升11.11%；达到同等命中率所需波束数减少53%以上。EG-GRPO在点击、曝光、覆盖率三个维度实现同步提升，避免单指标退化。在线A/B测试在主流移动电商平台TmallAPP上，GMV提升1.15%，UCTCVR提升0.40%，生成式召回通道贡献了50.25%的曝光、58.96%的点击和72.63%的购买。该工作验证了以语义簇ID替代唯一ID、用专家引导RL对齐多目标的范式在工业级召回中的可行性与高效性。
