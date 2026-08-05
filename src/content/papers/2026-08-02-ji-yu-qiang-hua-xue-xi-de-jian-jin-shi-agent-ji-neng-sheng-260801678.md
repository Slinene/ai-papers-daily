---
title: Progressive Agent Skill Generation via Reinforcement Learning
title_zh: 基于强化学习的渐进式 Agent 技能生成
authors:
- Junhao Shen
- Zhanqiu Zhang
- Yiwen Guo
- Hong Cheng
affiliations:
- The Chinese University of Hong Kong
- LIGHTSPEED
- Independent Researcher
arxiv_id: '2608.01678'
url: https://arxiv.org/abs/2608.01678
pdf_url: https://arxiv.org/pdf/2608.01678
published: '2026-08-02'
collected: '2026-08-05'
category: Agent
direction: Agent 技能生成 · 强化学习
tags:
- Agent
- Skill Generation
- Reinforcement Learning
- Rollback Reward
- GRPO
- Progressive Generation
one_liner: 用 RL 将技能生成为局部编辑序列，以 rollback reward 提供信用分配，显著超越基于流水线或启发式的方法
practical_value: '- **技能编辑的局部评估**：rollback reward 对每个编辑步骤进行锚定查询下的前后对比，避免依赖文本流畅度评估，可直接迁移到推荐
  Agent 的策略迭代中，用下游 A/B 效果替代人工规则。

  - **渐进式技能构建**：将长文档或大量经验分解为逐步编辑，适应电商 Agent 的增量学习场景，如促销规则更新、用户反馈积累。

  - **统一多源证据**：同一框架同时处理文档和执行轨迹，可用于混合知识源（如商品描述、用户日志）生成统一的推荐策略。

  - **动作空间设计**：CREATE/UPDATE/MERGE/PRUNE/NOOP 的编辑动作集可直接作为 Agent 技能库维护的元操作，用于自动优化搜索竞价策略模板或客服话术集。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent 依赖外部技能来指导推理和工具使用，但自动生成高质量技能缺乏直接的监督信号——文本流畅不等于任务有效。现有方法多为启发式或管道式，针对不同证据源需单独设计，且无法判断每条证据应如何改变技能。

### 方法关键点
- **渐进式生成**：将技能构建分解为顺序编辑步骤，每一步基于当前技能和一条证据选择一次局部编辑（CREATE/UPDATE/MERGE/PRUNE/NOOP）。
- **Rollback Reward**：编辑后的技能与上一版本在锚定查询上的执行结果通过验证器比较，仅当编辑带来提升时才给正奖励，实现编辑级别的信用分配。
- **训练流程**：先用强模型合成编辑轨迹做 SFT 热身，再用 GRPO 在 GPT-4o 作为固定 worker 的条件下训练 Qwen3-8B 作为编辑策略。
- **通用输入**：文档和任务执行轨迹统一序列化为标准格式，支持文档‑技能和体验‑技能两种场景。

### 关键结果
- 在 GPT-4o worker 下，CL-Bench 平均成功率比最强基线高 3.3 个百分点，tau2-bench 高 6.7 个百分点。
- 跨 worker 迁移到 Claude-Sonnet-4.5 时仍保持最优或相近，显示生成的是可转移的知识。
- 消融：去掉 rollback reward 后性能接近 SFT-only，说明编辑级执行反馈是核心驱动；去掉 MERGE/PRUNE 大幅下降，证明需要结构化精简。
- 证据批量 4 单位/步时效果最好，过小则编辑短视，过大则编辑焦点模糊。
