---
title: 'CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression
  for Industrial Recommendation at Tencent'
title_zh: CCFormer：面向腾讯工业级推荐的高效跨域特征交互与分层序列压缩
authors:
- Yunlong Wang
- Huizhe Zhang
- Haonan Hu
- Yudong Li
- Bing Wen
- Jianchao Tu
- Chengxiang Zhuo
- Zang Li
affiliations:
- Platform and Content Group, Tencent
arxiv_id: '2607.28070'
url: https://arxiv.org/abs/2607.28070
pdf_url: https://arxiv.org/pdf/2607.28070
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 工业推荐模型 · 长序列建模
tags:
- Long-Sequence Modeling
- Cross-Field Interaction
- Subspace Token Mixing
- Hierarchical Compression
- Industrial Recommender System
one_liner: 统一特征域分离交叉注意力与子空间token混合，实现长序列推荐的高效交互与2.21×训练加速
practical_value: '- 特征域分离的交叉注意力：将用户、行为序列、目标物品显式解耦，仅执行必要的定向注意力，避免全 token 自注意力的二次方开销；同时支持单个前向为请求内所有候选目标并行打分，在线峰值
  QPS 提升 30%。

  - 子空间 token 混合替代自注意力：沿序列和通道维度分组，局部混合 token 与 hidden 维度，以轻微精度损失换取 2.21× 训练加速，适合长行为序列的粗粒度编码。

  - 层次化序列压缩：Transformer 层间使用 1D 卷积下采样逐步收缩序列长度，自动构建多尺度感受野（短期→长期），在保持长程依赖的同时大幅缩减后续层的计算量。

  - 工程化部署优化：混合精度训练（BF16）、嵌入表 INT8 量化 + 双哈希压缩、候选物品并行预测，实际验证了复杂架构在工业流量的可行性与收益。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工业推荐中，基于自注意力的序列模型在扩展序列长度和模型容量时，面临二次方计算和显存瓶颈，无法在严格的延迟与资源约束下部署。现有压缩或截断方案易丢失细粒度行为信号或长程兴趣，难以兼顾充分的特征交互与效率。

## 方法关键点
- **特征域分离的交叉注意力**：将输入 token 显式划分为用户、行为序列、目标物品三个语义域，执行三路定向注意力（用户→序列、目标→序列、目标→用户），避免全量 token 间自注意力。
- **子空间相对时序-位置编码**：在行为序列的局部子空间内，通过可学习的相对时序衰减和相对位置偏置，高效注入时间与位置信息，复杂度为 O(L·m)。
- **长序列子空间 token 混合**：将行为序列 token 沿序列维和通道维分组为子空间，每个子空间内使用逐通道前馈网络（PFFN）进行局部混合，替代全局自注意力，牺牲少量精度换取大幅训练加速。
- **层次化序列压缩**：每层后接 1D 卷积下采样（kernel=3, stride=2），逐步收缩序列长度，同时扩大感受野（浅层捕获短期、深层提取长期），降低深层计算量。
- **工程优化**：混合精度训练、稀疏嵌入 INT8 量化 + 双哈希压缩、候选物品并行预测。

## 关键结果
- 公开数据集：Taobao AUC 93.67%，KuaiRec AUC 83.35%，均优于 STCA、OneTrans、HSTU 等基线。
- 工业数据集（>4B 样本）：相比 HSTU，AUC 提升 1.01%，GAUC 提升 2.40%；模型尺寸和序列长度均展现出可预测的 Scaling 增益。
- 在线 A/B（腾讯视频推荐 + 广告排序）：CTR +3.57%，广告收入 +1.71%，页面浏览 +3.86%；训练速度较 HSTU 提升 2.21×。
- 消融验证：子空间 token 混合贡献最大，移除后 AUC 跌 0.21%；序列压缩是效率关键，移除后训练加速从 2.21× 降至 1.29×。

**最值得记住的一句话**：通过解耦特征域交叉注意力与局部子空间混合，CCFormer 在工业长序列建模中首次实现了精度上升与训练加速 2.21× 的双赢，已全量部署于腾讯推荐系统。
