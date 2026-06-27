---
title: 'UnityShots: Memory-Driven Multi-Shot Audio-Video Generation with Boundary-Aware
  Gating'
title_zh: 'UnityShots: 记忆驱动多镜头音视频生成与边界感知门控'
authors:
- Jiehui Huang
- Yuechen Zhang
- Bin Xia
- Jiahao Wang
- Xu He
- Zhenchao Tang
- Meng Chu
- Xin Tao
- Pengfei Wan
- Jiaya Jia
affiliations:
- The Hong Kong University of Science and Technology
- The Chinese University of Hong Kong
- Kling Team, Kuaishou Technology
- Tsinghua University
- Sun Yat-sen University
arxiv_id: '2606.21661'
url: https://arxiv.org/abs/2606.21661
pdf_url: https://arxiv.org/pdf/2606.21661
published: '2026-06-18'
collected: '2026-06-27'
category: Other
direction: 多镜头视频生成 · 记忆机制
tags:
- Multi-Shot
- Audio-Video Generation
- Memory
- Boundary-Aware
- AdaLN
one_liner: 用固定大小记忆槽和边界感知门控实现跨镜头一致性音视频生成，指标领先开源并与闭源持平
practical_value: '- **多镜头连贯生成可直接用于商品展示视频**：固定大小的长期记忆（锚定开场镜头）与短期记忆（前一镜头尾部）槽位设计，可在自动生成多角度、多场景商品介绍时保持产品外观、环境的一致性，避免人工拼接。

  - **边界感知门控可用于用户行为序列的切点检测**：将视觉切幅概率与节拍信号融合的思路，可迁移到电商用户session划分中，用行为突变信号（如点击间隔、内容切换）触发推荐策略切换。

  - **离散切类型先验作为可控开关**：通过AdaLN学习离散过渡强度，在生成时可控制镜头连接的平滑或突兀程度，类似推荐系统中多样性/一致性的可调节参数，适用于广告混剪的节奏控制。

  - **参考说话人token保持音色**：在虚拟主播、广告旁白等多镜头音频生成中，可保证人声一致性，无需滑窗音频库，降低工程复杂度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多镜头视频生成需要跨镜头保持主体外观、场景和说话人身份，而现有方法要么无法扩展，要么使用线性增长的记忆库导致低效，或缺少多镜头感知的生成骨干。

**方法**：基于LTX-2.3构建UnityShots，视频流设有两个固定尺寸记忆槽：长期记忆（LTM）锚定开场镜头，短期记忆（STM）保存前一镜头尾部。在每个切点，通过边界感知门控（融合视觉切幅概率和节拍跟踪信号）更新记忆。音频流在每个镜头注入参考说话人token以保持音色。一个离散切类型先验通过AdaLN学习，可作为推理时过渡强度的控制旋钮。还发布了覆盖6个文化区域、10+语言的200个多镜头基准。

**结果**：在I2V、T2V、R2V模式下，跨镜头连贯性指标上全面领先开源基线，并与最强闭源系统在多镜头轴向上持平。
