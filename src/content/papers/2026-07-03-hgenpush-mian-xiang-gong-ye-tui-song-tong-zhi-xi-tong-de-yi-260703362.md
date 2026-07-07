---
title: 'HGenPush: A Heterogeneous Generative Recommendation Architecture for Industrial
  Push Notification Systems'
title_zh: HGenPush：面向工业推送通知系统的异构生成式推荐架构
authors:
- Xiao Liang
- Jiali Feng
- Xin Feng
- Yiqing Wang
- Baolin Ye
- Siyao Feng
- Zhihui Deng
- Cunyi Zhang
- Huajin Sun
- Xuanping Li
affiliations:
- Kuaishou Technology
arxiv_id: '2607.03362'
url: https://arxiv.org/abs/2607.03362
pdf_url: https://arxiv.org/pdf/2607.03362
published: '2026-07-03'
collected: '2026-07-07'
category: GenRec
direction: 生成式推荐 · 异构内容联合生成
tags:
- Generative Recommendation
- Semantic ID
- Multi-Token Prediction
- Push Notification
- Reinforcement Learning
- Decoder-Only
one_liner: 解耦自回归生成，以链式多token预测和行为偏好对齐统一推荐视频与作者，快手推送获+0.181% DAU提升。
practical_value: '- **链式多token预测（Chained-MTP）替代自回归**：用稳定的用户兴趣表示作为全局上下文，叠加前序语义ID的累计嵌入来建模层级依赖，整个序列的token可并行预测。相比Transformer级联方式，推理吞吐提升34%，效果基本持平，很适合需要高QPS的生成式推荐落地。

  - **异构目标统一生成**：对作者（或店铺、媒体源）采用行为偏好对齐得到偏好感知的embedding，经RQ-Kmeans离散化为语义ID，再与视频一级语义ID拼接成混合ID，用同一个decoder生成。这样在系统中自然融合商品推荐与信任源推荐，可直接借鉴到电商中“商品+店铺”或“文章+作者”的组合推荐。

  - **用户消费偏好对齐（UCPA + GSISPO）**：用点击后会话中真实消费行为（播放完成、点赞、转发等）作为奖励信号，序列级计算重要性采样权重并裁剪，避免token级优化的语义碎片化，同时保留高价值长尾行为的梯度。该RL对齐方案无需额外critic网络，能有效抑制标题党，提升深度消费指标。

  - **多场景多视角行为融合**：将长/短期feed行为、推送点击行为、推送发送行为与用户静态特征串联输入causal decoder，分别抽取[cls]表示供不同生成分支使用。这种跨场景行为组合及特殊token设计，可迁移到需要跨业务线联合建模的用户理解模块。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
短视频平台用户既想要高质量内容，也倾向追随可信作者。现有生成式推荐（如TIGER、OneRec）仅处理单一类型目标，且采用自回归方式逐token生成语义ID，推理效率低，难以满足工业推送对延迟和吞吐的要求。为此，论文提出端到端的异构生成式推荐架构HGenPush，旨在一个模型中同时完成视频和作者的推荐，并大幅提升生成速度。

**方法关键点**
- **混合用户行为理解**：融合长/短期feed序列、push点击序列、push发送序列及用户静态特征，通过decoder-only Transformer生成用户兴趣表示，输出两个特殊token cls_v 和 cls_a 分别用于视频和作者推荐。
- **视频推荐分支（Chained-MTP）**：以cls_v 为稳定兴趣锚点，对目标视频的每一层语义ID，通过累加已预测token的嵌入来建模不同粒度间的依赖，所有token并行通过FC层生成。训练用交叉熵，推理直接一次前向得到全部语义ID，完全摒弃自回归。
- **作者推荐分支**：先将作者特征与cls_a 对齐（InfoNCE loss），得到偏好感知的作者表示，再用RQ-Kmeans在线离散化为作者语义ID。最终生成目标为混合ID（作者ID + 视频第一层ID），使推荐可直接指向信任作者的特定视频。
- **用户消费偏好对齐（UCPA）**：基于点击后会话中的消费行为（完整播放、点赞、转发等）定义规则奖励，提出GSISPO算法进行序列级RL优化，对重要性采样权重截断以保证梯度稳定，提升内容满意度而非单纯点击。

**关键实验与数字**
在快手推送系统数据集上，离线视频分支HitRate@100达0.3915，作者分支达0.4848，均优于TIGER和SASRec。Chained-MTP较DeepSeek-MTP效果持平而QPS提升33.86%。在线A/B测试完整方案（视频+UCPA+作者）相比生产基线取得：DAU +0.181%，CTR +1.577%，App使用时长 +0.148%，且各消费深度指标显著正向（转发率+7.57%）。
