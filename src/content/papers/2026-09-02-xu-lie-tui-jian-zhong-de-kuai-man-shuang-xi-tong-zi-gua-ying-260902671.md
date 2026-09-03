---
title: Recommender System as Slow and Fast Thinkers
title_zh: 序列推荐中的快慢双系统自适应推理框架
authors:
- Zichen Yuan
- Xiaoxuan Dong
- Linkun Dai
- Jinwei Yang
- Jining Luan
- Dexu Yu
- Chunxiao Li
- Joemon M. Jose
- Youhua Li
- Hanwen Du
affiliations:
- City University of Hong Kong
- University of Electronic Science and Technology of China
- Shanghai Jiao Tong University
- Fenz.AI
- University of Science and Technology of China
arxiv_id: '2609.02671'
url: https://arxiv.org/abs/2609.02671
pdf_url: https://arxiv.org/pdf/2609.02671
published: '2026-09-02'
collected: '2026-09-03'
category: RecSys
direction: 自适应快慢推理 · 序列推荐
tags:
- Sequential Recommendation
- Adaptive Inference
- Conditional Computation
- Dual System
- Latent Refinement
- Routing
one_liner: 提出 DS-Frame 插件式快慢推理框架，用样本级路由只对难样本做多步 latent refinement，在 SASRec/BERT4Rec
  上平均提升约 7%
practical_value: '- 在不改主排序模型架构的前提下，把「一次性前向」升级为「共享 encoder + 轻量 slow path + 路由 gate」。线上可以按
  latency budget 调整慢路径激活率或阈值，适合精排/粗排做样本级算力分配。

  - Selector 训练直接用 fast/slow 的 loss + 成本比较构造 oracle 标签，再用 budget regularizer 约束激活率；这种方法不用额外标注，业务里可先在离线训练
  gate，在线只过 MLP，成本可控且路由可解释。

  - Slow System 不重新 encode 整条用户序列，而是在共享表示后逐步拼接 reasoning token 做 latent refinement；配合
  step embedding、KL 连续性和渐进温度退火，能稳定多步推理。可迁移到 LLM-based Rec 或 Agent 生成中间推理轨迹时稳定输出。

  - 评估不仅看整体 NDCG/HR，还按用户历史长度和物品流行度分层看 group-wise 收益。电商推荐中长历史、小众兴趣用户往往是难例，这种分层能直接看到自适应推理是否真的补到短板。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
静态序列推荐对所有样本使用同一条计算图，但用户环境高度异质。论文先在 SASRec 和 BERT4Rec 上按交互长度、历史物品流行度分层评估：长历史或小众兴趣用户构成 challenging 环境，NDCG@10 相对下滑 13.7%–22.0%。这说明问题不只是某些用户难预测，而是静态推理没有把额外算力分配给真正需要它的样本。

**方法关键点**
- 共享 Transformer encoder 得到用户序列表示，Fast System 直接做 next-item 预测。
- Slow System 在原始序列后逐步加入 reasoning token，进行 K 步 latent refinement；步骤间共享参数，并通过多步监督、KL 连续性正则和渐进温度退火稳定推理过程。
- Selector 是轻量 MLP，只用共享表示做路由。训练时以 fast/slow 的 loss + 归一化成本构造 oracle 标签，再用预算正则约束慢路径激活率；推理时仅过 gate，不依赖 ground-truth。
- 框架对 backbone 无侵入，可直接插到 SASRec、BERT4Rec 等模型上。

**关键实验**
在 Yelp 和 Amazon Video Games/Beauty/Sports/Toys 五个真实数据集上，DS-Frame 让 SASRec 平均 NDCG@10 提升 7.5%、NDCG@20 提升 6.6%；BERT4Rec 分别提升 6.7%、6.3%。分组看，challenging 用户增益显著更大：SASRec 从 common +3.3% 升到 challenging +8.4%，BERT4Rec 从 +3.2% 升到 +8.5%。在 Beauty 上，learned selector 在 40.2% 慢路径激活率下达到 0.0453 NDCG@10，明显优于同预算的 random routing，并接近 oracle upper bound；40%–60% 预算的 select routing 已超过全量 Slow Only。

**最值得记住的一句话**
把推荐推理从「所有用户同一次前向」升级为「按样本预期收益分配慢计算」，是用可控成本换取长历史、小众偏好等难用户上显著收益的有效路径。
