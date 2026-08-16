---
title: 'NARU: A Benchmark for NARrative Evolution and Cultural Nuance Understanding
  in Japanese Extreme Long Video'
title_zh: 日本超长视频叙事演进与文化细微理解基准 NARU
authors:
- Yuheng Huang
- Jianlang Chen
- Jiayang Song
- Hua Qi
- Aza Kai
- Vincent Markert
- Edison Marrese-Taylor
- Jianjun Zhao
- Lei Ma
affiliations:
- The University of Tokyo
- Kyushu University
- Macau University of Science and Technology
arxiv_id: '2608.13210'
url: https://arxiv.org/abs/2608.13210
pdf_url: https://arxiv.org/pdf/2608.13210
published: '2026-08-13'
collected: '2026-08-16'
category: Eval
direction: 多模态 LLM 长视频叙事与文化评估
tags:
- Benchmark
- Long-form Video
- MLLM
- Narrative Reasoning
- Cultural Understanding
- Japanese
one_liner: 含 1,481 个问题，覆盖 155 个视频 146.8 小时，评估长视频叙事与文化理解，揭示 MLLM 明显不足
practical_value: '- 借鉴层级记忆式标注管线：将原始日志（如用户多轮会话、观看序列）按“事件-叙事-文化”多粒度结构化，再生成评测或训练样本，有助于明确模型需要在哪一层推理。

  - 借鉴迭代式 shortcut removal：构建内部评测集时，反复剔除仅靠表面统计或常见捷径就能回答的问题，确保考察真实深层理解，可用于生成式推荐的解释质量、对话式推荐题目的校验。

  - 对非英语/高语境内容单独设立评估维度：跨境电商或出海推荐中，模型需理解本地文化细微差别，可按文化维度构建测试集，避免英语中心偏差影响线上效果。

  - 长程依赖建模短板提示：在长 session 或长期用户兴趣建模中，考虑引入层级记忆/摘要机制，而不是单纯堆叠长上下文。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有长视频理解基准大多只评估孤立事件检索，忽略叙事演进和隐性文化含义，且以英语内容为主，缺少高语境非英语媒体评测。

**方法关键点**：NARU 构建了 1,481 个问题，基于 155 个总时长 146.8 小时的日本视频，覆盖四个叙事维度和五个文化维度。标注采用层级记忆式管线：先将原始视频转化为结构化事件、叙事与文化标注，再进行任务导向问题合成，并通过迭代式 shortcut removal 剔除表面捷径。全过程包含两轮母语者验证，共 68 名标注者参与。

**关键结果**：在八种模型配置上评估，当前 MLLM 在长程叙事整合和文化基础推理上均暴露明显局限，说明高语境长视频理解仍存在持续差距。
