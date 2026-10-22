---
title: 'LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data'
title_zh: LongZero：从零数据增强 LLM 长上下文推理
authors:
- Zhennan Wan
- Jianfei Chen
affiliations:
- Tsinghua University
arxiv_id: '2610.30132'
url: https://arxiv.org/abs/2610.30132
pdf_url: https://arxiv.org/pdf/2610.30132
published: '2026-10-21'
collected: '2026-10-22'
category: Reasoning
direction: 长上下文推理 · 零数据自合成 RL
tags:
- LLM
- long-context
- reasoning
- GRPO
- self-synthesis
- RL
one_liner: LongZero 让 LLM 无需外部数据，通过自合成紧凑证据再展开为长上下文，用 GRPO 提升长上下文推理
practical_value: '- 在电商/搜索推荐 Agent 中，常需对长会话、多商品描述、多文档策略进行推理；可借鉴 LongZero 的思路，让模型先生成结构化的证据链（问题-答案-支持证据），再将证据扩展为多文档上下文，构造无外部标注的
  RL 训练数据。

  - 当业务场景缺少高质量长上下文标注数据或不想依赖更强教师模型时，可以用 GRPO 在自合成任务上训练，提升模型在长文档抽取、多跳推理、多轮检索上的泛化能力。

  - 将自合成多轮检索任务加入训练，有助于优化 Agent 在长上下文中的检索与定位能力，例如在商品知识库、用户评论、活动规则中定位支撑某一推荐/答案的证据。

  - 注意该方法主要针对长上下文推理本身，不直接提升推荐精度；作为基础能力训练手段，可集成到现有 Agent/LLM 训练流程中，重点解决推理链路可靠性与长上下文定位问题。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：RL 是增强 LLM 长上下文推理的有效手段，但需要长、多样、有挑战且可验证的训练数据；人工标注昂贵，自然数据稀缺，现有合成方法依赖外部语料或更强的教师模型，模型越强越难获得。零数据 RL 在短上下文任务中表现优秀，但尚未覆盖长上下文。

**方法关键点**：LongZero 让 LLM 在无外部数据条件下自我提升长上下文推理。核心思路是先让模型合成紧凑结构化的问题、答案和支持证据，再单独将证据展开为多文档长上下文，避免直接基于现有文档生成 QA 时模型不理解文本的问题。该方法混合自生成的多跳推理任务与自生成的多轮检索任务，使用 GRPO 进行强化学习训练。

**关键结果**：在两个 LLM 上、五个长上下文推理基准上评估，LongZero 能泛化到真实任务，并优于基于外部语料合成数据的 RL 基线。
