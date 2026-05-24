---
title: Will It Go Viral? Grounding Micro-Video Popularity Prediction on the Open Web
title_zh: 基于开放网络的微视频流行度预测
authors:
- Ryang Heo
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2605.18653'
url: https://arxiv.org/abs/2605.18653
pdf_url: https://arxiv.org/pdf/2605.18653
published: '2026-05-18'
collected: '2026-05-24'
category: RecSys
direction: 开放网络增强的流行度预测
tags:
- popularity prediction
- micro-video
- open-web context
- online adaptation
- SHORTS-CAST
- evidence-card
one_liner: 引入开放网络实时上下文与趋势感知在线适应，提升微视频流行度预测
practical_value: '- 在电商短视频推荐中，可抓取外部趋势信号（如新闻、社交媒体热度）构建类似“证据卡片”，辅助视频排序与广告出价，弥补仅依赖内容特征的不足。

  - 设计多维度外部上下文（如话题新鲜度、争议度、饱和度）的结构化表示，便于模型理解和融合，可直接借鉴到内容冷启动或实时热度预估中。

  - 在线部署时，利用延迟的播放量标签，选择性更新“上下文→流行度”映射层，仅微调少量参数即可适应趋势漂移，避免全量重训，适合高时效性场景。

  - 开源数据集 WEBSHORTS 可用于流行度预估的离线评估和在线模拟，验证外部上下文的增益。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

动机：微视频流行度受外部趋势驱动，仅靠视频内容或平台内历史检索无法判断话题当前是否在走热、争议或已饱和。现有多模态预测方法忽略实时开放网络语境。

方法：构建 WEBSHORTS 数据集，为 14K 微视频搜集上传时刻的开放网络上下文，组织成结构化“证据卡片”，覆盖三个互补维度（如新闻提及量、搜索趋势、社交媒体信号）。提出 SHORTS-CAST 框架，先基于证据卡片生成维度级理由（rationale），再输入推荐理由以指导流行度回归；部署时利用延迟到达的真实播放量标签，有选择地更新上下文到流行度的映射权重，快速适应趋势变化。

结果：在离线评估和延迟标签在线模拟中，SHORTS-CAST 均优于仅用内容、视频检索增强及标准在线适应基线，验证了结构化外部上下文与趋势感知自适应对流行度预测的必要性。
