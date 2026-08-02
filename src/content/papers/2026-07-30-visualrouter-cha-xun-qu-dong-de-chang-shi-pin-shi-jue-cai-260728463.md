---
title: 'VisualRouter: Query-Grounded Visual Sampling for Long Video Understanding'
title_zh: VisualRouter：查询驱动的长视频视觉采样
authors:
- Haiyue Zhang
- Yi Bin
- Xun Jiang
- Zeyu Ma
- Duo Peng
- Guoqing Wang
- Yang Yang
- Heng Tao Shen
arxiv_id: '2607.28463'
url: https://arxiv.org/abs/2607.28463
pdf_url: https://arxiv.org/pdf/2607.28463
published: '2026-07-30'
collected: '2026-08-02'
category: Multimodal
direction: 查询感知的视觉采样策略
tags:
- visual sampling
- query-grounded
- LVLMs
- long video understanding
- training-free
one_liner: 区分全局/局部查询的自适应视觉采样框架，即插即用，无需训练，显著提升多模态大模型的长视频理解能力。
practical_value: '- 查询类型分类（全局 vs 局部）的思路可直接复用到多模态搜索与推荐：对用户 query 进行意图分类，分别采用不同召回或排序策略。

  - 训练无关、即插即用的设计适合快速集成到现有视频理解 pipeline，如商品视频标签提取、直播切片精选等，无需额外训练成本。

  - 事件感知的帧选择策略（事件划分→段级分配→段内选择）可借鉴到长视频推荐场景：对视频内容做事件切割，按事件分配曝光帧数，保证多样性。

  - 相关性、覆盖度、多样性三平衡的采样准则可应用于推荐系统的物品选择或内容摘要，避免信息冗余，提升用户体验。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：长视频理解因视觉 token 过多、上下文窗口有限而困难，现有视觉采样方法要么依赖相关性导致冗余和覆盖不足，要么固定采样不受查询类型影响。

**方法**：提出 VisualRouter，一个无需训练、即插即用的查询驱动视觉采样框架。它首先将查询分类为全局（需要整体时序理解）或局部（聚焦特定事件），然后分别采用对应策略：
- 全局查询：使用相关性-覆盖度混合采样，在保留时间均匀性的同时增加与查询相关的帧；
- 局部查询：通过事件划分、段级帧数分配和段内帧选择（基于相关性、覆盖度、多样性联合打分），精准定位关键帧。

**结果**：在 Qwen2.5-VL-7B 上，Video-MME、LongVideoBench、MLVU 分别提升 5.2%、7.7%、11.6%，统一采样基线被显著超越，且优于同等设置下的其他无训练视觉采样方法。
