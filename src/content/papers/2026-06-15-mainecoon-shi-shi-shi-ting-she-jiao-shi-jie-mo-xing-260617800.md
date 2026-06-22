---
title: 'MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model'
title_zh: MaineCoon：实时视听社交世界模型
authors:
- Lichen Bai
- Tianhao Zhang
- Shitong Shao
- Dingwei Tan
- Qiyu Zhong
- Zhengpeng Xie
- Haopeng Li
- Qinghao Huang
- Dandan Shen
- Tengjiao Ji
affiliations:
- Catnip AI Team
arxiv_id: '2606.17800'
url: https://arxiv.org/abs/2606.17800
pdf_url: https://arxiv.org/pdf/2606.17800
published: '2026-06-15'
collected: '2026-06-22'
category: Multimodal
direction: 实时视听世界模型 · Agent流式推理
tags:
- audio-visual
- autoregressive
- real-time
- world model
- agentic streaming
- reinforcement distillation
one_liner: 首个实时视听自回归世界模型，22B参数单GPU可达47.5 FPS，支持千秒级流式生成与亚秒交互
practical_value: '- **实时视听生成可赋能电商直播**：单GPU低延迟流式生成技术可直接用于虚拟主播或商品讲解视频的实时制作，大幅降低内容生产成本。

  - **长上下文的Agent缓存与规划**：代理流式推理框架中的缓存管理与提示规划能解决长序列生成中的漂移问题，可迁移到对话式推荐Agent，保持长时间交互的主题一致性。

  - **跨模态对齐提升推荐质量**：论文中的跨模态表示对齐方法可借鉴到视频推荐的多模态特征融合，优化视觉与文本、音频的联合表示，提升排序效果。

  - **在线策略蒸馏加速模型迭代**：ROPD等强化蒸馏技术可应用于推荐模型的在线学习，将大模型的偏好快速蒸馏到轻量部署模型，兼顾效果与推理效率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：社交平台上的视频消费极度依赖实时互动，但现有世界模型忽视人类中心的社交动态与听觉信息，无法模拟高参与感、情感共鸣和快速对话节奏。为此，提出面向社交场景的视听世界模型MaineCoon。

**方法关键点**：
- 首个实时视听自回归模型，22B参数，从视觉和音频联合建模社交动态。
- 训练侧引入四项技术：自重采样缓解分布偏移、跨模态表示对齐融合视觉与音频、领域感知偏好优化使生成更贴近社交数据特性、以及强化在线策略蒸馏(ROPD)压缩推理模型。
- 推理侧设计首个代理(Agentic)流式框架，结合缓存管理与提示规划，支持千秒级连续生成而避免语义漂移。

**关键结果**：单GPU下实现最高47.5 FPS的实时生成与亚秒交互，在高质量、低延迟、长时域视听生成任务上达到新SOTA，验证了面向社交平台的生成范式。
