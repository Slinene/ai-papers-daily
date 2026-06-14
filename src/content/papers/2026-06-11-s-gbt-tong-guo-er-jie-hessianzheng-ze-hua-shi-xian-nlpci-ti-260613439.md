---
title: 'S-GBT: Smooth Growth Bound Tensor for Certified Robustness Against Word Substitution
  Attacks in NLP'
title_zh: S-GBT：通过二阶Hessian正则化实现NLP词替换认证防御
authors:
- Mohammed Bouri
- Mohammed Erradi
- Adnane Saoud
affiliations:
- College of Computing, Mohammed VI Polytechnic University, Morocco
- ENSIAS, University Mohamed V of Rabat, Morocco
- CID Development, Morocco
arxiv_id: '2606.13439'
url: https://arxiv.org/abs/2606.13439
pdf_url: https://arxiv.org/pdf/2606.13439
published: '2026-06-11'
collected: '2026-06-14'
category: Other
direction: NLP对抗鲁棒性 · 二阶认证
tags:
- Certified Robustness
- Hessian Regularization
- Second-order
- Adversarial Defense
- LSTM
- CNN
one_liner: 利用逐元素Hessian界的平滑增长张量正则化，将认证鲁棒准确率提升最高23.4%
practical_value: '- 思路可迁移至推荐模型的鲁棒训练：对用户/物品文本描述或评论进行词替换攻击防御，可借鉴S-GBT的二阶正则项，在embedding层后加入Hessian范数惩罚，提升模型对输入微小扰动的稳定性。

  - 针对电商搜索或推荐中的query改写攻击，可将S-GBT嵌入query理解模型（如LSTM/CNN编码器）的训练目标，同时约束梯度和曲率，获得更紧的认证界。

  - 二阶正则化技巧可泛化到多模态模型（例如图文匹配）中，对视觉特征提取器施加类似的平滑性约束，增强多模态表示的鲁棒性。

  - 在Agent规划中，若使用LSTM/CNN处理文本上下文，可引入S-GBT正则，防止对抗输入导致错误动作预测，提升安全关键场景下的可靠性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：NLP模型易受词替换攻击，现有防御多基于一阶敏感度（梯度），忽略梯度变化（曲率），导致攻击者仍可绕过。

方法：提出平滑增长张量（S-GBT），对Hessian矩阵逐元素定界，并从理论上推导出输出变化的上界（含线性项和二次项）。训练时增加正则项最小化这些界，迫使模型输出对扰动既低敏感又曲率平滑。针对LSTM和CNN推导了具体计算公式。

结果：在多个文本分类数据集上，结合一阶和二阶正则化后，认证鲁棒准确率相比先前方法提升最高23.4%，同时原准确率保持竞争力。
