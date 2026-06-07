---
title: 'To Be Multimodal or Not to Be: Query-Adaptive Audio-Visual Person Retrieval
  via Active Modality Detection'
title_zh: 多模态还是单模态？查询自适应音视频人物检索的主动模态检测
authors:
- Erfan Loweimi
- Mengjie Qian
- Kate Knill
- Guanfeng Wu
- Chi-Ho Chan
- Abbas Haider
- Muhammad Awan
- Josef Kittler
- Hui Wang
- Mark Gales
affiliations:
- University of Cambridge
- Queen's University Belfast
- University of Surrey
- Cisco
- Southwest Jiaotong University
arxiv_id: '2606.05931'
url: https://arxiv.org/abs/2606.05931
pdf_url: https://arxiv.org/pdf/2606.05931
published: '2026-06-04'
collected: '2026-06-07'
category: Multimodal
direction: 多模态自适应融合 · 主动模态检测
tags:
- Multimodal retrieval
- Active modality detection
- Query-adaptive fusion
- Speaker embedding
- Face embedding
- Broadcast archive
one_liner: 通过跨模态得分一致性检测活跃模态，避免缺失模态噪声，检索精度显著提升
practical_value: '- 多模态推荐中的缺失噪声抑制：当商品图片模糊或文本描述缺失时，可借鉴跨模态一致性检测，通过联合检索得分对齐度判断模态可用性，动态选择单模态或加权融合，避免固定融合引入噪声。

  - 轻量级模态活跃度门控：训练一个分类器，输入两模态的检索得分分布、顺序统计量等特征，输出模态活跃概率，作为后续融合的软开关，可集成到现有推荐架构中，实现查询级自适应。

  - 生成式推荐中的应用：在利用文本与图像生成商品描述时，可藉此判断输入模态的质量，引导生成过程忽略不可靠的模态信息，提高生成准确性。

  - 架构迁移：该方法不依赖特定模态编码器，只需单模态检索分数即可构建跨模态特征，适合在已有检索流上快速部署，无需改动底层模型。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：真实视频档案（如 BBC Rewind）中目标人物可能只出声音、只露面或两者兼有，强制融合语音和面部特征会因缺失模态引入噪声，反而降低检索精度。

**方法**：提出查询自适应框架，核心是**主动模态检测**——利用跨模态得分一致性判断各模态是否活跃。当两个模态都有效时，一个模态检索出的高分文件在另一模态下同样得分高；若一致性被打破，说明某模态缺失。基于此构建分类器，输入为两模态检索得分列表的统计特征，输出模态活跃状态。检测准确率达 89%。在活跃模态确定后，自适应系统仅融合两者均活跃时的得分，否则退回单模态最佳结果。

**结果**：在超过 12,000 个广播视频的 BBC Rewind 语料上，自适应系统取得 P@1 94.2%，远优于单一语音 (82.9%)、单一面部 (93.4%) 和固定融合 (90.0%)，并恢复至有真实模态标签的 Oracle 系统 (96.6%) 之间差距的 64%。
