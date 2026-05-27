---
title: 'Personalize-then-Store: Benchmarking and Learning Personalized Memory for
  Long-horizon Agents'
title_zh: 个性化存储：长程Agent记忆基准与学习
authors:
- Yeonjun In
- Wonjoong Kim
- Sangwu Park
- Kanghoon Yoon
- Chanyoung Park
affiliations:
- KAIST
arxiv_id: '2605.25535'
url: https://arxiv.org/abs/2605.25535
pdf_url: https://arxiv.org/pdf/2605.25535
published: '2026-05-24'
collected: '2026-05-27'
category: Agent
direction: 个性化LLM Agent记忆管理
tags:
- Personalized Memory
- Storage Gating
- Agent Benchmark
- Memory Retention
- Long-horizon Agents
one_liner: 提出首个评估个性化记忆系统的基准PerMem-Bench，发现会话级存储门控可显著提升保留率但准确门控仍是挑战
practical_value: '- 电商场景中不同用户对同一域（如售后、导购）的交互需求差异显著，可借鉴 session-level gating 思想，在对话结束后判断是否持久化记忆，减少存储预算浪费。

  - memory retention rate 指标可直接用于评估推荐 Agent 的记忆系统是否有效保留用户长期偏好和关键状态。

  - 结构感知门控方法通过识别会话间的项目结构来推断长期任务，结合用户意图的长程建模，可提升电商 Agent 个性化响应的连贯性。

  - 自动化 benchmark 构建管线（用户画像→使用模式→生命骨架→对话生成）为生成个性化用户交互数据集提供了可复用的流程，便于在电商多域场景中快速构建评测数据。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有 LLM Agent 记忆系统对所有用户采用统一的存储策略，忽略了一个根本事实：不同用户对同一领域的交互性质可能截然不同（如 Alice 将食谱规划视为长期项目，Bob 则只是一次性查询）。这种一刀切方式导致有限的记忆预算浪费在瞬时交互上，而真正需要持久化的关键上下文却被遗忘。论文首次提出个性化记忆问题，并构建了首个基准 PerMem-Bench，用于评估记忆系统是否能够学习并执行用户特定的“值得存储”策略。

**方法关键点**  
- **基准构建**：全自动化管线，基于 Nemotron-Persona 用户画像，为每个用户生成域参与、频率、记忆必要性三元组，构建包含多年、多域的生命骨架，通过用户/代理双模拟器生成带金标准参考记忆的对话。静态版（PerMem-Bench s）涵盖 20 用户的 26-78 个会话、多达 72 个参考记忆；动态版（PerMem-Bench d）模拟使用模式转移。  
- **会话级存储门控**：轻量级个性化框架，在每个会话后预测该会话属于长期任务还是瞬时交互，若为瞬时则完全跳过记忆操作，使预算集中于值得存储的会话。实现了三种门控方法：Greedy（仅当前会话）、Context-aware（滑动窗口摘要）、Structure-aware（维护跨会话的项目结构笔记，可近似推断域级使用模式）。  
- **评估指标**：记忆保留率（RR），持续采样检查参考记忆是否被正确保留至其目标生命周期结束。

**关键结果**  
- 在 Mem0、Memory-R1、RMM 三个记忆系统上，Oracle（完美门控）相比 Universal（无门控）大幅提升 RR，尤其在小预算（100-200 条目）下增益显著，最高可达约 0.15-0.2 的绝对提升。  
- 当前门控方法中 Structure-aware 在 PerMem-Bench s 上 F1 最高达 0.844（Qwen3-14B），但其在实际动态转移场景中性能急剧下降（FNR 升高），而 Greedy 方法对转移更鲁棒。Greedy 和 Context-aware 的 F1 仅 0.66-0.75，结合后端记忆系统后收益甚微，揭示准确门控仍是关键的开放挑战。  
- 论文强调，个性化记忆的潜力远未被释放，方向在于提升门控精度以及结合事后纠错（如个性化淘汰策略）。
