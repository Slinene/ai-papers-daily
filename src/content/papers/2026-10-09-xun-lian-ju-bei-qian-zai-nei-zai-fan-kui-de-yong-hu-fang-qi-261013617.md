---
title: Training User Simulators with Latent Intrinsic Feedback
title_zh: 训练具备潜在内在反馈的用户仿真器
authors:
- Tarek Naous
- Craig Boutilier
- Wei Xu
- Ofer Meshi
affiliations:
- Google Research
- Georgia Institute of Technology
arxiv_id: '2610.13617'
url: https://arxiv.org/abs/2610.13617
pdf_url: https://arxiv.org/pdf/2610.13617
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: 用户仿真器 · 内禀奖励多轮RL
tags:
- User Simulator
- Latent Evaluation States
- Multi-turn RL
- Intrinsic Reward
- LLM Assistant
- Compute Efficiency
one_liner: 提出带潜在评估状态的用户仿真器，同时生成用户话术与逐轮评分，用于多轮RL训练助手并省一半以上算力
practical_value: '- 在导购/客服 Agent 做离线 RL 时，可把用户模拟器输出结构化为「下一轮用户消息 + <eval> rating/feedback」，用
  rating 直接当逐轮 reward，省掉外部 LLM-as-judge。文中 RL 计算量从 5.48e19 降到 2.45e19 FLOPs，约省 55%，且满意度不降反升（41.44%
  vs 41.08%）。

  - 用真实聊天日志构造 simulator：用大模型对历史会话补标 latent eval 和 intent，再 SFT 小模型，比直接 prompt 大模型
  roleplay 更真实、评分更接近真人。适合在电商客服/导购数据上复制，得到可控制、可复用的仿真环境。

  - intent 条件化值得做：把用户高层意图作为 system prompt，提升反馈行为可控性，便于按场景（如“找一款送父母的蓝牙耳机”“售后问询”）生成特定仿真任务。

  - 若只需要低成本 reward，可简化 LES 只保留 Rating；代价是文本 realism 下降。想要更真实话术，需加入 Internal_Thought/Feedback
  等语言型子状态。另外注意反应类不平衡：WildChat 中 Praise 仅占 1.26%，Critique 约 14.15%，训练 reward 或分类时可能需要重采样。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**

用户仿真器正成为训练多轮 LLM assistant 的重要环境，但现有仿真器主要只做用户话术生成，奖励信号通常要依赖外部 LLM judge，既增加推理开销，又可能与真实用户的主观评价相关度不高。很多用户评估不会显式写在下一句话里，而是藏在 latent reasoning 中。

**方法关键点**

- 在 WildChat-1M 真实用户-ChatGPT 日志上，用 Gemini3.1-Pro 为每轮（从第二轮起）生成 latent evaluation states，包含五个子状态：Internal_Thought、Rating(1–5)、Instruction_Followed、Reaction(Critique/Praise/Neutral)、Feedback。
- 用 Gemma3 4B/12B/27B 与 Qwen2.5 3B/7B/14B base 模型做全参 SFT，训练目标为 P(z_{t+1}, u_{t+1}|c_t)，即先生成评估状态，再生成下一轮用户话术。
- 引入用户高层 intent 作为 system prompt 做条件化，提升仿真可控性与反馈行为。
- 在 RL 阶段，用 Qwen2.5-1.5B-Instruct 做 assistant，在 100k WildChat 样本上做多轮 GRPO；环境切换为 prompted Simulator / SFT Simulator / LES Simulator，reward 来源切换为外部 judge 或 simulator 内禀 rating。

**关键实验与结果**

- 在 WildChat held-out 4,000 对话上，LES simulator 的 realism 明显超过同尺寸 prompted baseline：Gemma3-12B-LES 的 statistical alignment 为 0.8635，而 IT baseline 仅 0.5135；PPL 3.13 vs 13.41。
- SimulatorArena 上，LES 生成的 rating 与真人评分相关性一致优于同尺寸 prompted baseline，如 Gemma3-4B-LES 总体 Spearman ρ=0.384 vs IT 0.244；12B 为 0.401 vs 0.295。
- SFT simulator 在 critique F1 上略高于 LES，主要因为 LES 更谨慎批评（recall 下降）；但 SFT 不输出 rating，无法直接当 reward。
- 多轮 RL：助手从无 RL 的 28.78% checklist satisfaction 提升到 LES+intrinsic reward 的 41.44%；intrinsic reward 略优于 external judge 的 41.08%，同时 RL 总 FLOPs 从 5.48e19 降到 2.45e19，计算量减少超过一半。
- 消融显示：只保留 Rating 子状态时反馈行为最好但 realism 最低；加入语言型子状态能提高 realism；intent conditioning 一致改善反馈行为。

**最值得记住的一句话**：让用户仿真器输出 latent 评估状态，能把环境同时变成奖励函数，既提升奖励与真人判断的相关性，又消除外部 judge、砍掉一半以上 RL 算力。
