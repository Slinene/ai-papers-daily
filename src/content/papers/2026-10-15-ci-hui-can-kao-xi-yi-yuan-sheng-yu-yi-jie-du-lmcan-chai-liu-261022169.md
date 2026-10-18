---
title: 'Lexical Reference Frames: Interpreting LM Residual Streams in Native Semantics'
title_zh: 词汇参考系：以原生语义解读LM残差流
authors:
- Jian Gu
- Hongyu Zhang
- Chunyang Chen
- Aldeida Aleti
affiliations:
- Monash University
- Chongqing University
- Technical University of Munich
arxiv_id: '2610.22169'
url: https://arxiv.org/abs/2610.22169
pdf_url: https://arxiv.org/pdf/2610.22169
published: '2026-10-15'
collected: '2026-10-18'
category: LLM
direction: LLM可解释性 · 残差流原生语义
tags:
- Interpretability
- Residual Stream
- Logit Lens
- Early Exit
- Steering
- Attribution
one_liner: 利用模型自身剩余层读取隐藏状态，构建词汇参考系，使残差流可读、可归因、可操控，早期退出可跳过近半层
practical_value: '- 线上LLM推荐/搜索生成可集成LexFrame[1]做early exit或self-speculative decoding：在中间层检测confident
  readings，跳过约45%层，延迟降低且输出差异仅0.16 nats。

  - 归因分析替代attribution patching：lexical frame的系数更忠实反映预测来源，用于电商推荐/搜索模型审计，定位影响query或item生成的关键token段。

  - 用lexical basis做受控steering：在不影响其他token前提下引导预测，可应用于电商文案/搜索词生成，如注入品牌词、规避敏感词、约束推荐理由风格。

  - 该方法不依赖对模型输出的拟合，直接复用前向过程，工程实现轻量，适合嵌入现有LLM推理框架作为内省工具。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：语言模型隐藏状态的语义缺乏原生定义；现有方法要么使用固定lens（如logit lens）逐层读取，要么将状态视为点云，均未按模型自身处理方式来解读状态。

方法关键点：提出词汇参考系（lexical reference frames），通过模型自身剩余层读取目标隐藏状态，固定若干轮跨位置注意力交互，其余位置使用典型注意力输出，无需拟合模型最终输出。一阶版本LexFrame[1]将隐藏状态输入后续层，得到与模型输出对齐的词汇分布。

关键结果数字：在SmolLM3-3B和OLMo3-7B中部层，固定方向lens的coherence上限仅为0.30/0.35，而LexFrame[1]达到0.97/0.97，读取状态与模型输出差距仅0.16 nats；其系数归因比attribution patching更忠实；lexical basis能够在spare其他token的同时steer预测；基于confident readings的early exit可跳过0.45/0.42层，而lens几乎无法跳过。
