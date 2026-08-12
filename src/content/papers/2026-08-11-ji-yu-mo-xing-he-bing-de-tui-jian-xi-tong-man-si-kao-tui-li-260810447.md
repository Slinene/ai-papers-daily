---
title: Towards Efficient Reasoning in LLM-Based Recommender Systems via Model Merging
title_zh: 基于模型合并的推荐系统慢思考推理高效压缩
authors:
- Linh Dieu Le
- Tong Chen
- Shazia Sadiq
- Hongzhi Yin
- Ming Jin
- Junliang Yu
affiliations:
- The University of Queensland
- Griffith University
arxiv_id: '2608.10447'
url: https://arxiv.org/abs/2608.10447
pdf_url: https://arxiv.org/pdf/2608.10447
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: LLM推荐系统推理压缩 · 模型合并
tags:
- Model Merging
- Reasoning Compression
- Slow-Thinking Recommender
- Attention Heads
- Fisher-weighted Merging
- Chain-of-Thought
one_liner: 首次将模型合并用于慢思考推荐系统的推理压缩，在注意力头粒度选择性注入简洁行为，缩短推理长度最高24.3%且保持准确率
practical_value: '- 可以通过模型合并，在无需重新训练的情况下压缩慢思考推荐模型的冗长推理链，降低线上推理延迟和成本。

  - 合并时以注意力头为单位，依据检索关键性、决策忠实度和参数更新敏感度分配合并系数，保护关键推理头，避免精度损失。

  - 对于电商/广告推荐中需要复杂用户偏好推理的场景，可以先训练慢思考模型获得高准确率，再通过REAM压缩推理长度，平衡效果与效率。

  - 工程实现仅需少量校准数据（如500条）计算头级信号，无需额外梯度更新，可快速部署。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
基于LLM的慢思考推荐系统通过逐步推理（如分析用户偏好、物品特征、匹配度）提升预测准确率，但推理过程往往过度冗长，增加了推理延迟和计算开销。现有压缩方法要么需要额外训练（蒸馏、长度惩罚优化），要么依赖推理时硬性约束（token预算），难以稳定地平衡准确性和效率。模型合并作为一种无需训练的参数迁移技术，通过组合快思考和慢思考模型的参数，有可能将简洁生成行为注入慢思考模型，但直接全局合并可能破坏推荐相关的关键推理。

## 方法关键点
- **头级别合并系数**：REAM将合并粒度从通常的层级别细化到单个注意力头。每个注意力头根据其在推理中的作用和参数敏感性分配独立的合并系数。
- **检索关键性（retrieval criticality）**：统计每个头在生成推理链时从用户、物品上下文中成功检索相关证据的频率，识别哪些头是推理的核心支撑。
- **决策忠实度（decision faithfulness）**：衡量每个头在生成最终评分时对推理链中匹配段（match）的关注程度，反映头连接推理与决策的重要性。
- **更新敏感性**：基于对角经验Fisher矩阵，评估慢思考模型对快思考更新方向的参数敏感度，高敏感头需要更保守的合并。
- **约束优化分配**：综合上述三个信号计算扰动风险，通过求解带预算约束的线性规划，最大化快思考更新总量，同时限制总推理扰动。
- **FFN层处理**：FFN层按层取平均头系数，并固定排除最后几层（如30‑35层）的FFN合并，避免干扰输出映射。

## 关键结果
- 在Amazon Book、Yelp、Amazon Music三个评分预测数据集上，REAM将推理长度缩短最高24.3%。
- 相比RecZero（慢思考基模型）：Book上MAE从0.6650降至0.6338，推理token从313.58降至237.33；Yelp上MAE从0.7769降至0.7564，token从314.54降至258.19；Music上MAE从0.5433降至0.5348，token从344.28降至271.49。
- REAM在准确率‑效率权衡上全面优于Task Arithmetic、AIM、ACM等基线和数据驱动合并方法。
- 消融实验表明，检索关键性、决策忠实度和敏感性三项信号互补，共同保障压缩后的推荐质量。
