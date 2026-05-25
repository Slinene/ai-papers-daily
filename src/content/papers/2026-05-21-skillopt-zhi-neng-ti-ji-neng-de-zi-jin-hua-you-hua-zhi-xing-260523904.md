---
title: 'SkillOpt: Executive Strategy for Self-Evolving Agent Skills'
title_zh: SkillOpt：智能体技能的自进化优化执行策略
authors:
- Yifan Yang
- Ziyang Gong
- Weiquan Huang
- Qihao Yang
- Ziwei Zhou
- Zisu Huang
- Yan Li
- Xuemei Gao
- Qi Dai
- Bei Liu
affiliations:
- Microsoft
- Shanghai Jiao Tong University
- Tongji University
- Fudan University
arxiv_id: '2605.23904'
url: https://arxiv.org/abs/2605.23904
pdf_url: https://arxiv.org/pdf/2605.23904
published: '2026-05-21'
collected: '2026-05-25'
category: Agent
direction: Agent 技能优化 · 文本空间训练
tags:
- Skill Optimization
- Agent Skills
- Self-Evolution
- Text-space Optimization
- Validation Gate
- Rejected-Edit Buffer
one_liner: 第一个系统性的可控文本空间优化器，将有界编辑、拒绝缓冲等引入技能训练，在52项测试中全部最佳。
practical_value: '- **将技能优化视为带约束的文本训练过程**：借鉴学习率（编辑预算）、验证集门控、负反馈缓冲区等概念，可在电商 Agent 的技能迭代中引入类似控制，避免无监督改写导致的退化。

  - **离线优化、零部署成本**：SkillOpt 只在高能力优化器上训练一次，导出紧凑的 best_skill.md（<2k tokens），部署时无额外推理开销。电商场景中可用这种模式批量生产领域技能，大幅降低在线
  Agent 的推理成本。

  - **技能跨模型和执行环境迁移**：实验证明优化技能可跨模型规模、跨工具链（Codex ↔ Claude Code）甚至跨任务转移。这对构建可复用的电商领域技能库很有启发：一个技能可用于多个相关任务或不同能力模型。

  - **拒绝编辑缓冲提供负反馈学习**：类似训练中保留失败样本以指导后续更新，可借鉴到推荐系统或 Agent 的在线学习环节，利用用户反馈的负面信号修正策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机：** 当前大模型智能体的技能主要依赖手工编写、一次性生成或松散自修订，缺乏稳定、可控的优化机制。作者提出将技能文档视为可训练的外部状态，并为之引入类似深度学习的优化过程（学习率、验证、动量），以实现可复现、可审计的技能改进。

**方法关键点：**
- **解耦执行与优化**：目标模型冻结，仅用额外的优化器模型对技能文档进行结构化编辑（添加/删除/替换）。
- **有界文本更新**：使用编辑预算（学习率）限制每步修改行数，并带有余弦衰减调度，防止一次改写破坏原有有效规则。
- **拒绝编辑缓冲区**：记录未通过验证门控的编辑及其效果，作为后续迭代的负反馈，帮助优化器避开已知失败方向。
- **跨 epoch 的慢/元更新**：比较当前 epoch 与前一个 epoch 的技能表现，生成长周期指导（类似动量），并写入保护区域不被步骤更新覆盖。
- **部署产物紧凑**：导出的 best_skill.md 仅 300~2000 tokens，不包含任何优化器调用。

**关键结果：** 在 6 个不同领域基准（搜索QA、电子表格、办公文档、多模态QA、数学、具身决策）、7 种目标模型（GPT-5.5 至 Qwen）、3 种执行模式（直接聊天、Codex、Claude Code）的 52 个（模型×基准×环境）评估单元中，SkillOpt 全部达到最佳或并列最佳；GPT-5.5 在直接聊天模式下的平均增益为 +23.5 分，在 Codex 和 Claude Code 下分别为 +24.8 和 +19.1 分；跨模型、跨工具链和跨基准迁移实验均保持正向提升；消融实验表明，有界编辑、拒绝缓冲和慢更新是性能的关键保障。
