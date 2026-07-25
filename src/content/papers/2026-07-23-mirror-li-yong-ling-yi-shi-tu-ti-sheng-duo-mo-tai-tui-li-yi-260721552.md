---
title: 'MIRROR: Learning from the Other View for Multi-Modal Reasoning'
title_zh: 'MIRROR: 利用另一视图提升多模态推理一致性'
authors:
- Wen Ye
- Yuxiao Qu
- Aviral Kumar
- Xuezhe Ma
affiliations:
- University of Southern California
- Carnegie Mellon University
arxiv_id: '2607.21552'
url: https://arxiv.org/abs/2607.21552
pdf_url: https://arxiv.org/pdf/2607.21552
published: '2026-07-23'
collected: '2026-07-25'
category: Reasoning
direction: 多模态推理 · 自监督强化学习
tags:
- Multi-modal Reasoning
- Reinforcement Learning
- Self-supervision
- Vision-Language Models
- Geometry
one_liner: 通过视图间互惠强化学习，利用多模态行为差异提升几何推理准确性与跨模态一致性
practical_value: '- **多视图对齐训练范式**：电商场景中商品信息天然有文本描述、主图、规格图等多模态视图，可借鉴 MIRROR 在训练时主动暴露视图差异，用表现最好的视图监督其他视图，提升商品问答、图文匹配等任务的一致性与准确性。

  - **强化学习替代方案**：传统 RLHF 依赖人类偏好，MIRROR 用模型自身在视图间的表现差距作为奖励信号，无需外部标注，可迁移到 Agent 评估或多模态检索中，用“容易版”问题教会“困难版”推理。

  - **自监督推理一致性提升**：推荐系统中用户行为、评论、图片等不同模态可能蕴含同一决策意图，可设计类似 Teacher-Student 机制，用强模态监督弱模态，减少模态缺失时的性能下降。

  - **构建模态依赖测试集**：在业务评测中加入纯文本、纯图、混合视图的对照测试，暴露模型对特定模态的过拟合，指导训练改进。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：VLM 在相同几何问题下，纯文本、纯图、图文结合三种视图会表现截然不同的推理行为——文本解得出但看图失败，或反之。这暴露了视图特有的故障模式，标准多模态后训练未能充分利用这种互补性。

**方法**：构建高质量成对数据集 ODA-Data，每个问题含三种视图，专门训练评估模态依赖行为。提出 MIRROR 方法：对每个问题，用所有视图进行推理评估，选取表现最好的视图作为教师，通过反向 KL 散度对其他视图进行强化学习，让差视图模仿最佳视图的推理路径，实现自监督的互惠优化。

**结果**：在几何推理基准上，MIRROR 显著优于标准 RL，提升准确率，并使跨模态行为更一致。
