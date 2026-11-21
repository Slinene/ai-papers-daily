---
title: 'EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning'
title_zh: EgoCaptioner：第一视角视频的全面细粒度时序描述生成
authors:
- Yuqi Tang
- Yang Shi
- Yuran Wang
- Tengfei Liu
- Rundong Wang
- Zongyang Qiu
- Qixun Wang
- Zhuoran Zhang
- Xuanyu Zhu
- Yifan Xu
affiliations:
- HKUST(GZ)
- KlingAI Research
- Peking University
- University of Science and Technology of China
- Nanjing University
arxiv_id: '2611.26380'
url: https://arxiv.org/abs/2611.26380
pdf_url: https://arxiv.org/pdf/2611.26380
published: '2026-11-18'
collected: '2026-11-21'
category: Multimodal
direction: 多模态视频 Captioning 与 RL 训练
tags:
- Egocentric Video
- Video Captioning
- MLLM
- GRPO
- Temporal Alignment
- Data Annotation
one_liner: 第一视角视频captioning：粗到细标注+多奖励GRPO，生成带时间戳的步骤级细粒度描述
practical_value: '- 商品视频/直播切片理解可借鉴“整体概述 + 带时间戳步骤”的结构：为卖点提取、推荐理由生成提供可定位的时间证据，方便下游切分消费。

  - 粗到细标注比单次标注更有效，适合电商短视频/直播数据生产：先标事件边界，再补物体交互、空间移动等细节，能提升短动作和动作顺序的时序准确率。

  - GRPO 中解耦事实覆盖、时间对齐、碎片/冗余惩罚三类奖励，业务里可对直播解说/商品卖点生成分别调权；有交互日志或姿态数据时可注入弱监督，降低幻觉。

  - timestamped steps 天然适配搜索/推荐场景的片段化理解，可作为商品教程、短视频自动打点、直播高光提取的基础。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：第一视角视频描述要求细粒度细节和准确时序，但现有多模态大模型常忽略短促动作、混淆顺序或误解穿戴者运动。现有 caption 格式也难以结合详细叙述与精确时间戳。

方法：EgoCaptioner 将描述分为视频级概述和带时间戳的步骤，步骤叙述根据感知需求调整并标记关键时刻。开发粗到细标注流水线，先生成事件结构再扩展步骤描述，从八个第一视角视频来源产生 5 万训练样本。使用互补奖励：事实准确性与覆盖度、步骤级时间对齐、惩罚碎片化和冗余叙述，通过 GRPO 优化。当传感器数据可用时，用姿态推导的运动事实补充监督。

结果：在五个第一视角基准上，开源模型中领先；在 PhysCapBench 上超过 Gemini 3.1 Pro，在 Minerva-Ego 的 caption-to-QA 协议下超过所有专有基线。消融证明事实与时间奖励互补，粗到细标注优于单次标注。
