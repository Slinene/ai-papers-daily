---
title: What Would You Click? Personalized Video Thumbnail Generation with Preference-aware
  Highlight Retrieval
title_zh: 个性化视频缩略图生成：偏好感知高亮检索与可控生成
authors:
- Zhiyu He
- Zecheng Zhao
- Tong Chen
- Zi Huang
- Yiqun Liu
- Min Zhang
arxiv_id: '2607.12882'
url: https://arxiv.org/abs/2607.12882
pdf_url: https://arxiv.org/pdf/2607.12882
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 个性化视觉内容生成·高亮检索
tags:
- personalized generation
- highlight retrieval
- video thumbnail
- diffusion models
- VLM-guided
- click engagement
one_liner: 提出个性化视频缩略图生成任务，结合用户偏好高亮帧检索和VLM引导扩散生成，显著提升点击偏好
practical_value: '- 广告/商品创意图个性化：借鉴偏好感知检索，根据用户历史行为选择视频/图像中的关键区域（锚点），再用生成模型个性化重构，例如动态广告图生成。

  - 两阶段解耦架构：检索阶段融合用户交互和内容语义，生成阶段注入VLM提取的语义线索，可提高生成结果的相关性和质量。

  - 面向点击优化：通过用户研究直接验证个性化缩略图能提升点击率，类似方法可用于电商搜索推荐中的创意元素个性化（如主图背景、文案风格）。

  - 技术细节：使用扩散模型基于锚点图像指导生成，结合文本提示（如VLM描述）控制风格，可迁移至商品场景图的个性化生成。'
score: 8
source: arxiv-cs.IR
depth: abstract
---

动机：视频缩略图是吸引点击的关键，但现有自动生成方法产生通用结果，忽视用户个体偏好，限制点击率优化。为此提出个性化视频缩略图生成新任务，需解决两大挑战：如何从视频中选取既个性化又信息丰富的关键帧作为锚点，以及如何基于锚点生成视觉连贯且忠于原视频的缩略图。
方法：提出两阶段框架，紧密耦合偏好感知检索与可控生成。第一阶段设计个性化高亮检索器，建模细粒度用户-视频交互，并引入视频摘要语义，实现选择与用户偏好和视频上下文匹配的多样化锚点帧。第二阶段利用VLM引导的扩散生成管线，从锚点帧提取语义视觉线索并注入生成过程，在提升个性化程度的同时保持视觉一致性和内容保真度。
结果：在两个公开视频数据集上，方法在检索和生成基线中均取得SOTA性能。用户研究进一步表明，所生成的个性化缩略图显著提升用户的点击偏好，验证其在增强用户参与方面的有效性。
