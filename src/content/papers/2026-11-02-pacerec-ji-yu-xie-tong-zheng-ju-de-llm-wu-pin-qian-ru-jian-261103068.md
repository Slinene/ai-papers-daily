---
title: 'PACERec: Progressive Adaptation of LLM Item Embeddings with Collaborative
  Evidence for Recommendation'
title_zh: PACERec：基于协同证据的 LLM 物品嵌入渐进自适应用于推荐
authors:
- Junzhao Huang
- Xi Wu
- Zihan Wang
- Zijing Wang
- Ming Wang
- Kang Liu
- Xiaocui Yang
- Shi Feng
- Daling Wang
- Yifei Zhang
affiliations:
- Northeastern University
- Ant Group
arxiv_id: '2611.03068'
url: https://arxiv.org/abs/2611.03068
pdf_url: https://arxiv.org/pdf/2611.03068
published: '2026-11-02'
collected: '2026-11-03'
category: RecSys
direction: LLM 表征适应 · 长尾序列推荐
tags:
- Sequential Recommendation
- LLM Embeddings
- Flow Matching
- Long-tail
- ID-free
- Item Representation
one_liner: 用 flow matching 学共享速度场，将静态 LLM 物品嵌入渐进适配前序行为目标，实现无 ID 长尾序列推荐
practical_value: '- **电商冷启动 / 长尾 item 可直接复用无 ID 思路**：用 frozen LLM embedding 对商品标题/描述编码，经两层
  MLP 降维到推荐主模型维度，PCA 初始化投影层保留语义几何；新商品只要有过文本属性就能拿到有效表示，避免长尾 ID embedding 欠训。

  - **离线构造行为目标成本低且有效**：对每个 item，取训练序列中它前面 L 步内的前驱 item 初始语义向量，按 recency 指数加权平均 + norm
  matching + clip，生成固定的 behavior target；这相当于给每个 item 一个“用户接下来会买什么”的监督信号，可以离线一次算好，训练时直接当
  flow matching 的 target。

  - **只对频繁 item 监督、共享速度场推断长尾**：设置频次阈值 κ，只让 c_i≥κ 的 item 参与 flow matching，loss 用 sqrt(c_i/(c_i+c0))
  做 confidence weighting；学到的 velocity field 以 item semantic source 为条件，长尾甚至零交互 item
  也能直接过 flow 得到行为适应表示。工程上可离线缓存全量 adapted embeddings 供后续双塔/序列模型使用。

  - **排序层加参数无关语义相似度旁路**：在 frozen LLM 空间对用户最近 history 加权池化得到 semantic query，与候选 item
  cosine 相似度做 per-user z-score 标准化，再和 preference score 加权融合。这个旁路对 tail 指标提升明显，权重用
  validation 上固定值选择即可，不需要可学习参数，部署简单。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM item embedding 在序列推荐里被用来补充稀疏交互，但它只表达静态内容相似度，和用户连续偏好转移冲突：例如买相机后更可能买镜头，而不是另一个语义相似的相机。文章在 Yelp/Food/Beauty 上测量发现，frozen LLM 空间的 K 近邻对训练前驱 item 的覆盖率仅 1.59%–5.22%（K=20），而高频前驱参考可达 57%–68%。现有方法要么保留 ID embedding 融合语义，长尾仍欠训；要么只做全局几何校准，缺少前序交互上下文的显式监督。

### 方法关键点
- **语义源**：frozen LLM embedding 经两层 MLP 降维到 d=256，PCA 初始化保持主要语义几何。
- **行为目标**：对每个 item，取训练序列中它前 L 个 lag 内的前驱 item 的初始语义向量，按 recency 指数衰减加权池化，再做 norm matching 和 clip，得到固定 behavior target。
- **渐进适应 flow**：用 source-conditioned flow matching 学共享速度场 vθ(z, xi, t)，从 semantic source xi 逐步走到 behavior target pi；只用训练频次 c_i≥κ 的 item 监督，frequency-weighted，S=2 步 Euler 更新；对位移做 tanh 径向 bound 防止漂移。
- **训练约束**：语义 anchor 惩罚当前 source xi 偏离初始 PCA 表示 xi^(0)；正样本按 c_med/c_i 加权，强调长尾。
- **用户与排序**：用户表示 = 序列 backbone 最后 hidden state + recency-weighted intent residual；候选分 = preference score + λ × 参数无关 semantic similarity score（frozen LLM 空间 cosine 相似度做 per-user 标准化）。

### 关键实验与结果
在 Yelp、Food、Beauty 三个数据集，SASRec、FMLP-Rec、LRURec 三个 backbone 上，PACERec 在 Overall/Tail Hit@10 和 NDCG@10 全部 9 个 setting 优于最强 baseline。Overall NDCG@10 平均相对提升 13.53%，Tail NDCG@10 平均相对提升 33.31%；Yelp 上 Tail NDCG@10 相对 FAERec 提升 71%–79%。消融显示去掉 flow 适配会使 Tail NDCG@10 下降 8.6%–10.1%，去掉 semantic anchor 下降 6.2%–8.5%。更换为 Qwen3-4B 或 Llama-NV-Embed-Reasoning-3B 的 frozen embedding 后，PACERec 仍一致优于 FAERec。

### 最值得记住的一句话
把“item 的前序交互上下文”作为行为目标，用共享 flow matching 只从高频 item 学语义→行为的适应方向，可以无 ID 地把协同转移模式泛化到长尾和冷启动 item。
