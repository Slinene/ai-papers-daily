---
title: 'LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks'
title_zh: LLM-as-a-Coach：面向非可验证任务的经验学习
authors:
- Tianzhu Ye
- Li Dong
- Guanheng Chen
- He Zhu
- Xun Wu
- Shaohan Huang
- Furu Wei
affiliations:
- Microsoft Research
- Tsinghua University
- Peking University
arxiv_id: '2607.18110'
url: https://arxiv.org/abs/2607.18110
pdf_url: https://arxiv.org/pdf/2607.18110
published: '2026-07-19'
collected: '2026-07-21'
category: Training
direction: LLM 后训练从标量奖励转向经验反馈
tags:
- Experiential Learning
- LLM-as-a-Coach
- Context Distillation
- Non-Verifiable Tasks
- Reward Hacking Mitigation
- LLM Post-training
one_liner: 将 LLM 评估从标量奖励升级为细粒度经验反馈，通过上下文蒸馏提升开放任务的后训练效果
practical_value: '- **广告文案 / 推荐理由生成**：将点击、转化等弱信号通过教练模型转化为细粒度的文本反馈（如“信息量不足”“说服力弱”），再用
  EL 蒸馏优化生成策略，替代只优化点击率的标量奖励，能显著提升文案质量与多样性。

  - **对话式推荐系统**：在多轮交互中，用 LLM 教练对每轮回复进行多维度评价（相关性、说服力、个性等），作为经验知识输入策略模型，缓解纯奖励优化导致的单调回复或“套路化”问题。

  - **反馈信号设计**：借鉴 EL 的教练设计，将评分准则（rubric）的文本描述直接作为经验知识，无需额外训练奖励模型，适合电商场景中快速部署新产品推荐的文案评估。

  - **工程实现**：EL 的 on-policy 上下文蒸馏可通过偏好对（preference pairs）实现，与 DPO 流程兼容，避免复杂的 RL 基础设施，对线上系统实时更新更友好。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 在开放任务的后训练中，标准 RL 将详尽的文本评测压缩为标量奖励，丢弃了细粒度反馈，导致相同奖励的响应无法区分，且容易奖励黑客。

**方法关键点**：
- **重定位反馈模型**：将 LLM-as-a-Judge 改造为 LLM-as-a-Coach，输出包含具体优缺点和改进建议的“经验知识”，而不仅是分数。
- **On-policy 经验蒸馏**：教练对每条策略生成的响应进行评估，提炼出可迁移的经验知识（如“本回复说服力强，但缺少案例支持”）。这些经验条件化一个教师模型，再通过上下文蒸馏将知识内化到策略模型中，实现高带宽监督。
- **保留细粒度偏好**：与标量奖励不同，经验知识保留了高质量响应之间的细微偏好差异，提供密集学习信号。

**关键结果**：
- 在多种策略模型（开源/闭源）和反馈模型（策略自评/专有模型）组合下，EL 在保留集和未见的开放任务上一致优于基于标量奖励的 RL。
- EL 展现出更强的分布外泛化能力，并显著缓解奖励黑客现象。
- 分析表明，经验知识作为学习信号更丰富且更通用，为非可验证任务的后训练建立了新的范式。
