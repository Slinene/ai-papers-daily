---
title: 'ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation'
title_zh: ShortOPD：通过短到长在轨蒸馏恢复剪枝后LLM生成能力
authors:
- Qingyu Zhang
- Qianhao Yuan
- Hongyu Lin
- Yaojie Lu
- Xianpei Han
- Le Sun
- Xiang Li
- Ming Xu
- Jiarui Li
- Xiuyin Zhao
affiliations:
- ByteDance
- Institute of Software, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2607.13124'
url: https://arxiv.org/abs/2607.13124
pdf_url: https://arxiv.org/pdf/2607.13124
published: '2026-07-13'
collected: '2026-07-16'
category: Training
direction: 结构化剪枝后LLM的生成能力恢复训练
tags:
- Structured Pruning
- On-Policy Distillation
- LLM Compression
- Repetitive Suffixes
- Short-to-long Schedule
one_liner: 基于短到长的在轨蒸馏，消除冗余后缀以加速剪枝LLM的生成恢复训练
practical_value: '- 剪枝压缩后的大模型在线上生成时出现质量崩塌（如重复后缀），可直接借鉴 ShortOPD 的在轨蒸馏恢复方案，用未剪枝模型做教师，快速回血生成能力。

  - 短到长训练调度能大幅度减少低信息量重复令牌的训练开销，适合需要严格控制训练预算的场景（如电商智能客服、推荐理由生成），可加速迭代。

  - 重复前缀检测与截断策略可作为通用技巧，集成到长文本生成的在线学习或 RLHF 流程中，避免模型在无效 token 上浪费算力。

  - 对于 Agent 系统中的核心大模型，若经历量化或剪枝后指令跟随能力下降，可用此方法微调恢复，保障多轮交互的任务完成率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：结构化剪枝虽能减小LLM体积，但压缩后的模型在自由生成任务上常崩溃，主要表现为后缀重复，导致pass@1几乎清零。观察发现pass@k可以大幅恢复，说明生成能力只是被降级而非丧失。恢复训练需要通过压缩模型自身的在轨状态进行密集监督，即在轨蒸馏（OPD），但长轨迹OPD早期预算大量消耗在重复后缀上，收敛缓慢。
**方法**：提出ShortOPD，一种短到长的OPD调度策略。训练时检测教师模型确认的重复后缀，将其截断，仅保留有效前缀作为蒸馏序列，并动态增长有效长度，使训练预算始终集中在当前策略能合理利用的上下文长度上。
**结果**：在数学、代码和开放式生成任务上，ShortOPD使压缩模型得分提升至未恢复时的约9倍，达到标准恢复方法（SFT、KD、SeqKD）的1.6–4.4倍；用四分之一的训练时间（8.5 vs 35.9小时）和71%更少的轨迹令牌即可匹配固定8192令牌长度的恢复效果。
