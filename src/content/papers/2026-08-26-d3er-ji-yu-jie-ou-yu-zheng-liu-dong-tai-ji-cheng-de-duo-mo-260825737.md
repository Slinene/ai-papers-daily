---
title: 'D3ER: Supporting Multi-Modal Recommendation via Disentangle and Distillation-based
  Dynamic Ensemble'
title_zh: D3ER：基于解耦与蒸馏动态集成的多模态推荐
authors:
- Bingnan Wang
- Yi Li
- Xiongxin Tang
- Fanjiang Xu
- Jiangmeng Li
affiliations:
- Institute of Software, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2608.25737'
url: https://arxiv.org/abs/2608.25737
pdf_url: https://arxiv.org/pdf/2608.25737
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 多模态推荐 · 动态集成与知识蒸馏
tags:
- Multi-modal Recommendation
- Gradient Boosting
- Knowledge Distillation
- Dynamic Ensemble
- Disentangled Learning
one_liner: 首次将梯度提升引入多模态推荐，交替学习模态同质与异质判别信息，并以知识蒸馏和全局校正正则增强集成
practical_value: '- 多模态商品/内容理解中，显式拆解“跨模态同质判别信息(HOI)”与“模态特有异质判别信息(HEI)”，分别建模再动态集成，可避免单一联合表示的内部冲突，适合电商图文/短视频/标题等多模态商品表征。

  - 借鉴 gradient boosting 的交替训练与样本聚焦思路：轮换训练不同专家模型，让各模型专注处理自己擅长的样本（如视觉突出 vs 文本突出），后续以动态
  ensemble 融合，提升整体排序效果。

  - 多个专家模型上线成本高时，可用 knowledge distillation 把多专家集成知识迁移到单一轻量 student，保留集成增益的同时降低存储/推理开销，适合推荐系统线上
  serving。

  - global correction regularization 可作为防止交替训练陷入局部最优的通用正则，迁移到其他多任务/多专家训练框架中。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有多模态推荐(MR)通常将多模态信息融合为统一表示，但联合学习模态同质判别信息(HOI)与模态异质判别信息(HEI)会相互削弱，导致各自的判别效果下降。

**方法关键点**：
- 首次将 gradient boosting 引入 MR，形式化交替学习 HOI 与 HEI 的优化目标，让专注于不同类型判别信息的模型各自聚焦其擅长样本，实现专业化优化。
- 通过 disentangle 设计，显式解耦 HOI 与 HEI，分别训练不同专家模型，再以 dynamic ensemble 动态集成。
- 为缓解 gradient boosting 固有的高存储成本和局部最优风险，引入 knowledge distillation 将多专家知识压缩到轻量模型，并加入 global correction regularization 进行全局校正。

**关键结果**：在多个真实世界数据集上验证了 D3ER 优于现有多模态推荐方法，证实解耦 + 蒸馏 + 动态集成的有效性。
