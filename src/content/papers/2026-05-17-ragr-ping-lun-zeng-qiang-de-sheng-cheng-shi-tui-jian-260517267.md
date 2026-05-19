---
title: 'RAGR: Review-Augmented Generative Recommendation'
title_zh: RAGR：评论增强的生成式推荐
authors:
- Yingyi Zhang
- Junyi Li
- Yejing Wang
- Wenlin Zhang
- Xiaowei Qian
- Sheng Zhang
- Yue Feng
- Yichao Wang
- Yong Liu
- Xiangyu Zhao
affiliations:
- Dalian University of Technology
- City University of Hong Kong
- Huawei Technologies Ltd.
arxiv_id: '2605.17267'
url: https://arxiv.org/abs/2605.17267
pdf_url: https://arxiv.org/pdf/2605.17267
published: '2026-05-17'
collected: '2026-05-19'
category: GenRec
direction: 生成式推荐 · 用户评论增强
tags:
- Generative Recommendation
- Review-Augmented
- Semantic ID
- DPO
- RQ-VAE
- Sequential Recommendation
one_liner: 将用户评论反馈编码为语义ID融入生成式用户序列，并通过DPO对齐确保模型偏好物品生成而非评论生成。
practical_value: '- **用户反馈文本可直接转为语义ID注入生成序列**：在电商评论场景中，可利用现有多模态编码器（如T5）将商品标题、评论等文本预先量化为离散语义ID，与物品语义ID按时间交错拼接，直接改造任意生成式推荐模型（如TIGER）的输入，无需改动模型架构。

  - **引入评论预测作为辅助任务**：将下一个评论的语义ID也作为生成目标之一，与物品预测共享同一生成空间，可隐式地让模型学习“物品-评论”的共现语义，缓解物品ID空间分布集中的问题，提升长尾物品的表示学习。

  - **用DPO显式对齐生成偏好**：当输入序列中同时包含物品和评论ID时，构造（输入，物品ID，评论ID）三元组，使用DPO将物品ID设为偏好输出，评论ID设为拒绝输出，可简洁地防止模型在预测位置“短路”直接生成评论，确保推荐目标不漂移。

  - **实体文本的语义ID tokenization 优于直接混用不同来源文本训练 tokenizer**：实验表明，仅用物品文本训练RQ-VAE得到的语义ID，在效率和下游推荐性能上均优于混合物品和评论文本，可避免语义空间过于分散带来的噪声。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有生成式推荐（如TIGER、LETTER）仍沿袭传统序列推荐的“仅物品交互轨迹”假设，只捕捉用户“选了什么”而忽略“为什么选”。用户评论中隐含的质量、美观等评价因素能解释决策动因，因此有必要将评论反馈融入生成式序列，填补“仅行为”的建模缺口。

**方法关键点**：
- *统一语义ID空间*：先用T5编码物品文本，再用RQ-VAE量化为多层离散语义ID，形成物品与评论共用的token空间。
- *评论增强的用户序列建模*：将物品语义ID与对应评论语义ID按时间顺序交织，构造混合行为-语义序列，使模型在自回归生成下个物品时可直接利用评论上下文。
- *物品中心的任务生成对齐*：引入基于DPO的对齐阶段，将目标物品ID设为偏好输出，对应评论ID设为拒绝输出，迫使模型在预测步偏好物品而非评论，确保评论仅作为证据而非替代目标。

**关键实验与结果**：在Amazon Beauty、Toys、Sports三个数据集上评估，以TIGER和LETTER为backbone，RAGR在HIT@5上相对提升7%~26%（Beauty上TIGER提升13%、LETTER提升20%），消融实验表明仅注入评论而不加任务对齐反而有损，完整框架收益显著且稳定。tokenizer训练仅用物品文本的效果与效率最佳。语义ID数量为4时平衡效果最好。
