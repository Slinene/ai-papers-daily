---
title: 'Socratic Skill Learning: Interleaving Teaching and Practice for Transferable
  Agent Skills'
title_zh: 苏格拉底式技能学习：教学与实践交替习得可迁移 Agent 技能
authors:
- Letian Zhu
- Han Li
- Yifan Yao
- Xinping Lei
- Xinyu Che
- Jiahao Wang
- Dianyi Wang
- Yucheng Fu
- Jiakai Wang
- Zhiqi Bai
affiliations:
- Nanjing University
- Alibaba Group
arxiv_id: '2610.17860'
url: https://arxiv.org/abs/2610.17860
pdf_url: https://arxiv.org/pdf/2610.17860
published: '2026-10-12'
collected: '2026-10-22'
category: Agent
direction: Agent 技能获取与迁移学习
tags:
- Agent Skills
- Skill Transfer
- LLM Agents
- Socratic Learning
- Benchmark
one_liner: 通过教学与实践交替学习可复用的 Agent 技能，并构建 SkillTransferBench 验证迁移性
practical_value: '- 将任务过程提炼为可复用 Skill 包（指令 + 可执行资源），而非一次性 prompt，便于跨场景复用；在电商/广告场景可将选品策略、文案生成规则、竞价逻辑封装为
  Skill 供多个 Agent 会话调用。

  - 采用教学与实践交替：Educator 只提供引导和反馈，Student 作为唯一环境操作者和 Skill 作者，可以质疑、测试并调整建议，这样学到的 Skill
  能覆盖边界条件，避免简单模仿成功轨迹带来的过拟合。

  - Issue-Guided SSL 通过跟踪未解决问题动态选择回顾内容，大幅降低 token 消耗（Educator tokens 减少 61.7%），适合成本敏感的生产环境；可将类似机制用于内部技能库的维护与更新。

  - 构建 SkillTransferBench 的思路值得借鉴：用任务家族变体（不同商品类目、不同 query 模式）作为 held-out 测试，验证技能在全新
  solver 会话中的迁移能力，可作为评估自研 Agent 技能泛化性的基准。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Agent Skills 使 LLM Agent 的任务知识跨会话复用，但学习可迁移技能需要明确步骤、使用条件与适应时机，仅靠成功轨迹可能未测试关键边界。现有方法如 Trace2Skill（轨迹蒸馏）和 SKILL-KD（对比蒸馏）缺乏对使用条件的主动验证。

**方法关键点**：提出 Socratic Skill Learning (SSL)，交错专家教学（Educator）与学生实践（Student）。Educator 引导调查，Student 是唯一环境操作者和 Skill 作者，能够提问、测试并调整建议，从而获得更完整的程序证据。构建 SkillTransferBench，包含 35 个任务家族、408 个可执行案例，公开变体规格，在新 solver 会话中 held-out 评估迁移性。主 cohort 为 22 家族、155 案例。进一步提出 Issue-Guided SSL，跟踪跨 Skill 修订的未解决问题，动态选择回顾内容以降低成本。

**关键结果**：在主 cohort 上，Fixed-Window SSL 达到 0.801 utility，对比无 Skill 0.723、Trace2Skill 0.761、SKILL-KD 0.751；三个模型对上交错引导均优于专家撰写和事后教学。Issue-Guided SSL 达到 0.805 utility，同时比 Fixed-Window SSL 减少 61.7% Educator tokens 和 16.9% 总获取 tokens。过程分析表明引导与学生写作和包修订相关，案例研究展示了学生测试并优化程序以供复用。
