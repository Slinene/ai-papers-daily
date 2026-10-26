---
title: 'On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models'
title_zh: 基于 On-Policy 自训练的数据无关大语言模型自我改进
authors:
- Leon Sick
- Lukas Hoyer
- Yannick Strümpler
- Christian Reisswig
- Timo Ropinski
- Federico Tombari
affiliations:
- Google
- Ulm University
arxiv_id: '2610.32770'
url: https://arxiv.org/abs/2610.32770
pdf_url: https://arxiv.org/pdf/2610.32770
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: LLM 自训练 · 数据自由自我改进
tags:
- Self-Training
- On-Policy Distillation
- LLM
- Synthetic Data
- Self-Improvement
- Multimodal
one_liner: 用高层主题描述合成问答与推理轨迹，在无外部监督下完成 on-policy 自蒸馏并跨领域提升模型能力
practical_value: '- 在搜索/推荐场景中，仅凭类目或主题描述即可为模型合成针对性训练数据，显著降低人工标注 query-答案对的成本，可用于意图识别、query
  改写、推荐理由生成等任务的领域适应。

  - 将 on-policy 自蒸馏用于对话式推荐 Agent：让模型自己生成用户 query 和响应轨迹，再用自身生成的高置信度推理作为 dense token
  目标，减少 offline SFT 的 exposure bias，改善在线交互表现。

  - 合成 privileged reasoning traces（如逐步决策过程）并对模型进行蒸馏，可迁移到电商多步推理场景，例如购物决策路径生成、广告创意推理、客服多轮对话策略优化。

  - 该框架不依赖外部教师模型，适合在业务数据敏感、无法调用 GPT-4 等外部 API 的私有化部署环境中做持续自我改进，且能保留非训练领域能力，降低灾难性遗忘风险。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 on-policy self-distillation（OPSD）虽然能避免 offline SFT 的 exposure bias 和 RLVR 的稀疏奖励问题，但仍依赖 ground-truth QA 对、人工 curated 数据集或监督信号，限制其在无标注场景下的扩展。

**方法关键点**：将 OPSD 重构为 self-training 框架，仅输入粗粒度高层主题描述，模型自主合成 curriculum 式 query 与 privileged reasoning traces，不接触任何人工 prompt 或答案。用这些全合成数据进行 on-policy 自蒸馏：学生模型采样自身轨迹，由自身生成的 privileged reasoning 提供 dense next-token 目标，实现数据自由自我改进。

**结果**：在多个标准语言基准上取得一致提升，且对未参与自训练的领域保持原有能力；框架同时适用于文本与多模态（Visual Question Answering）场景，证明基础模型具备可通过无外部任务监督被放大的潜在能力。
