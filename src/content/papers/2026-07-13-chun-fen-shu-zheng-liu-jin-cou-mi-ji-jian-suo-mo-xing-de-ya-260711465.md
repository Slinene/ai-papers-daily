---
title: Score-Only Distillation for Compact Dense Retrieval
title_zh: 纯分数蒸馏：紧凑密集检索模型的压缩训练方法
authors:
- Kirill Dubovikov
- Martin Takac
- Salem Lahlou
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2607.11465'
url: https://arxiv.org/abs/2607.11465
pdf_url: https://arxiv.org/pdf/2607.11465
published: '2026-07-13'
collected: '2026-07-15'
category: RecSys
direction: 知识蒸馏 · 密集检索压缩
tags:
- knowledge distillation
- dense retrieval
- model compression
- score-only distillation
- PairMSE loss
one_liner: 仅用教师模型输出的分数向量蒸馏学生模型，无需教师隐藏状态，实现 4.7× 查询编码加速
practical_value: '- **黑盒蒸馏**：只需要教师模型的分数输出，无需访问隐藏状态或嵌入，可直接蒸馏第三方大模型或 API 模型，适用于无法获取内部表示的闭源检索模型。

  - **内存高效 PairMSE 损失**：采用行中心分数向量目标替代显式 pairwise 边际计算，将内存复杂度从 O(k²) 降到 O(k)，适合大规模候选行训练，可直接用于电商搜索精排或双塔召回的蒸馏。

  - **数据管线设计**：论文给出了基于正样本和负样本候选行的数据生成流程，并单独评估了 student-teacher hard-negative mining，离线挖掘难负样本的策略可迁移至商品搜索的负样本构造。

  - **在匹配协议下压缩有效**：实验表明蒸馏在相同的检索协议（如推理阶段使用相同的候选生成方式）下可恢复 50% 的教师提升，但跨场景迁移不稳，提示部署时需保持检索协议一致性，避免直接泛化到不同检索配置。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：大嵌入模型在线服务成本高，紧凑模型蒸馏通常需访问教师隐藏状态或嵌入，本文探索仅用黑盒分数向量让学生学习教师排序，更适用于闭源或 API 教师。

**方法**：提出两种做法：（1）行中心分数向量目标，对同一候选行中的学生与教师分数向量中心化后最小化残差平方范数，等价于均匀 PairMSE 损失但内存效率更高；（2）数据生成管线利用真实正例和多种负样本构造候选行，并扩展了 student-teacher 难负样本挖掘。整套蒸馏流程无需教师嵌入或隐藏状态。

**结果**：在 8 任务评估面板上，0.6B 学生模型恢复基准到教师质量差距的 50%，查询编码速度提升 4.7 倍，文档编码提升 9.7 倍；但外部迁移性能好坏参半，表明该方法更适合在匹配检索协议下压缩排名，不能保证跨域泛化。
