---
title: Learning Interpretable Text Signals for Structured Responses
title_zh: 为结构化响应学习可解释文本信号
authors:
- Cixiao Jiang
- Ben Powell
- Niall MacKay
affiliations:
- University of York
arxiv_id: '2606.25268'
url: https://arxiv.org/abs/2606.25268
pdf_url: https://arxiv.org/pdf/2606.25268
published: '2026-06-24'
collected: '2026-06-28'
category: RecSys
direction: 可解释评分预测 · 有监督主题模型
tags:
- interpretability
- non-negative matrix factorization
- supervised topic model
- rating prediction
- text-response modeling
one_liner: 联合非负矩阵分解与二项回归，学习对齐评分的可解释文本主题表示
practical_value: '- 评论驱动的评分预测场景中，可同时获得预测值和具体的主题-响应关联解释，直接用于商品评价洞察或 badcase 归因

  - NMF 得到的文档-主题表示可作为下游推荐模型的可解释特征，替代或结合稠密 embedding，在特征工程阶段注入先验结构

  - 联合训练的思路可迁移到深度学习：在 BERT 微调时增加评分回归辅助任务，并通过稀疏/非负约束增强可解释性

  - 模型能恢复稳定信号，适合冷启动或数据稀疏场景，为在线反馈较少的商品提供鲁棒的文本侧特征'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机** 文本评论常与结构化评分共存，但现有做法要么只做预测（黑盒），要么只做无监督话题抽取，无法解释哪些文本模式驱动了评分变化。需要在统一的框架下同时学习语义有意义且评分对齐的文本表示。

**方法关键点** 提出联合非负矩阵分解（NMF）与二项回归的模型。文档-话题负荷矩阵同时优化两项损失：基于泊松似然的文本重构误差，以及基于二项回归的评分预测误差（将 bounded rating 建模为成功次数）。NMF 保证话题可解释，回归使话题权重直接关联评分。

**关键结果** 在模拟数据上能准确恢复预设的评分相关话题信号；在真实 Yelp 评论数据上，评分预测 MSE 与线性回归、岭回归可比（例如 MSE 约 1.2× 基线），同时每个话题的词分布可清晰解读，展示出具体的打分驱动词（如“服务慢”对应低分话题）。
