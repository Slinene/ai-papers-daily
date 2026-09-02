---
title: 'TGR: Advancing Industrial Recommendation from Generative-Paradigm Ranking
  toward Unified Generation and Reasoning'
title_zh: TGR：从生成式排序迈向统一生成与推理的工业推荐系统
authors:
- TGR Team
- Lei Cheng
- Haonan Hu
- Beibei Kong
- Yudong Li
- Zang Li
- Yunsheng Pang
- Hongyang Su
- Jianchao Tu
- Yunlong Wang
affiliations:
- Tencent PCG
arxiv_id: '2609.00986'
url: https://arxiv.org/abs/2609.00986
pdf_url: https://arxiv.org/pdf/2609.00986
published: '2026-09-01'
collected: '2026-09-02'
category: GenRec
direction: 生成式推荐 · 统一生成与推理
tags:
- Generative Recommendation
- Semantic ID
- Industrial Deployment
- LLM Reasoning
- Transformer Ranking
- Slate Generation
one_liner: 提出并部署覆盖生成式排序、端到端生成和推理增强的工业级生成推荐框架TGR，在腾讯多场景取得显著线上收益
practical_value: '- **CCFormer 的特征场分离交叉注意力 + 层次序列压缩**：精排模型可借鉴，避免全量 self-attention，用定向注意力流（user→seq、target→seq、target→user）处理异构特征交互，用子空间
  token mixing 处理长行为序列，再通过跨层卷积压缩保持长程依赖，训练快 2.21 倍且 GFLOPs 减半，可直接替换现有 DLRM。

  - **BARGE 的层次路径重排序**：在生成式召回（语义 ID 逐 token 解码）中，对 beam search 的候选路径做全局语义一致性重排，而不是只看累计
  log-prob，能显著减轻前缀错误传播，两个工业场景 Hit@5 提升 10–17%。

  - **HiGR 的整页生成**：把推荐列表作为一个结构化对象生成，用 coarse-to-fine decoder 分离全局 slate 规划与局部 item
  生成，再用 ORPO 直接优化列表级多目标（ranking fidelity、用户兴趣、多样性），推理快 5 倍、P99 <50ms，适合信息流/广告位布局优化。

  - **TGR-Reason 的离线推理摊销**：用 LatentRec 训练 Think 模型离线生成语义 ID 级别的 reason token，在线只作为条件注入生成器，零请求路径推理开销，冷启动新用户
  Hit@1 提升 477.8%，可直接用于电商冷启动、长尾商品推荐。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐系统长期沿用召回-粗排-精排-重排的级联架构，面临三个结构性问题：碎片化 DLRM 无 LLM 式缩放定律；阶段级优化和逐项打分忽视列表级依赖与位置效应；缺乏多模态语义和推理能力，冷启动、长尾、模糊意图场景效果差。业界正在从级联范式转向生成范式，但现有生成式推荐要么只替换单阶段，要么推理开销过大难以落地。

### 方法关键点
TGR 框架分三个方向：
- **TGR-GenRank (CCFormer)**：保留级联但替换精排模型。CCFormer 将特征分为 user/sequence/target 三组 token，使用特征场分离交叉注意力（user→seq、target→seq、target→user），避免全局 self-attention；用子空间 token mixing 高效建模长行为序列；用层次序列压缩跨层缩短序列。支持单遍并行候选打分，训练快 2.21 倍。
- **TGR-GenRec**：端到端生成，两个独立模型。**BARGE** 针对 NTP 范式中层次语义 ID 的物品边界丢失和前缀语义漂移，提出 item context-aware attention、层次路径重排序、正交双路径解码。**HiGR** 针对 NSP 范式，用 prefix-contrastive RQ-VAE 构建可控前缀语义 ID，coarse-to-fine decoder 分离整页规划与逐项生成，ORPO 列表级多目标对齐。
- **TGR-Reason**：用 LatentRec 训练 Think 模型离线生成语义 ID 推理 token，在线作为条件注入解码器，不增加请求路径推理成本。

### 关键实验
- CCFormer 在 Taobao/KuaiRec 和 40 亿样本工业数据集上超过 HSTU/OneTrans/STCA，GFLOPs 约为 HSTU 一半；五个 A/B 场景显著提升，两个全量上线（视频 CTR +3.57%，广告收入 +1.71%）。
- BARGE 在两个工业场景 Hit@5 超过 OneRec 10.2-16.9%，全量上线后 CTR +0.60%，总阅读时长 +1.70%。
- HiGR 整页生成质量比同容量 OneRec 提升 15.9-21.3%，推理快 5 倍，P99<50ms，GPU 需求降 60%；A/B 提升平均观看时长 +1.22%、视频观看数 +1.73%、CTR +0.68%、广告收入 +0.56%。
- TGR-Reason 冷启动新用户 Hit@1 提升 477.8%，线上有效消费率 +1.75%，新用户曝光到转化率 +13.09%。

### 最值得记住的一句话
生成式推荐不是单模型替换，而是一个分层栈：生成式排序先在现有级联中落地，端到端生成逐步替换召回/排序，推理能力通过离线摊销 reason token 注入而不增加线上成本。
