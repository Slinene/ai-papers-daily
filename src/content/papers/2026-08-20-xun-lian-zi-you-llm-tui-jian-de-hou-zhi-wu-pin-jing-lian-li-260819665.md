---
title: Training-Free LLM-Based Recommendation with Post-LLM Item Refinement Using
  Collaborative Signals
title_zh: 训练自由 LLM 推荐的后置物品精炼：利用协作信号
authors:
- Kyungho Kim
- Sunwoo Kim
- Geon Lee
- Shinhwan Kang
- Sojeong Kim
- Liam Collins
- Bhuvesh Kumar
- Donald Loveland
- Kijung Shin
affiliations:
- KAIST
- Snap Inc.
arxiv_id: '2608.19665'
url: https://arxiv.org/abs/2608.19665
pdf_url: https://arxiv.org/pdf/2608.19665
published: '2026-08-20'
collected: '2026-08-21'
category: RecSys
direction: 训练自由 LLM 推荐 · 协作信号后置精炼
tags:
- LLM4Rec
- Collaborative Filtering
- Training-Free
- Item Embedding Refinement
- Sequential Recommendation
one_liner: 提出 CoRRe，在不微调 LLM 的前提下，通过共购图方向传播与流行度模长校准精炼物品嵌入，大幅提升训练自由推荐效果
practical_value: '- 在电商/推荐中，若已用 LLM 生成用户兴趣 query embedding，可对物品标题 embedding 做后处理：构建
  item-item 共购图（R^T R），做对称归一化传播，再与原始语义 embedding 加权组合，无需训练就能融合协作信号，适合作为零成本召回/粗排增强。

  - 物品流行度对检索分数影响显著，可对 embedding 模长做 popularity^alpha 校准；超参 alpha 通常取 0.05-0.2，数据集不同最优值差异大，建议按业务域单独验证。

  - 该方法证明 pre-LLM 的 RAG/rerank 注入协作信号增益有限，post-LLM 对 item 表示直接精炼更有效；在资源受限或冷启动场景可优先尝试训练-free
  后处理路线。

  - 若业务有共购/共点击数据，可以完全复用该框架：用 LLM 文本编码器得到统一向量空间，再叠加图传播与模长校准，实现快速迭代验证。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 在零样本推荐中虽能推断用户高层兴趣，但生成结果往往停留在宽泛语义层，难以区分仅在设计、颜色、季节等细微属性上不同的商品。现有训练自由方法多采用 pre-LLM 策略：先用 CF 召回候选再让 LLM 重排，或用 RAG 把协作信息塞进 prompt；这些方式对最终 item 选择的影响有限且不稳定。

## 方法关键点
- **总体范式**：CoRRe 采用 post-LLM 思路，先用 LLM 从用户交互历史生成自然语言 profile 并编码为 query embedding；物品侧用标题初始化 embedding，然后注入协作信号。
- **方向精炼**：构建 item-item 共购图 A=R^T R，计算对称归一化传播 e_GP_i = sum_j A_ij / sqrt(d_i d_j) e_SEM_j；再与原始语义 embedding 加权组合并 L2 归一化，得到方向精炼后的物品表示。
- **模长精炼**：用物品流行度 p_i 对方向精炼后的 embedding 做 p_i^alpha 缩放，调整检索分数中的流行度影响。
- **排序**：最终用 query embedding 与精炼后 item embedding 的点积进行 top-K 检索，整个过程无任何模型训练或微调。

## 实验结果
在 Amazon Reviews 的 Sports、Toys、Beauty 三个域上，对 1000 个用户做 leave-one-out 评估。
- CoRRe 在全部 12 个 training-free baseline 对比中均排名第一，相对最强 training-free 方法最高提升 132.43%。
- 与训练类方法相比，CoRRe 在 Sports 和 Toys 上取得最佳 H@10（0.0453 和 0.0507），在 Beauty 上排名第二；在 12 个训练类对比项中 8 项最优或次优。
- 消融表明：去掉图传播或原始语义 embedding 均导致性能下降，而去掉模长精炼会使指标大幅下滑，验证了方向与模长两个精炼组件都关键。

## 关键结论
在 LLM 生成语义表示之后，用共购图传播和流行度校准直接精炼物品 embedding，比在 LLM 输入前做候选重排或 RAG 注入协作信号更有效，是一条简单且实用的训练自由推荐路径。
