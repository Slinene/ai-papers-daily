---
title: Diverse-Teacher On-Policy Distillation for Generative Recommendation
title_zh: 多样教师在线策略蒸馏用于生成式推荐
authors:
- Zhipeng Yi
- Xinyu Lin
- Minxuan Shan
- Zipeng Chen
- Yujiao Zhao
- Chuanyu Xu
- Wenjie Wang
affiliations:
- University of Science and Technology of China
- National University of Singapore
- Alibaba Group
arxiv_id: '2611.03272'
url: https://arxiv.org/abs/2611.03272
pdf_url: https://arxiv.org/pdf/2611.03272
published: '2026-11-02'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · On-Policy Distillation 消偏
tags:
- Generative Recommendation
- On-Policy Distillation
- Popularity Bias
- Semantic ID
- Knowledge Distillation
- Diversity
one_liner: 提出 HERO，通过异构教师路由和多样性物品 rollout 缓解生成式推荐中 on-policy distillation 的流行度偏差
practical_value: '- 在生成式推荐做蒸馏时，不要用单一教师，可以按物品流行度分组训练两个专家教师（head/tail），训练样本根据 ground-truth
  item 的流行度路由到对应教师，能有效缓解头部偏差。

  - 在 on-policy 训练中，学生生成的路径容易偏向头部物品，导致冷门 SID 路径很少被监督。可额外将冷门物品的真实 SID 前缀加入蒸馏损失（tail-path
  GT-KL），提高尾部路径的覆盖率。

  - 该方法只更新学生模型，教师冻结，推理时仅用学生，不增加在线推理成本，工程实现简单，适合快速上线验证。

  - 评估生成式推荐时不要只看整体 Hit，应同时关注 DTR（需求-曝光比）和 ORR（头部重复推荐占比），避免准确率提升掩盖流行度偏差的加剧。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式推荐用 Semantic ID 直接生成下一物品，相比 SFT 的 one-hot 监督，on-policy distillation (OPD) 提供教师模型在所有 token 上的概率分布，训练更高效、收敛更快。但 OPD 会加剧流行度偏差：教师反馈偏向热门物品 token，学生生成也偏向热门，导致冷门 SID 路径几乎不被生成和监督，形成偏差放大循环。本工作针对该问题，从教师来源和 rollout 数据覆盖两个角度设计消偏方案。

## 方法关键点
- **异构教师蒸馏**：训练两个教师模型，分别专精热门和冷门物品。每个训练样本根据 ground-truth item 的流行度分组路由到对应教师，用该教师的 next-token 分布监督学生。
- **多教师 OPD**：学生通过 trie-constrained beam search 生成多个 SID 轨迹，在每个生成 prefix 上与路由教师的分布计算 forward KL，作为 rollout loss。
- **多样性物品 rollout**：除学生生成路径外，对冷门样本额外加入 ground-truth SID 路径的 KL 损失，保证冷门路径获得监督；同时保留所有样本的 ground-truth CE loss。
- 总损失为 `L = L_rollout + L_GT-CE + I[g=t] * L_tail-GT-KL`，只更新学生，教师冻结。

## 关键实验
- 数据集：1688 工业数据 + Amazon Beauty/Pet、MovieLens-1M 三个公开数据集。
- 对比 baseline：SASRec、TIGER、SFT、SFT++、GT-KD、Off-policy KD、GKD、MOPD、SID-GRPO、Ghost-AUO、BEAR。
- HERO 在 1688 上 Click Hit@240 达 0.5819（GKD 0.5786），Tail Click Hit@240 达 0.5416（GKD 0.5301），DTR* 0.3920 最接近 1，ORR 0.0025 较低；公开数据集上整体和尾部 Hit@20 均为最佳。
- 在线 A/B：在 1688 首页“猜你喜欢”模块部署，15 天实验 GMV 提升 3.412%（p=0.0104）。
- 消融显示移除 rollout KL 尾部准确率下降最大，异构教师路由优于单一教师或固定混合，tail-path GT-KL 显著提高冷门前缀覆盖率。

## 最值得记住的一句话
OPD 的稠密监督优势值得保留，但必须同时解决教师偏好和 rollout 覆盖两个偏差源，否则会放大头部集中。
