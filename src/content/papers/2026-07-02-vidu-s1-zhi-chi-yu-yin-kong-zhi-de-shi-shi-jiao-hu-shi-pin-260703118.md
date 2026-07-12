---
title: 'Vidu S1: A Real-Time Interactive Video Generation Model'
title_zh: Vidu S1：支持语音控制的实时交互视频生成模型
authors:
- Jintao Zhang
- Kai Jiang
- Jintao Chen
- Xu Wang
- Yang Luo
- Yuji Wang
- Dechuang Chen
- Jungang Li
- Chengyang Ye
- Marco Chen
affiliations:
- Tsinghua University
- Shengshu Technology
arxiv_id: '2607.03118'
url: https://arxiv.org/abs/2607.03118
pdf_url: https://arxiv.org/pdf/2607.03118
published: '2026-07-02'
collected: '2026-07-12'
category: Other
direction: 实时交互视频生成
tags:
- Video Generation
- Real-Time
- Speech Control
- Diffusion Models
- Interactive AI
one_liner: 实现语音控制数字角色的无限时长实时视频生成，消费级GPU上540p/42 FPS
practical_value: '- 对于电商数字人客服/直播场景，可借鉴语音实时驱动角色视频的思路，实现低延迟交互式导购

  - TurboDiffusion/TurboServe 的加速方法可能迁移到推荐系统流量侧的实时推理优化，如降低特征抽取或排序模型延迟

  - 支持用户上传自定义形象和音色，类似个性化推荐中“用户自定义偏好”的模式，可启发商品推荐中的个性化表达

  - 整体属于视频生成领域，与搜索推荐的核心业务关联有限，但实时交互范式对构建Agent化购物助手有参考意义'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频生成模型（Sora、Veo等）均为离线一次性生成，用户需等待数分钟且无法主动交互。为打破这一范式，需实现实时、语音可控、无限时长的视频生成。

**方法**：提出 Vidu S1，通过语音指令实时控制数字角色行为。核心包括：1) 语音引导的未来视频生成，允许用户随时干预；2) 无限时长生成，避免模糊、漂移或失真；3) 基于 TurboDiffusion 和 TurboServe 的高效推理，在消费级 GPU 上以 540p 分辨率达到最高 42 FPS；4) 支持用户上传真人、动漫、宠物等自定义形象，并选择不同语音音色，实现个性化体验。

**结果**：实验表明 Vidu S1 在所有测试指标上达到最优，同时完全满足实时推理需求。在线演示验证了流畅、无失真的无限长度交互。
