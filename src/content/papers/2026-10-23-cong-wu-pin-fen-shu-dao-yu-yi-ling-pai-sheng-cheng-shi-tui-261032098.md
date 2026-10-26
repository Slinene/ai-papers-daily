---
title: 'From Item Scores to Semantic Tokens: Test-Time Collaborative Adaptation for
  Generative Recommendation'
title_zh: 从物品分数到语义令牌：生成式推荐的测试时协作自适应解码
authors:
- Xiongfeng Shan
- Xing Tang
- Hanchong Chen
- Fuyuan Lyu
- Lingjie Li
- Jingyan Jiang
- Duguang Liu
- Xiuqiang He
affiliations:
- Shenzhen Technology University
- McGill University
- Shenzhen University
arxiv_id: '2610.32098'
url: https://arxiv.org/abs/2610.32098
pdf_url: https://arxiv.org/pdf/2610.32098
published: '2026-10-23'
collected: '2026-10-26'
category: GenRec
direction: 生成式推荐 · 测试时协作解码
tags:
- Test-Time Adaptation
- Generative Recommendation
- Semantic ID
- Beam Search
- Discriminative-Generative Fusion
one_liner: TCBSA 将判别式分数 margin 投影到语义 ID 共享边并在 beam 剪枝前门控修正，无需重训练即可提升生成式推荐新兴兴趣发现
practical_value: '- 已有判别式模型（如 SASRec/BERT4Rec/双塔）可以在线提供全量 item score，不需要重训练生成器；把 item
  score 相对 top-R cutoff 做 margin，再投影到 semantic ID 的 prefix-token 边，就能在 beam search
  剪枝前修正路径分数，保护被生成器低估但判别器看好的候选。

  - 工程上预计算 item-to-path 查找表，测试时只算 margin 和聚合，额外成本可控；隐私和延迟敏感场景下，置信度 gate 用 max softmax
  probability 调节干预强度，避免低置信判别分数扭曲生成偏好。

  - 聚合共享边支持推荐 top-R 之外的 item，说明不需要把生成器的输出空间限制在判别器召回集合内；这对电商中新兴兴趣/长尾商品发现尤其有用。

  - 实验证明同等 beam width 下延迟增加 1.43-1.63x，但 TCBSA beam=20 比原生 TIGER beam=50 精度更高且延迟更低；在预算受限时优先用判别器信号做解码修正，而不是盲目加大
  beam。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式推荐用 semantic ID 自回归生成物品，beam search 在每一层只保留 top-B 前缀，早期剪枝不可逆。当最近交互体现新兴兴趣但更长历史偏向旧偏好时，生成器可能提前剪掉目标前缀。同一用户历史下，判别式推荐器可以全量打分并对目标排名靠前，但它的 item-level 分数无法直接作用于共享多个物品路径的 token 级决策。现有训练时方法需要改生成器，后融合又无法恢复已剪枝路径。

## 方法关键点
- **跨空间分数投影**：判别器对全 catalog 打分，取相对 top-R cutoff 的 margin（正部分），消除绝对分数偏移的影响。
- **共享边聚合**：离线构建 item-to-path 查找表，把每个 top-R 物品的 margin 沿其 semantic ID 路径投影到 prefix-token 边；用 top-M mean 或 max 聚合为 collaborative potential。共享边可让 top-R 之外的物品受益。
- **置信度门控**：用 max softmax probability 作为置信度代理，经 sigmoid 缩放得到干预强度 η，低置信时自动减弱修正，避免扭曲原生 beam 分数。
- **剪枝前修正**：在每层 beam 选择前，将 original cumulative log-prob 加上 η * 边 potential，再取 top-B。整个生成器和判别器保持冻结。

## 关键实验
在 Amazon Science/Music/Office 和 Yelp 四个数据集上做全 catalog 评估，对比 GRU4Rec、SASRec、BERT4Rec、TIGER、HSTU、MiniOneRec、Human-Prior、APAO 和 MemGen。三种配对（TIGER-SASRec, TIGER-GRU4Rec, MiniOneRec-SASRec）在全部 16 个 dataset-metric 上取得最优，14 个显著超越最强 baseline。新兴兴趣子集上，TCBSA 相对 TIGER 的 NDCG@10 提升 Science 16.29%/31.95%、Yelp 76.31%/103.29%。解码分析显示目标前缀存活率提升 24.4%，且正确推荐中有 0.86%-5.16% 位于判别器 top-R 之外。消融证明移除置信度门控下降 1.88%-9.08%，移除目标路径的共享边修正使 outside-set hits 损失 28-30%。

## 最值得记住的一句话
在 semantic ID 生成推荐的 beam search 剪枝前，把判别式分数 margin 投影到共享语义边并做置信度门控修正，是一种训练无关、可跨模型复用的测试时协作范式，对新兴兴趣和长尾推荐尤其有效。
