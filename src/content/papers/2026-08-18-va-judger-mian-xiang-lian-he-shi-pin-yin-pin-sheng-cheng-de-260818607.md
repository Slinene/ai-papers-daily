---
title: 'VA-Judger: Reward Modeling from Human Preference Feedback for Joint Video-Audio
  Generation'
title_zh: VA-Judger：面向联合视频音频生成的人类偏好反馈奖励建模
authors:
- Yinming Huang
- Shuyuan Tu
- Xi Yan
- Zihan Yang
- Jianhua Han
- Xu Hang
- Yu-Gang Jiang
- Zuxuan Wu
affiliations:
- Fudan University
- Shanghai Innovation Institution
- Yinwang Intelligent Technology Co., Ltd
arxiv_id: '2608.18607'
url: https://arxiv.org/abs/2608.18607
pdf_url: https://arxiv.org/pdf/2608.18607
published: '2026-08-18'
collected: '2026-08-23'
category: Multimodal
direction: 多模态生成奖励建模 · 视频音频对齐
tags:
- Reward Model
- Video-Audio Generation
- RLHF
- Chain-of-Thought
- Preference Dataset
- Multimodal
one_liner: 构建10K人类偏好数据集与评测基准，提出链式思考全模态奖励模型VA-Judger，通过分维度强化学习对齐人类偏好
practical_value: '- 多模态生成评估中，单一标量奖励容易被 hack，可将评分分解为 prompt match、audio-visual consistency、audio
  quality、video quality、completeness 等维度，分别评分加总，使奖励更密集、可解释，也便于定位生成缺陷；类似电商广告视频生成可定义画面-文案一致性、卖点覆盖、音画同步等维度。

  - 构建小规模人类偏好对比数据时，先让模型在明显差距样本上学习结构化输出，再用拒绝采样对难分样本蒸馏解释，降低人工标注成本；可用于业务中快速训练创意评估模型。

  - 奖励模型后训练可采用 dimension-wise RL，把二元偏好分解到各维度，提供更密集训练信号，比只优化全局偏好更稳定；在广告创意 A/B 测试中可对应分维度打分作为辅助
  reward shaping。

  - CoT 让奖励模型输出各维分数和推理过程，便于线上审计和错误分析，但会增加推理延迟，业务中可在离线评估或数据标注环节使用，在线打分可只取结构化分数。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：联合视频音频生成的奖励信号常由独立质量指标组合，这些指标各自评估音频、视频、同步等单维度，无法捕捉文本-视频-音频整体语义与时序一致性，优化时容易 reward hacking，产生高分但不连贯的内容。

**方法**：构建人类偏好数据集 VAPref-10K，含 9K prompts 和 10.3K 高质量成对比较；提出 VA-Judger-Bench 包含 in-domain 和 out-of-domain 对比。训练链式思考全模态奖励模型 VA-Judger，三阶段：先在质量差距明显的 pair 上学习结构化输出与粗略偏好判别；再用拒绝采样从难分样本中蒸馏可靠偏好解释，以人类标注验证；最后按质量维度分解人类反馈做强化学习，提供比单一二元标签更密集的奖励信号。

**结果**：在 in-domain 和 out-of-domain 评估上，VA-Judger 预测人类偏好均优于指标 baseline；将其奖励用于后训练音频视频生成模型，生成质量显著提升，与人类一致性最高。
