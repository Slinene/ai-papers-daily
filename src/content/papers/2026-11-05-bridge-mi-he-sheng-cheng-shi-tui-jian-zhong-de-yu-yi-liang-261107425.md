---
title: 'BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation'
title_zh: BRIDGE：弥合生成式推荐中的语义量化鸿沟
authors:
- Yatong Xiao
- Mingjie Sun
- Peng Wang
- Wenjin Wu
- Peng Jiang
affiliations:
- Kuaishou Technology
arxiv_id: '2611.07425'
url: https://arxiv.org/abs/2611.07425
pdf_url: https://arxiv.org/pdf/2611.07425
published: '2026-11-05'
collected: '2026-11-06'
category: GenRec
direction: 生成式推荐 · Semantic ID
tags:
- Generative Recommendation
- Semantic ID
- RQ-VAE
- EMA Distillation
- Recurrent Decoder
- E-commerce Advertising
one_liner: 识别生成式推荐的语义量化鸿沟，从语义锚定、邻域蒸馏与难度感知递归三方面弥合
practical_value: '- 生成式召回里别只盯着 SID tokenization 质量：RQ-VAE 的 codebook centroids 和 item
  邻域结构是廉价高价值训练信号。可以对 level-1 centroids 做一次 coarse clustering（如 Vc=256），在 decoder 首
  token 前增加 latent reasoning slot，并用 prototype CE + cosine regression 做训练期锚定；线上不依赖目标侧标签，增量实现较轻，离线
  R@10 提升约 +10%。

  - 有现成 item embedding 库时，可以用 EMA teacher + 训练期目标 item top-k 语义近邻作为 privileged input，配合
  on-policy student 做 JSD 蒸馏；这能同时缓解 teacher forcing exposure bias 和一 hot 监督丢失邻域几何的问题。注意用
  entropy gate 和 distillation warm-up，避免早期 teacher 不可靠伤害训练。

  - 层级 SID 生成天然有难度递减先验，不要对每级用一样深度。共享 weight loop decoder + right-aligned 调度（如 m=4/2/1）可让粗粒度首级获得更多迭代、后续残差级少算，较固定深度节省参数并提升
  QPS；适合广告多候选生成和轻量部署。

  - 离线指标之外，线上 A/B 在 eCPM 上 0.65% 收益是重要的工程信号。如果业务已经在做生成式广告召回，建议优先尝试 CGLR，因为实现最轻且离线信号明确；再叠加
  PESD 与 EAR 做增量收益验证。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

生成式推荐用 RQ-VAE 将 item 编码为层级 Semantic IDs，decoder 逐级生成。但量化阶段利用了丰富的连续信号：codebook centroids、邻域几何、逐级熵；decoder 只接收离散 ID，形成 Semantic Quantization Gap（SQG）。作者将其分解为：grounding gap，首级 SID 高熵且缺乏语义锚；neighborhood gap，one-hot 监督丢弃 item 相似度并加剧 teacher forcing exposure bias；difficulty gap，计算均匀分配，但越早层级越难。

**方法关键点**

- Codebook-Grounded Latent Reasoning（CGLR）：SID 生成前用共享 LoopDec 迭代 R=4 次产生 latent representation r；将 level-1 centroids 再聚类为 Vc=256 个 coarse prototypes，用 prototype CE + cosine regression 锚定 r，把量化 codebook 变成训练期语义接口。
- Privileged EMA Self-Distillation（PESD）：EMA teacher 在训练期接收目标 item top-3 语义邻居均值作为 privileged input；on-policy student 用 symmetrized JSD + reason cosine distillation 向 teacher 学习；entropy gate 与 warm-up 稳定早期训练。
- Effort-Aware Recurrence（EAR）：right-aligned loop schedule m=(4,2,1)，共享 3 层 LoopDec，首级更多迭代、后续递减；参数不随迭代增加，相比 GR4AD 的 9 层 decoder 参数少 57.3%，在线 QPS 高约 20%。

**关键实验**

在 Amazon Beauty、Sports、Toys 上对比 TIGER、ReaRec、COBRA、GR4AD 等，Recall@10 提升 7.8%–12.6%，NDCG@10 提升 8.0%–10.7%；相对最强 baseline 平均 +10.9% / +9.7%。消融显示 CGLR 单独带来 Beauty R@10 +10.5%，PESD 单独 +5.4%。短视频电商广告平台 5% 流量线上 A/B eCPM +0.65%。

**最值得记住的一句话**：生成式推荐的真正瓶颈不仅在 tokenization，而在 quantizer 与 decoder 之间的语义信息不对称；显式注入 codebook geometry、neighborhood soft targets 与层级难度先验，可以在不增加参数甚至降低推理成本下获得一致收益。
