---
title: 'OptST: Optimizing Semantic Tokenization for LLM-Enhanced Recommendation'
title_zh: OptST：面向 LLM 增强推荐的语义分词优化
authors:
- Hanchong Chen
- Jie Liu
- Fuyuan Lyu
- Dugang Liu
- Lingjie Li
- Xiuqiang He
- Xing Tang
affiliations:
- Shenzhen Technology University
- The Hong Kong Polytechnic University
- McGill University
- Shenzhen University
arxiv_id: '2611.07523'
url: https://arxiv.org/abs/2611.07523
pdf_url: https://arxiv.org/pdf/2611.07523
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: 语义分词 · 下游任务感知适配
tags:
- Semantic Tokenization
- RQ-VAE
- LLM-enhanced Recommendation
- Straight-Through Estimator
- Low-Rank Adaptation
- CTR Prediction
one_liner: 让预训练语义 tokenizer 在下游推荐监督下做低秩几何适配与交互条件深度选择，AUC 全面超越基线
practical_value: '- 将 LLM 生成的 user/item 语义 embedding 离线用 RQ-VAE 离散化为 semantic tokens，再作为
  categorical 特征进 CTR/排序模型；比连续 dense 向量更省内存和带宽，且 encoder/codebook 冻结，线上只需 token ID
  和 lookup embedding。

  - 不要只把 token 当固定特征：可以用共享低秩变换 C0+C0UV + anchor loss，让下游点击/转化损失通过 STE 微调 codebook
  几何；每层仅 2dr 参数，与码本大小 K 无关，适合作为轻量插件部署。

  - 交互级 prefix depth gate 提供自适应语义分辨率：输入 residual norm、最近/次近码距、user/item log-frequency、layer
  position 等轻量特征，可迁移到广告/push 的个性化特征粒度控制，减少深层冗余 token。

  - 方法对 backbone 无关，可挂在 DCN/DeepFM/AutoInt 等主流排序模型上，AUC 在多个数据集稳定提升；即使在 UserIP 等强离散语义基线基础上仍有明显增益。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
在大规模 LLM 增强推荐中，连续 dense 语义向量缓存和读取成本高；RQ-VAE 语义分词能提供紧凑离散接口，但常见两阶段管道把 token assignment 固定，下游推荐只能学习如何利用已有索引，无法修改语义分区；同时固定 token depth 对所有交互暴露相同语义分辨率。

**方法关键点**
- 冻结预训练 RQ-VAE encoder 和 base codebooks，逐层学习共享低秩变换：C̃_ℓ = C0_ℓ + C0_ℓ U_ℓ V_ℓ，U/V 分别为 d×r 与 r×d，r≪d，每层仅 2dr 参数量，与码本大小 K 无关。
- anchor loss 限制 effective codebook 整体位移和近邻余弦相似度变化，防止几何扭曲偏离预训练语义。
- hard nearest-code assignment 保留在 forward，soft assignment 用于 backward，即 straight-through estimator，使推荐 loss 能通过 softmax(-δ/τ) 回流到低秩因子和 lookup embeddings。
- 交互条件 prefix gate 依据 residual norm、相对 residual、与胜出码向量余弦、最近两次距离间隔、user/item log-frequency、layer position 做 stop/continue 决策；同样用 STE，depth loss 防止默认全深度。
- 最终 semantic feature 是选中 prefix 内 hard token lookup 的和，与 ID 等结构化特征拼入推荐 backbone。

**关键结果与数字**
在 Movies/Yelp/Games/Clothing 四数据集上，OptST AUC 分别为 0.8237/0.7420/0.7532/0.6380，全面超过 13 个 shallow/deep/LLM 增强基线；相对最强 LLM 基线 UserIP 分别提升 +0.0021/+0.0021/+0.0044/+0.0056。多 backbone 实验在 AutoInt/DeepFM/DCNv2/xDeepFM/FinalMLP 上均获 AUC 提升。消融显示 codebook adaptation 是主要收益来源，prefix gate 提供互补；共享低秩策略优于自由更新和逐项加法低秩；对 Qwen3 不同尺寸和 Llama-2-7B 均稳定。

**最值得记住的一句话**
下游推荐损失通过 STE 重塑 token assignment 几何，而低秩 + anchor 约束保证不破坏预训练语义结构。
