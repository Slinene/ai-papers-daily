---
title: 'Which Skill to Distill? SGUID: Selecting a Compact Skill Bank for Model-Skill
  Co-Evolution'
title_zh: 哪个技能值得蒸馏？SGUID：为模型-技能协同进化选择紧凑技能库
authors:
- Yuhan Liu
- Xiyao Ma
- Zhongkai Sun
- Xu Han
- Chengyuan Ma
- Benjamin Z. Yao
- Chenlei Guo
affiliations:
- New York University
- Amazon
arxiv_id: '2610.12367'
url: https://arxiv.org/abs/2610.12367
pdf_url: https://arxiv.org/pdf/2610.12367
published: '2026-10-08'
collected: '2026-10-10'
category: Training
direction: LLM 技能蒸馏与模型-技能协同进化
tags:
- Skill Distillation
- Model-Skill Co-Evolution
- On-Policy Distillation
- Skill Selection
- LLM Training
one_liner: 提出SGUID，通过筛选能持续提供有效蒸馏信号的技能子集，实现更稳定高效的模型-技能协同进化。
practical_value: '- 在构建技能/指令库用于 RAG 或 Agent 时，不要仅按语义相关性全量检索；借鉴 SGUID，用 on-policy 蒸馏信号评估每个技能的真实效用，只保留能持续提供正向学习信号的技能，可显著压缩技能库规模（论文中
  6 个技能 vs 全库最多 11 倍），降低推理与蒸馏开销。

  - 模型-技能协同进化循环可迁移到搜索推荐场景：从线上模型 rollouts 中挖掘新的有效技能（如 query 改写规则、排序策略提示），用选择机制过滤无效技能，避免全量回放导致性能退化（论文中
  Qwen3-4B 未过滤技能使 HMMT25 下降 0.3 点）。

  - 对生成式推荐或 QueryRec 中的 prompt/技能管理：不是所有提示模板或策略都值得固化进模型，可以通过蒸馏信号筛选少数高价值技能，实现轻量级模型能力提升，特别适合频繁迭代的线上系统。

  - 强调选择步骤是保证稳定进化的关键；实际业务中应设置在线评估或小流量实验验证技能有效性，避免直接引入未过滤技能伤害线上模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：技能作为可复用的程序性指导能在推理时提升 LLM 性能，但现有工作按语义相关性检索技能库并用于推理或蒸馏，忽略了单个技能的实际效用。作者发现在 on-policy 蒸馏中，不到 25% 的检索技能能提供有用的蒸馏信号。

**方法关键点**：提出 SGUID，选择紧凑技能子集进行蒸馏。只保留在训练中始终产生有效学习信号的技能，然后蒸馏所选技能以提升模型。支持模型-技能协同进化：一轮蒸馏后，从更新模型的 rollouts 中策划新候选技能库，SGUID 再选择下一轮要内化的技能。

**关键结果**：在 Olmo 和 Qwen 系列四个模型上，蒸馏 6 个选定技能在四个模型中的三个上匹配或超过全库蒸馏的 mean avg@12，第二轮再蒸馏 3 个新选定技能后所有四个模型均超过，而全库最多大 11 倍。第二轮循环选择 3 个新技能，Qwen3-8B 从 64.3% 提升到 66.3%。选择步骤对稳定性至关重要：在 Qwen3-4B 上，用未过滤技能更新模型性能下降，HMMT25 下降 0.3 个百分点，而 SGUID 第一轮提升 0.5 点，第二轮提升 1.1 点。
