---
title: 'ActionOPD: Distilling Decisions, Not Tokens'
title_zh: ActionOPD：蒸馏决策，而非令牌
authors:
- Huining Yuan
- Xiangmin Yi
- Zelai Xu
- Zixu Wang
- Xinlei Chen
- Xiao-Ping Zhang
- Yu Wang
- Chao Yu
affiliations:
- Tsinghua University
arxiv_id: '2610.19820'
url: https://arxiv.org/abs/2610.19820
pdf_url: https://arxiv.org/pdf/2610.19820
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent 动作级在线蒸馏
tags:
- ActionOPD
- On-Policy Distillation
- Semantic Actions
- Agent Distillation
- Tool Use
- RL
one_liner: 提出动作级在线蒸馏，用语义一致奖励替代 token 概率，实现跨模型家族黑盒 teacher 蒸馏
practical_value: '- 做对话/工具型业务 Agent（如导购、售后、广告投放助手）时，可用强模型作为黑盒 teacher，只采样其动作，不需要 logits
  或同 tokenizer；学生模型用语义匹配奖励做 PPO 更新，teacher 选择只看决策质量，便于跨模型家族蒸馏。

  - 语义匹配奖励可复用：工具调用先程序化比较工具名和规范化参数（忽略 dict key 顺序、归一化整数浮点），剩余差异交给冻结 LLM；消息比较意图和事实内容，不比较
  reasoning token。适合电商 Agent 的动作一致性评估。

  - state-group rollout + group-relative advantage：每步采 4 个候选，选最高奖励动作执行，但所有候选都参与训练，用组内均值做
  baseline。可缓解 on-policy 漂移并提高样本效率，适合多轮对话策略优化。

  - 奖励设计上，invalid 动作给 -1，valid 无匹配给 0，首个匹配给 1，额外匹配给频率 bonus；可降低稀疏语义匹配的方差。但 teacher
  动作错误会传播，业务中需对 teacher 动作做有效性过滤或人工审核。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：蒸馏 LLM Agent 时有两个问题：在哪些状态对齐，以及用什么粒度对齐。离线蒸馏提供密集 token 监督，但存在 teacher-student 状态分布不匹配；token 级在线蒸馏（OPD）缓解了不匹配，却通常要求 teacher token 概率和相同 tokenizer。本文观察到，语义动作（工具调用或回复意图）是更自然的监督单元，同一决策可由不同 reasoning 和措辞实现。因此目标不是复现 teacher token 序列，而是在 student 遇到的状态上提高与 teacher 动作语义一致的概率。

**方法关键点**：
- 目标函数：最大化 student 在自身访问状态上生成 teacher 语义动作的期望似然，推导为 REINFORCE 形式的策略梯度，奖励是语义一致 indicator。
- 实用实现：每个状态采样 K=3 个 teacher 动作和 N=4 个 student 候选；匹配器对工具调用先程序化比较工具名和规范化参数，剩余差异交给冻结 LLM，对消息比较意图和事实内容。
- 奖励 r_λ：invalid 为 -1；valid 但无匹配为 0；首个匹配给 1，额外匹配给 λ*(c-1)/(K-1)，λ=0.5。
- 训练采用 state-group rollout：每步用最高奖励候选执行，但所有候选保留训练；优化目标是 group-relative advantage + PPO clipped surrogate，最后对 active token 取均值。
- 只需要 teacher 的生成接口，不需要 token 概率或 tokenizer 对齐，可跨模型家族。

**关键实验**：在 AWM 和 EnvScaler 共 6,697 个任务上训练，Qwen3-4B/8B 配合 Qwen3.7-Flash/DeepSeek-V4-Flash。四个 OOD 基准平均提升 3.3–6.9 个百分点；更大学生和更强 teacher 带来更高最终平均。τ2-bench 上与 KD、token OPD 对比，ActionOPD 单轮成功 pass1 达 40.0%，超过 OPD 39.6%、KD 37.5%，但 pass4 低于 KD。消融显示语义奖励优于仅有效性奖励。Self-ActionOPD 用同模型 teacher + privileged context，pass1 平均提升 4.8 个百分点。

**最值得记住的一句话**：把蒸馏监督从 token 复现改为动作语义一致，是在黑盒、跨模型家族条件下缩小 agent 差距的关键。
