---
title: Hierarchical Continuous Diffusion Language Models
title_zh: 层次连续扩散语言模型
authors:
- Hui Ren
- Zihan Li
- Chang Liu
- Huidong Liu
- Alexander Schwing
affiliations:
- University of Illinois Urbana-Champaign
- Amazon.com, Inc.
arxiv_id: '2610.02193'
url: https://arxiv.org/abs/2610.02193
pdf_url: https://arxiv.org/pdf/2610.02193
published: '2026-09-30'
collected: '2026-10-02'
category: LLM
direction: 连续扩散语言模型 · 离散连续耦合去噪
tags:
- diffusion language models
- continuous diffusion
- discrete diffusion
- variational inference
- structured reasoning
- language modeling
one_liner: HC-DLM 将离散 token 生成与连续潜变量去噪耦合，在 Sudoku/Countdown/LM1B 上超过匹配规模扩散基线
practical_value: '- 面向需要全局约束或双向推理的文本生成任务（如广告文案、商品标题、搜索 query 改写、推荐理由），可考虑扩散式生成替代自回归，便于多步修改并满足关键词、违禁词、风格等多约束。

  - 可借鉴 HC-DLM 的“离散 token 读出并反馈为脚手架”机制：在生成式推荐中使用连续向量表示全局用户意图/会话状态，每步读出候选 item 或 Semantic
  ID 后反馈调整潜变量，保持序列内依赖，避免并行解码时 token 独立采样的问题。

  - 训练目标基于 token 似然的变分下界，把离散生成目标与连续去噪过程对齐，比将连续上下文简单附加到离散链更稳定；实现时可在每步去噪后做 token readout
  作为下一步条件，降低训练与推理不一致。

  - 注意扩散模型多步去噪带来的推理延迟，适合离线批量生成或对延迟不敏感的约束复杂规划场景（如选品组合、活动文案库生成），不适合超低延迟在线实时推荐。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：离散扩散语言模型在并行解码时对每个 token 独立采样边际，割裂 token 间统计依赖；连续扩散语言模型虽然共享连续状态，但去噪器只看到连续状态，与有效 token 配置脱节。需要一种把离散 token 生成与连续潜变量轨迹耦合的方法。

**方法关键点**：HC-DLM 使连续潜变量成为唯一持久生成状态，每步从潜变量读出 token，并把这些 token 作为脚手架反馈到下一步潜变量更新，形成层次去噪过程。训练目标由 token 似然的变分下界推导，端到端可训练。与近期方法将连续上下文附加到自包含离散链不同，HC-DLM 不依赖独立离散链，潜变量逐步被离散 token 结构化。

**关键结果**：在 Sudoku、Countdown 和 LM1B 上，同等模型规模下 HC-DLM 的 puzzle 准确率和生成困惑度均优于离散和连续扩散基线。
