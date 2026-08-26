---
title: 'TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming'
title_zh: TLive-Omni：面向电商直播的全模态理解模型
authors:
- Yibo Hu
- Yu Qian
- Mao Gu
- Yingfan Tao
- Yuhao Chen
- Yongdong Luo
- Zhuoqun Liu
- Meiguang Jin
- Junfeng Ma
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2608.20958'
url: https://arxiv.org/abs/2608.20958
pdf_url: https://arxiv.org/pdf/2608.20958
published: '2026-08-20'
collected: '2026-08-26'
category: Multimodal
direction: 多模态大模型 · 电商直播理解
tags:
- Omni-modal
- E-commerce Live Streaming
- Reinforcement Fine-Tuning
- Video Understanding
- GRPO
one_liner: 面向电商直播的全模态理解模型，通过三阶段监督训练和 Faithful-RFT 强化微调，实现长时多模态流的准确实时理解
practical_value: '- 直播场景中商品信息分散在语音、视频帧、商品图、叠加文字和用户 query，可借鉴 Per-vGrid 时间戳 token 组织：将视频
  grid 与对应的音频段放在显式边界 token 内，强化时序对齐，适合长视频理解任务。

  - Faithful-RFT 强化微调思路值得迁移：直接对最终答案使用任务可验证反馈打分，而不在 rollout 过程中优化推理式探索，能平衡答案忠实度与实时响应，对电商推荐/客服等延迟敏感场景有参考价值。

  - 数据生产引擎将直播音视频流自动转为 ASR、说话人分析、视觉 grounding、OCR、时序 grounding、dense caption、全模态 QA
  等原子能力训练信号，可复用到电商内容理解、商品属性抽取与标注。

  - 工程实现上，同步长度分组采样减少 padding 且保持多 worker 负载均衡，轻量动态采样保持 GRPO 相对优势，对大规模多模态训练有实用参考。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：电商直播流时间长、噪声大，商品事实分散在主播语音、视频帧、商品图、叠加文字和用户 query 中，单一模态难以完整理解，需要全模态对齐与长时序建模。

方法关键点：TLive-Omni 将图像、视频、音频、文本映射到统一表示空间；引入 Per-vGrid 时间戳 token 组织，把每个视频 grid 与其时间对应的音频段放进显式边界 token，增强时序对齐。训练采用三阶段监督：从全模态感知逐步到指令跟随响应；随后用 Faithful-RFT 强化微调，直接对最终答案进行任务可验证反馈打分，避免 rollout 中推理式探索，兼顾实时性与忠实度。此外配合场景化原子能力 taxonomy 和紧凑数据生产引擎，将直播音视频流自动生成 ASR、说话人分析、商品视觉 grounding、OCR、时序 grounding、dense caption、全模态 QA 等训练信号；训练时使用同步长度分组采样减少 padding，轻量动态采样策略维持 GRPO 相对优势。

结果：在电商直播基准上各任务表现强劲，且在通用多模态基准上泛化良好。
