---
title: Experience-Handoff Reinforcement Learning for Recursive Self-Improvement
title_zh: 经验交接强化学习实现递归自我改进
authors:
- Doyoung Kim
- Byeongguk Jeon
- Kailin Zhang
- Sherry Yang
affiliations:
- New York University
- KAIST AI
arxiv_id: '2611.16409'
url: https://arxiv.org/abs/2611.16409
pdf_url: https://arxiv.org/pdf/2611.16409
published: '2026-11-11'
collected: '2026-11-14'
category: Agent
direction: Agent 经验交接强化学习
tags:
- Experience-Handoff RL
- Recursive Self-Improvement
- GRPO
- Agentic RL
- Playbook
- Multi-role training
one_liner: ACE-RL 联合训练 actor/reflector/curator，用可验证下游奖励优化经验交接，让模型学会写出更有效的 playbook
practical_value: '- **把 agent 的反思/笔记/playbook 也纳入 RL 训练**：电商 Agent 里常见『先搜索/推荐，再总结经验，下次调用』的
  harness，但经验文本通常由 frozen model 生成。可借鉴 ACE-RL，固定 harness，对候选经验 artifact 做一次下游 rollout，用任务
  verifier 给 reward，让模型学会写对后续调用真正有用的经验/指令，而不是只优化最终动作。

  - **为中间文本设计 per-role comparison group**：反射器和编辑器的输出不要共享整条链的 final reward，而是同输入采样多个输出、组内归一化
  advantage。这能降低 credit assignment 方差，尤其适合电商多阶段 Agent（query 改写 → 商品筛选 → 文案生成）中中间步骤的训练。

  - **端到端训练 harness 内所有角色，优先于只训练 actor 再套 harness**：论文显示 actor-only RL 后放入固定 harness
  往往不如直接训练 harness 内的模型。在业务中如果计划上线带记忆/反思的搜索推荐 Agent，应把记忆管理模块也纳入 RL 训练，而不是只 post-train
  决策模块。

  - **可验证的 playbook 价值评估**：对候选 playbook 执行一次完整 rollout 得到标量奖励，优于 learned critic 的端到端训练，训练更稳定且不易
  collapse。可作为电商 Agent 中 memory/知识库更新的训练信号。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
Outcome-only RL 只用标量奖励压缩整个 trial，丢弃环境中的细粒度信息（错误日志、tool outputs、约束）；而 reflection/playbook 等 harness 虽能保存经验传给后续 rollout，但写经验的模型本身不被训练，质量受限于 frozen 权重。论文提出 experience-handoff RL，同时利用标量奖励的梯度更新和丰富经验 artifact。

**方法关键点**  
- 固定 ACE harness，同一模型扮演三个角色：actor 求解任务、reflector 从轨迹提取 insight、curator 编辑 task-local playbook。  
- 每次 handoff 迭代：actor 生成轨迹 τ → reflector 写 insight z → curator 输出结构化 edit u，更新 playbook P′，随后用新 playbook 做一次 fresh rollout 得到 verifiable reward。  
- 奖励定义：curator 输出 u 的 reward = 候选 playbook P′ 执行后的任务奖励；reflector 输出 z 的 reward = 由其生成的所有 admissible edits 对应 playbook 执行奖励的均值；actor rollout 用自身任务奖励。  
- 为每类角色构建 comparison group：同一输入采样多个输出，组内归一化 advantage，避免整条链共享 final reward 导致的高方差 credit assignment。actor、reflector、curator 共享一次策略更新。  
- playbook 按任务本地保存，每 F 次 encounter 重置，训练中只保留相对当前 seed reward 有提升的候选 playbook。

**关键实验与结果**  
在 Mastermind、MBPP、AppWorld、MiniSWEBench 四个 benchmark 上，同等训练 compute 下，ACE-RL 的 held-out RSI@3 全面超过 GRPO pass@3、GRPO run in harness、PPO、ERL 和 Delayed-joint PPO。例如 MBPP 上 ACE-RL 达 0.987 vs GRPO pass@3 0.867，AppWorld 上 0.667 vs 0.624。RSI@K 优势保持到 K=8，超过训练 horizon。edits-discarded 控制实验证实 playbook 本身对任务成功有正向贡献。

**最值得记住的一句话**  
训练 agent 不仅要优化当前 rollout 的动作，还要优化未来 rollout 继承的 model-written experience；用可验证下游 reward 训练这些经验 artifact，能让模型在 harness 内实现更稳定的递归自我改进。
