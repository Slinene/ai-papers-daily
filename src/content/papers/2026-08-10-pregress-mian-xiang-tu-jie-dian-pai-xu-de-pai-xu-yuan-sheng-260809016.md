---
title: 'PreGress: Ranking-Native Pre-training and Prompting for Graph Node Ranking'
title_zh: PreGress：面向图节点排序的排序原生预训练与提示框架
authors:
- Lujie Ban
- Jiasheng shi
- Yingli Zhou
- Kaiwen Xue
- Daiyin Wang
- Xubin Li
- Shuanghua Li
- Chenhao Ma
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Huawei Technologies Co., Ltd.
arxiv_id: '2608.09016'
url: https://arxiv.org/abs/2608.09016
pdf_url: https://arxiv.org/pdf/2608.09016
published: '2026-08-10'
collected: '2026-08-11'
category: RecSys
direction: 图节点排序 · 预训练与提示微调
tags:
- Graph Neural Networks
- Node Ranking
- Pre-training
- Prompt Tuning
- Subgraph Neural Networks
- Ranking Loss
one_liner: 首个排序原生的图预训练+提示微调框架，通过度中心性与属性重建预训练，配合任务特定提示，统一支持多种节点排序准则
practical_value: '- **图构建与预训练复用**：对用户-物品交互图，用度中心性作为自监督目标预训练节点表示，无需人工标注，训练一次后通过轻量提示适应不同排序准则（如
  PageRank、子图计数），大幅降低下游任务训练成本。

  - **Ego 网络避免过平滑**：抽取 k-hop ego 网络并采用子图 GNN 作为骨干，限制消息传递范围，有效避免深层堆叠带来的节点表示坍缩，适合需要精细区分的推荐排序场景。

  - **提示模块设计**：对无结构输入（如中心性预测）使用可学习向量；对有结构输入（如模式图匹配）使用轻量 GNN 生成提示，并通过 Soft CCA 正则对齐分布。可参照此思路在推荐系统里用提示注入多模态信息或业务规则。

  - **排序导向的损失设计**：预训练中结合 MSE 回归与 listwise KL 正则，显式建模排序一致性，比仅用点损失更符合 top-K 推荐目标，可直接移植到排序模型的预训练阶段。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
不同图分析任务依赖不同的节点重要性准则（如中心性、子图计数、PageRank），现有方法要么逐个准则精确计算开销大，要么用 GNN 近似但需针对每个准则重新训练，无法跨任务迁移。图预训练与提示微调范式虽能复用知识，但现有工作面向分类任务，输出空间与排序的连续数值空间不匹配，导致适配排序任务时性能不佳。

### 方法
- **预训练任务选择**：采用度中心性预测（输出连续值且标签易得）作为主任务，同时用属性重构作为辅助任务，共同捕捉图的结构与属性信息。
- **骨干网络设计**：将原图拆分为 k-hop ego 网络，使用子图 GNN（SNN）学习节点表示，限制感受野以抑制过平滑，并保持节点区分度。
- **预训练损失**：度中心性部分使用 MSE 回归 + mini-batch 内的 listwise KL 散度正则，使预训练即关注排序一致性；属性重构使用 InfoNCE 损失。
- **提示微调**：下游适配时冻结 SNN 骨干，仅训练轻量提示模块。对中心性任务，用一个可学习向量加到输入特征上；对子图计数任务，用轻量 GNN 从模式图中生成提示向量，并引入 Soft CCA 正则增强模式与 ego 网络的相似性对齐。

### 关键结果
在 6 个公开图和 Yelp2018、MovieLens 推荐数据集上评估。中心性预测任务中，PreGress 在 5/6 数据集上取得最优 NDCG@10/20，如 Flickr 上 NDCG@10 达 0.6667（比最强基线提升 12.7%）。子图计数任务也在多数据集上显著领先。推荐任务中，在 Yelp2018 达到与强基线 SimGCL 几乎相同的 Recall@20（0.0636 vs 0.0638），但可训练参数减少 99.9%，下游训练速度提升 39.1 倍。消融实验证实提示调优、子图骨干与 ego 网络抽取均对排序质量有显著贡献。
