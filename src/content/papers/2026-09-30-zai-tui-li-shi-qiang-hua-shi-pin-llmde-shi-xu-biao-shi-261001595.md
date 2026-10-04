---
title: 'Before It Fades: Reinforcing Temporal Representations at Inference Time in
  VideoLLMs'
title_zh: 在推理时强化视频LLM的时序表示
authors:
- Youngwoo Shin
- Yusung Ro
- Minseo Kim
- Junmo Kim
affiliations:
- Korea Advanced Institute of Science and Technology (KAIST)
arxiv_id: '2610.01595'
url: https://arxiv.org/abs/2610.01595
pdf_url: https://arxiv.org/pdf/2610.01595
published: '2026-09-30'
collected: '2026-10-04'
category: Multimodal
direction: 视频LLM时序推理的推理时激活注入
tags:
- Temporal Reasoning
- VideoLLMs
- Activation Injection
- Inference-Time
- Representation Analysis
- Multimodal
one_liner: 发现时序信息在中间层达到峰值后逐渐消失，提出无需训练的 Temporal Activation Injection (TAI) 在推理时注入激活以强化时序推理
practical_value: '- 在电商/内容平台使用 VideoLLM 做商品视频、直播切片、短视频广告素材理解时，可直接在推理阶段集成 TAI（无需训练），提升对时间顺序类问题的回答准确率，如“主播先展示哪款商品后再讲解优惠”、“使用步骤的先后”等；对非时序任务几乎无副作用，适合即插即用。

  - TAI 的核心是层间时序分歧曲线的测量与衰减补偿，这一诊断思路可迁移到多模态 LLM 的推荐场景：对商品属性、价格、款式等特定信息做层间表示分析，定位表达该信息的关键层，为后续推理时干预、提示设计或模型裁剪提供依据。

  - 在 Agent 工作流中若包含视频理解子模块，TAI 仅增加一次前向的激活注入，工程实现简单、延迟开销小；可复用其从分歧向量峰值处提取信号并沿层衰减回注的做法，作为强化特定模态/时序能力的通用推理时增强手段。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：VideoLLMs 接收有序帧但时序推理仍弱，反转帧顺序往往不改变预测。为定位问题，定义了时序分歧向量 τ_l，表示反转帧顺序引起的层间表征差异。追踪其幅值发现一致轮廓：中间层达到峰值，向输出逐渐衰减。确认该峰值对时序推理特异且对预测关键，表明模型在中间层获取时序信息但未能保持到输出。

方法关键点：提出 Temporal Activation Injection (TAI)。对每个输入在峰层提取 τ_l，依据实测衰减将其重新注入后续层，补偿时序表征的消失。无需训练，不改模型参数。

结果：在三个 VideoLLMs、四个基准上一致提升时序推理，对非时序任务影响可忽略。代码开源。
