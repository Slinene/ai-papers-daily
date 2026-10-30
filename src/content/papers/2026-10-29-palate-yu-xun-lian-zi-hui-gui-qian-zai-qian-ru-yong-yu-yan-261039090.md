---
title: 'PALATE: Pretrained Autoregressive LATent Embeddings'
title_zh: PALATE：预训练自回归潜在嵌入用于广告排序
authors:
- Sizhang Zhao
- Praveen Gondhi
- Bin Li
- Utsaw Kumar
affiliations:
- DoorDash
arxiv_id: '2610.39090'
url: https://arxiv.org/abs/2610.39090
pdf_url: https://arxiv.org/pdf/2610.39090
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 生成式用户表示 · 广告排序
tags:
- generative user representation
- sequential recommendation
- ads ranking
- sampled softmax
- exploration weighting
- frozen embeddings
one_liner: 用 GPT 式序列模型学习用户门店互动，以 last-token 隐藏向量作为冻结用户表示接入排序，双场景显著提升收入与转化
practical_value: '- 冻结用户 embedding + daily batch inference 是低成本把序列个性化接入多 surface 的方式：比在每个
  ranker 内建 DIN/Transformer 更易维护，DIN 增量仅 +0.03%，证明一个共享表示可覆盖大部分收益。

  - 在复购/重购型电商，用探索加权 loss 打破 repeat 主导：对新商家/新交互给 9:1 或 3:1 的权重，能明显提升对新商品的召回和新意图表达；业务上对应拉新/发现场景。

  - 负样本设计可替代 exact softmax：固定热门池 + 曝光未转化 + random + in-batch，成本低且 Recall 更好；对高基数 item
  vocab 的场景可直接迁移。

  - 两阶段课程：先 click 预训练再 conversion 微调，并 warm-start，可以保留浏览广度同时锐化转化意图；适合有 click→purchase
  漏斗的电商/广告场景。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机：**
DoorDash 广告排序需要强个性化，但消费者历史稀疏、门店空间高基数，且复购行为在总互动中占主导；生产 ranker 只用手工聚合特征、类别 embedding 和 order-agnostic 的 pooled history，没有 learned per-consumer 序列表示。希望有一个统一、可复用的用户 embedding，同时服务 Discovery 和 Search 两个意图相反的场景。

**方法关键点：**
- 用 GPT 式 decoder-only Transformer 建模消费者门店互动序列：每个位置由 store id、business id 和 5 个上下文特征拼接后投影到 768-d trunk；3 层、3 头×256，context 200。
- 预测目标为下几步的 business 粒度而非 store，输出 256-d last-token hidden state 作为用户 embedding；softmax 层行向量作为 business embedding，与用户向量同空间。
- 训练目标使用 sampled softmax，负样本由固定热门商家池（约 60K）、曝光未下单商家、random 和 in-batch 组成；多步预测 horizon 权重 α1=1，α≥2=0.5。
- 复购主导领域引入探索加权：新商家 target 权重 0.9，重复商家 0.1，迫使表示偏向发现；两阶段 curriculum 先 click 预训练再 conversion fine-tune，并从 click 检查点 warm start。
- 下游以 frozen 特征进入 DCNv2 ranker：输入 u, c, u⊙c, cos(u,c)，不回流梯度；每日批量推理刷新，供双 surface 共享。

**关键实验：**
- Intrinsic：hard negatives 使 R@10 提升 +14.3%；探索加权 9:1 使新商家 R@10 提升 +29.1%，但整体 recall 下降；full softmax 虽降 perplexity，但 conversion recall 持平，生产成本保留 sampled softmax。
- Extrinsic：冻结用户 embedding 是 DCNv2 排序 ladder 中最大单特征增益，Discovery relative Eval-AUC +0.59%、Search +0.57%；uniform weighting 无增益，9:1 探索加权才有效；再加 DIN 仅 +0.03%。
- Online：作为 bundled ranker retrain 一部分，Discovery revenue +0.79%、CVR +1.17%；Search revenue +0.94%、CVR +1.50%。

**最值得记住的一句话：**
在复购型电商广告排序中，用一个每日刷新的冻结生成式用户向量可以替代每个 surface 独立序列建模，且探索加权与硬负样本设计是让 embedding 具备发现能力的关键。
