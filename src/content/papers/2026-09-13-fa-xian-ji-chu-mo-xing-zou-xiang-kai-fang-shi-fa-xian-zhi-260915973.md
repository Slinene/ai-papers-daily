---
title: 'Discovery Foundation Models: Toward Open-Ended Discovery Intelligence'
title_zh: 发现基础模型：走向开放式发现智能
authors:
- Ling Yang
- Zhenfei Yin
- Yingcheng Wu
affiliations:
- PhAI Labs
arxiv_id: '2609.15973'
url: https://arxiv.org/abs/2609.15973
pdf_url: https://arxiv.org/pdf/2609.15973
published: '2026-09-13'
collected: '2026-09-15'
category: Other
direction: 基础模型 · 开放式发现智能
tags:
- Discovery Foundation Models
- Open-Ended Discovery
- Research State
- Verification Gating
- Discovery Skill Evolution
one_liner: 提出 Discovery Foundation Models 框架，让基础模型从解题升级为参与新知识的创建、验证与修订
practical_value: '- 将推荐/广告策略迭代重构成“可修订研究状态”闭环：把每个召回或排序改动视为 intervention，用离线评估、A/B 实验或线上指标作为
  evidence gating，自动更新策略状态，减少人工排期和主观判断。

  - 在生成式推荐或 query 推荐中引入外部证据校验：对 LLM 生成的 Semantic ID、推荐理由或搜索词，不只依赖模型自评，而要接入商品属性、用户行为、库存等外部
  grounding，通过 gate 过滤低置信输出，提升可信度。

  - 跨场景的 Discovery Skill 抽取与复用：将问题定义、假设生成、实验设计等子能力模块化，在多个品类或场景间持续微调，让 Agent 在新业务冷启动时快速迁移已有发现能力。

  - 采用过程为中心的评估：除了最终 CTR/GMV 等指标，也量化中间步骤质量（如假设覆盖率、证据充分度、实验设计的可验证性），用于诊断 Agent 系统的瓶颈，引导迭代优化。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：基础模型已从学习现有知识、用工具和反馈行动，进展到需要参与新问题、新表征、新解释与新知识的创建过程。论文将这种能力定义为 Discovery Intelligence，提出 Discovery Foundation Models（DFMs）作为通用开放式发现系统。

方法关键点：DFM 基于可修订的研究状态运行，覆盖七个耦合能力：问题发现、问题形式化、表征构建、假设形成、干预实施、基于证据的修订、持续发现改进。框架通过两个实例落地：Zetema 耦合显式研究状态动力学、验证与实验门控、外部 grounding 和跨任务发现技能演化；GALILEO 则在药物发现场景中打通 Dry-Lab 推理、机器人/湿实验、外部生物证据和迭代假设修订的物理闭环。进一步提出统一的能力形成与过程中心评估方法，使发现行为可训练、可改进、可度量，而非只看最终答案。

结果：论文未给出传统 benchmark 数值，而是建立发现作为基础模型系统可学习、可执行、可评估的能力范式，并开放代码与协作计划，强调从知识学习到知识生产的智能扩展路径。
