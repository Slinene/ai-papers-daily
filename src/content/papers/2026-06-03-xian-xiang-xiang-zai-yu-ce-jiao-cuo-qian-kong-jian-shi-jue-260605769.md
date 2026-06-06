---
title: 'Imagine Before You Predict: Interleaved Latent Visual Reasoning for Video
  Event Prediction'
title_zh: 先想象再预测：交错潜空间视觉推理用于视频事件预测
authors:
- Tianxiang Jiang
- Linquan Wu
- Sheng Xia
- Songze Li
- Ziang Yan
- Haoyu Yang
- Yu Qiao
- Yi Wang
affiliations:
- Shanghai AI Laboratory
- University of Science and Technology of China
- City University of Hong Kong
- Nanjing University
- Fudan University
arxiv_id: '2606.05769'
url: https://arxiv.org/abs/2606.05769
pdf_url: https://arxiv.org/pdf/2606.05769
published: '2026-06-03'
collected: '2026-06-06'
category: Multimodal
direction: 多模态推理 · 潜空间视觉预测
tags:
- Video Event Prediction
- Latent Reasoning
- MLLM
- Reinforcement Learning
- Autoregressive Decoding
one_liner: 通过交错生成语言与连续视觉潜空间片段，保留细粒度动态线索，大幅提升视频MLLM的未来事件预测精度
practical_value: '- 多模态推荐场景（如直播带货、短视频电商）中，对用户行为或交互序列的预测可借鉴潜空间视觉推理，避免过早文本化损失动态姿态、几何关系等细粒度信息。

  - 生成式推荐或Agent规划可引入交替生成语言token与连续视觉潜状态的方式，提升对未来场景的连续预测能力；特别是商品搭配、虚拟试穿等任务，保留视觉中间态可能减少幻觉。

  - 使用RL优化采样得到的潜空间轨迹（LA-DAPO），结合结果对比奖励和时间多样性奖励，可迁移到对话式Agent或多步推荐策略中，用来微调生成路径的质量。

  - 训练数据筛选策略——“选择未来视觉线索对预测有帮助的样本”——可类比推荐中挖掘对用户意图跳转有强信号的交互片段，用于训练预测模型。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：视频事件预测要求模型从部分观测帧推断未来隐动态。现有视频MLLM将中间推理全部文本化，会丢失运动、几何、交互等细粒度视觉线索，导致幻觉。

**方法**：提出Future-L1，让MLLM在自回归解码时交替生成语言token与连续潜空间视觉片段（latent spans），使模型内部保持视觉语义。训练分两步：1) 构建Future-L1-50K数据集，筛选未来视觉线索对预测有帮助的样本，并将潜状态与未来帧嵌入对齐；2) 用LA-DAPO进行RL优化，引入结果对比奖励（正确预测未来帧）与时间多样性奖励（避免坍缩），直接优化采样得到的潜轨迹质量。

**结果**：在FutureBench上，将Qwen3-VL-8B准确率从61.0%提升至85.4%，超过先前最佳模型10.4个百分点；在TwiFF-Bench上平均分从2.44升至3.04，均达到SOTA。表明保留中间视觉潜空间语义对面向未来的推理至关重要。
