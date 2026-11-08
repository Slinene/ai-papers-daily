---
title: On the Opportunities and Challenges of Prefill-to-Autoregressive Cross-Model
  Transfer
title_zh: Prefill-to-Autoregressive 跨模型迁移的机遇与挑战
authors:
- Zhenyi Shen
- Junru Lu
- Wei Liu
- Jiangnan Ye
- Jiazheng Li
- Di Yin
- Xing Sun
- Tameem Adel
- Yali Du
- Lin Gui
affiliations:
- King’s College London
- Tencent Youtu Lab
- National Physical Laboratory
arxiv_id: '2611.06976'
url: https://arxiv.org/abs/2611.06976
pdf_url: https://arxiv.org/pdf/2611.06976
published: '2026-11-04'
collected: '2026-11-08'
category: LLM
direction: LLM 跨模型潜在通信协作
tags:
- PACT
- Cross-Model Transfer
- Latent Communication
- Parameter-Efficient Training
- Evaluation
one_liner: 开源 PACT 框架 PLatour 证明部分跨模型增益来自适配而非通信，并提出 PACT-Check 量化真实通信收益
practical_value: '- 做大小模型协同或蒸馏式架构时，必须设置 uninformative sender、self-communication、receiver-only
  等对照实验；否则容易把可训练 bridge 的参数高效适配当成“通信收益”，误导架构决策。

  - 零初始化线性 bridge + 冻结模型，用任务 reward 直接训练，是低成本复用大模型 prefill 表示、不增加推理解码开销的可行方案，适合在已有在线服务上做渐进式改造。

  - 在电商/广告场景，若用大模型处理 user/context 前缀、小模型生成推荐文案/搜索词，可先跑 PACT-Check 量化真实通信增益，避免只为小模型自身适应而引入复杂的跨模型链路。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：PACT 用大模型 prefill 表示与小模型自回归生成结合，平衡能力与推理成本，但现有系统缺乏独立评估，任务提升不等于接收方真正利用发送方信息。

方法关键点：PLatour 连接冻结模型，通过轻量零初始化线性桥，直接以任务奖励训练，支持混合注意力架构；设计面向无信息发送方、自通信、仅接收方训练的对照实验，隔离通信贡献；提出 PACT-Check 量化真实通信增益。

关键结果：在生成任务上显著优于开源基线，在数学/编码基准上用更小 sender 超过 Mostik 的已报告结果；但部分任务增益可被无信息 sender、self-communication 或 receiver-only 复现，表明可训练 bridge 可能只是参数高效适配而非有效通信。
