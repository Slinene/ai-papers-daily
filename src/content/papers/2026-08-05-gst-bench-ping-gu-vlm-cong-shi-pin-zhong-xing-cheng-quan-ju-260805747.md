---
title: 'GST-Bench: Can VLMs Develop Global Spatial Awareness from Video?'
title_zh: GST-Bench：评估 VLM 从视频中形成全局空间感知的基准
authors:
- Qifeng Zhang
- Kaixiang Huang
- Heng Dong
- Huang Fang
- Junting Chen
- Junjie Zhu
- Yonghang Chen
- Zhiyu Zhang
- Wei Li
affiliations:
- ByteDance Seed
- Zhejiang University
- National University of Singapore
arxiv_id: '2608.05747'
url: https://arxiv.org/abs/2608.05747
pdf_url: https://arxiv.org/pdf/2608.05747
published: '2026-08-05'
collected: '2026-08-08'
category: Reasoning
direction: 视觉语言模型空间推理评估
tags:
- global spatial awareness
- video understanding
- VLM benchmark
- spatial reasoning
- embodied agents
one_liner: 提出全局时空视频理解基准，发现最强 VLMs 零样本得分仅 42.68（人类 79.08），长视频场景整合能力严重不足
practical_value: '- 主要是学术贡献，对电商/推荐系统的直接工程借鉴有限。

  - 若未来涉及 AR/VR 导购或机器人店内导航，长序列视觉空间整合的评估思路可参考。

  - 合成视频数据生成策略可用于构建训练数据，辅助需要空间感知的视觉下游任务。

  - 揭示了当前 VLM 在长时程多视角视觉融合上的短板，提示设计用户行为理解模型时不可忽视长期依赖性建模。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 VLM 空间智能基准聚焦单帧或短序列局部感知，忽视从连续、长时视频流中构建全局一致空间表征的能力，而这对具身智能至关重要。

**方法**：提出 GST-Bench，包含 6790 分钟合成视频及人工验证的 VQA 题目，要求模型从视频中未见的新视角进行空间推断，并将自我中心观测映射到全局俯视图。另构建 GST-Bench-Local（局部空间任务）探误差来源，并提供 GST-Train 训练集。

**结果**：22 个 SOTA VLM 的零样本评估显示，最强模型仅获 42.68，远低于人类 79.08。局部空间任务中模型表现良好，但无法整合长时间观察形成全局一致表示，揭示全局时空融合是当前架构的关键瓶颈。
