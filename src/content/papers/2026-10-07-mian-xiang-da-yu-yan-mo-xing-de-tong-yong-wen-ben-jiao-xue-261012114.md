---
title: Universal Textual Teaching for LLMs
title_zh: 面向大语言模型的通用文本教学
authors:
- Zhanyi Lu
- Huan Wang
affiliations:
- Westlake University
arxiv_id: '2610.12114'
url: https://arxiv.org/abs/2610.12114
pdf_url: https://arxiv.org/pdf/2610.12114
published: '2026-10-07'
collected: '2026-10-13'
category: LLM
direction: LLM 文本知识蒸馏 · Primer
tags:
- Knowledge Distillation
- Primer
- Multi-role LLM
- Parameter-free
- Code Generation
- Math Reasoning
one_liner: 提出 UTT，无需参数更新，将 Teacher-Student 知识差距蒸馏为可迁移的自然语言 Primer，显著提升推理与代码生成性能
practical_value: '- 业务中有强模型（如 GPT-4/Claude）和弱模型（如开源小模型或 API 便宜模型）时，可借鉴 UTT 对困难 query/商品/广告创意做配对评估，自动生成可复用
  prompt/Primer，无需微调弱模型即可提升效果，尤其适合只能调用 API 的模型。

  - 知识差距选择比随机选择更有效：先找出教师答对、学生答错的样本，再让教师针对性生成教学指令和演示，比直接让教师总结全量数据更利于迁移。可用于构建困难样本集或优化
  few-shot 示例。

  - 验证门控机制实用：每次更新 prompt/Primer 前，用小批量验证集确认不降低学生已有能力，避免自动 prompt 优化或 Agent 指令库更新时出现退化。

  - 跨模型迁移性提示：同一个文本提示可在不同版本/不同家族的模型间复用，适用于多模型路由、灰度发布或模型升级时的知识继承。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有 LLM 知识蒸馏通常需要训练学生参数，知识隐式绑定在特定模型权重中，不可解释、难以跨模型复用，且不适用于 API-only 模型。本文研究能否将 Teacher-Student 知识差距显式化为自然语言表示，在不更新参数的情况下提升学生模型。

**方法关键点**：
- 知识差距构建：通过配对评估教师和学生在一批任务上的表现，划分蒸馏集（教师优于学生）、保留集（学生不差于教师）、前沿集（两者都错）。仅用蒸馏训练集合成 Primer。
- 多角色闭环合成：Student 用当前 Primer 尝试任务；失败时 Prompter 根据评估反馈诊断差距并生成教学指令；Teacher 给出针对性演示；Synthesizer 将教学记录整合进全局 Primer。所有角色由 LLM 扮演，参数冻结。
- 验证门控：候选 Primer 需在当前 batch 上不降低学生正确率才被接受，防止知识积累导致性能退化。
- Primer 是紧凑、可解释的文本学习指南，不是解题存档，包含推理策略、校验方法、常见陷阱等可迁移知识。

**关键实验与结果**：
- 在 KernelBench 代码生成上，Pro→Flash 学生准确率从 9.4% 提升到 48.6%，Fast1 从 9% 到 35%；Omni-MATH-2 数学准确率从 27.6% 到 51.7%。
- 跨模型迁移：为 Flash 合成的 Primer 直接用于 Qwen，KernelBench 准确率 +32.0 个点、Omni-MATH-2 +25.8 个点；更换教师和源学生后仍有效，说明 Primer 具有跨模型通用性。
- 与 APO 和参数更新式 KD 方法相比，UTT 在多数设置下最优；合成仅需 1.6 小时 281 次 API 调用，无需 GPU 训练。

**最值得记住的一句话**：自然语言可以作为一个可部署、可解释、跨模型复用的知识载体，将教师-学生能力差距蒸馏为 Primer，无需更新任何参数。
